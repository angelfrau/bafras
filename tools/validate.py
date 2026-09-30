from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"

REQUIRED_FILES = [
    "index.html",
    "CNAME",
    "css/tokens.css",
    "css/base.css",
    "css/components.css",
    "css/pages.css",
    "js/site.js",
    "js/router.js",
    "js/form.js",
    "README.md",
    "docs/architecture.md",
    "pyproject.toml",
]

CSS_LINKS = [
    "css/tokens.css",
    "css/base.css",
    "css/components.css",
    "css/pages.css",
]

JS_SCRIPTS = [
    "js/site.js",
    "js/router.js",
    "js/form.js",
]


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[dict[str, str]] = []
        self.scripts: list[dict[str, str]] = []
        self.assets: list[str] = []
        self.routes: set[str] = set()
        self.hashes: list[str] = []
        self.ids: set[str] = set()
        self.forms: list[dict[str, str]] = []
        self.inline_style_blocks = 0
        self.inline_script_blocks = 0
        self._in_script_without_src = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = {key: value or "" for key, value in attrs}
        if "id" in data:
            self.ids.add(data["id"])
        if tag == "link":
            self.links.append(data)
            href = data.get("href", "")
            if href:
                self.assets.append(href)
        elif tag == "script":
            self.scripts.append(data)
            if not data.get("src"):
                self._in_script_without_src = True
        elif tag == "style":
            self.inline_style_blocks += 1
        elif tag in {"img", "source"}:
            src = data.get("src") or data.get("srcset", "")
            if src:
                self.assets.append(src)
        elif data.get("data-pagina") is not None:
            self.routes.add(data["data-pagina"])
        elif tag == "a":
            href = data.get("href", "")
            if href.startswith("#/"):
                self.hashes.append(href)
        elif tag == "form":
            self.forms.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._in_script_without_src:
            self.inline_script_blocks += 1
            self._in_script_without_src = False


def local_path(reference: str, source: Path) -> Path | None:
    if not reference or reference.startswith(("data:", "http:", "https:", "mailto:", "tel:", "#")):
        return None
    if reference.startswith("//"):
        return None
    clean = unquote(urlparse(reference).path)
    if clean.startswith("/"):
        return ROOT / clean.lstrip("/")
    return (source.parent / clean).resolve()


def collect_css_urls() -> list[tuple[str, Path]]:
    found: list[tuple[str, Path]] = []
    for css_file in (ROOT / "css").glob("*.css"):
        text = css_file.read_text(encoding="utf-8")
        for match in re.finditer(r"url\((['\"]?)(.*?)\1\)", text):
            found.append((match.group(2), css_file))
    return found


def validate() -> list[str]:
    errors: list[str] = []

    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            errors.append(f"Missing required file: {rel}")

    html = INDEX.read_text(encoding="utf-8")
    parser = SiteParser()
    parser.feed(html)

    css_links = [link.get("href", "") for link in parser.links if link.get("rel") == "stylesheet"]
    local_css = [href for href in css_links if href.startswith("css/")]
    if local_css != CSS_LINKS:
        errors.append(f"Unexpected CSS order: {local_css}")

    script_sources = [script.get("src", "") for script in parser.scripts if script.get("src")]
    if script_sources != JS_SCRIPTS:
        errors.append(f"Unexpected JS order: {script_sources}")
    for script in parser.scripts:
        if script.get("src") and "defer" not in script:
            errors.append(f"Script is missing defer: {script.get('src')}")
    if parser.inline_script_blocks:
        errors.append("Unexpected inline script block remains in index.html")
    if parser.inline_style_blocks != 1 or "<noscript><style>" not in html:
        errors.append("Only the noscript fallback style block should remain inline")

    for reference in parser.assets:
        path = local_path(reference, INDEX)
        if path and not path.exists():
            errors.append(f"Missing referenced asset: {reference}")

    for reference, source in collect_css_urls():
        path = local_path(reference, source)
        if path and not path.exists():
            errors.append(f"Missing CSS asset from {source.relative_to(ROOT)}: {reference}")

    for href in parser.hashes:
        target = href.removeprefix("#/")
        route, _, anchor = target.partition("@")
        route = route.rstrip("/")
        if route and route not in parser.routes:
            errors.append(f"Hash route has no matching data-pagina: {href}")
        if anchor and anchor not in parser.ids:
            errors.append(f"Hash anchor has no matching id: {href}")

    if not any(form.get("action") == "https://formsubmit.co/info@bafras.com" for form in parser.forms):
        errors.append("Expected FormSubmit form action not found")
    form_js = (ROOT / "js/form.js").read_text(encoding="utf-8")
    if "https://formsubmit.co/ajax/info@bafras.com" not in form_js:
        errors.append("Expected FormSubmit AJAX endpoint not found")

    operative_files = [INDEX, *Path(ROOT / "css").glob("*.css"), *Path(ROOT / "js").glob("*.js")]
    for file_path in operative_files:
        content = file_path.read_text(encoding="utf-8")
        if re.search(r'(?<!assets)/images/', content):
            errors.append(f"Legacy /images/ reference remains in {file_path.relative_to(ROOT)}")

    data_fotos = re.findall(r'data-foto="([^"]+)"', html)
    for value in data_fotos:
        first = value.split(",")[0]
        if not any((ROOT / "assets/images/team").glob(f"{first}.*")):
            errors.append(f"data-foto has no team asset candidate: {first}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
