# Lattice Maxwell <F12(0)F12(n e0)>, Feynman gauge
Control: control.txt = 1.0.

## Method
k0 integral closed form: int dk/2pi e^(ikn)/(A-2cos k)=r^n/sqrt(A^2-4), A=2+s1+s2+s3, r=(A-sqrt(A^2-4))/2; remaining 3D integral by midpoint rule on [0,pi]^3 (x8), N=64/128/256 (g.py).

## (a) G(0) = 0.5000000000 (|err|<1e-9; exact by hypercubic symmetry: sum_mu s_mu/khat^2=1, each term 1/4). Claim 1/2 confirmed.

## (b),(c) G(n) (N=256; N=256 vs 128 differ < 1.0e-10 absolute, so abs accuracy ~1e-10 for all n; relative error at n=16 about 6e-5 — quoted 'abs 1e-10' is a self-convergence estimate, not a proof)
| n | G(n) | sign |
|---|---|---|
| 0 | 0.5000000000 | + |
| 1 | 6.8874745800e-02 | + |
| 2 | 1.1152717700e-02 | + |
| 3 | 2.2622376000e-03 | + |
| 4 | 6.0539630000e-04 | + |
| 5 | 2.1313130000e-04 | + |
| 6 | 9.3343300000e-05 | + |
| 7 | 4.7648200000e-05 | + |
| 8 | 2.7023200000e-05 | + |
| 9 | 1.6523200000e-05 | + |
| 10 | 1.0690200000e-05 | + |
| 11 | 7.2294000000e-06 | + |
| 12 | 5.0671000000e-06 | + |
| 13 | 3.6583000000e-06 | + |
| 14 | 2.7079000000e-06 | + |
| 15 | 2.0477000000e-06 | + |
| 16 | 1.5773000000e-06 | + |

G(n)>0 for all n=1..16 (consistent with reflection positivity, F12 even under x0 reflection).

## (d) Exponent
Log-log fit n=8..16: p = 4.09 (c=0.133). Local exponents fall monotonically 4.18 -> 4.04 (n=8..16), and n^4 G(n) decreases 0.1084 -> 0.1034 toward the continuum value 1/pi^2 = 0.1013 (from -(d1^2+d2^2) of 1/(4 pi^2 x^2) at transverse zero). So asymptotically p=4, with 1/n^2 lattice corrections; the fitted 4.09 is a finite-n bias, not a different exponent. Fit-range uncertainty on p: about +-0.05.

## Predicates (g.py docstring, fixed before run)
P1 G(0)=0.5 within 1e-3: pass. P2 N=256 vs 128 < 1e-4: pass (1e-10). P3 positive: pass. P4 p in [3.7,4.3]: pass. Failed predicates: none (so none to classify).

## Grandchild (grandchild/)
Control int 4sin^2(k/2)=2 passed (2e-16). Direct 4D midpoint sums N=16..48 (no closed form): G(0)=0.5 to 2e-16; G(1)=0.0688747462 (Richardson N^-4), error est 3e-9. Mine: G(1)=0.0688747458: agrees within 4e-10. I read result.md/g4d.py outputs and RERAN the scripts in a copy (gc_rerun/): identical numbers (N=48 G1=0.068874745583685), all its predicates True. I did not audit its code line by line (it noted unused leftover arrays).

## PCP OS
Register pcp; checks K1 g_main, analysis, K3/K4 grandchild reruns. (init: method not found, expected.)

## Rerun
cd /home/user/z4-workers/a8-chalB2/child; rm -f G_results.txt analysis.txt; python3 g.py; python3 a.py
cd grandchild; rm -f results.txt control.txt; python3 control.py; python3 g4d.py
