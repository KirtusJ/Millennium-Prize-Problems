# T59 report: free-field linearized Wilson loop norms on Z^4

Control: 1x8 strip has **8** plaquettes (control.txt).

Method: G(a,b,0,0)=∫ ive(a,2t)ive(b,2t)ive(0,2t)^2 dt (own Bessel routine, since scipy is not installed; periodic-trapezoid integral), log-t Simpson up to T=2e4 plus an analytic tail. V=Σ s_i s_j δ_μμ' G(x_i-x_j) over link pairs. Results: res_run3.json (T=2e4) and res_run4.json (T=5e3, different grid). The two runs agree to 1.2e-7 on all V values.

Checks: G(0)=0.1549333892 (tolerance 5e-6, set by the 6 digits quoted); G(0)-G(e1)=0.12499999900 (tolerance 1e-8, set by quadrature); V(1x1)=0.49999999600 (tolerance 1e-8).

| w | V(1xw) | V/(w V11) | V(wxw) | V/(w² V11) |
|---|---|---|---|---|
| 1 | 0.500000 | 1.0000 | 0.500000 | 1.00000 |
| 2 | 0.862251 | 0.8623 | 1.369312 | 0.68466 |
| 4 | 1.537616 | 0.7688 | 3.261484 | 0.40769 |
| 8 | 2.872708 | 0.7182 | 7.167860 | 0.22400 |
| 16 | 5.539779 | 0.6925 | 15.115398 | 0.11809 |
| 32 | 10.873211 | 0.6796 | 31.149865 | 0.06084 |
| 64 | 21.539903 | 0.6731 | 63.359009 | 0.03094 |

Fitted slope between w=32 and w=64: a(1xw)=0.986, a(wxw)=1.024. So sqrt(V) goes like w^0.493 (strip) and w^0.512 (square). Both are close to w^(1/2), i.e. V grows roughly with the perimeter, not the area. The square slope is above 1 and the strip slope below 1. A pure power law was not tested, so I don't claim these are asymptotic exponents.

## Verdicts
- (i) V(1x1)=1/2: STANDS (0.499999996; the 4e-9 gap is within the 1e-8 quadrature tolerance).
- (ii) V(1xw) <= w V11: STANDS. 7 of 7 w qualify. Ratio falls 1 → 0.673.
- (iii) V(wxw) <= w² V11: STANDS, but it is far from sharp. 7 of 7 qualify, and the ratio falls to 0.031.
- (iv) exponents: slopes as above, w^(a/2) with a≈0.99 and 1.02.

## Failed predicates
- K1 (v_run1): ImportError, scipy missing. Environment gap, not a defect of the statement.
- K2 (v_run2): crash when writing JSON (numpy bool). My own code defect. The computed numbers were fine and identical in run3. The partial res_run2.json is kept.
- No predicate of the statement failed. "For all" claims were tested per case: 7 of 7 qualify in each.

## Grandchild
Task T61 (e3-strip-grandchild, parent T59), admitted and released. It did an independent finite periodic lattice FFT check with L=16 and 32 (grandchild/run.py, results.txt). Its control G(0)-G(e1)=(1/8)(1-L^-4) matched to all printed digits. Its V(1x2)=0.862219 at L=16 and 0.862249 at L=32. I reread results.txt. Mine, in infinite volume, is 0.8622505, so they agree to the expected finite-size level (about 2e-6 at L=32 by trend). Its V11 was 0.4999995 at L=32.

## Rerun
cd /home/user/z4-workers/e3-strip/child
python3 v.py 6001 2e4 new_result.json
python3 v.py 8001 5e3 new_result2.json
cd grandchild && python3 run.py   (writes with mode x; use a fresh results name or remove the old one)

## Verify lines
- python pcp_os verify: result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)
- pcpos verify: A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.
