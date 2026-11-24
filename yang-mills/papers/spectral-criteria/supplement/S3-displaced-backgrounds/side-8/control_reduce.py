"""Control part 2 (written after C1/C2 failed; C3a fixed before running this, C3b/C4 are post hoc replacements, labelled as such).
C2' (post hoc): mix8 delta=0 columns 1-5 byte-identical to my build of G4's unchanged binary, 4 streams.
C3a: reduce.py applied to G4's ARCHIVED minus8 streams gives four-face ratio within 1e-4 of 0.0441 and error within 1e-4 of 0.0020,
     one-face ratio within 1e-4 of 0.0592(29), variance within 1e-5 of 0.05877 (tolerance: rounding of the published table).
C4 (post hoc, replaces C3): reduce.py on my replay of the same design (different floating-point trajectory) gives four-face ratio
     within 2*sqrt(e_mine^2+0.0020^2) of 0.0441 (tolerance: 2 sigma combined stream-jackknife errors).
"""
import json, subprocess, sys
r=lambda files: json.loads(subprocess.run([sys.executable,"reduce.py","x"]+files,capture_output=True,check=True,text=True).stdout)
ok=True
c2=all(open(f"results/control/g4bin-minus8-s{i}.csv").read().splitlines()[1:]==[",".join(l.split(",")[:5]) for l in open(f"results/control/mix8-delta0-replay-s{i}.csv").read().splitlines()[1:]] for i in range(4))
print("C2'", "MET" if c2 else "FAILED"); ok&=c2
g=r([f"g4/full-complement/unz_fixed/minus8-s{i}.csv" for i in range(4)])["estimates"]
print("G4 archive reduced:",{k:[round(v[0],6),round(v[1],6)] for k,v in g.items()})
c3=abs(g["ratio_average"][0]-0.0441)<=1e-4 and abs(g["ratio_average"][1]-0.0020)<=1e-4 and abs(g["ratio_single"][0]-0.0592)<=1e-4 and abs(g["var_average"][0]-0.05877)<=1e-5
print("C3a","MET" if c3 else "FAILED"); ok&=c3
m=r([f"results/control/g4bin-minus8-s{i}.csv" for i in range(4)])
e=m["estimates"]; print("my replay reduced:",{k:[round(v[0],6),round(v[1],6)] for k,v in e.items()})
print("per-stream four-face ratios:",[round(p["ratio_average"],4) for p in m["per_stream"]])
c4=abs(e["ratio_average"][0]-0.0441)<=2*(e["ratio_average"][1]**2+0.0020**2)**.5
print("C4","MET" if c4 else "FAILED"); ok&=c4
with open("results/control/control_reduce.json","x") as f: json.dump({"G4_archive":g,"my_replay":m},f,indent=1)
sys.exit(0 if ok else 1)
