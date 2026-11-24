"""Sampled clear backgrounds, side 8, period 16, beta 3.399810242.
Stage A (gen): 2 independent unconditioned chains (G4 pilot cycle = heat-bath sweep + reflection sweep), hot start,
  seeds 4000451 and 4100451, 200 discarded cycles, then 30 configurations 10 cycles apart per chain (60 skeletons).
  For each: slice-0 frozen links dumped (text), and the angle from -I, arccos(-Re U), of all 192 coarse 2x2 spatial faces.
Selection rule (fixed before the run): threshold theta = pi/4 (G4 gate range 0<theta<=pi/4). Keep the FIRST three skeletons
  (order: chain A cfg0..29, then chain B cfg0..29) with min angle > pi/4. If fewer than 3 qualify, use theta = pi/8 with
  the same rule. If still fewer than 3, take the 3 with the largest min angle, labelled 'max-clearance' (not clear at pi/8).
  Rule 4: the number qualifying at each threshold is reported.
Stage B (clear): each kept skeleton frozen as sampled (no gauge fixing); B := normalised traceless part of the actual xz
  coarse holonomy at the origin (tests Re(Bhat g1), Re(Bhat gbar)); the raw-holonomy versions Re(H g1), Re(H gbar)
  (G4's code literally) are measured as well. 8 streams per skeleton, seed 5000451+100000*m+7919*i, hot=i%2,
  864 discarded conditional sweeps, 256 measurements 6 sweeps apart.
Predicates: P_gen: chain plaquette average of first and second half of the 30 configs agree within 0.002 (tolerance:
  ~3x typical stream fluctuation of the volume-averaged plaquette at this size; a thermalisation sanity check only).
  S1 >= 4 streams; T1/T1b hot-vs-cold (reduce.py).  Files opened with "x".
"""
import subprocess, sys, math, json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
B=3.399810242; MIX=str(Path("build/g4/mix8/mix8").resolve())
gd=Path("results/clear/skeletons"); gd.mkdir(parents=True,exist_ok=True)
def gen(c):
    name,seed=c
    with open(gd/f"{name}.csv","x") as fo:
        return subprocess.run([MIX,"gen",repr(B),str(seed),"200","30","10","8","16",str(gd/name)],stdout=fo).returncode
with ThreadPoolExecutor(2) as ex: codes=list(ex.map(gen,[("chainA",4000451),("chainB",4100451)]))
assert codes==[0,0]
allc=[]; summ={}
for ch in ("chainA","chainB"):
    rows=[l.split(",") for l in open(gd/f"{ch}.csv").read().splitlines()[1:]]
    plaq=[float(r[4]) for r in rows]; h1=sum(plaq[:15])/15; h2=sum(plaq[15:])/15
    summ[ch]={"plaq_first_half":h1,"plaq_second_half":h2,"P_gen":"MET" if abs(h1-h2)<=0.002 else "FAILED"}
    for r in rows: allc.append({"chain":ch,"cfg":int(r[0]),"min_angle":float(r[1]),"mean_angle":float(r[2]),"n_le_pi4":int(r[3])})
counts={t:sum(c["min_angle"]>v for c in allc) for t,v in (("pi/4",math.pi/4),("pi/8",math.pi/8))}
kept=[c for c in allc if c["min_angle"]>math.pi/4][:3]; rule="pi/4"
if len(kept)<3: kept=[c for c in allc if c["min_angle"]>math.pi/8][:3]; rule="pi/8"
if len(kept)<3: kept=sorted(allc,key=lambda c:-c["min_angle"])[:3]; rule="max-clearance"
sel={"chains":summ,"n_sampled":len(allc),"n_qualifying":counts,"rule_used":rule,"kept":kept,"all":allc}
with open("results/clear/selection.json","x") as f: json.dump(sel,f,indent=1)
print(json.dumps({k:sel[k] for k in ("chains","n_sampled","n_qualifying","rule_used","kept")},indent=1))
od=Path("results/clear/runs"); od.mkdir(parents=True,exist_ok=True)
jobs=[(m,c,i,5000451+100000*m+7919*i,i%2) for m,c in enumerate(kept) for i in range(8)]
def run(j):
    m,c,i,seed,hot=j
    sk=str((gd/f"{c['chain']}-cfg{c['cfg']}.skel").resolve())
    name=od/f"k{m}-{c['chain']}-cfg{c['cfg']}-s{i}-{'hot' if hot else 'cold'}"
    with open(str(name)+".csv","x") as fo, open(str(name)+".meta","x") as fe:
        r=subprocess.run([MIX,"clear",repr(B),str(seed),str(hot),"864","256","8","16",sk],stdout=fo,stderr=fe)
        fe.write(json.dumps({"cmd":f"{MIX} clear {B!r} {seed} {hot} 864 256 8 16 {sk}"})+"\n")
    return r.returncode
with ThreadPoolExecutor(2) as ex: codes=list(ex.map(run,jobs))
print(codes); sys.exit(max(codes))
