# notes.md — h1-chal (T87), challenger of SCALING_LIMIT.md
## Step 0 (17:2x) control
control.txt = 0.272341 (-ln tanh 1). Register pcp initialised. Lean READY exists (not used so far).
## Step 1 child started (T93, child-run1 in background, product-Gaussian trial quotient, NO cutoff — see later)
## Step 2 citation read (fetch sub-agent): arXiv:1606.02008 Ruiz-Antolin & Segura, "A new type of sharp bounds for ratios of modified Bessel functions", 2016, HTML v1, Thm 2 read verbatim by sub-agent: I_v/I_{v-1} < x/(v-1/2+sqrt((v-1/2)^2+x^2)) (v>=1/2), > x/(v+sqrt(v^2+x^2)) (v>=0). After shift v->v+1 this is exactly U1's sandwich. Attribution in paper: Segura / Laforgia-Natalini, not Amos. RS XIII.47/67 and Simon 1983: NOT reachable (search blocked / 403).
## Step 3 desk check of SCALING_LIMIT (before numerics)
- L3: identity sign. Sum_a <chi g,K chi g> = <g,Kg> - 1/2 iint k g g sum(dchi)^2, hence <g,(1-K)g> = sum<chi g,(1-K)chi g> MINUS 1/2 iint ... The text has PLUS. Downstream bound only uses |term| (Schur), so consequence survives.
- L4: arithmetic: 5 pi^2 ||B||/M^2 with ||B||<=2 b s^2, M^2=b/2 gives 20 pi^2 s^2 = 197 s^2, not 98.7 s^2. With 197: sqrt2 s - 197 s^2 >= s needs s <= 0.0021, so s_*=0.002 still (barely) works modulo o(s). My own count (only d in {0,+-2}, pinching) gives 8 pi^2 = 79 s^2.
- U4: e^b/Z^2 bound is valid (crude); Z lower bound OK.
- Gaussian trial without cutoff: <g,Wg> explodes (exponent 2b at a1=a2=pi/2 beats Gaussian decay for b>=~100). Compact support (C3) is essential; child's trial lacks it (my prompt's choice).
## Step 4 child T93 returned (child-run1 = register check K2, exit 0, 188 s). Control graded FIRST: 2.000000 and 0.697775 both correct.
Child: Gaussian trial w/o cutoff -> ln<g,Wg> = 18.79 (b=64), 224 (256), 1301 (1024); Q=1 to double precision; b^{1/3}nu = 121, 1512, 13280. Grandchild T94 (admitted/released by child) recomputed ||g1||^2 and <g1,K g1> at b=64, agrees 1e-13.
My rerun (independent quadrature): ||g1||^2 = 0.0043220870387298 (child 0.0043220870387314), ln<g,Wg> = 18.7931 (child 18.79). REPRODUCED.
Grading: the failure is of MY prompt's trial (no compact support), not of the target: U4/U5 use C3's compactly supported phi (|Y|<=R), so the exploding region a~pi/2 is outside. It does confirm that compact support (or decay faster than e^{-2b a^4}) is necessary — the text says so (U5 last bullet). Child's "fixed R=0.8 does not rescue" uses R in a-units, not the doc's |Y|<=R (a<=R b^{-1/3}); not applicable. T93 released (event 186).
## Step 5 chal-run2 killed at ~1.5 min: numpy used ~2 cores (rule 8 breach, my defect). Rerun as chal-run3 with OMP/OPENBLAS_NUM_THREADS=1 under taskset -c 0.
## Step 6 results chal-run3 (K4, exit 0, 257 s, 1 core) -> results/chal_run3.json
P1 18361/18361 met (min rel slack 9.1e-13); P2 18361/18361 met (2.5e-9); P3 2807 met; P4 2807 met; P5 71407 met; P6 met; P7 met; P8 met (1.1e-15);
P9 FAILED (a'=2.33711: my shooting overshot r=0 by one step; own defect) -> repaired in chal2 Q1: a'=2.3381074105, E0_lower=2.94583 met.
P10 ('+' sign as written in L3) FAILED: lhs=+0.070669, '+' term=-0.070669. P11 ('-' sign) met to 2e-14. => L3 identity has the wrong sign; DEFECT of target (harmless downstream). P12 met (ratio 0.0026).
P13 (L4) 48/48 claimed cases met at b=1e3..1e6; lam/s -> 2 as b grows; truncation diff <=1.4e-16. Cap (measured): b=1e3, s=1: lam=0.991 < s-1/b=0.999 (outside claim; shows cap needed).
P14 (a),(b) met 4/4; (c) chain bound infinite at all b (e^{R^4 b^{-1/3}/2} with R=4) -> vacuous; b^{1/3}nu_trial = 28.4, 11.2, 3.688, 3.629 at b=64,256,1024,4096 vs E_trial 3.5717; b^{1/3}d = 99, 49, 1.17, 0.92; minus E_0 = +25, +7.9, +0.34, +0.28.
cf-vs-quadrature cross-check 0.996 (my check invalid: cancellation points). chal2 Q2 (repaired) FAILED at 1.05e-6 > 1e-8; source (CF vs quadrature) not resolved in budget.
