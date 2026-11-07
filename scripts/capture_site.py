"""QA HTTP y dossier visual del build real. Requiere Playwright solo en el entorno de QA.

Desde la raíz: python scripts/capture_site.py --browser <Chrome/Chromium>
--baseline-root permite comparar visualmente una salida anterior sin incorporarla al producto.
No reconstruye el sitio, no publica, no mantiene una lista independiente de páginas.
"""
from __future__ import annotations

import argparse
import functools
import hashlib
import json
import shutil
import struct
import subprocess
import threading
from contextlib import contextmanager
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from bafras_web.adapters.filesystem import ProjectPaths
from bafras_web.application.configuration import load_site_routing
from bafras_web.application.editorial import EditorialLoadRequest, inspect_editorial
from bafras_web.editorial.integrity import build_editorial_bundle

WIDTHS = (320, 375, 390, 768, 1024, 1440)
VIEWPORTS = {"desktop": {"width": 1440, "height": 900}, "mobile": {"width": 390, "height": 844}}
STABLE_STYLE = "*,*::before,*::after {animation:none!important;transition:none!important;scroll-behavior:auto!important}"


MEASURE = r"""() => {
  const width = document.documentElement.clientWidth;
  const overflow = [...document.querySelectorAll('body *')].filter(e => {
    const r=e.getBoundingClientRect(), s=getComputedStyle(e);
    return r.width && s.position !== 'absolute' && s.visibility !== 'hidden' && (r.right > width+1 || r.left < -1);
  }).map(e=>e.tagName+'.'+e.className);
  const headings=[...document.querySelectorAll('h1,h2,h3,h4')].map(e=>Number(e.tagName.slice(1)));
  const jumps=headings.filter((h,i)=>i && h>headings[i-1]+1);
  return {width, scrollWidth:document.documentElement.scrollWidth, overflow, jumps,
    h1:document.querySelectorAll('h1').length,
    landmarks:['header','main','footer'].map(t=>document.querySelectorAll(t).length),
    images:[...document.images].every(i=>i.complete && i.naturalWidth && i.alt),
    disabledFields:[...document.querySelectorAll('input,textarea,button[type="button"]:not(.menu-toggle)')].every(e=>e.matches(':disabled'))};
}"""

CONTRAST = r"""() => {
  const color = s => { const v=s.match(/[\d.]+/g); return v ? v.map(Number) : [0,0,0,0]; };
  const luminance = rgb => rgb.slice(0,3).map(c=>{c/=255; return c<=.04045?c/12.92:((c+.055)/1.055)**2.4;}).reduce((a,c,i)=>a+c*[.2126,.7152,.0722][i],0);
  const failures=[];
  for(const e of document.querySelectorAll('body *')) {
    if(![...e.childNodes].some(n=>n.nodeType===3 && n.textContent.trim())) continue;
    const s=getComputedStyle(e), r=e.getBoundingClientRect();
    if(!r.width||!r.height||s.visibility==='hidden'||e.closest('fieldset[disabled]')) continue;
    let bg=[255,255,255], parent=e, layers=[];
    while(parent) {layers.unshift(color(getComputedStyle(parent).backgroundColor)); parent=parent.parentElement;}
    for(const layer of layers) {const alpha=layer[3]??1; bg=bg.map((c,i)=>layer[i]*alpha+c*(1-alpha));}
    const fg=color(s.color), a=luminance(fg), b=luminance(bg), ratio=(Math.max(a,b)+.05)/(Math.min(a,b)+.05);
    const large=parseFloat(s.fontSize)>=24 || (parseFloat(s.fontSize)>=18.66 && parseInt(s.fontWeight)>=700);
    if(ratio < (large?3:4.5)) failures.push({tag:e.tagName,cls:e.className,text:e.textContent.trim().slice(0,50),ratio});
  }
  return failures;
}"""


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


@contextmanager
def serve(directory):
    server = ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(QuietHandler, directory=str(directory)))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}"
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


def file_hashes(directory):
    return {p.relative_to(directory).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(directory.rglob("*")) if p.is_file()}


def source_fingerprint(root):
    entries = {f"{folder}/{name}": value for folder in ("src", "assets", "config", "content")
               for name, value in file_hashes(root / folder).items() if "__pycache__" not in name and ".egg-info/" not in name}
    return hashlib.sha256(json.dumps(entries, sort_keys=True).encode()).hexdigest()


