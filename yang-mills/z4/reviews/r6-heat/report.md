# Z4 challenger report: B4 charged spatial heat trace (r6-heat)

Role: challenger. I used only the seven files in input/. Director B4 and I share a model family, so my agreement does not count as independent review. Control: control.txt = 0.272341.

## 1. Verdict table

| Item | Verdict | One line of evidence |
|---|---|---|
| Upper bound E F_s/V ≤ 2^{5/2}s^{-3/2}[2^{-(m/2)^3}+exp(-s/(2b²(5m²+65536B)))] (wilson-law, README l.26-34) | STANDS | I re-derived each step by hand: the density bound 19.17(1+R)^{3/2}, the bad-cube probability 20/512 < 1/16, the 256 and 16384 constants, 5m²+65536B, the return-probability bound, and the Golden–Thompson chain. check_constants P3–P6 met. check_cube Q1 met on 3000 of 3000 random SU(2) cubes (worst λ/r_p² = 0.041, against the stated floor 1/256). |
| Choice m = 2⌈x^{1/5}⌉ gives 2^{7/2}s^{-3/2}exp[-c min(x^{3/5},x/B)] with c = 1/132000 (README l.35-38) | STANDS | P1 and P2 met on x ∈ [1,10^60] and B ∈ [1,10^10]. Margin in logs is at least 0.29. By hand: 160x^{2/5}+131072B ≤ 131232·max(x^{2/5},B). |
| Lower bound E F_s ≥ exp[-C(x/m² + m³(B+log 2m))], cost ≤ 5x^{3/5}L^{2/5} (rare-cubes l.7-19) | STANDS (SU(2)); general G only sketched | Haar cap mass, the conditional density ≥ e^{-2(B-1)} and the sine trial (6π²+6)/m² all check. Q2 met on 600 of 600 near-flat cubes (λ at most 0.32 of the bound). P7 and P8 met. |
| Main limit log(-log E F_s)/log x → 3/5 (rare-cubes boxed, README l.7-10) | STANDS as an asymptotic statement | The two sides combine as described. The window narrows only like log(1/c)/log x. On β = log(1/b) the stated upper bound says nothing for b ≥ 10^{-3}, and at b = 10^{-50} it only confines the ratio to [0.549, 0.619] (M1). Toy optimization by the child: see §5. |
| Hypothesis B = x^{o(1)} is needed for 3/5 | STANDS (scope note) | The upper side only needs B ≤ x^{2/5}. If B = x^γ with γ > 0, the bounds only give a window [min(3/5, 1-γ), (3+2γ)/5]. β = c·log(1/b) satisfies the hypothesis: B ≈ 3c·log x. |
| Mean normalization: Y_b → 0 in probability, log log E Y_b^p/log x → 3/5 (rare-cubes l.36-49) | STANDS | Re-derived. The good event has probability ≥ 1-C\|Λ\|e^{-cx^{3σ}}. Hölder gives the lower side and Y ≤ C/E F gives the upper side. |
| Positive-time decorrelation \|E[V̄_{t+j}V_t]\| ≤ 3(h_b+√q_b), uniform in j≢0 and in P (positive-time l.21-33) | STANDS | The Cauchy–Schwarz step uses only that Z is 𝒢_t-measurable and that Pr(E_t\|𝒢_t) ≤ q_b almost surely. Var U_t ≥ 1-(h+√q)² → 1, so the factor 3 is enough. |
| Spectral escape ν_b([0,x^η/a]) → 0 for 0 < η < 3/5 (positive-time l.38-48) | STANDS, given a positive transfer S_b | It needs ⟨v,Sv⟩ ≥ e^{-aR}ν[0,R], i.e. S ≥ 0. The notes assume this through a positive-type kernel, as an explicit hypothesis. The choice η/3 < σ < 1/5 works. |
| Hamiltonian M_1(F_s/√V) ≤ 36d²/(βs²) (hamiltonian l.7-28) | STANDS (arithmetic). Its content is weak. | 24·2^{3/2}/e = 24.97 ≤ 72 (P9). The bound is on the raw, unnormalized weight. Nothing bounds ‖F_sΩ‖ from below, so the bound does not control the normalized fraction of weight. |
| General-group 3/5 and q-exponent (representations.md) | NOT CHECKED in detail | This is a sketch: the sublevel exponent α comes from a Łojasiewicz-type argument and q = k·dim G/(2α) is not explicit. Plausible, but I did not verify it. |
| Group hypothesis consistent across files | DEFECT (wording, minor) | README l.7 and l.53 say "compact connected **simple**". representations.md l.3 says "compact connected Lie group" and never uses simplicity. The theorem summary and the proof file disagree. The README is the weaker of the two, so this is harmless. |
| Notation | DEFECT (presentation, minor) | positive-time uses F_t for the trace on slice t, while elsewhere F_s indexes diffusion time. U_t is a normalized trace, but U also denotes links. V is the volume, V_t a test vector and v(x) a potential. κ_B (bare) sits next to B = 1+4β_s+2β_t. None of these changes a result, but each is a misreading hazard. |
| Cross-references outside input (../periodic-time, ../hamiltonian-time, ../joint-cutoff, HeatTrace.lean, replay.py, controls.py) | NOT CHECKED | Not supplied. The README's vacuum-norm claim (l.43) and the anisotropic Wilson-transfer clause (l.55) rest on these files. |

