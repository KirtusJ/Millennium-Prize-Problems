# c1-excl (T10): report. Can exclusion prove (A)?

Worker c1-excl of Director Z4, 23 Nov 2026. Principal: Kirtus Justus. Control: `control.txt` = 0.272341 (−ln tanh 1).

**The one thing: exclusion fails in principle.** The principle "no continuous symmetry to break ⇒ gapped, except at isolated critical couplings" is **false**. There is a rigorous counterexample with a finite gauge group: 4D Z_N, N large, has a massless intermediate phase on an open interval of couplings (Fröhlich–Spencer 1982). For a compact, connected, simple and perfect gauge group the counterexample is numerical: 5D SU(2) Wilson has a first-order bulk transition at β_c ≈ 1.64 into a weak-coupling phase with zero string tension. Perturbation theory says that phase is massless; nobody has proved it is. So an exclusion argument for (A) has to use d = 4 in a way that fails at d = 5, and also forbid an *emergent* continuous one-form symmetry. Both are dynamical statements about the running of the coupling. That is the wall the ledger already names.

## 1. Verdict table

| # | Item | Verdict | Evidence (one line) |
|---|---|---|---|
| 1 | The general principle "discrete (one-form) symmetry only ⇒ gap except at isolated couplings" | **DEFECT** (the principle is false) | Fröhlich–Spencer, CMP 83 (1982) 411–454, abstract: 4D Z_N, N large, has an intermediate massless QED phase with dynamical restoration of local U(1). Z_N has only a Z_N one-form symmetry. CITED at abstract level only; full text not read (§4). |
| 2 | The same principle restricted to compact, connected, simple, reflection-positive gauge groups, with no dimension stated | **DEFECT, numerically** (expected counterexample, not proved) | arXiv:1110.4210 §3 ¶1 and Fig. 1: 5D isotropic SU(2) Wilson has a bulk first-order transition at β_c ≈ 1.64 (credited to Creutz, PRL 43 (1979) 553) with strong hysteresis, and the string tension is zero above β_c. Masslessness of that phase is perturbative expectation and is not stated in the text read. Child plus my rerun on 4⁵: hysteresis gap 0.090 ± 0.003 at β = 1.6; below 0.002 at 1.3, 1.5, 1.9 and 2.2. |
| 3 | Consequence: exclusion can prove (A) only by using d = 4 in a way that fails at d = 5 | **STANDS** (argued; it follows from 1 and 2) | All six shared properties of the ledger, plus perfectness and positive Ricci curvature, hold for SU(2) in d = 5. Reflection positivity in site planes is dimension-independent: no plaquette straddles a site plane. That fact is CLAIMED: it was re-derived in this program for d = 4 and not rechecked by me for d = 5. |
| 4 | Brief (b): Z = {β : m(β) = 0} is closed | **DEFECT** (not provable from continuity; only upper semicontinuity follows) | Runner-up lemma below. `usc_test.py` P3 builds a continuous family of spectral measures in which Z = (1, ∞) is not closed. |
| 5 | Brief (b): the correlation length must diverge as β ↑ β* = inf Z | **DEFECT** (not forced) | Upper semicontinuity allows a jump, and P4 exhibits one: the correlation length is 1 up to β* and then infinite. Real examples of finite correlation length at a transition are first-order ones, such as 4D U(1) (believed) and 5D SU(2) (numerical). |
| 6 | Brief (b): the free energy is non-analytic at β* | **NOT CHECKED** (no theorem found) | No theorem of the form "gap vanishes ⇒ free energy non-analytic" was found. Only the converse direction exists (cluster expansions give gap and analyticity together). |
| 7 | Brief (a): a rigorous lattice Goldstone theorem for one-form symmetries | **NOT CHECKED** (none found) | For U(1) the massless photon is proved directly (Guth 1980; Fröhlich–Spencer 1982), not through a one-form Goldstone theorem. For a finite center no consequence follows, and item 1 shows the converse fails. |
| 8 | Brief (c): area law ⇒ gap | **DEFECT** (already in the ledger) | Abstractly false: a confining theory tensored with a decoupled massless field has an area law and no gap (ledger, vortex break 2). I added nothing new. |
| 9 | Child: 5D SU(2) hysteresis on 4⁵ | **STANDS** (measured only) | My rerun is bit-identical, 12 of 12 means (register K5). Short runs (200 Metropolis sweeps, one seed per start). Consistent with β_c ≈ 1.64. It says nothing about masslessness. |

