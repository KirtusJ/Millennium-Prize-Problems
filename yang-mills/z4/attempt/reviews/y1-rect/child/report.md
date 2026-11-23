# T197 report: W12 > 0 on 4D SU(2) Wilson lattice (MC)
Control: control.txt = 0.480000 (exact 12/25).

## Verdicts
| item | verdict | evidence |
|---|---|---|
| W12 > 0 at beta in {0.5,1,2,2.3,3.4}, L=4 | STANDS | 5/5 cases qualify (W12 > 3 sigma); W12/err = 85, 300, 430, 536, 2274 |
| same at L=6 (beta 0.5, 2.3, 3.4 only) | STANDS | W12/err = 103, 777, 2670 |
| 0 < W12 < W11, W11 increasing in beta | STANDS | all 8 cases; L=4 W11 monotone |
| beta=0.5: W11 ~ u | STANDS (within my tolerance) | L=4 +1.3 sigma, L=6 +2.2 sigma, diff 3-4e-4 |
| beta=0.5: W12 ~ u^2 | STANDS (within my tolerance) | L=4 +1.1 sigma, L=6 +1.8 sigma |
| update correctness | STANDS | cold vs hot start W11 diff -0.75 sigma; W11(2.3)~0.60 as expected for SU(2); sub-agent's independent code agrees |
| reflection positivity for all beta>=0 | NOT CHECKED | only 5 betas, 2 sizes tested |
| continuum/larger L | NOT CHECKED | |

## Measured (heatbath + 2 overrelaxation sweeps; errors by blocking, plateau max)
u(0.5)=I2/I1=0.123718, u^2=0.015306 (power series).
| beta | L | sweeps (therm+meas) | W11 | W12 |
|---|---|---|---|---|
| 0.5 | 4 | 400+3000 | 0.12406(26) | 0.01551(18) |
| 1.0 | 4 | 400+3000 | 0.24302(30) | 0.05908(20) |
| 2.0 | 4 | 400+3000 | 0.50150(55) | 0.25960(60) |
| 2.3 | 4 | 400+3000 | 0.60903(49) | 0.39805(74) |
| 3.4 | 4 | 400+3000 | 0.76103(16) | 0.61622(27) |
| 0.5 | 6 | 100+800 | 0.12415(19) | 0.01557(15) |
| 2.3 | 6 | 100+800 | 0.60302(34) | 0.38716(50) |
| 3.4 | 6 | 100+800 | 0.76043(14) | 0.61418(23) |
Cold start L=4 beta=0.5 (seed 77): W11=0.123792(249), W12=0.015421(176).
Raw: res/*.txt, analysis.txt. Sub-agent (2^4, beta=0.5) got W11=0.12508(54), +2.5 sigma above u, and the same small positive offset.

## Failed predicates
None failed. Caveats: the tolerance 3 sigma + 1e-3 was my own allowance for higher-order strong-coupling terms (expected O(u^5)~3e-5, much smaller than 1e-3). W11 sits 1.3 to 2.5 sigma above u in all three independent estimates (L=4, L=6, grandchild 2^4), always positive. Not significant individually. I did not resolve whether it is a real small effect (e.g. finite-size or a higher-order coefficient) or fluctuation.

## Not checked
Error bars from few blocks at L=6 (800 sweeps) are rough. Autocorrelation times not computed separately. No L>6, no betas besides the five. The exactness of "u^2" beyond leading order was not derived. Reflection positivity itself not tested (only W12>0 as the consequence).

## Sub-agent
Question: independent recomputation of u(0.5) and of W11 at beta=0.5 on 2^4, plus the beta=0 case. Task id T198 (admitted, released by me). Its control (2*3*7-1=41) correct. I reread grandchild/result.md and its outputs: u=0.12371793 matches my 0.123718; beta=0 W11=-0.00008(36), W12=0.00039(34), both 0 within errors; W11(2^4,0.5)=0.12508(54) is +2.5 sigma from u, passed its 4 sigma predicate. I did not rerun gc.py. Its sampler uses an inverse-CDF grid (not exact), noted by it.

## Rerun
cd /home/user/z4-workers/y1-rect/child (new result files need fresh names or removal of res/)
for b in 0.5 1 2 2.3 3.4: python3 mc.py 4 $b 400 3000 <seed> res/L4_b$b.txt   (seeds 5,1,2,23,34)
python3 mc.py 6 2.3 100 800 236 res/L6_b2.3.txt ; python3 mc.py 6 0.5 100 800 605 res/L6_b0.5.txt ; python3 mc.py 6 3.4 100 800 634 res/L6_b3.4.txt
python3 check.py ; python3 analyze.py