def inspect_page(page, base, url, model, *, direct_contact=True):
    errors = []
    failed_http = []
    on_error = lambda error: errors.append(str(error))
    on_response = lambda response: failed_http.append(f"{response.status} {response.url}") if response.status >= 400 else None
    page.on("pageerror", on_error)
    page.on("response", on_response)
    try:
        response = page.goto(base + url, wait_until="networkidle")
        assert response is not None and response.status == 200, f"HTTP {response.status if response else 'sin respuesta'}"
        page.evaluate("document.fonts.ready")
        page.locator("img").evaluate_all("images=>{images.forEach(i=>i.loading='eager'); return Promise.all(images.map(i=>i.decode()));}")
        page.add_style_tag(content=STABLE_STYLE)
        assert page.locator("main h1").inner_text() == model.sections[0].title, "documento distinto del solicitado"
        assert page.locator("main section").evaluate_all("sections=>sections.map(s=>s.id)") == [s.id for s in model.sections]
        assert page.evaluate("document.styleSheets.length > 1 && getComputedStyle(document.documentElement).getPropertyValue('--pine').trim() === '#0E2B25'"), "CSS no cargado"
        measurement = page.evaluate(MEASURE)
        assert measurement["h1"] == 1 and measurement["landmarks"] == [1, 1, 1] and measurement["images"], measurement
        assert not measurement["overflow"] and not measurement["jumps"] and measurement["scrollWidth"] <= measurement["width"], measurement
        contrasts = page.evaluate(CONTRAST)
        assert not contrasts, contrasts
        assert not errors and not failed_http, {"javascript": errors, "http": failed_http}
        if model.page_id == "contacto" and direct_contact:
            assert page.locator("main form, main input, main textarea, main fieldset, main button").count() == 0
            assert "Formulario no disponible" not in page.locator("main").inner_text()
            assert page.locator('main a[href^="mailto:"]').count() == 1 and page.locator('main a[href^="tel:"]').count() == 1
        return {"status": "passed", "http_status": response.status, "javascript_errors": errors,
                "http_errors": failed_http, "assets": "loaded", **measurement}
    finally:
        page.remove_listener("pageerror", on_error)
        page.remove_listener("response", on_response)