Counts: **STANDS 2, DEFECT 5, NOT CHECKED 2.** Program predicates: **met 8, failed 0, measured only 3.** The 8 are P1–P4 of `usc_test.py` (final run) and the child's P1–P4 (rerun). Measured only: the child's plaquette values, the β = 1.7 gap, and the comparison with the one-loop value 1 − 3/(5β) below. Program runs that failed, all my own code defects: 2 (§3).

### The one thing, step by step (tags)

1. **CITED** (abstract via search snippet; theorem not read). Fröhlich and Spencer, "Massless phases and symmetry restoration in abelian gauge theories and spin systems", Commun. Math. Phys. 83 (1982) 411–454. The 4D Z_N lattice gauge theory with N large has an intermediate massless (QED) phase, in which local U(1) invariance is restored dynamically. Not yet checked:
   - which action (Wilson or Villain);
   - the exact form of the massless statement;
   - the exact interval in β.

   Supporting, also via snippet: Elitzur, Pearson and Shigemitsu (1979) found the same phase by duality and approximate methods. arXiv:2401.04800 argues the Coulomb phase is generic for Z_N one-form theories and proves it in the Villain formulation.
2. **PROVED, elementary.** Z_N gauge theory has no continuous global or one-form symmetry: its one-form symmetry is the center Z_N. So "no continuous symmetry ⇒ gap off a discrete set of couplings" fails on an open interval. **Discriminator:** this kills the abelian or finite-group version only. Z_N is neither connected nor perfect.
3. **What the escape route costs (argued).** In that phase the IR has an emergent U(1) one-form symmetry. So an exclusion principle would have to forbid an emergent continuous symmetry, which is a dynamical statement of the size of (A).
4. **CITED** (arXiv:1110.4210, Knechtli, Luz and Rago, §3 first paragraph and Fig. 1; read through a fetch agent from the HTML v2; no page numbers). Isotropic 5D SU(2) Wilson has a first-order bulk transition at β_c ≈ 1.64, with strong hysteresis said to survive infinite volume. The string tension is zero above β_c ("deconfined"). §2 after eq. (2.3) says a continuum limit is possible only at g₅ = 0, so the theory is trivial there.

   Also CITED, abstract only via snippet: Creutz, PRL 43 (1979) 553. It reports a weak-coupling "spin-wave" phase in 5D and no transition in 4D.
5. **CLAIMED, not found stated in the text read.** The 5D weak-coupling phase is massless: three gluons, massless at the perturbative level, in a Coulomb phase. Supporting points:
   - The unverified summary of §4.3 of 1110.4210 mentions a 5D Coulomb potential in the deconfined phase, but at anisotropy γ < 1.
   - My own perturbative argument: the 5D coupling is IR-irrelevant, so weak coupling stays weak.

   **This is the first unproved step.** My test of it, measured only and weak: in the child data the weak-coupling plaquette approaches the free-field equipartition value 1 − 3/(dβ):
   - β = 2.2: measured 0.6925 against one-loop 0.7273;
   - β = 1.9: measured 0.630 against 0.684.

   The difference shrinks roughly like 1/β² (0.035 against 0.054), as a perturbative phase should. Equipartition: 3(d−1) physical modes per site against d(d−1)/2 plaquettes per site, for SU(2). This is consistent with a perturbative (spin-wave) phase and is not a measurement of a massless correlator.
