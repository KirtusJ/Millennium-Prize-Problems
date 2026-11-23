# Report a3-C: claim (C) for SU(2), d = 4, assuming (A) and (B)

**First line:** this is NOT a proof of (C). The chain in PROOF.md reduces (C) to the inequality (C′) for the slice-flowed SU(2) magnetic density (step 6, MISSING). Step 7 (lattice-local variant only) is CLAIMED. Step 0 rests on the assumption that the infinite-volume state exists at every β.

Control: control.txt = 0.272341 (−ln tanh 1).

## 1. Verdict table (steps with tags)

| Item | Tag / verdict | Evidence |
|---|---|---|
| Step 0: reflection positivity, transfer matrix, infinite-volume state | CITED (abstract level) + assumption | OS78 and Lüscher 1977 (LIT_RIGOROUS R2); infinite-volume state at large β assumed (A1 §1) |
| Step 1: log-convexity; u(n) = mean energy of e^(−nH/2)ψ | PROVED | (log C)″ = variance ≥ 0 |
| Step 2: (C) ⇔ u(cξ) ≤ K m ⇔ spectral weight in [1, K] after damping | PROVED | two-line integrals; Lean `A3C.weight_implies_C` (finite sums) exit 0 |
| Step 3: (C′) 1 − C(1)/C(0) ≤ K′m ⇒ (C) and (C⁺) with D_j = e^(2K′) for all j | PROVED | chord slope of convex log C; Lean `A3C.step_chain` (integer form) exit 0 |
| Step 4: (C′) fails for lattice-local observables in the free field | PROVED (numerically on the discriminator) | ξ(1 − C₂(1)/C₂(0)) = 0.963ξ, P4 met |
| Step 5: additive doubling ⇒ (C), (C⁺); the multiplicative (1/2+δ) form is not enough | PROVED; converse NOT CHECKED | iteration; free field has A = 1/2 |
| Step 6: (C′) for the flowed SU(2) density, infinite volume, uniform in β | **MISSING** | free analogue holds: ξ(1 − C1/C0) → 4.78 (s = 0.1), P3 met |
| Step 7: C(1)/C(0) ≥ c > 0 uniformly in β (lattice-local) | CLAIMED | weakest point: needs Balaban-type control of gauge-invariant expectations |
| Step 8: Euclidean-time smearing by O(ξ) does not make (C) automatic; adaptive smearing does, but loses locality or gives a single atom | PROVED | two-atom counterexample, Q3 (6/6 cases before a crash) and Q3b met |
| Step 9: free massive field, m → 0, lattice-local: (C) true | PROVED numerically (discriminator) | R(256) = 5.504244 vs continuum 5.503975 (φ); 30.2967 vs 30.2937 (φ²); child agrees to < 10⁻⁶ |
| Step 10: (C) fails iff the bottom weight is exponentially small; a hole with a polynomial bottom gives (C) **and a single-atom limit** | PROVED (examples) | Q1, Q2, Q5 met; HHp: R → e^(1/2) |
| Step 11: lower-bound tools in the literature | NOT CHECKED beyond group-blind RP + Jensen | Griffiths/Ginibre for abelian models is recollection only, with no locator |

Counts (predicates): **met 10, failed 5, measured only 2.**
- Met: P1–P4, Q1, Q2, Q5, Q3b, Lean compile + axioms, child rerun bytes identical.
- Failed: P5, P6, P7, Q4, Q3 (see §3).
- Measured only: P8, and the res1/res2 quadrature comparison.

## 2. Hypotheses each statement uses, and where stated

- Steps 1–5, 8, 10 use only: T self-adjoint with 0 ≤ T ≤ 1, ψ ⟂ Ω, ν finite (A1 §1); for real n, spectral calculus. Steps 2 and 3 additionally use (A) (ξ < ∞) and, in step 3, ξ ≥ 2K′ and ξ/2^j ≥ 1 (PROOF.md step 3).
- Step 0: Wilson action; physical positivity (OS78, Lüscher, abstract level). The infinite-volume state at every β is assumed (A1 §1, §4.5).
- Step 6: the slice-flowed magnetic density of SPATIAL_FLOW.md §2 at flow time sξ², fixed s and f; infinite-volume m(β); L ≫ √s ξ if done in boxes.
- Step 9: free field action ½φ(−Δ+M²)φ, M² = 2(cosh(1/ξ) − 1); continuum value from the 4D propagator M K₁(Mr)/(4π²r).
- Step 6, free analogue: B3 of SPATIAL_FLOW.md, valid only under s·Ψ′_b/P_b < 1/7 and ℓ/√s ≳ 9 (per its challenge).

## 3. Failed predicates

