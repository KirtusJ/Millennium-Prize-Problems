"""Predicates fixed before first run.
P1: number of lines containing \\item between the line with \\label{pf:sec-standard}
    and the next \\end{enumerate}.
P2: same count by a different method: regex over the joined block, counting
    items that start with an italic lead (\\item \\emph{...} or \\item \\textit{...}),
    plus any non-italic items counted separately; P2 total must equal P1.
Also: prose facts after the list = line starting 'We also use' following the block.
"""
import re
src = open('../paper/sec_proof.tex').read().split('\n')
s = next(i for i,l in enumerate(src) if 'label{pf:sec-standard}' in l)
e = next(i for i in range(s, len(src)) if r'\end{enumerate}' in src[i])
blk = src[s:e+1]
p1 = [s+1+i for i,l in enumerate(blk) if r'\item' in l]
text = '\n'.join(blk)
ital = re.findall(r'\\item\s*\\(?:emph|textit)\{', text)
allit = re.findall(r'\\item\b', text)
print('P1 =', len(p1), 'lines', p1)
print('P2 italic-lead =', len(ital), ' all \\item regex =', len(allit))
print('agree:', len(p1) == len(allit))
for i in p1: print(i, src[i-1][:70])
after = next((j for j in range(e+1, len(src)) if src[j].startswith('We also use')), None)
print('We also use at line', after+1 if after is not None else None)
if after is not None:
    print('prose facts after list: 3 (Weyl integration formula; Plancherel on Z^4 plus residue computation (counted as one entry by the sentence list as written: Weyl, Plancherel+residue, Isserlis))')
