import sys
import sys, re, json, glob, os
sys.stdout.reconfigure(encoding="utf-8")
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.stack=[]; s.out=[]; s.cur=None; s.txt=''; s.style=''; s.instyle=False; s.ids=[]; s.links=[]; s.imgs=[]; s.forms=[]; s.scripts=0; s.navs=0; s.headers=0; s.footers=0; s.mains=0
    def handle_starttag(s,t,a):
        a=dict(a)
        if 'id' in a: s.ids.append(a['id'])
        if t=='style': s.instyle=True
        if t=='script': s.scripts+=1
        if t=='nav': s.navs+=1
        if t=='header': s.headers+=1
        if t=='footer': s.footers+=1
        if t=='main': s.mains+=1
        if t in('h1','h2','h3','a','button','summary','label'):
            s.cur=(t,a); s.txt=''
        if t=='img': s.imgs.append((a.get('src'),a.get('alt')))
        if t in('input','textarea','select'): s.forms.append((t,a.get('name') or a.get('id'),a.get('type'),'required' in a,'disabled' in a))
        if t=='form': s.forms.append(('FORM',a.get('action'),a.get('method'),None,'disabled' in a))
    def handle_endtag(s,t):
        if t=='style': s.instyle=False
        if s.cur and s.cur[0]==t:
            txt=re.sub(r'\s+',' ',s.txt).strip()
            if t=='a': s.links.append((txt,s.cur[1].get('href'),s.cur[1].get('class')))
            elif t in ('button','summary','label'): s.out.append((t.upper(),txt[:90]))
            else: s.out.append((t,txt))
            s.cur=None
    def handle_data(s,d):
        if s.instyle: s.style+=d
        if s.cur: s.txt+=d
for f in sorted(glob.glob(sys.argv[1]+'/**/*.html',recursive=True)):
    h=open(f,encoding='utf-8').read(); p=P(); p.feed(h)
    print('\n#########', os.path.relpath(f,sys.argv[1]), len(h),'bytes')
    t=re.search(r'<title>(.*?)</title>',h,re.S); print('TITLE:',t and t.group(1).strip()); print('LANG:',re.search(r'<html[^>]*lang="([^"]+)"',h) and re.search(r'<html[^>]*lang="([^"]+)"',h).group(1))
    print('LANDMARKS header/nav/main/footer:',p.headers,p.navs,p.mains,p.footers,'scripts:',p.scripts, 'ext css/js:', re.findall(r'(?:href|src)="(https?://[^"]+)"',h)[:3])
    css=p.style+' '.join(re.findall(r'style="([^"]*)"',h))
    print('HEX:',sorted(set(x.upper() for x in re.findall(r'#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b',css))))
    print('FONTS:',sorted(set(re.findall(r'font-family:\s*([^;}]+)',css)))[:4])
    print('MEDIA:',sorted(set(re.findall(r'@media[^{]+',css))))
    print('MAXW:',sorted(set(re.findall(r'max-width:\s*([0-9.]+(?:px|rem|ch))',css)))[:12])
    print('IDS:',p.ids)
    for k,v in p.out: print('  ',k,':',v)
    print('LINKS:'); [print('   ',x) for x in p.links]
    print('IMGS:',p.imgs); print('FORM:',p.forms)
    print('MARKERS:',sorted(set(m.lower() for m in re.findall(r'(maqueta|prototipo|demo\w*|no publicable|provisional|pendiente[^<.]{0,40}|NO_PUBLICAR|data-preview-link)',h,re.I)))[:15])
