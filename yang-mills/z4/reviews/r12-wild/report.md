# r12-wild report (wildcard, seed "slice"), worker of Director Z4

Control: `control.txt` = 0.272341 (−ln tanh 1). Lean READY present; Lean used.

## THE ONE THING

**S6″ (`repo/fixed-size/STATEMENT.md`, addendum) and the spatial-flow remedy that its own caveat and the NEW reports adopt cannot both hold.**

- S6″ asks for 0 < c ≤ t²⟨E_b(t)⟩ ≤ C uniformly as b → 0, where E_b is the flowed **¼G·G**. Its caveat then says that exact reflection positivity on a slice "needs the spatial flow".
- Under the spatial flow (flowchal's reading: spatial links flowed by the spatial-plaquette gradient, a₄ not flowed), the **electric** half of ¼G·G is not regularized:
  - The longitudinal part of each temporal plaquette θ_{i4}, namely D_i a₄ − D₄(P_L a)_i, has per-mode weight (p² + q₄²)/A = 1 exactly. That is a pure contact term, and no flow factor reaches it.
  - The flowed density per site is therefore e(τ) → 1 in lattice units. In physical units this is ≈ 1/b⁴, so t²⟨E_el⟩ ~ t²/b⁴ → ∞.
  - The transverse electric remainder also diverges. It falls only like τ^(−1.41) in lattice units (measured; the continuum expectation is τ^(−3/2)), which gives roughly b⁻¹·t^(−3/2) in physical units.
- Under the full 4D flow the same program gives e = m with τ²(e + m) → 3/(64π²), which is finite.
- The NEW reports avoid the problem because they compute only B₃ (`NEW_flowchal` T5b/T5c/T6; `NEW_flowbounds` P₃₃ throughout).
  - B₃² is the magnetic density, which STATEMENT item 4 (line 77) says is not a Lorentz scalar and mixes with T₀₀. S6″ was written to replace exactly that observable (STATEMENT line 116).
  - So "replace the 4D flow by a flow within one time slice" silently changes the observable back from ¼G·G to the magnetic density.
  - It also cannot keep the electric part inside one slice in any case: θ_{i4} spans two slices plus temporal links. In the Hamiltonian frame of STATEMENT, E_i is the conjugate momentum, and a flow of the slice's A does not act on it at all.

Program `efield.py` (free U(1), 4D periodic lattice; run1 has L = 48):

| τ | spatial flow e(τ) | spatial τ²m(τ) | full-flow τ²(e+m) |
|---|---|---|---|
| 1 | 1.01115 | 0.006591 | 0.005508 |
| 4 | 1.00164 | 0.006342 | 0.004896 |
| 8 | 1.00061 | 0.006317 | 0.004789 |
| 16 | 1.00022 | 0.006249 | 0.004642 |

Continuum values for comparison:
- magnetic sum Σ_{i<j}: 1/(16π²) = 0.006333. This equals 3 × flowchal's 1/(48π²), which it reproduces.
- full flow, Σ_{μ<ν}: 3/(64π²) = 0.004749.

Lean `R12Slice.lean` proves two things: the per-mode identity p/A + q(p/p)/A = 1, and that t²/b⁴ is unbounded as b → 0. It is only the algebra; the lattice sum is not formalized.

**Runners-up (one line each):**
1. `NEW_flowbounds` §2 says the spatially flowed O "is still a function of time-zero fields", and `NEW_literature` item 2 says the same about positivity. That holds only for magnetic observables; any electric or ¼G·G density spans a two-slice slab, so the single-slice transfer argument needs a restatement. I did not check that restatement.
2. The normalizations ⟨¼F²⟩ (flowchal T5a, 3/(128π²t²)) and Σ_{μ<ν}F² differ by a factor 2. S6″ names "¼G·G" but quotes no density convention for E_b. My own P4 fell into this.

## Verdict table

| Item | Verdict | Evidence |
|---|---|---|
| S6″ normalization 0 < c ≤ t²⟨E_b(t)⟩ ≤ C combined with the caveat's spatial flow | DEFECT | e(τ) ≥ 0.99 at all five τ, at L = 16 and L = 48. Longitudinal weight = 1 per mode: 200/200 random modes (mine), 65520/65520 (child). Monte Carlo agrees (grandchild). |
| NEW reports' spatial-flow results for B₃ (⟨B₃²⟩ = 1/(48π²t²)) | STANDS | τ²m = 0.006317 at τ = 8, against 3/(48π²) = 0.006333: −0.25%. |
| NEW reports as a replacement for S6″'s ¼G·G | DEFECT (scope) | They treat only B₃, which STATEMENT line 77 and line 116 set aside. |
| Full 4D flow, free total density | STANDS | τ²(e+m) = 0.004789 at τ = 8, +0.8% from 3/(64π²). This comparison is post hoc; the pre-registered P4 failed (see below). |
| Positivity argument for electric observables under spatial flow | NOT CHECKED | Runner-up 1. |

## Hypotheses used and where stated
- Free U(1) Gaussian limit with Feynman covariance δ/A, k = 0 removed. Gauge-invariant quantities do not depend on this choice. This is the setting of `NEW_flowchal` T1–T3 and of STATEMENT's free benchmark.
- Spatial flow means a_i → (P_T e^(−τp²) + P_L)a_i with a₄ not flowed. This is flowchal's stated reading (its T3, "Hypothesis used").
- Lattice electric density is Σ_i θ_{i4}² and magnetic density is Σ_{i<j}θ_{ij}², in lattice units. The physical density is these divided by b⁴, with t = τb² (g = 1).
- S6″'s requirement is read from STATEMENT.md addendum, the first bullet: "0 < c ≤ t²⟨E_b(t)⟩ ≤ C … uniformly as b → 0".
- Assumption: the conclusion is drawn in the free theory only. A contact term ~ b⁻⁴ is a perturbative leading-order fact; an interacting theory could only add to it. I did not check whether some subtraction scheme rescues it. ⟨E_b⟩ is subtracted inside O, but S6″ demands t²⟨E_b⟩ itself be bounded.

## Failed predicates
- Smoke run (L = 16): P1 failed on 2 of 2 (τ²m off by −37% and −82%) and P4 failed on 2 of 2. Both come from my own setup: the predicates were stated for L = 48, and L = 16 is too small a volume for τ = 8 and 16.
- run1 (L = 48): P4 failed on 2 of 2, with τ²(e+m) = 0.004789 and 0.004642 against my expected 0.0094989. This was **my own expectation error**: Σ_{μ<ν}F² = 2·(¼Σ_{μν}F²), so the continuum value is 3/(64π²) = 0.004749, not 4·3/(128π²). It is kept as failed. The post-hoc deviations (+0.8% and −2.3%) are measured only.
- Child rerun K3 exited 1. This was my rerun setup slip: I did not copy `control.txt`, which `flow.py` reads. K6 reran with it and the output is identical to the child's.
- Child's own failure: P5 used factor 1 instead of 2 for the transverse polarizations. The child flags this as its own expectation error.

**Counts (met, failed, measured only):**
- run1: 408, 2, 6. The met cases are P0 200, P_formula 200, P1 2, P2 5, P3 1. The measured-only items are M1 at 5 values of τ plus the post-hoc P4 deviation.
- smoke: 406, 4, 5.
- Lean: 2, 0, 0.

Tolerances:
- P0 and P_formula: 1e−12, float64 roundoff.
- P1 and P4: 10%, my estimate of the O(1/τ) lattice correction plus finite volume.
- P2: 0.99. The source is the exact per-mode weight 1 minus the p = 0 fraction 1/L³.
- P3: ≥ 10. The expected value is 16 if m ~ τ⁻² and e ~ const.

## What I did not check
- The interacting theory, and any additive renormalization of ⟨E_b⟩ that would subtract the contact term.
- Whether a different "spatial flow" convention (for example, also flowing a₄ by a spatial heat kernel) removes the divergence. A spatial heat kernel on a₄ would damp D_i a₄ but not D₄ a_i^L, so I expect it does not. Not computed.
- The positivity of electric observables (runner-up 1).
- `NEW_flowbounds` proofs, beyond rederiving its constant √π/(640π²) by hand. It agreed.
- `NEW_literature` sources: no network was used.

## Delegated questions and outcomes
- **Child (sonnet, check K4, exit 0, 90 s).**
  - Control: the BZ average of 4 sin²(k/2) at L = 64. Known answer 2.000000, computed by me first. The child answered 2.000000, which is **correct**; I graded it before reading anything else.
  - Asked: e(τ), m(τ) at L = 16 for τ = 1, 4, 16, plus the per-mode longitudinal identity.
  - Returned: e = 1.0111277555, 1.0016304900, 1.0004608860. These equal my smoke run to all printed digits. The identity held for all 65520 qualifying modes (max deviation 8.9e−16).
  - I reran its `flow.py` (K6) and the output is identical.
- **Grandchild (the child's sub-agent, in child/grandchild/).**
  - Asked: an independent Monte Carlo of e(τ = 4) at L = 8 (2000 Gaussian samples, seed 12345), with a known-answer control first.
  - Returned: MC 1.00326752 ± 0.00035587 against exact 1.00331441, z = −0.13.
  - The child reran it, and I reran `run.py` myself (K5) with the same output. I did not audit run.py line by line.

## Exact commands to rerun
```
cd /home/user/z4-workers/r12-wild
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P init pcp --principal principal --principal-name "Kirtus Justus"        # fresh copy only
$P check --ws pcp --name efield-L16 --expect-exit 0 -- python3 efield.py 16 smoke   # new tag if result_smoke.json exists
$P check --ws pcp --name efield-L48 --expect-exit 0 -- python3 efield.py 48 run1    # new tag if result_run1.json exists
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
mkdir rerun_child2 && cp child/flow.py child/control.txt rerun_child2/
$P check --ws pcp --name child-rerun2 --cwd rerun_child2 --expect-exit 0 -- python3 flow.py
mkdir rerun_gc && cp child/grandchild/*.py rerun_gc/
$P check --ws pcp --name grandchild-rerun --cwd rerun_gc --expect-exit 0 -- python3 run.py
$P check --ws pcp --name lean-R12Slice --cwd /home/user/z4-lean --expect-exit 0 --timeout 600 -- bash -c 'PATH=$HOME/.elan/bin:$PATH lake env lean /home/user/z4-workers/r12-wild/R12Slice.lean'
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Last lines of the verify commands:
- `$P verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify`: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

Register checks:

| Check | Program | Exit |
|---|---|---|
| K1 | efield L16 | 0 |
| K2 | efield L48 | 0 |
| K3 | child rerun | 1 (my setup slip) |
| K4 | child-run1 | 0 |
| K5 | grandchild rerun | 0 |
| K6 | child-rerun2 | 0 |
| K7 | Lean | 0 |

Director, I, child and grandchild share a model family; this is not independent review.