Counts (all predicates, mine plus the child's, rerun by me): **14 met, 1 failed, 3 measured only**.
- Mine: 11 met (P1–P9, Q1, Q2), 2 measured only (M1, M2).
- Child: 3 met (A1, A2, B0), 1 failed (B1), 1 measured only (A3).

Verdict rows: 9 STANDS, 2 DEFECT (wording and notation only, minor), 2 NOT CHECKED. I found no mathematical defect in the SU(2) proofs I read.

## 2. Hypotheses each statement uses, and where they are stated

- **Upper bound** (README l.17-34, wilson-law): the original finite periodic 4D SU(2) Wilson law with β_s, β_t ≥ 0 multiplying ½ReTr U_p, extents ≥ 3 and normalized product Haar. B = 1+4β_s+2β_t (README l.17). The particle is fundamental, with an embedded Dirichlet test domain Λ (README l.17). Even block side m with an embedding/padding condition (README l.17, l.26). Uniform in spatial volume and number of time slices (l.35).
- **Lower bound and 3/5** (rare-cubes l.3): a fixed bounded physical Dirichlet domain containing a cube of positive physical side, fixed s > 0, x = s/b² → ∞, B = x^{o(1)} meaning log B/log x → 0. Enclosing lattices may grow. Finite-volume laws. The particle representation has no invariant vectors (README l.7, representations l.3).
- **Main theorem in my words (H1).** Fix a physical Dirichlet box and a diffusion time s (a length squared). Take any sequence of finite periodic 4D Wilson lattices with spatial mesh b ↓ 0 that pad the box, with couplings satisfying 1+β_s+β_t = x^{o(1)}, x = s/b². Then the first moment E F_s of the charged heat trace Tr exp(-sA_U) satisfies -log E F_s = x^{3/5+o(1)}. Region and s are fixed. There is **one limit, b ↓ 0**, along a coupling trajectory β(b), taken after nothing: each bound holds at every finite b uniformly in the enclosing volume and period. So the enclosing volume is not a second limit, and no continuum object appears. Regime class: **joint (regulator trajectory) limit of finite-volume lattice expectations; not a continuum statement.** The 3/5 is a statement about the expectation only. The spectral statement is separate (positive-time) and one-sided: it gives escape above x^η/a for η < 3/5, with no upper location of the weight. Order of limits there: temporal period P → ∞ at fixed b and fixed finite spatial lattice, then b ↓ 0. No infinite-spatial-volume transfer is claimed.
- **Mean normalization** (rare-cubes l.36-49): same hypotheses, plus |Λ| = O(x^{3/2}) at fixed volume and good blocks of side x^σ, σ < 1/5.
- **Positive time** (positive-time l.5-33): same hypotheses, plus a conditional bound that holds uniformly given 𝒢_t (all links except the spatial links of slice t).
- **Spectral** (positive-time l.38-48): adds time homogeneity, finite spatial gauge volume, P → ∞, and a positive temporal coupling with a positive-type Wilson kernel, so the transfer S_b ≥ 0. Applied with a = b, isotropic.
- **Hamiltonian** (hamiltonian l.3-28): continuous-time SU(2) Hamiltonian γΣ(-Δ_{S³}) + W, with γ = 1/(2κ_B) and bare clock κ_B = βb. The external convention is taken from ../hamiltonian-time, which was not supplied.
- **Other groups** (representations l.3-32): compact connected G (simplicity is not used). Fixed ρ, π with no invariant vectors. The constants and q depend on (G, ρ, π).

### H3: units
s is fixed, so x = s/b² → ∞ and E F_s = exp(-x^{3/5+o(1)}) decays faster than any power of b. Proved on B = x^{o(1)} (the weaker b²B → 0 already gives vanishing).
- Unit mean gives Y_b → 0 in probability, and E Y_b^p diverges with log-log exponent 3/5: proved, on the same trajectory, on a single slice (rare-cubes l.36-49). Time-smeared averages over polynomially many slices are also covered (l.53-55).
- Centered, unit variance gives a correlation bound uniform in **every** lattice separation j ≢ 0 mod P, including j = 1, and uniform in P. A fixed physical time separation t = ja is therefore covered as well. So the notes do make a claim at fixed physical time separation: the normalized correlation tends to 0 at every separation. The notes leave open only reflected OS correlations under normalizations that are not equal-time L² (positive-time l.34, rare-cubes l.57).

### H4: spectral weight in physical units
η can be any value in (0, 3/5). The clock is the gauge-transfer log energy -a^{-1}log S_b. On β = c·log(1/b) with a = b, the threshold is R_b = x^η/a = s^η·b^{-(1+2η)} in physical units. This diverges, and **faster than the cutoff scale 1/a, by the factor x^η** (M2: η = 0.59 and b = 10^{-4} give R·a ≈ 5·10^4). So the probe's normalized weight sits asymptotically above a physical threshold that diverges, in fact at super-cutoff energies. Scope: the statement is about one vector sequence. It extends automatically to every deterministic affine renormalization of F_s, because centering and unit variance absorb a deterministic multiplier e^{sμ_b} and an additive shift. It also extends at every fixed s and fixed region. It says nothing about s_b → 0 with x bounded, field-dependent subtractions, or other gauge-invariant observables. So B4's claim "obstruction for this probe only" is accurate. The word "only" should be read as "for this probe and its whole deterministic-renormalization class at fixed s".

## 3. Failed predicates
- None of my own failed (K1 and K2 both exit 0).
- Child B1 (d=1 toy slope 0.3938 vs 1/3 ± 0.06) **failed**. Cause: the sub-agent's expectation about finite-t corrections; not a defect of the target.
- Child run 1 A1 failed because of a precision defect in the sub-agent's code. It was fixed in run 2, with the predicate unchanged.

## 4. What I did not check
- The Lean file and the replay workers (not supplied). The execution.md claims about them are not verified.
- The external notes: periodic-time (vacuum norm and P → ∞ transfer limit), hamiltonian-time (clock convention), joint-cutoff (anisotropic Wilson transfer comparison), central-quotients.
- The general-group sublevel exponent and q (representations l.11-15). Only the SU(2) proofs were checked line by line.
- The low-mode count exponent 3/2 (rare-cubes l.25-34). Read only; it looks consistent with the same block argument, but I did no computation.
- The numbers in execution.md's controls (Abelian response ratios, one-square control).
- I did not test the large-block majority/iteration step in full 4D Wilson sampling. I checked it as algebra only.

### H5: scope sentences (quoted)
- README l.13: "This establishes spectral escape for this observable; the lowest physical excitation of the full theory remains undetermined."
- README l.41: "The estimate gives a necessary scale and leaves its sufficiency and any counterterm prescription open."
- README l.49: "Determining nonzero continuum vacuum correlations and a gap for those excitations remains open."
- rare-cubes l.23: "Neither the leading constant nor a power of the logarithm in -log E F_s has been identified."
- rare-cubes l.51: "Field-dependent subtractions, changes to the charged operator and other gauge-invariant observables are separate mathematical questions."
- positive-time l.48: "A low physical excitation orthogonal to these vectors is compatible with the estimate."
- hamiltonian l.34: "Neither clock argument establishes a nonzero renormalized heat observable with finite physical excitation energy."
- execution l.13: "The nontrivial continuum gauge theory and its physical mass gap remain open."

**Summary sentences stronger than, or misleading against, their theorem:**
1. README l.7 states 3/5 "for each fixed compact connected simple gauge group and each fixed charged particle representation". The boxed proof is written for SU(2). The general case relies on a sketched sublevel lemma and leaves out "fixed Wilson action representation ρ", which is stated in representations l.3. This is stronger than what is written out.
2. README l.55 says the Hamiltonian estimate "bounds positive-energy weight". It bounds the **raw** weight of (F_s/√V)Ω. Without a lower bound on that vector's norm, it says nothing about the fraction. On the Euclidean side the raw norm is itself exp(-x^{3/5+o(1)}), so C/(βs²) carries no information there. The fuller text (hamiltonian l.28: "raw Hamiltonian spectral measure") is accurate. The summary is not.
3. README l.13 "at weak isotropic coupling with B = x^{o(1)}": B = x^{o(1)} also includes bounded β, so "weak" is not a hypothesis. This is harmless.
4. README l.43 ("the norm of the vector excited by the bare trace vanishes ... in the discrete transfer vacuum") depends on an unsupplied file. The arithmetic part (E F² ≤ 2Vs^{-3/2}E F) is correct.

### H6: internal consistency
β_s and β_t multiply ½ReTr U_p (README l.17), and B = 1+4β_s+2β_t is used the same way in wilson-law, rare-cubes, positive-time, representations and hamiltonian l.34. Isotropic means B = 1+6β. a is the time step, b the spatial mesh, and a = b in the isotropic case. These are consistent. The group generality differs (simple vs. connected Lie). SU(2) is actually used in: the quaternion-linear conditional law and the 20(1+R)^{3/2} bound; the identity (I-U_p)*(I-U_p) = r_p²I; the constants 256, 16384 and 65536; the explicit lower-bound density e^{-2(B-1)}; the probabilistic λ_min bound; the whole Hamiltonian section; the adjoint control; and the Lean checks. Other groups enter through representations.md only, with unspecified constants.

## 5. Delegated question and outcome
Question delegated (TOY, to a general-purpose sub-agent working in child/ with its own register child/pcp). The sub-agent was given (A) the exact integer optimization min_m [x/m^2 + m^3 L], with L = B + log(2+x) on the trajectory beta = log(1/b), s = 1, isotropic, together with the upper-side ratio for c = 1/132000; and (B) the d = 1 analogue of the obstacle-survival exponent d/(d+2) = 1/3, computed by exact DP. Its control question was sum 1/k^2, and it answered 1.644934 (correct).

What came back, which I reran myself (my K3, exit 1 as expected, results identical in child/results_3.txt):
- K = (5/2)(2/3)^{3/5} ≈ 1.96013. I checked the derivation by hand.
- A1 met: the integer optimum is within 0.21% of K x^{3/5} for x ≥ 10^6.
- A2 met: log(cost)/log x → 3/5 monotonically, with gap 0.0056 at x = 10^300.
- A3 measured only: the stated upper bound first gives a nonnegative exponent at x = 10^9. At x = 10^300 it gives 0.5829, which agrees with my own M1 (0.5829), computed independently.
- B0 met: DP equals brute force for t ≤ 14.
- **B1 failed**: the fitted slope over t ∈ [500, 2000] is 0.3938, against 1/3 with tolerance 0.06. The local slope falls steadily (0.477 → 0.387 between t = 40 and 1600). This failure comes from the sub-agent's tolerance, its own expectation of how fast the finite-t corrections fade. It is not a defect of B4's target. The toy is in d = 1 and is not B4's model.
- The sub-agent's first run (its K1) failed A1 because of a precision defect in its own code (60 digits). It fixed the precision, kept the predicate, and kept results_1.txt.

Conclusion: the toy supports the optimization arithmetic behind 3/5 (exact for the stated cost function) and shows how slow the convergence is. It does not independently test B4's probabilistic bounds.

## 6. Exact commands to rerun
```sh
cd C:/Users/donke/z4-workers/r6-heat
export PYTHONUTF8=1
python -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"        # control
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name constants --expect-exit 0 -- python check_constants.py
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name cube --expect-exit 0 -- python check_cube.py
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name child_toy_rerun --expect-exit 1 -- bash -c "cd child && python toy.py"
(cd child && python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp)
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
```
Result files are never overwritten: each run writes results_*_<n+1>.txt.

PCP verify (last line): `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`. The child register gives the same line.