All five are **my own expectation errors or my own program defects, not defects of the target**:
- **P5, P6, P7 (test_c.py).** I chose the counterexample atom weights too large (w = e^(−ξ/2), m⁴, e^(−2ξ)). The atom then dominates at n = ξ, and R tends to a constant (4.37, e^(1/2), e^(1/2)). Lesson kept as step 10: a hole alone does not violate (C); the bottom weight must be exponentially small. The corrected families pass in test_c2.py.
- **Q4 (test_c2.py).** For the hole with w = m⁴, R is bounded asymptotically (→ e^(1/2)), but its supremum is 151 at ξ = 256, not ≤ 5 as I had set.
- **Q3 (test_c2.py).** The program crashed at ξ = 256 on exp(−765) underflow (division by zero) after 6 of 6 earlier cases qualified. Recomputed in log space in test_c3.py: Q3b met.
- Inside the child: the grandchild's P2 (two-resolution agreement < 10⁻⁶) failed at 1.05·10⁻⁶. This was its own quadrature tolerance, not a defect of the target.

## 4. What I did not check

- The converse of step 5 (from (C⁺) to pointwise doubling).
- Any SU(2) number: no Monte Carlo; (C′) for SU(2) is untested.
- The full texts of OS78 and Lüscher (strict positivity of T).
- Griffiths/Ginibre inequalities and any lower-bound correlation inequality for gauge theories: no source read, nothing fetched.
- The electric contact term of SPATIAL_FLOW §1.3 entering C(1) through the temporal links.
- Whether a single-atom limit (step 10, HHp; step 8(iii)) is excluded by anything in A1. As far as I can see it is not: A1 §4 item 3 covers Gaussian limits and leaves (E) to carry it.
- Discriminator rows for 3D U(1) beyond the Göpfert–Mack abstract.
- Lean covers only the finite-sum forward direction of (2c) and the integer chain of step 3, not the real-n convexity argument.

## 5. Delegated questions and outcomes

- **Child** (sonnet, headless, register event child-run1, exit 0 in 100 s).
  - Control: K₁(1) to six decimals; my answer computed first: 0.601907. **Child answered 0.601907: correct** (graded before reading anything else).
  - Question: R1(ξ) = G(ξ/2)/G(ξ) for the free 4D lattice field by the momentum integral, ξ = 4…128, and convergence to 2K₁(1/2)/K₁(1) = 5.503975.
  - Returned: 6.5835480, 5.9212916, 5.5796295, 5.5215749, 5.5083075, 5.5050540; deviation decreasing like ~1/ξ².
  - My reading: I reread r1.py. The octant reduction is valid (the integrand is even in each k_i), and the map k = πs⁴ is a valid Gauss–Legendre change of variables. I reran it under my register (child-r1-rerun): output bytes identical to its r1_result.txt. Its values agree with my independent Schwinger values (test_c.py) to < 10⁻⁶ relative at every common ξ.
- **Grandchild** (started by the child).
  - Control: I₀(1) = 1.266066: correct.
  - Question: R1 at ξ = 16 by the Schwinger representation.
  - Returned: 5.5796296 (fine) vs the child's 5.5796295. Its own two-resolution predicate failed marginally (§3). The child reports rerunning it. I did not rerun the grandchild program myself; its number is consistent with mine (5.579630).

## 6. Commands to rerun (from /home/user/z4-workers/a3-C)

```
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')" > control.txt
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P init pcp --principal principal --principal-name "Kirtus Justus"
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P check --ws pcp --name test-c-res1 --expect-exit 0 -- python3 test_c.py result_test_c_res1.txt 1   # exits 1 (P5-P7 fail); new output name on rerun (mode x)
$P check --ws pcp --name test-c-res2 --expect-exit 1 -- python3 test_c.py result_test_c_res2.txt 2
$P check --ws pcp --name test-c2 --expect-exit 0 -- python3 test_c2.py result_test_c2.txt        # exits 1 (Q4 fail, Q3 crash)
$P check --ws pcp --name test-c3 --expect-exit 0 -- python3 test_c3.py result_test_c3.txt
$P check --ws pcp --name child-r1-rerun --cwd child --expect-exit 0 -- python3 r1.py /home/user/z4-workers/a3-C/result_child_r1_rerun.txt
$P check --ws pcp --name lean-a3c --cwd /home/user/z4-lean --expect-exit 0 --timeout 600 -- bash -c 'PATH=$HOME/.elan/bin:$PATH lake env lean /home/user/z4-workers/a3-C/lean/A3C.lean'
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

The expect-exit values recorded in the register are the ones above. test-c-res1 and test-c2 were registered with expect 0 and exited 1; this is recorded as a mismatch in the register, kept, and explained by the failed predicates.

Last lines:
- `$P verify --ws pcp`: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- `pcpos verify pcp/register.jsonl`: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."

Lean: /home/user/z4-lean/READY exists. lean/A3C.lean has no sorry. `#print axioms` gives [propext, Classical.choice, Quot.sound] for both theorems.

Director, worker, child and grandchild are one model family. This is not independent review.
