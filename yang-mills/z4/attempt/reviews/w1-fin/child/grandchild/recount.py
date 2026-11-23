"""Predicates (stated before running):
H0 (unmerged hunk): one non-'equal' difflib.SequenceMatcher opcode on line lists
   (autojunk=False), orig range a[i1:i2], patched range b[j1:j2], reported 1-based inclusive;
   empty range shown as 'none (after line N)'.
H3 (merged hunk): consecutive non-equal opcodes joined when the 'equal' block between
   them has <=3 lines.
Proof block: \\begin{proof} ... \\end{proof} found by regex on patched lines (lines with a
   % comment prefix ignored; text after an unescaped % stripped). Stack-matched, so nesting is
   detected; a block spans begin line..end line inclusive; unclosed begin -> flagged, spans to EOF.
   An \\end{proof} with no open begin is reported as stray.
Inside test (hunk's patched lines vs union of proof spans): yes = every patched line of the hunk
   in a span; partly = some but not all; no = none. Pure deletion (empty patched range after line N):
   yes if some span has begin<=N<end, else no.
"""
import difflib, re
a = open('orig_in/tun_lower.tex').read().split('\n')
b = open('patched_in/tun_lower.tex').read().split('\n')
if a and a[-1]=='': a.pop()
if b and b[-1]=='': b.pop()
ops=[o for o in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes()]
nz=[o for o in ops if o[0]!='equal']
def merge(nz,gap):
    out=[]
    for o in nz:
        if out and o[1]-out[-1][2]<=gap and o[3]-out[-1][4]<=gap:
            p=out[-1]; out[-1]=('merged',p[1],o[2],p[3],o[4])
        else: out.append(o)
    return out
h3=merge(nz,3)
def rng(l,h):
    return f'{l+1}-{h}' if h>l else f'none(after {l})'
# proofs
spans=[];stack=[];notes=[]
for n,l in enumerate(b,1):
    s=re.sub(r'(?<!\\)%.*','',l)
    for m in re.finditer(r'\\(begin|end)\{proof\}',s):
        if m.group(1)=='begin':
            if stack: notes.append(f'nested begin at {n} inside begin at {stack[-1]}')
            stack.append(n)
        else:
            if stack: spans.append((stack.pop(),n))
            else: notes.append(f'stray end at {n}')
for st in stack:
    notes.append(f'unclosed begin at {st}'); spans.append((st,len(b)))
spans.sort()
def inside(j1,j2):
    if j2==j1:
        return 'yes' if any(s<=j1<e for s,e in spans) else 'no'
    L=range(j1+1,j2+1)
    c=sum(any(s<=x<=e for s,e in spans) for x in L)
    return 'yes' if c==len(L) else 'no' if c==0 else 'partly'
out=[]
out.append(f'lines orig={len(a)} patched={len(b)}')
out.append(f'unmerged hunks (plain opcodes): {len(nz)}')
out.append(f'merged hunks (gap<=3): {len(h3)}')
out.append('proof blocks (patched): '+str(spans)); out.append('notes: '+str(notes))
for name,hs in (('UNMERGED',nz),('MERGED',h3)):
    out.append(f'--- {name}')
    for k,o in enumerate(hs,1):
        out.append(f'{k}\t{o[0]}\torig {rng(o[1],o[2])}\tpatched {rng(o[3],o[4])}\tinside_proof={inside(o[3],o[4])}')
t='\n'.join(out)
with open('recount_result.txt','x') as f: f.write(t+'\n')
print(t)
