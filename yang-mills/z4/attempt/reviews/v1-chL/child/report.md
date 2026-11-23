# T182 report

**Control:** integral of sin(x)^2 over [0,pi] = **1.570796** (control.txt, written first).

| Q | Verdict | My value |
|---|---|---|
| Q1 c* | AGREES | 4.6054131945 (3 quadratures within 3e-14; claim off by 5.5e-9, so the claim is rounded correctly). Grandchild got 4.605413194531 independently. |
| Q2 | AGREES | e(S)=log A(S): max err 2.2e-16 on 2001 log-grid points S in [1e-6,1e6]. (h-2)(1+2S^2h)=h: float error grows to 6.5e-4 at S~1e6 (cancellation in h-2, see failed predicates); in 60-digit Decimal the worst rel. error is 1.1e-48 on 25 points. |
| Q3 | AGREES (with two remarks) | MA2 at 0.4, 0.2, 0.1, 0.05, 0.01 = 12.0607, 20.5522, 37.9149, 72.8236, 352.522. eta*MA2 = 3.5252 (1e-2), 3.4971 (1e-4), 3.49683 (1e-6) -> log(1/m1)=3.496823. m1=0.030293. Exact switch of m: eta=(4/3)*log(1/(1-2 m1)) = 1/12 exactly (diff 3e-17). Remark 1: the max() inside MA2 never switches on [1e-3,0.4]; the first branch coth(eta)*log(1/m1) wins everywhere, with a margin of 6.4 at eta=0.4. Remark 2: this is a different switch from that of m. |
| Q4 | AGREES | Mc12 at 0.4, 0.2, 0.1, 0.05, 0.01 = 18.0473, 30.3824, 54.3589, 101.615, 475.722. min(Mc12-MA2) = 5.98656 on 4005 equispaced points (eta=0.4i/4005), attained at eta=0.4; also 5.98656 over 2e5 log-spaced points in [1e-8,0.4]. sqrt2*(e(sqrt2)+1) = 4.65620. |
| Q5 | AGREES | (a) 0.41605<0.5. (b) the inequality reduces to 4 sqrt2 r/S <= 1, i.e. r <= 0.177 S, so r <= S/8 suffices; max relative excess -0.0586, so it holds on 400x400 points. (c) max arcsin(r)/r = 1.002623 <= 1.003; max (arcsin r - r)/r^3 = 0.16785 <= 0.17. (d) min slack 0.0034 over 1e6 random pairs (seed 0). (e) min slack 0.00444 over 400 etas in [1e-6,0.4]. |
| Q6 | AGREES | m0(0.4)=0.12959, m1=0.030293, so m=m1 and m/2=0.015147, which rounds to 0.0151. min (1-exp(-3eta/4))/eta = 0.648 >= 0.555 (a looser bound than needed). max sinh(eta)/eta = 1.02688 <= 1.03. |
| Q7 | AGREES | 0 violations out of 1,929,600 grid evaluations. Min slack of ineq 1 is 3.75e-4, at eta=1e-3, S=sinh(eta), xc=0. Min slack of ineq 2 is 2.51e-5, at eta=1e-3, S=sinh(eta), xc=1. The slack is tightest at the small-eta corner, so it shrinks as eta -> 0 and the claim is only checked down to 1e-3, as specified. |

## Failed predicates
- **Q2b (second identity) in double precision.** Predicate: rel. error < 1e-9. It failed (6.5e-4 for S in [1e4,1e6]). **The cause is my own expectation, not a defect of the target.** h->2 for large S, so h-2 cancels catastrophically in floating point. I reran in 60-digit Decimal (q2_hp.py, predicate fixed beforehand: < 1e-40). Worst error 1.1e-48, so the identity holds. The grid was 25 points there, not 2001. The failed run is kept in results_q.txt.
- No other predicate failed.

Tolerance origins: the Q1 5e-7 tolerance covers the claim's 7-digit rounding, and the quadratures agree to 3e-14. The Q3 and Q4 tolerances are half the last printed digit of each claim (0.005, or 0.05 for claims given to one decimal). The 1e-12 float tolerance in Q7 and the 1e-15 in Q5b are roughly the double-precision rounding level. The Q2 1e-12 is a few ulps.

## Grandchild (T183, label v1-chL-grandchild)
Question: independently recompute c* with its own quadrature, including a known-answer control, boundary behaviour near a=0 and a=pi, and the symmetry a<->pi-a. Its predicates P1 (control), P2 (methods agree within 1e-7) and P3 (|value-4.6054132|<5e-7) all passed. It reported value 4.605413194531 with three methods and symmetric/full-range variants. Its boundary check gave f~2 sqrt(a) at both ends. I reread grandchild/result.txt and reran gc.py in rerun_gc/ through `pcp_os check` (K3), with identical output. T183 was released with task-release.

## Verification
- `pcp_os.py verify --ws pcp` last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl` last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

Files: pcp_q.py (results_q.txt), q2_hp.py, grandchild/, rerun_gc/, notes.md.
Register checks: K1 pcp_q, K2 q2_hp, K3 gc_rerun.
