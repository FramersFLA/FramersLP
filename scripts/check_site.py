"""Check static Pages files, navigation, project-relative links and PDF integrity."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
EXPECTED = {'index.html','about.html','faq.html','contact.html','protocol.html'}
class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.links=[];self.ids=set();self.nav=[];self.in_nav=False;self.current=[];self.h1=0
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=='nav':self.in_nav=True
        if tag=='h1':self.h1+=1
        if 'id' in a:self.ids.add(a['id'])
        if self.in_nav and tag=='a':
            self.nav.append(a['href'])
            if a.get('aria-current')=='page':self.current.append(a['href'])
        for key in ('href','src'):
            if key in a:self.links.append(a[key])
    def handle_endtag(self,tag):
        if tag=='nav':self.in_nav=False
pages={}
for path in DOCS.glob('*.html'):
    p=Page();p.feed(path.read_text());pages[path.name]=p
assert EXPECTED<=pages.keys()
assert (DOCS/'.nojekyll').exists()
for name,p in pages.items():
    assert set(p.nav)==EXPECTED,(name,'navigation')
    assert p.h1==1,(name,'heading')
    assert p.current==([name] if name in EXPECTED else []),(name,'current page')
    text=(DOCS/name).read_text()
    assert text.rstrip().endswith('</html>'),(name,'truncated HTML')
    for link in p.links:
        url=urlsplit(link)
        if url.scheme or url.netloc:continue
        assert not url.path.startswith('/'),(name,'root-absolute path breaks project prefix',link)
        target=DOCS/unquote(url.path) if url.path else DOCS/name
        assert target.is_file(),(name,'missing target',link)
        if url.fragment and target.suffix=='.html':
            assert url.fragment in pages[target.name].ids,(name,'missing anchor',link)
pdf=(DOCS/'FLP_Whitepaper.pdf').read_bytes()
assert pdf.startswith(b'%PDF-') and b'%%EOF' in pdf
print(f'PASS: {len(pages)} complete pages; shared navigation; case-sensitive local links; anchors; Pages entry; .nojekyll; PDF signature.')
