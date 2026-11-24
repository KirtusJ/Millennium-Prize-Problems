"""Reduce all z1-mix8 runs (mix deltas, clear skeletons) with reduce.py; write results/summary_<tag>.json (mode x)
and print a compact table. Adds: beta*ratio, min angle from -I from the .meta files, integrated autocorrelation
time of f4 per stream (Sokal window c=5, descriptive only), and colour labels plane/parity (k = 8*o + px + 2py + 4pz,
o: 0=xy, 1=xz, 2=yz). Predicates are those of reduce.py (T1, T1b, S1) and C5 (run_mix.py docstring).
Usage: python3 analyze_all.py <tag>
"""
import json, subprocess, sys, glob, re, numpy as np
B=3.399810242; tag=sys.argv[1]
def tau(x):
    x=x-x.mean(); n=len(x); c=np.correlate(x,x,"full")[n-1:]/np.arange(n,0,-1); c/=c[0]; t=0.5
    for w in range(1,n//4):
        t+=c[w]
        if w>=5*t: break
    return float(t)
groups={}
for f in sorted(glob.glob("results/mix/*.csv")):
    k=re.search(r"/(d\d-c[0-9.]+)-s",f).group(1); groups.setdefault("mix "+k,[]).append(f)
for f in sorted(glob.glob("results/clear/runs/*.csv")):
    k=re.search(r"/(k\d-chain\w-cfg\d+)-s",f).group(1); groups.setdefault("clear "+k,[]).append(f)
out={}
lab=[f"{p}-{k&1}{(k>>1)&1}{(k>>2)&1}" for p in ("xy","xz","yz") for k in range(8)]
for g,files in groups.items():
    # only complete streams
    def complete(f):
        try: m=json.loads(open(f[:-4]+".meta").readline())
        except Exception: return False
        return sum(1 for _ in open(f))==m["samples"]+1
    files=[f for f in files if complete(f)]
    if len(files)<2: print(g,"skipped: fewer than 2 complete streams"); continue
    r=json.loads(subprocess.run([sys.executable,"reduce.py",g]+files,capture_output=True,text=True,check=True).stdout)
    metas=[json.loads(open(f[:-4]+".meta").readline()) for f in files]
    r["min_angle_from_minusI"]=sorted(set(round(m["min_angle_from_minusI"],12) for m in metas))
    r["W"]=metas[0]["W"]; r["B_holonomy"]=metas[0]["B_holonomy"]
    r["beta_times_ratio_average"]=[B*v for v in r["estimates"]["ratio_average"]]
    r["beta_times_ratio_single"]=[B*v for v in r["estimates"]["ratio_single"]]
    r["tau_int_f4_per_stream"]=[tau(np.loadtxt(f,delimiter=",",skiprows=1,usecols=1)) for f in files]
    r["colour_labels"]=lab
    out[g]=r
with open(f"results/summary_{tag}.json","x") as f: json.dump(out,f,indent=1)
for g,r in out.items():
    e=r["estimates"]; fmt=lambda k: f"{e[k][0]:.5f}({e[k][1]:.5f})"
    print(f"{g}: n={r['n_streams']} rows={r['rows_per_stream'][0]} minang={r['min_angle_from_minusI']}")
    print(f"   J1={fmt('J_single')} J4={fmt('J_average')} V1={fmt('var_single')} V4={fmt('var_average')} r1={fmt('ratio_single')} r4={fmt('ratio_average')} spread={fmt('spread')}")
    print(f"   beta*r4={r['beta_times_ratio_average'][0]:.4f}({r['beta_times_ratio_average'][1]:.4f}) beta*r1={r['beta_times_ratio_single'][0]:.4f}  T1={r.get('T1_ratio_hot_cold')} T1b={r.get('T1b_var_hot_cold')} S1={r['S1_streams_ge_4']}")
    if "hot" in r: print(f"   hot r4={r['hot']['ratio_average']} cold r4={r['cold']['ratio_average']} hot V4={r['hot']['var_average']} cold V4={r['cold']['var_average']}")
    print("   per-stream r4:",[round(p["ratio_average"],4) for p in r["per_stream"]]," V4:",[round(p["var_average"],4) for p in r["per_stream"]]," mean f4:",[round(p["mean_average"],3) for p in r["per_stream"]])
    print("   tau_f4:",[round(t,1) for t in r["tau_int_f4_per_stream"]])
    if "per_colour" in r:
        for t in ("single","average"):
            fr=np.array(r["per_colour"][t]["fraction_of_sum"]); idx=np.argsort(-fr)
            print(f"   colour shares {t}: "+", ".join(f"{lab[i]}:{fr[i]:.3f}" for i in idx[:8])+f" | rest {fr[idx[8:]].sum():.3f}")
