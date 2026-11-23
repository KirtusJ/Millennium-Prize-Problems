# report.md: worker a3-Afs (builder, claim (A) by a finite-size criterion)

**NOT a proof.** The chain in PROOF.md has one CLAIMED step in Half 1 (S1, the Dobrushin–Shlosman criterion) and two MISSING steps in Half 2:
- S5: the flux coupling z is unbounded in L for every β. This is equivalent in strength to a confinement statement.
- S6: the bridge from a large z to the criterion K.

Control: control.txt = 0.272341. Lean READY exists, but Lean was not used: no step is pure algebra worth formalizing within the budget.

## 1. Verdict table (steps carry their tags in place of STANDS/DEFECT)

| Item | Verdict / tag | One line of evidence |
|---|---|---|
| S0 infinite-volume RP state exists; RP passes to limits | CITED (abstract level) | LIT_RIGOROUS R2 (OS78, Lüscher77, abstract only); INDEX (a)1 (Wilson RP periodic, Lean). The reflection plane type was not read. |
| S1 DS condition K(L, β, γ) ⇒ uniqueness + decay at rate −ln γ/(2L) | CLAIMED | DS 1985 not read (LIT R5d NOT CHECKED; sources conflict). Weakest point: the exact DS hypotheses and condition form are from memory. |
| S2 uniqueness ⇒ RP translation-invariant OS state | PROVED (given S0, S1) | Every periodic limit is Gibbs, hence it is the unique measure, hence it is RP. |
| S3 uniform-rate Euclidean decay on a dense set ⇒ spec H on Ω^⊥ ⊂ [m, ∞) | PROVED | Spectral measure argument, PROOF.md S3. |
| S4 z(L, β) = L·E_flux increasing in L for SU(2), constant for U(1) | CLAIMED | Perturbative b₀ sign (hole (v)). MC (one β, three sizes) does not refute it. |
| S5 sup_L z(L, β) = ∞ for every β | MISSING | Would follow from σ(β) > 0 at all β, which is Chatterjee Problem 4.1 (open). |
| S6 z(L) ≥ z* ⇒ K(kL, β, γ) | MISSING | No inequality is known. z is a periodic one-sector quantity; K is uniform over all exterior configurations. |
| S7 (A): m(β) ≥ c/(k L(β)) > 0 | PROVED from S1–S6 | Only as strong as S5 and S6. |
| Discriminator U(1), d = 4 | consistent | The first failing step is S4/S5. MC: z_U1 stays O(1/(2β)) up to the finite-T drift. |
| Discriminator finite group, d = 4 | route incomplete | z → 0 in the deconfined phase, so the route does not reach (A), which is true there. Not a contradiction. |
| Discriminator U(1), d = 3 | consistent | The route stops at S6 (bridge). |
| Discriminator d = 2 | consistent | z = −L² ln a holds exactly for both groups (child; rerun by me). The route stops at S6. |
| Non-abelian entry | S4 only | Sign of b₀ (perturbative, CLAIMED). |

Counts: PROVED 3, CITED 1, CLAIMED 2, MISSING 2.
Predicates (my program zflux.py): met 6, failed 1, measured only 6. The measured-only items are the six z values; the U(1) rotor-model comparison was added post hoc.

## 2. Hypotheses each statement uses, and where they are stated

- **S0:** compact gauge group, Wilson action, RP for periodic boxes (LIT_RIGOROUS R2; INDEX (a)1). The order of limits is box → ∞ at fixed β.
- **S1:**
  - compact metric spin space SU(2), with ρ the bi-invariant distance scaled to diameter 1;
  - finite-range interaction (plaquettes);
  - K(L, β, γ) with γ < 1, taken over all exterior configurations ω (PROOF.md S1).
  - DS's own hypotheses were not read.
- **S2:** S0 and S1. Translation invariance follows from uniqueness.
- **S3:**
  - an RP state;
  - T = e^{−H}, 0 ≤ T ≤ 1;
  - decay at a uniform rate m with an F-dependent constant K_F, on a set of local observables whose vectors are dense in Ω^⊥.
- **S4:** z defined with T → ∞ first, at fixed L. The claim rests on perturbative b₀ > 0 for SU(2) and b₀ = 0 for U(1).
- **S5:** none established. The target statement is "for all β, sup_L z = ∞".
- **S6:** none established. The target statement is "∃ z*, k, γ such that ∀ β, L: z(L, β) ≥ z* ⇒ K(kL, β, γ)". Uniformity in the volume is used here: K must hold for all exterior configurations, hence in every volume containing the box.
- **S7:** β is fixed and L(β) is finite. Nothing is needed uniformly in β.

