# Z_n gap asymptote report

Derivation. x=exp(-beta d), c=cos(2pi/n), d=1-c. lam0=1+2x+..., lam1=1+2cx+... so m=2d x-2d(1+c)x^2+..., hence M=beta m = A(N) with k=2 (k=1 only n=2, single j=1 term), and
M/A-1 = -(1+c) x + (higher powers of x from j>=2 plaquettes). n=4 is exact: lam0=(1+x)^2, lam1=1-x^2, m=ln((1+x)/(1-x)), so M/A-1 = +x^2/3+..., x=e^{-N^2}. n=6: -(3/2) e^{-N^2/2}.

| n | N | M(N) | M/A | M/A-1 | predicted leading |
|---|---|------|-----|-------|------|
| 3 | 2 | 0.0297083430418238 | 0.998766749169272 | -0.0012332508 | -0.0012393761 |
| 3 | 4 | 1.81206458121976e-9 | 0.999999999981124 | -1.8875673e-11 | -1.8875673e-11 |
| 3 | 8 | 3.89969791245084e-40 | 1.0 | -1.0155463e-42 | -1.0155463e-42 |
| 3 | 16 | 1.30701378830724e-164 | 1.0 | -8.5092044e-168 | -8.5092044e-168 |
| 4 | 2 | 0.146541498974785 | 1.0001118433884 | 0.00011184339 | 0.00011182088 |
| 4 | 4 | 3.60112559101631e-6 | 1.0 | 4.2213885e-15 | 4.2213885e-15 |
| 4 | 8 | 2.05287793990226e-26 | 1.0 | 8.5740312e-57 | 8.5740312e-57 |
| 4 | 16 | 3.38752566103526e-109 | 1.0 | 1.4591637e-223 | 1.4591637e-223 |
| 5 | 2 | 0.331703482839321 | 0.951816225855101 | -0.048183774 | -0.082524872 |
| 5 | 4 | 0.000349274340180667 | 0.99997936727571 | -2.0632724e-5 | -2.0677764e-5 |
| 5 | 8 | 5.50694227662368e-18 | 1.0 | -8.1503916e-20 | -8.1503916e-20 |
| 5 | 16 | 5.31704187502133e-75 | 1.0 | -1.9673337e-77 | -1.9673337e-77 |
| 6 | 2 | 0.477021696171036 | 0.881185018353709 | -0.11881498 | -0.20300292 |
| 6 | 4 | 0.00536470442232817 | 0.999497405991078 | -0.00050259401 | -0.00050319394 |
| 6 | 8 | 8.10506595142012e-13 | 0.999999999999981 | -1.8996248e-14 | -1.8996248e-14 |
| 6 | 16 | 6.58485599396458e-54 | 1.0 | -3.8583141e-56 | -3.8583141e-56 |

Shrink of |M/A-1| (N->2N): n=4: 2.6e10, 4.9e41, 5.9e166 (N=2->4, 4->8, 8->16); n=6: 236, 2.6e10, 4.9e41. This is x_N -> x_N^4, as predicted (error ~ exp(-N^2 d), N^2 quadruples).
Numbers agree with the analytic leading term to <0.5% for N>=4 (n=5,6 at N=2 only ~58%: higher orders matter when x~0.1).

Verdict. k=2 is correct for n=4 and n=6 (and n=3,5): M/A -> 1, not 1/2. The relative error is tiny and vanishes super-exponentially: -(1+cos(2pi/n))e^{-N^2 d} (n=6: -1.5 e^{-N^2/2}; n=4: +e^{-2N^2}/3, since the O(x) term cancels as c=0 and j=2 compensates). Caveat: run 1 at 320 digits failed P3 at N=16 for n=3,4 from precision floor; rerun at 900 digits passed (kept both). Control -ln tanh 1 = 0.272341.

PCP verify last line: result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)
