"""CONTROL for z1-mix8 (side 8, period 16, beta 3.399810242, W=-I, B=i).

Predicates (fixed before the first run):
C1 (bit replay of G4's binary): G4's replicas.rs built unchanged, run as
   `replicas fixed 3.399810242 <1800451+7919 i> <i%2> 288 144 8 16 -1`, i=0..3,
   produces stdout byte-identical to g4/full-complement/unz_fixed/minus8-s<i>.csv.
   Tolerance: exact (deterministic SplitMix64 + same arithmetic); any byte difference fails.
C2 (my modified program = G4 at delta=0): `mix8 mix 3.399810242 <same seed> <same hot> 288 144 8 16 0`
   gives, in its first five columns, strings identical to G4's five columns. Tolerance: exact.
C3 (reduction): my own reduction (reduce.py, pooled plug-in variance, delete-one-stream
   jackknife) of the four replayed streams gives four-face J/Var within 1e-4 of G4's
   published 0.0441 and its error within 1e-4 of 0.0020 (tolerance = rounding of the
   published 4-decimal table entry).
Result files are opened with mode "x" (never overwritten).
"""
import subprocess, sys, os, filecmp
from pathlib import Path
root=Path(__file__).resolve().parent
G4BIN=root/"build/g4/full-complement/replicas"; MIX=root/"build/g4/mix8/mix8"
out=root/"results/control"; out.mkdir(parents=True,exist_ok=True)
ok={"C1":True,"C2":True}
for i in range(4):
    seed=1800451+7919*i; hot=i%2
    r=subprocess.run([str(G4BIN),"fixed","3.399810242",str(seed),str(hot),"288","144","8","16","-1"],capture_output=True,check=True)
    with open(out/f"g4bin-minus8-s{i}.csv","xb") as f: f.write(r.stdout)
    ref=(root/f"g4/full-complement/unz_fixed/minus8-s{i}.csv").read_bytes()
    same=r.stdout==ref; ok["C1"]&=same
    print(f"C1 stream {i} seed {seed} hot {hot}: byte-identical={same}")
    r2=subprocess.run([str(MIX),"mix","3.399810242",str(seed),str(hot),"288","144","8","16","0"],capture_output=True,check=True)
    with open(out/f"mix8-delta0-replay-s{i}.csv","xb") as f: f.write(r2.stdout)
    with open(out/f"mix8-delta0-replay-s{i}.meta","xb") as f: f.write(r2.stderr)
    a=[",".join(l.split(",")[:5]) for l in r2.stdout.decode().splitlines()[1:]]
    b=ref.decode().splitlines()[1:]
    same2=a==b; ok["C2"]&=same2
    print(f"C2 stream {i}: first-5-columns identical={same2} ({len(a)} rows)")
print("C1", "MET" if ok["C1"] else "FAILED"); print("C2", "MET" if ok["C2"] else "FAILED")
sys.exit(0 if all(ok.values()) else 1)
