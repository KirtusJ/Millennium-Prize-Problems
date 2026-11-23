# T45 report: free lattice Maxwell 12-face covariance

Control: c(0) = **0.500000** (control.txt; 3D midpoint quad N=96: 0.50000000154, N=144: 0.50000000030).

Method: 3D midpoint quadrature (shifted grid, q=0 not a node), quad.py; tolerance = max|c_96-c_144| = 5.0e-09 (two meshes).

## c(m), m=0..8
|m|c(m)|
|-|-|
|0|0.5000000003|
|1|-0.0688747455|
|2|-0.0111527174|
|3|-0.0022622373|
|4|-0.0006053960|
|5|-0.0002131310|
|6|-0.0000933430|
|7|-0.0000476478|
|8|-0.0000270229|

## X(d)=2c(2d)+c(2d-1)+c(2d+1)
|d|X(d)|sign|mesh diff|
|-|-|-|-|
|1|-9.3442e-02|-|5.0e-09|
|2|-3.6862e-03|-|5.1e-09|
|3|-4.4746e-04|-|5.3e-09|
|4|-1.1822e-04|-|5.7e-09|
|5|-4.5132e-05|-|6.1e-09|
|6|-2.1020e-05|-|6.6e-09|
|7|-1.1120e-05|-|7.3e-09|
|8|-6.4355e-06|-|8.0e-09|
|9|-3.9827e-06|-|8.9e-09|
|10|-2.5965e-06|-|1.0e-08|
|11|-1.7649e-06|-|1.1e-08|
|12|-1.2413e-06|-|1.3e-08|
|13|-8.9822e-07|-|1.4e-08|
|14|-6.6576e-07|-|1.6e-08|
|15|-5.0368e-07|-|1.9e-08|

15/15 cases qualify (X<0 beyond mesh error); no positive X.

## N(L)
|L|N(L)|L*N(L)|bound (1/2L)Var(D0)|
|-|-|-|-|
|2|0.215563|0.431125|0.215563|
|4|0.096101|0.384404|0.107781|
|8|0.044886|0.359088|0.053891|
|16|0.021640|0.346236|0.026945|

Var(D0)=2c(0)+2c(1)=0.862251. At L=2 the bound is an equality (N(2)=Var(D0)/4 identically); L=4,8,16 strict.

## Predicates (fixed in main.py docstring before first run)
- P1 (X(d)<=0, d=1..15): **met** (15/15 negative; X(1)=-0.0934, decaying roughly like d^-3 or faster).
- P2 (L*N(L) bounded): **met** on L=2..16: 0.431, 0.384, 0.359, 0.346, decreasing, not growing. Only a finite range was measured, so asymptotic N=O(1/L) is measured only, not proven.
- Identity N(L)<=L^-2*(L/2)*Var(D0): **met** for all four L (holds given all X<=0).
- Control c(0)=1/2: met (|dev|<1e-4; actual 3e-10). No predicate failed.

## Grandchild: task id T46 (released)
Question: independent recomputation of c(1), X(1) by a 4D torus sum (N=32, 48), control c(0)=1/2 first.
Result (reread torus.py and rerun in a clean dir, identical output): c(1)=-0.06887484, c(2)=-0.01115281, c(3)=-0.00226233, X(1)=-0.09344280 at N=48 (N=32: X(1)=-0.09344438). Mine: c(1)=-0.06887475, X(1)=-0.09344242 (quad minus torus-48: c(1) 9e-8, X(1) 3.8e-7, consistent with the torus finite-size shift of ~1.6e-6 between N=32 and 48). Agreement. Caveat: it used a direct cosine sum on the p1-marginal, not an FFT; it is still an independent 4D sum. c(0) torus = 1/2 - 1/(2N^4) from omitted p=0 mode (expected).

## Rerun
```
cd /home/user/z4-workers/e1-chalA4/child   # result files are mode x: remove control.txt results/main.json first
python3 control.py; python3 main.py
cd grandchild && rm -f control.txt results.txt && python3 torus.py control && python3 torus.py results
```
PCP: pcp register K1 (control), K2 (main). `pcp_os.py verify --ws pcp` last line: result: PASS (a local fact about these files; ...). Rust `pcpos verify pcp/register.jsonl` last line: A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.
Init reported method not found (expected).
