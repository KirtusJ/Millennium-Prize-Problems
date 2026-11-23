"""Reads results_main.json + control.txt; checks the predicates P1-P5 of main.py (fixed there). Exit 1 if any FAIL (expected: P4 and Q2-upper-as-stated)."""
import json,sys,math
R=json.load(open("results_main.json")); c=float(open("control.txt").read())
bad=0
def chk(n,ok):
    global bad; print(("PASS " if ok else "FAIL ")+n); bad+=(not ok)
chk("control c*=4.605413",abs(c-4.605413)<1e-6)
for b,r in R.items():
    chk(f"b={b} P1 sector-vs-literal flux<1e-10",r["flux_rel_diff_sector_vs_literal"]<1e-10)
    if "plain_rel_diff" in r: chk(f"b={b} P1 plain subtraction vs flux <1e-4 ({r['plain_rel_diff']:.1e})",r["plain_rel_diff"]<1e-4)
    chk(f"b={b} Q2 lower holds ratio {r['r_lower']:.3f}",r["r_lower"]<=1)
    chk(f"b={b} Q2 upper as stated (factor 2) ratio {r['r_upper_stated']:.3f}",r["r_upper_stated"]>=1)
    chk(f"b={b} Q2 upper factor 4 ratio {r['r_upper4']:.3f}",r["r_upper4"]>=1)
    chk(f"b={b} P4 N vs 2N conv<1e-3 ({r.get('conv_rel',float('nan')):.1e})",r.get("conv_rel",1)<1e-3)
    chk(f"b={b} P5 residual<1e-10 and f>0 in A",max(r["resid_e"],r["resid_o"])<1e-10 and r["f_pos_in_A_interior"])
v=[R[b]["neglogD_over_sb"] for b in ("16","64","256","1024","4096")]
chk("P3 |v-c*| decreasing: "+str([round(x,4) for x in v]),all(abs(v[i]-c)>abs(v[i+1]-c) for i in range(4)))
sys.exit(1 if bad else 0)