def capture_page(page, filename):
    dimensions = page.evaluate("({width:document.documentElement.scrollWidth,height:document.documentElement.scrollHeight})")
    assert page.locator(".menu-toggle").get_attribute("aria-expanded") == "false"
    data = page.screenshot(path=str(filename) if filename else None, full_page=True, animations="disabled")
    assert len(data) > 1000 and data.startswith(b"\x89PNG\r\n\x1a\n"), "PNG vacío o inválido"
    width, height = struct.unpack(">II", data[16:24])
    assert width == dimensions["width"] and height >= dimensions["height"], "captura recortada"
    return data, {"width": width, "height": height, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def keyboard_checks(browser, base, routing, bundle):
    page = browser.new_page(viewport=VIEWPORTS["mobile"], device_scale_factor=1)
    try:
        home = next(pid for pid in routing.routes.pages if routing.url(pid, "es") == "/")
        inspect_page(page, base, routing.url(home, "es"), bundle.get_page(home))
        page.keyboard.press("Tab")
        assert page.locator(".skip-link").evaluate("e=>e===document.activeElement && getComputedStyle(e).outlineStyle!=='none'")
        page.keyboard.press("Enter")
        assert page.evaluate("location.hash") == "#contenido"
        toggle = page.locator(".menu-toggle")
        toggle.focus()
        page.keyboard.press("Enter")
        assert toggle.get_attribute("aria-expanded") == "true"
        page.keyboard.press("Escape")
        assert toggle.get_attribute("aria-expanded") == "false" and toggle.evaluate("e=>e===document.activeElement")
        destination = page.locator(".site-nav a").first.get_attribute("href")
        toggle.click()
        page.locator(".site-nav a").first.click()
        assert page.url == base + destination
        contact_url = routing.url("contacto", "es")
        inspect_page(page, base, contact_url, bundle.get_page("contacto"))
        for selector in ('main a[href^="mailto:"]', 'main a[href^="tel:"]'):
            link = page.locator(selector)
            link.focus()
            assert link.evaluate("e=>e===document.activeElement && getComputedStyle(e).outlineStyle!=='none'")
        page.set_viewport_size(VIEWPORTS["desktop"])
        before = page.evaluate("({dpr:devicePixelRatio,width:innerWidth})")
        for _ in range(4):
            page.keyboard.press("Control++")
        after = page.evaluate("({dpr:devicePixelRatio,width:innerWidth})")
        return {"keyboard": "passed", "zoom": {"before": before, "after": after,
                "real_200_percent_verified": False, "limit": "Zoom real 200% requiere comprobación manual; no se sustituye por viewport."}}
    finally:
        page.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--browser", type=Path)
    parser.add_argument("--baseline-root", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.project.resolve()
    paths = ProjectPaths(root)
    build_root = root / "build/preview"
    output = args.output or root / "artifacts/web-v03/visual-review/es"
    routing = load_site_routing(paths)
    bundle = build_editorial_bundle(inspect_editorial(paths, EditorialLoadRequest(locale="es", policy="COMPLETE")))
    pages = {pid: routing.url(pid, "es") for pid in routing.routes.pages}
    assert all(pages.values()) and len(list(build_root.rglob("*.html"))) == len(pages), "build incompleto o inaccesible"
    browser_path = args.browser or next((p for p in [Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
                Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")] if p.is_file()), None)
    if browser_path is None:
        candidate = shutil.which("chromium") or shutil.which("google-chrome")
        if candidate:
            browser_path = Path(candidate)
    if browser_path is None:
        parser.error("indica Chrome/Chromium mediante --browser")
    from playwright.sync_api import sync_playwright

    for device in VIEWPORTS:
        (output / device).mkdir(parents=True, exist_ok=True)
    build_files = file_hashes(build_root)
    reference = {"fingerprint": hashlib.sha256(json.dumps(build_files, sort_keys=True).encode()).hexdigest(),
                 "files": build_files, "source_fingerprint": source_fingerprint(root),
                 "git_head_before_commit": subprocess.check_output(["git", "-c", f"safe.directory={root.as_posix()}", "rev-parse", "HEAD"], cwd=root, text=True).strip()}
    manifest = {"build": reference, "viewports": VIEWPORTS, "device_scale_factor": 1, "browser": None,
                "pages": [], "responsive_checks": [], "errors": [], "status": "incomplete"}
    try:
        with serve(build_root) as base, sync_playwright() as playwright:
            browser = playwright.chromium.launch(executable_path=str(browser_path), headless=True)
            manifest["browser"] = browser.version
            page = browser.new_page(viewport=VIEWPORTS["desktop"], device_scale_factor=1, reduced_motion="reduce")
            try:
                for width in WIDTHS:
                    page.set_viewport_size({"width": width, "height": 900})
                    for pid, url in pages.items():
                        record = {"page_id": pid, "viewport_width": width}
                        try:
                            record.update(inspect_page(page, base, url, bundle.get_page(pid)))
                        except Exception as error:
                            record.update(status="failed", error=str(error))
                            manifest["errors"].append(record.copy())
                        manifest["responsive_checks"].append(record)
                for pid, url in pages.items():
                    record = {"page_id": pid, "public_path": url, "local_url": base + url,
                              "build_reference": reference["fingerprint"], "captures": {}, "errors": []}
                    for device, viewport in VIEWPORTS.items():
                        try:
                            page.set_viewport_size(viewport)
                            inspection = inspect_page(page, base, url, bundle.get_page(pid))
                            filename = output / device / f"{pid}.png"
                            data, metadata = capture_page(page, filename)
                            metadata.update(path=filename.relative_to(output).as_posix(), status="captured",
                                            http_status=inspection["http_status"], assets=inspection["assets"], errors=[])
                            if args.baseline_root:
                                with serve(args.baseline_root.resolve()) as baseline:
                                    inspect_page(page, baseline, url, bundle.get_page(pid), direct_contact=False)
                                    previous, _ = capture_page(page, None)
                                metadata["matches_before"] = data == previous
                                if pid != "contacto":
                                    assert data == previous, f"regresión visual fuera de Contacto: {pid}/{device}"
                            record["captures"][device] = metadata
                        except Exception as error:
                            record["captures"][device] = {"status": "failed", "error": str(error)}
                            record["errors"].append(f"{device}: {error}")
                    record["status"] = "captured" if not record["errors"] else "failed"
                    manifest["pages"].append(record)
                manifest["interaction"] = keyboard_checks(browser, base, routing, bundle)
            finally:
                browser.close()
        assert file_hashes(build_root) == build_files, "el build cambió durante el QA"
        assert source_fingerprint(root) == reference["source_fingerprint"], "las fuentes cambiaron durante el QA"
        if not manifest["errors"] and all(row["status"] == "captured" for row in manifest["pages"]):
            manifest["status"] = "complete"
    finally:
        (output / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    count = sum(capture["status"] == "captured" for row in manifest["pages"] for capture in row["captures"].values())
    print(json.dumps({"status": manifest["status"], "pages": len(manifest["pages"]), "captures": count,
                      "responsive_checks": len(manifest["responsive_checks"]), "output": str(output)}, ensure_ascii=False))
    return 0 if manifest["status"] == "complete" else 1



if __name__ == "__main__":
    raise SystemExit(main())
