# REGISTRATION — e2-repair new side-six run (written and hashed BEFORE the first production run)

Worker e2-repair, task T230. Written 2026-11-24 before any production stream was started.
(The only sampler executions before this file: two timing runs in scratch/ with seed 99, not used in any result.)

## Design
- Lattice side 6, temporal period 12, beta = 3.276133577, sampler build/z1m6 (sha256 81c1589463bb09437ef8a1678f1dddc9771e51008bf3bbfd45491976b8c78a20,
  source build/src/mine/z1m6.rs sha256 3437fc562f9b35d63660d849d0833b4ec9b1b4f2f73abadb0853deb576a55948).
- Two arms in the same design:
  - tag N-d2: skeleton skeletons/d2.txt (delta = 2/beta = 0.6104757187; sha256 1afe1b5fe7dbe2400bc399ea8a22c13b7221851843bda083fe8d66fb9bb3918e, copy of ../z1-mix6/skeletons/d2.txt)
  - tag N-d0: skeleton skeletons/d0.txt (delta = 0; sha256 d6d3de2411db84cdca36869e3d7ad0fb80717be3c047595a7f655aa62b2c1815, copy of ../z1-mix6/skeletons/d0.txt)
- 32 streams per arm, stream IDs i = 0..31.
- Split (registered): hot = (i mod 2 == 1) by NUMERICAL stream ID; cold = even i. 16 hot, 16 cold per arm.
  The hot flag passed to the sampler is i % 2 and is recorded in each s<i>.meta.txt "args" line (4th token after "args");
  the reducer asserts that the numerical-ID split equals this recorded flag for every stream.
- Seeds (fresh; checked against every 5–9 digit integer in every non-CSV file under /home/user/z4-workers: 0 collisions):
  - N-d2: seed_i = 9310007 + 7919 i, i = 0..31
  - N-d0: seed_i = 9420013 + 7919 i, i = 0..31
  (Seeds are independent between arms; the ratio error is therefore an INDEPENDENT-arm error; a paired-by-index jackknife is reported as sensitivity only.)
- Burn-in: 1152 conditional heat-bath sweeps discarded (double the 576 of the prior L-* long runs).
- 1152 measurements, 6 sweeps apart.
- Command per stream: build/z1m6 fixed 3.276133577 <seed_i> <i%2> 1152 1152 6 6 12 <skeleton> results/<tag>/s<i>
- 2 streams concurrently (2 cores, brief allows 2).

## Estimators (unchanged from the prior reducer, G4's definitions)
Pooled plug-in variance (ddof 0) over all measurements of all streams; J = pooled mean of j column; ratio r = J/Var;
errors = delete-one-stream jackknife. Marks: one-face (single, j_single), four-face (average, j_average); raw B columns are primary,
traceless-B columns reported as well.

## Predicates (fixed now)
- R1 (exit): every sampler call exits 0 (sampler-internal asserts). pcp check --expect-exit 0.
- R2 (split): for every stream, recorded hot flag == ID % 2; 16 hot and 16 cold per arm. Hard assertion.
- R3 (hot/cold, per arm, per mark r1 and r4): z = (r_hot - r_cold) / (2 SE_pooled), |z| <= 2.
  Tolerance 2: the prior preregistered tolerance (run.py T2); SE_pooled = jackknife error of pooled ratio; 2 SE approximates the
  SE of a difference of two half-size strata.
- R4 (burn-in drift, per arm, per mark): r on measurements 0..575 vs 576..1151 of every stream, each with stream jackknife error;
  d = (r_second - r_first)/sqrt(e1^2 + e2^2), |d| <= 2 (conventional ~95% two-sided; the halves are treated as independent,
  which neglects their positive correlation through shared streams -> this test is conservative-to-neutral).
- R5 (reproduction of prior claim): Q1 = r1(N-d2)/r1(N-d0), error from independent arms (relative jackknife errors in quadrature).
  "reproduced" iff |Q1 - 1.016| <= 2 sqrt(e_Q1^2 + 0.011^2). Otherwise "not reproduced".
- Measured only: J1, Var1, J4, Var4, r1, r4, traceless versions, Q4 = r4(N-d2)/r4(N-d0) (compared with prior L-d2/L-d0),
  whether Q1 is consistent with 1 within 2 sigma, paired-by-index jackknife of Q1, Q4.