6. **What the 5D case shows (argued).** SU(2) in d = 5 has everything the ledger lists as separating SU(2) from U(1): it is perfect, has positive Ricci curvature and has signed dual amplitudes. It also has a discrete center and no continuous symmetry. If step 5 is right, any proof of (A) that does not use d = 4 essentially proves something false. The natural d = 4 input is the sign of the β-function, i.e. "the coupling runs".
7. **Side remark.** Link 0 of the ledger assumes uniqueness of the infinite-volume state at every β. That assumption fails in 5D at β_c, where the phases coexist, and in 4D U(1) at its believed first-order point. For 4D SU(2) it is itself an assumption that no bulk first-order transition exists. A modified action (the 4D adjoint-mixed SU(2) action) is numerically known to have one; that is from memory and NOT CHECKED here.

### Runner-ups (one line each)

- **Lemma (PROVED, given weak continuity of β ↦ μ_β, which follows from link 0's uniqueness at every β plus the closed graph of the DLR equations).** Under that hypothesis m(β) = inf over local F and k of −(1/2k)·log(C_F(2k)/C_F(0)). This is an infimum of continuous functions, because the Lyapunov ratio is monotone. So m is upper semicontinuous: {m ≥ c} is closed, and Z = {m = 0} is a G_δ that need not be closed. The gap may drop to zero by a jump at β*, and lower semicontinuity of the gap is MISSING. Tested in `usc_test.py`, P1–P4 met.
- The child's 5D SU(2) hysteresis (item 9) independently places the bulk transition in the window 1.5–1.7, consistent with β_c ≈ 1.64.

## 2. Hypotheses each statement uses, and where they are stated

- **Item 1:** the Fröhlich–Spencer hypotheses: N ≥ N₀ large, and the action as in their paper (not read). Stated in their abstract, CMP 83 (1982) 411.
- **Item 2:**
  - the 5D Wilson action S = β Σ (1 − ½Tr U_p);
  - isotropic couplings;
  - finite lattices extrapolated to infinite volume (1110.4210 §2–3).

  Masslessness rests on perturbation theory (CLAIMED).
- **Item 3:** reflection positivity in d = 5 (site-plane argument as in `THEOREM_B.md` Lemma 1, assumed dimension-independent), and items 1–2.
- **Runner-up lemma:**
  - (H1) a unique infinite-volume Gibbs state at every β (ledger link 0, "assumed");
  - (H2) the DLR specification is continuous in β and in the boundary condition. This holds for a compact spin space with a finite-range continuous action; it is CLAIMED as standard and no source was read;
  - (H3) reflection positivity, giving C_F(n) = ⟨F, Tⁿ F⟩ − |⟨Ω, F⟩|² on Ω⊥. Even n are used, so the sign of T is irrelevant;
  - (H4) local positive-time observables are dense in the OS Hilbert space (by construction).

  Proof sketch:
  1. (H1) and (H2), with Prokhorov compactness, give weak continuity of β ↦ μ_β. So each C_F(n) is continuous in β.
  2. By Lyapunov's inequality, g_k = −(1/2k) log(a_{2k}/a₀) is nonincreasing and tends to −log ‖T|_{span}‖. So m_F = inf_k g_k.
  3. By (H4), m = inf_F m_F.
  4. An infimum of continuous (or +∞) functions is upper semicontinuous.
- **`usc_test.py` P3 example:** an abstract spectral family, not a lattice model. It shows that nothing beyond upper semicontinuity follows from continuity of correlations. It does not show that SU(2) realizes such a jump.

## 3. Failed predicates and failed runs

- `usc_test.py` run K1: exit 1. Underflow (0.05⁴⁰⁰ = 0 in double precision, giving a math domain error). This was **my program's defect**. It left an empty `usc_result.txt`, which was not overwritten.
- Run K2: exit 1. A second underflow, exp(−4000), in `m_formula`. **My defect.** P1 and P2 were already met in `usc_result_run2.txt`.
- Run K3: all predicates met.
- The child's `control.py` first run failed (`np.trapz` is missing in numpy 2.5): the child's code defect.
- The grandchild's first run gave P = 0.0007 because it updated plaquette-sharing links simultaneously: the grandchild's own bug, fixed with a checkerboard update.
- No predicate failed that reflects a defect of a target.

Tolerances:
- P1: 1e-12, from double rounding.
- P2: an explicit analytic bound written in the docstring.
- P3: grid step × derivative bound.
- Child's 0.02 and 0.03: its own guesses, not derived, and it says so.

Note: the docstring of `usc_test.py` describes the P3 family loosely: the text "delta_{1/2…}" is a leftover. The code defines it exactly as e^{−n} + max(0, β−1)·(uniform density on [½, 1)).

## 4. What I did not check

- The Fröhlich–Spencer theorem text (action, statement, interval). The IHES PDF fetch failed because the file is over 10 MB. That host is outside my brief's network allowance (arxiv.org plus web search). I made one failed attempt and received no content.
- Creutz 1979 beyond its abstract snippet.
- Any rigorous or explicit numerical statement that the 5D SU(2) weak-coupling phase is massless: no correlator, no gluon propagator, no Wilson-loop perimeter law measured or read.
- Sections 4–5 of 1110.4210, which reached me only through a summary.
- Free-energy non-analyticity at β*.
- A one-form Goldstone theorem.
- Whether Theorem B′ goes through in d = 5. It plausibly does, since the free correlation is positive, but this is unchecked.
- Lean: `/home/user/z4-lean/READY` exists, but I did not use Lean. No Lean claim.

## 5. Delegated questions and outcomes

- **Child (T12, admitted under T10, released after return).** Question: on 4⁵, 5D SU(2) Wilson, run hot and cold starts at β ∈ {1.3, 1.5, 1.6, 1.7, 1.9, 2.2}; does hysteresis appear near 1.6–1.7 and not at the ends?
  - Control: E[½ Tr U] at β = 1 for a single link = I₂(1)/I₁(1) = 0.240194, computed by me from the series first. The child answered 0.240194: **PASS**, graded before I read anything else.
  - Outcome: gap 0.090 ± 0.003 at β = 1.6, 0.018 at 1.7 (still drifting), and below 0.0015 at 1.3, 1.5, 1.9 and 2.2. P1–P4 met.
  - I read its sampler (checkerboard Metropolis; staple form checked by eye) and reran it unchanged (K5): bit-identical, 12 of 12.
- **Grandchild (T13, admitted under T12 by the child, released by the child).** Question: independent P at β = 0.4 on 4⁵ against the strong-coupling leading order I₂/I₁.
  - Its control was 0.240194, and its returned value P = 0.099383 ± 0.00059, against 0.099340 for the leading order.
  - Its first run failed on its own bug. The child reran it with identical output.
  - I did not rerun the grandchild myself.

## 6. Commands to rerun (from /home/user/z4-workers/c1-excl)

```
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"        # control
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P init pcp --principal principal --principal-name "Kirtus Justus"
$P check --ws pcp --name usc-test-run3 --expect-exit 0 -- python3 usc_test.py usc_result_run3.txt   # new output name each run (mode "x")
G=/home/user/z4-work/graph/attempt.jsonl; R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos
$R task-admit $G --by principal --label c1-excl-child --parent T10          # gave T12
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$R task-release $G --by principal --id T12
mkdir child_rerun2 && cp child/su2_5d.py child_rerun2/
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 $P check --ws pcp --name child-rerun-su2_5d --cwd child_rerun2 --timeout 290 --expect-exit 0 -- python3 su2_5d.py
$P verify --ws pcp
$R verify pcp/register.jsonl
```

Register: K1 (usc, exit 1), K2 (usc, exit 1), K3 (usc, exit 0), K4 (child-run1, exit 0, 211 s), K5 (child rerun, exit 0).

Last line of `$P verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`

Last line of `pcpos verify pcp/register.jsonl`: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

Sources: Fröhlich–Spencer CMP 83 (1982) 411, abstract via search; arXiv:1110.4210 §2, §3, Fig. 1; Creutz PRL 43 (1979) 553, abstract via search (doi 10.1103/PhysRevLett.43.553); arXiv:2401.04800, snippet only.

Director, worker, child and grandchild are one model family; this is not independent review.
