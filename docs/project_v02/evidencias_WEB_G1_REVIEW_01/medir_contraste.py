"""Contraste WCAG de nodos de texto visibles sobre fondo sólido calculado (Chrome headless, iframe 1440 px).
Indicativo: ignora texto sobre imágenes/gradientes y no sustituye una auditoría WCAG manual.
Uso: python -I contrast.py <scratchpad>"""
import sys, glob, os, re, subprocess, json, html

sys.stdout.reconfigure(encoding="utf-8")
SP = sys.argv[1]
CH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
JS = r"""
function rgb(s){var m=s.match(/rgba?\(([^)]+)\)/);if(!m)return null;var p=m[1].split(',').map(parseFloat);return {r:p[0],g:p[1],b:p[2],a:p.length>3?p[3]:1}}
function lum(c){function f(v){v/=255;return v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4)}return 0.2126*f(c.r)+0.7152*f(c.g)+0.0722*f(c.b)}
function bg(e,w){var stack=[];while(e){var cs=w.getComputedStyle(e);if(cs.backgroundImage&&cs.backgroundImage!=='none')return null;var c=rgb(cs.backgroundColor);if(c&&c.a>0){stack.push(c);if(c.a>=1)break}e=e.parentElement}
 var base={r:255,g:255,b:255};for(var i=stack.length-1;i>=0;i--){var c=stack[i];base={r:c.r*c.a+base.r*(1-c.a),g:c.g*c.a+base.g*(1-c.a),b:c.b*c.a+base.b*(1-c.a)}}return base}
function run(doc,w){var out=[],seen={};var tw=doc.createTreeWalker(doc.body,NodeFilter.SHOW_TEXT);var n;
 while(n=tw.nextNode()){var t=n.textContent.replace(/\s+/g,' ').trim();if(!t)continue;var e=n.parentElement;var cs=w.getComputedStyle(e);
  if(cs.visibility==='hidden'||cs.display==='none'||e.getClientRects().length===0)continue;
  var fg=rgb(cs.color);var b=bg(e,w);if(!fg||!b)continue;var op=parseFloat(cs.opacity);
  var f={r:fg.r*fg.a+b.r*(1-fg.a),g:fg.g*fg.a+b.g*(1-fg.a),b:fg.b*fg.a+b.b*(1-fg.a)};
  var L1=lum(f),L2=lum(b);var cr=(Math.max(L1,L2)+0.05)/(Math.min(L1,L2)+0.05);
  var px=parseFloat(cs.fontSize),wt=parseInt(cs.fontWeight);var large=px>=24||(px>=18.66&&wt>=700);var need=large?3:4.5;
  if(cr<need){var k=cs.color+'|'+JSON.stringify(b)+'|'+px;if(seen[k])continue;seen[k]=1;
   out.push({txt:t.slice(0,40),cr:Math.round(cr*100)/100,need:need,px:px,wt:wt,fg:cs.color,bg:'rgb('+Math.round(b.r)+','+Math.round(b.g)+','+Math.round(b.b)+')'})}}
 return out}
"""
WRAP = """<!doctype html><html><body style="margin:0"><iframe id="f" src="{src}" style="width:1440px;height:900px;border:0"></iframe>
<pre id="__probe">PENDING</pre><script>{js}
var f=document.getElementById('f');f.addEventListener('load',function(){{setTimeout(function(){{
try{{document.getElementById('__probe').textContent=JSON.stringify(run(f.contentDocument,f.contentWindow))}}catch(err){{document.getElementById('__probe').textContent='ERR '+err}}}},500)}});
</script></body></html>"""
res = {}
for f in sorted(glob.glob(SP + "/maq/**/*.html", recursive=True)):
    src = "file:///" + f.replace(chr(92), "/")
    wrap = os.path.join(SP, "__wrap_c.html")
    with open(wrap, "w", encoding="utf-8") as fh:
        fh.write(WRAP.format(src=html.escape(src), js=JS))
    out = subprocess.run([CH, "--headless=new", "--disable-gpu", "--no-first-run", "--allow-file-access-from-files",
                          "--user-data-dir=" + SP + "/chprof", "--window-size=1600,1000", "--virtual-time-budget=4000",
                          "--dump-dom", "file:///" + wrap.replace(chr(92), "/")],
                         capture_output=True, text=True, encoding="utf-8", timeout=120).stdout
    m = re.search(r'<pre id="__probe">(.*?)</pre>', out, re.S)
    val = html.unescape(m.group(1)) if m else "NO-RESULT"
    os.remove(wrap)
    try:
        data = json.loads(val)
    except Exception:
        data = val
    res[os.path.basename(f)] = data
    print("==", os.path.basename(f), len(data) if isinstance(data, list) else data)
    if isinstance(data, list):
        for d in data:
            print("   ", d)
with open(os.path.join(SP, "contrast_results.json"), "w", encoding="utf-8") as fh:
    json.dump(res, fh, ensure_ascii=False, indent=1)
