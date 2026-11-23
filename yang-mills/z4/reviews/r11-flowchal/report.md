# r11-flowchal report (challenger, Director Z4)

Control: `control.txt` = 0.272341 (-ln tanh 1). mpmath, sympy and scipy are **not installed**, so I used Python `decimal` at 45 digits (my own pi/cos series) instead of mpmath. The brief asked for mpmath; this replaces it. Lean was not used (`/home/user/z4-lean/READY` is absent, so Lean is not ready). I make no Lean claims.

## Verdict table

| item | verdict | evidence |
|---|---|---|
| T1 full-flow form, tau=6 | STANDS | Decimal 16^4 sum gives -0.009864957816795690839466881673; it differs from the printed value by 8.4e-19 (P1) |
| T2 spatial-flow form, tau=6 | STANDS | 0.057333237804766231595901211334, diff 3.2e-17 (P2). The child's Green-function route agrees to 25 digits |
| T3 K_tau formula: projector (q1²+q2²)/A, factor 2 in exponent, spatial variant | STANDS | Derived (see below). On 4^4, d is built as a matrix: projector max diff 1.1e-15, full flow 1.8e-17, spatial flow 1.4e-16. Using exp(-tau A) instead of exp(-2 tau A) misses by 8.3e-3 |
| T4 count 32, rate 6a, sign | STANDS | Mode count derived. (K2²-2K3²+K4²)/leading = 1.0065, 1.00031 and 1.0000007 at tau = 20, 30, 50. 2cos3ω(cosω-1) = -0.05826 |
| T4 smallest tau with full form < 0 | measured | tau* = 3.4968, i.e. **3.5** to 2 digits. The form is +4.58e-4 at tau=0 and stays negative on the whole grid after 3.5, up to 50 |
| T4 spatial form > 0 on [0,50] | STANDS | 1001 of 1001 grid points are positive. Minimum 4.58e-4 is at tau=0. Reason given below |
| T5a full flow <¼F²> = 3/(128π²t²) | STANDS | 0.0023747152/t². Analytic result, matched by quadrature to better than 1e-8 relative |
| T5b spatial flow <B3²> = 1/(48π²t²) | STANDS | 0.0021108580/t². Analytic result, matched by quadrature to better than 1e-8 |
| T5c ratios 8/3 and 4/3 | STANDS | Spatial magnetic mean = 1/(32π²t²) = 0.0031662870/t². Full magnetic mean = 3/(256π²t²) = 0.0011873576/t². Full total = 3/(128π²t²). Exact ratios 8/3 and 4/3 |
| T6 spectral powers 8 (point), 5 (zero momentum) | STANDS | Derived. Quadrature log-log slopes are 7.99996 and 4.99997 |

Counts (met, failed, measured only):
- Final run (run2): 9 met, 0 failed, 1 measured only (P4b).
- All runs together: 9 met, 3 failed, 1 measured only. The 3 failures were run1 P3a/b/c, caused by a defect in my own code; see below.

## Derivations and hypotheses each statement uses

- **T1/T2.** These use C4's definitions as given in the brief:
  - the β→∞ Gaussian limit with covariance = projection onto im d;
  - first-order (linearised) flow;
  - Wick's theorem for C(n) = K²/2;
  - periodic 16^4 lattice, k=0 excluded.

  Nothing beyond the finite sum is needed. The RP test vector Y1−Y2 is reflected through slice 0. The form ⟨Θ(X)X⟩ = C(2)−2C(3)+C(4) follows from the brief.
- **T3.** On 2-forms, (da)_12(k) = D1 a2 − D2 a1 with |D_j|² = q_j². On transverse links d^T d = A, and d annihilates longitudinal links. So P_{12,12} = (q1²+q2²)/A.

  Full flow on links is e^{-τ d^T d}, so F_τ = e^{-τ d d^T} F. On exact 2-forms (Bianchi dF=0), d d^T = Laplacian = A. Each field therefore gets e^{-τA}, and the covariance gets e^{-2τA}. The factor 2 is right.

  Spatial flow M = d_s^T d_s (spatial plaquettes only):
  - It is gauge invariant because d_s dχ = 0.
  - It leaves temporal links unchanged (checked numerically: 0 deviation).
  - F_12 is an exact 3-D form in its slice, so the heat factor is e^{-τ(q1²+q2²+q3²)} while the denominator stays A.

  Hypothesis used: "spatial flow" means flowing the spatial links by the gradient of the spatial-plaquette action and not flowing a_4. This is my reading of C4's "uses only the three spatial directions within each time slice".
- **T4.** Leading n-independent part of K: 4 modes (k1 or k2 = ±ω), each giving e^{-2τa}.

  Leading n-dependent part of K: 8 modes (k4 = ±ω together with k1 or k2 = ±ω), with A = 2a and projector ½. This gives 4·16⁻⁴ e^{-4τa} cos nω.

  The cross term in K² is therefore 2·4·4 = 32 at rate 6a. The constant parts cancel in the reflected combination, which gives cos2ω − 2cos3ω + cos4ω = 2cos3ω(cosω−1) < 0. Corrections are e^{-2τa} relative, consistent with the measured ratios.

  Why the spatial form is ≥ 0: for each spatial momentum, the k4-sum is a periodic chain Green function cosh(w(8−n))/(2 sinh w sinh 8w) ∝ λ^n + λ^{16−n} with λ = e^{−w} ∈ (0,1). So K(s+t) is a moment sequence of a positive measure, K² is again one (the product of two such measures is still such a measure), and the 2×2 Hankel form at s,t ∈ {1,2} is PSD. Equivalently, spatial flow keeps observables inside a single time slice, so transfer-matrix reflection positivity applies.

  It is not a "Laplace-type sum in τ": the positivity is in n, not in τ. Under full flow, the factor e^{−2τ q4²} destroys this structure.
