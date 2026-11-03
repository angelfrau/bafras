"""Mide desbordamiento horizontal de las maquetas en anchos fijos mediante iframe (Chrome headless).
Uso: python -I probe2.py <scratchpad> <anchos separados por comas>
No modifica las maquetas: escribe un contenedor temporal junto a cada copia extraída en el scratchpad."""
import sys, glob, os, re, subprocess, json, html

sys.stdout.reconfigure(encoding="utf-8")
SP = sys.argv[1]
WIDTHS = [int(w) for w in sys.argv[2].split(",")]
CH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

WRAP = """<!doctype html><html><body style="margin:0">
<iframe id="f" src="{src}" style="width:{w}px;height:900px;border:0"></iframe>
<pre id="__probe">PENDING</pre>
<script>
var f=document.getElementById('f');
f.addEventListener('load',function(){{
 var s=f.contentDocument.createElement('style');s.textContent='html{{scrollbar-width:none}}';f.contentDocument.head.appendChild(s);
 setTimeout(function(){{
 try{{var d=f.contentDocument.documentElement, w=f.contentWindow;
  var off=[];f.contentDocument.querySelectorAll('body *').forEach(function(e){{
   var r=e.getBoundingClientRect(), cs=w.getComputedStyle(e);
   if(r.width>0&&r.right>d.clientWidth+1&&cs.position!=='fixed'&&cs.visibility!=='hidden')
     off.push(e.tagName+'.'+String(e.className||'').slice(0,30)+'@'+Math.round(r.right));}});
  document.getElementById('__probe').textContent=JSON.stringify({{iw:w.innerWidth,cw:d.clientWidth,sw:d.scrollWidth,n:off.length,off:off.slice(0,5)}});
 }}catch(err){{document.getElementById('__probe').textContent='ERR '+err}}
}},500)}});
</script></body></html>"""

results = []
for f in sorted(glob.glob(SP + "/maq/**/*.html", recursive=True)):
    if "__" in os.path.basename(f):
        continue
    src = "file:///" + f.replace(chr(92), "/")
    for w in WIDTHS:
        wrap = os.path.join(SP, f"__wrap_{w}.html")
        with open(wrap, "w", encoding="utf-8") as fh:
            fh.write(WRAP.format(src=html.escape(src), w=w))
        out = subprocess.run(
            [CH, "--headless=new", "--disable-gpu", "--no-first-run", "--allow-file-access-from-files",
             "--user-data-dir=" + SP + "/chprof", "--window-size=1600,1000", "--virtual-time-budget=4000",
             "--dump-dom", "file:///" + wrap.replace(chr(92), "/")],
            capture_output=True, text=True, encoding="utf-8", timeout=120).stdout
        m = re.search(r'<pre id="__probe">(.*?)</pre>', out, re.S)
        val = html.unescape(m.group(1)) if m else "NO-RESULT"
        print(os.path.basename(f), w, val)
        results.append({"file": os.path.relpath(f, SP + "/maq").replace(chr(92), "/"), "width": w, "result": val})
        os.remove(wrap)
with open(os.path.join(SP, "overflow_results.json"), "w", encoding="utf-8") as fh:
    json.dump(results, fh, ensure_ascii=False, indent=1)