## 3. Failed predicates

- **P_D (zflux.py): FAILED.** Predicate: "z_U1(L) for L = 4, 6 within a factor 2 of 1/(2β) = 0.217". Measured: 0.553 ± 0.078 and 0.684 ± 0.068.
  - Cause: **my own expectation**, not a defect of the target. At T = 12 the free flux zero mode (levels q²/(2βL)) is thermally populated, so m_eff(1) overestimates E_1.
  - A post-hoc rotor model at T = 12 gives 0.422 and 0.500. This is the same direction and the same size up to about 1.5 to 2.6σ, with the residual likely from excited states and the lattice renormalization of β.
  - The predicate should have used T ≫ 2βL.
- **P_B MET, but weakened by the same effect.** The upward drift of z_U1 (0.34 → 0.55 → 0.68) is a finite-T artefact by the rotor model. P_B passed only because of its 20% / 3σ tolerance.
- **Met:** C1 (SU(2) and U(1) strong-coupling plaquette), C2 (U(1) Gaussian plaquette), P_A (z_SU2 increasing: 0.562, 2.12, 8.02), P_B, P_C (z_SU2(6)/z_U1(6) = 11.7 > 2).
- **Rule 4:** all 6 of 6 (group, L) cases qualified (C(2) > 3σ).

## 4. What I did not check

- The Dobrushin–Shlosman paper itself, which decides S1's tag.
- Whether K can hold at all at weak coupling, given the sup over atypical ω. A rough Gaussian estimate makes Σκ ~ |V|, that is marginal.
- Larger T and other β values.
- Fitting instead of m_eff(1). For SU(2), m_eff(2) < m_eff(1), so z_SU2 is overestimated.
- Autocorrelations. The U(1) Metropolis zero mode is slow, and 10 jackknife bins may underestimate the errors.
- L odd.
- Any β where the SU(2) box is genuinely in the perturbative regime.
- The OS78 reflection-plane details.
- Lean: not used.

## 5. Delegated questions and outcomes

- **Child** (child/, sonnet, register check K5 exit 0, 287 s).
  - Question: verify the 2D exact flux mass m_L = −L ln a(β) (a = I₁/I₀ for U(1), I₂/I₁ for SU(2)) at β = 2.3. Tabulate z(L) = −L² ln a for L = 1..8 and check by a 2D U(1) MC at L = 2, 3, T = 16.
  - Control question (answer computed by me first): I₂(2)/I₁(2) = 0.433127. Child's answer 0.433127: **CORRECT**, graded before reading anything else.
  - Returned:
    - the table (U(1) z = 0.299·L²; SU(2) z = 0.735·L²);
    - MC m_eff agreeing with the formula at L = 2 and 3 (all pulls < 3σ, two near 2.7);
    - no failed predicates;
    - SU(2) MC NOT CHECKED (self-reported).
  - My reruns (in rerun/), all identical to the child's outputs:
    - K2 prog1_table.py: identical;
    - K4 prog2_mc.py 2: identical apart from the runtime line.
  - I did not rerun L = 3. Its "pass" is used only as a 2D code check and does not discriminate between the groups.
- **Grandchild** (child/grandchild/, the child's Agent).
  - Question: independent power-series recomputation of the Bessel ratios.
  - Control "I₀(0) = 1": correct.
  - Result: I₁/I₀(2.3) = 0.74137542, I₂/I₁(2.3) = 0.47927908, I₂/I₁(2) = 0.43312743.
  - My rerun K3 is identical, and the values agree with my own trapezoid values.

## 6. Exact commands to rerun

```
cd /home/user/z4-workers/a3-Afs
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"        # control (0.272341)
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P init pcp --principal principal --principal-name "Kirtus Justus"
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P check --ws pcp --name zflux-run1 --expect-exit 0 --timeout 400 -- python3 zflux.py result_zflux_1.txt   # new output name on rerun (mode "x"); ~120 s, 1 core
$P check --ws pcp --name rerun-child-table --cwd rerun --expect-exit 0 -- python3 prog1_table.py           # fresh copy of child/prog1_table.py (writes table.txt, mode "x")
$P check --ws pcp --name rerun-gc-series --cwd rerun/gc --expect-exit 0 -- python3 series.py               # fresh copy of child/grandchild/series.py
$P check --ws pcp --name rerun-child-mc-L2 --cwd rerun --expect-exit 0 --timeout 300 -- python3 prog2_mc.py 2
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Last line of `$P verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
Last line of `pcpos verify pcp/register.jsonl`: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
