"""extract.py - extract text of fetched PDFs into ref/text/ and check page-1 identity.

Predicates (fixed before first run):
 E1 (for all fetched PDFs): pypdf opens the file and page 1 yields >= 200 characters of text.
    Tolerance 200 chars: an arbitrary floor separating a text layer from a scanned image.
 E2 (per file): the expected first-author surname appears (case-insensitive, accents stripped)
    in page-1 text. Expected: cmr->Cordes, witten->Witten, levy->Levy, plaq->(none fixed; measured only),
    teper->Teper.
 E3 (per file): an expected title keyword appears on page 1: cmr->"Lectures on 2D Yang",
    witten->"Two Dimensional Gauge Theories Revisited", levy->"Yang-Mills measure",
    teper->"glueball". Matching is case-insensitive, whitespace collapsed.
Hypothesis count for E1 is reported first. No result file is overwritten (refuses if exists).
Usage: python -I extract.py <ref dir> <out json>
"""
import sys, os, json, re, unicodedata
sys.path.append('C:/Users/donke/AppData/Roaming/Python/Python314/site-packages')
import pypdf

ref, out = sys.argv[1], sys.argv[2]
if os.path.exists(out):
    sys.exit("refuse to overwrite " + out)
exp = {'cmr': ('cordes', 'lectures on 2d yang'), 'witten': ('witten', 'two dimensional gauge theories revisited'),
       'levy': ('levy', 'yang-mills measure'), 'plaq': (None, None), 'teper': ('teper', 'glueball')}
def norm(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'\s+', ' ', s)
os.makedirs(os.path.join(ref, 'text'), exist_ok=True)
res, fails = {}, 0
for k, (au, ti) in exp.items():
    p = os.path.join(ref, k + '.pdf')
    r = pypdf.PdfReader(p)
    pages = [pg.extract_text() or '' for pg in r.pages]
    tp = os.path.join(ref, 'text', k + '.txt')
    if not os.path.exists(tp):
        with open(tp, 'w', encoding='utf-8') as f:
            for i, t in enumerate(pages):
                f.write(f'\n=== PAGE {i+1} ===\n{t}')
    p1 = norm(pages[0])
    e1 = len(pages[0]) >= 200
    e2 = None if au is None else (au in p1)
    e3 = None if ti is None else (ti in p1)
    for e in (e1, e2, e3):
        if e is False: fails += 1
    res[k] = dict(bytes=os.path.getsize(p), pages=len(pages), E1=e1, E2=e2, E3=e3, page1_head=p1[:300])
    print(k, len(pages), e1, e2, e3, '|', p1[:160])
print('E1 qualifying:', sum(v['E1'] for v in res.values()), 'of', len(res))
with open(out, 'w', encoding='utf-8') as f:
    json.dump(res, f, indent=1)
print('failed predicates:', fails)
sys.exit(1 if fails else 0)
