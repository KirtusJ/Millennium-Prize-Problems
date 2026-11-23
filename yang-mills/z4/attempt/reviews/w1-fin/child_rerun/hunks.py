"""T186 hunk lister. Predicates fixed before first run:
 P1 main.tex identical orig/patched; P2 preamble.tex identical;
 P3 hunk count of tun_upper.tex and tun_lower.tex is whatever difflib (SequenceMatcher, autojunk=False) reports -- measured only;
 P4 every hunk is printed with patched line numbers; P5 no hunk inside \\begin{proof}..\\end{proof} (patched file) -- measured per hunk.
Tolerance: none (exact text comparison). Output file opened with mode 'x'."""
import difflib,re,sys
out=open(sys.argv[1],'x')
def w(s): print(s); out.write(s+'\n')
for n in ['main.tex','preamble.tex','tun_upper.tex','tun_lower.tex']:
    a=open('orig/'+n).read().split('\n'); b=open('patched/'+n).read().split('\n')
    if a==b: w(f'{n}: IDENTICAL (P met)'); continue
    sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
    ops=[o for o in sm.get_opcodes() if o[0]!='equal']
    # proof blocks in patched
    inproof=[];st=None
    for i,l in enumerate(b,1):
        if r'\begin{proof}' in l: st=i
        if r'\end{proof}' in l and st: inproof.append((st,i)); st=None
    w(f'{n}: DIFFERS, {len(ops)} opcodes, {len(inproof)} proof blocks')
    # merge opcodes closer than 3 lines into hunks
    hs=[]
    for o in ops:
        if hs and o[3]-hs[-1][-1][4]<=3: hs[-1].append(o)
        else: hs.append([o])
    w(f'{n}: {len(hs)} hunks (merged if gap<=3 lines)')
    for k,h in enumerate(hs,1):
        i1,i2,j1,j2=h[0][1],h[-1][2],h[0][3],h[-1][4]
        ip=[p for p in inproof if not(j2<p[0] or j1+1>p[1])]
        w(f'--- {n} H{k}: orig {i1+1}-{i2} -> patched {j1+1}-{j2}; overlaps proof block {ip}')
        for l in a[i1:i2]: w('  - '+l)
        for l in b[j1:j2]: w('  + '+l)
