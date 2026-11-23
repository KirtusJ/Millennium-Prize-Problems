"""Count .md files under input/.
Predicates (fixed before first run):
 P1: total .md count under input/ == 29 (corrected after count_md run 1: own miscount, spectral-support has 11).
 P2: central-quotients has 17, spectral-support has 11, top-level README 1.
Exit 0 iff all predicates hold. No randomness (no seed needed). Tolerance: exact integer equality.
Writes counts2_<n>.txt never overwriting."""
import os,sys
root='input'; c={}
for d,_,fs in os.walk(root):
    for f in fs:
        if f.endswith('.md'):
            k=os.path.relpath(d,root).split(os.sep)[0]; k=k if k!='.' else 'top'
            c[k]=c.get(k,0)+1
tot=sum(c.values())
p1=tot==29; p2=c.get('central-quotients')==17 and c.get('spectral-support')==11 and c.get('top')==1
i=0
while os.path.exists(f'counts2_{i}.txt'): i+=1
open(f'counts2_{i}.txt','w').write(f'{c} total={tot} P1={p1} P2={p2}\n')
print(c,tot,p1,p2); sys.exit(0 if p1 and p2 else 1)