- **T5.** These use:
  - the Feynman-gauge propagator δ_{μν}/k² for action ¼F², g=1;
  - Lüscher's convention e^{−tk²} per field;
  - infinite volume.

  Key steps: Σ_{μν}⟨|F_{μν}|²⟩ = 6; ∫dk4/(2π) 1/(p²+k4²) = 1/(2p); ∫d⁴k/(2π)⁴ e^{−ak²} = 1/(16π²a²).
- **T6.** The one-particle spectral weight of B3 is (k1²+k2²)/(2p) ~ p. With d³k ~ p²dp, the one-particle density is ~ p³.
  - At a point, the two particles are independent and the density convolves to E⁷, so the mass is ~ ε⁸.
  - At zero spatial momentum, k' = −k, so the density is w² p² dp ~ p⁴, and the mass is ~ ε⁵.

  The flow factor e^{−2tp²} → 1 at small p, so it does not change the powers. Hypothesis: free field (g=0), continuum, infinite volume.

## Failed predicates

- **run1 (flowchal-run1, exit 1): P3a, P3b, P3c failed.** The cause was a defect in my own code, not in the target. `np.linalg.pinv` with its default rcond kept singular values of order 1e-15, so the "projector" was not symmetric (|P−Pᵀ| = 0.13) and not idempotent. The fix in v2 builds the projector and pseudo-inverse by `eigh` with a 1e-8 cutoff. Justification for the cutoff: the nonzero eigenvalues are ≥ 2 and the zero ones are O(1e-13). The predicates were not changed. In run2 all of them pass.
- There are no failures attributable to C4 or Z4.

## Tolerances and where they come from

| predicate | tolerance | source |
|---|---|---|
| P1 | 1e-17 | one unit of the last printed digit |
| P2 | 1e-16 | one unit of the last printed digit |
| P3 | 1e-10 | float64 eigen roundoff (~1e-13) on matrices of dimension 1536 |
| P4a | 1e-3 | the next correction is ~e^{−2τa} ≈ 3e-7 at τ=50 |
| P5 | 1e-8 relative | trapezoid quadrature on a smooth Gaussian integrand |
| P6 | ±0.05 on the slope | O(ε²) flow corrections over ε ∈ [1e-3, 1e-2] |

## What I did not check

- mpmath was not available; I used 45-digit `decimal` with my own π and cos series instead.
- No Lean (not ready).
- The non-linear flow and finite β; everything here is first order and Gaussian, as C4's definitions specify.
- Whether C4's "spatial flow" really leaves a_4 unflowed; I used that as my reading.
- The T4 positivity on [0,50] was tested on a 0.05 grid, not as a continuum statement. The analytic Hankel argument covers all τ.
- T4: I did not check analytically that τ* is the unique sign change. On the grid the form is positive before τ* and negative everywhere after it, up to 50.
- T6 used angular-averaged weights, which is exact for the powers but not for the prefactors. Prefactors were not checked.
- The 4^4 check covers only orientation 12.

## Delegated questions and outcomes

- **Child (sonnet, child-run1, exit 0, 60.8 s).**
  - Task: evaluate the spatial-flow K(0..4) at τ=6 by a closed-form temporal lattice Green function.
  - Control: Σ_{l=0}^{15} cos²(2πl/16) = 8. The child answered 8.0, which is correct; I graded it before reading anything else.
  - Returned K(0..4) and R = 0.0573332378047662315959012113…, which equal mine to all 25 printed digits.
  - Its closed form G was checked against the direct 16-term sum: 640 cases, max diff 9e-49.
  - I reran its `k_green.py` in a fresh copy (rerun-child-kgreen, exit 0, same R).
  - Caveat: my child prompt quoted the candidate closed form for G and asked the child to verify it. So its "derivation" was not independent of that hint; only its numerical check is.
- **Grandchild** (the child's sub-agent).
  - Task: closed-form vs direct G at m² = 2−2cos(π/8), n = 0..4.
  - Control: Σcos(2πl/16) = 0; it got −9.0e-16, which is correct.
  - Result: PASS, max diff 6.7e-16.
  - I reran its `check.py` in a fresh copy (rerun-grandchild, exit 0, PASS).

## PCP OS record

- `$P verify --ws pcp`, last line: `Result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl`, last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
- The child register `child/pcp` also verifies: `result: PASS`.

## Rerun commands

```
cd /home/user/z4-workers/r11-flowchal
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name flowchal-run2 --expect-exit 0 -- python3 flowchal_v2.py result_run2.txt   # use a new result file name; mode "x"
$P check --ws pcp --name flowchal-run1 --expect-exit 0 -- python3 flowchal.py result_run1.txt      # historical; failed P3 (own pinv defect)
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P check --ws pcp --name rerun-child-kgreen --cwd rerun_child --expect-exit 0 -- python3 k_green.py      # remove K_result.json first
$P check --ws pcp --name rerun-grandchild --cwd rerun_gc --expect-exit 0 -- python3 check.py             # remove result.md first
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Same model family as the director: this agreement is not independent review.
