"""Perturbed -I backgrounds, side 8, period 16, beta 3.399810242.
W_delta = -cos(delta) + k sin(delta) placed on the first fine half of the coarse y edge at (2,0,0) (all other
skeleton links identity), z edge at (2,0,0) first half = i, so B = i = e_x held fixed, displacement axis e_z
(G4 sparse-coarse-fields/disk.md convention W_delta=-cos d + e_z sin d, B=e_x).  delta in {0, .5/b, 1/b, 2/b}.
Design: 8 streams per delta, stream i: seed = 3000451 + 100000*k + 7919*i, hot = i%2 (4 hot, 4 cold),
864 discarded conditional sweeps, 512 measurements 6 sweeps apart. 2 processes in parallel.
Predicates (fixed before the run): S1 >= 4 streams per run; T1/T1b hot-vs-cold agreement (see reduce.py);
C5 (long control, pre-registered before this run): delta=0 four-face ratio within 2 combined sigma of at least
one of G4's side-8 values 0.0441(20), 0.0506(13).  Files opened with mode "x".
"""
import subprocess, sys, math
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
B=3.399810242; MIX=str(Path("build/g4/mix8/mix8").resolve())
out=Path("results/mix"); out.mkdir(parents=True,exist_ok=True)
jobs=[]
for k,c in enumerate([0,0.5,1,2]):
    d=repr(c/B) if c else "0"
    for i in range(8):
        jobs.append((k,c,d,i,3000451+100000*k+7919*i,i%2))
def run(j):
    k,c,d,i,seed,hot=j
    name=out/f"d{k}-c{c}-s{i}-{'hot' if hot else 'cold'}"
    with open(str(name)+".csv","x") as fo, open(str(name)+".meta","x") as fe:
        r=subprocess.run([MIX,"mix",repr(B),str(seed),str(hot),"864","512","8","16",d],stdout=fo,stderr=fe)
        fe.write(f'{{"cmd":"{MIX} mix {B!r} {seed} {hot} 864 512 8 16 {d}"}}\n')
    return r.returncode
with ThreadPoolExecutor(2) as ex: codes=list(ex.map(run,jobs))
print(codes); sys.exit(max(codes))
