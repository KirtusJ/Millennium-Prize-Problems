# Challenger report: A4 "wilson-contact" against the free benchmark (r8-contact)

Control: `control.txt` = 0.272341 (−ln tanh 1).
Director and challenger are the same model family, so this is not independent review. Everything about the interacting theory below comes from reading A4's arguments. The numbers are free-field, leading order in weak coupling.

## 1. Verdict table

| Item | Verdict | Evidence (one line) |
|---|---|---|
| K1 statement as written | STANDS (stated below) | A4 bounds the variance **removed** (Var O − Var Õ ≥ D_b) and the error of any exterior predictor, not the variance itself. Exact inequality at fixed cutoff, plus one β→∞, L→∞ limit along any trajectory. 1/18 = (1/36)·(1² + 1² + 0²). |
| K1 coefficient 1/18 (arithmetic) | STANDS | η=1/6, β²k_β→1/24, each link sits in 2 faces (Σw→2f), x- and y-links ⇒ b⁻⁵·(1/6)(1/24)·8 = 1/18. |
| K2 conversion | STANDS (unambiguous) | β(1−x_p) = Σ_a θ_a²/(2g²) + O(g²) ⇒ A4's O_b = ½ Σ_a b³Σ f(bx)(B₃^a)², i.e. three colours at prefactor ½. Free total coefficient T = (3/4)c. |
| K2 free total on the 4D Wilson lattice | measured | c₄ = 0.56258 ⇒ T₄ = 0.42194 ∫f². Sub-agent: 0.562579733, rerun by me to 10 digits. |
| K2 Hamiltonian vs 4D regularization | measured | c_H = 1.45682 (T_H = 1.0926). c₄/c_H = 0.3862: the coefficient falls by a factor of 2.59 when the regularization changes. |
| K2 bench known answer 8.110e-3 | NOT CHECKED (convention missing) | Bench gives c·∫f² for an f it never states. If f is a Gaussian with σ = 0.1: c_H·(πσ²)^{3/2} = 8.112e-3, which matches 8.110e-3 to 0.03%. This is an inference, not a check. |
| K2 1/18 below free total | STANDS | 1/18 = 0.0556 < 0.4219 (13.2% of the total). |
| K2 1/18 below free removable part | STANDS, and sharp for A4's method | Exact Gaussian conditioning on A4's mask gives R = 0.13407 = radial 0.05556 + transverse 0.07851. The radial term equals 1/18 exactly. A4's k_β = λ_∥ keeps only the radial (ξ²−1) term and drops the transverse term, so its bound is 41% of the free removable part. |
| K3 preservation at n ≥ 2 | STANDS | P_M O(t) uses spatial links on slices t−1, t, t+1 and the temporal links between them. O(t+n) uses only the spatial links at t+n. The double replacement needs n ≥ 2. |
| K3 distance one | STANDS as excluded; A4 is silent | A single replacement holds at n=1 (Cov(Õ(t),O(t+1)) = Cov(O(t),O(t+1))). Cov(Õ,Õ) at n=1 does change in general, because the masked links at t are staples of P_M O(t+1). |
| K4 4⁴, β=2.2 control | STANDS only as an identity check | 3.706 against 2.063+1.622 = 3.685, residual 0.021±0.043. The C(2) residual is 0.0003±0.041: its error bar is about 100× the signal, so it carries no information. It says nothing about 1/18, b⁻⁵, k_β or m_sp→1. |
| K5 quoted sentence "can still vanish, remain finite, or require further normalization" | NOT CHECKED (not in the supplied files) | grep finds no such sentence in input/a4/. The nearest is README l.7 ("size of the interacting separated reading … remain open"), which is correctly weak. |
| K5 "interacting counterpart of the free magnetic benchmark" (README l.7) | DEFECT (wording overreaches) | The benchmark has an asymptotic equality c·∫f². A4 has only a lower bound, 13% of the free total, on a different observable (prefactor ½, three colours, 4D lattice). It is a counterpart of the "at least b⁻⁵" half only. |

Counts (met, failed, measured only): own program k2_free.py 7, 0, 6; child programs as rerun by me 7, 0, 3. Review items: 9 STANDS, 1 DEFECT (wording), 2 NOT CHECKED.

## 2. Statements and their hypotheses (K1)

**Theorem (A4 README "One spatial slice", conditional.md).** These hypotheses apply throughout:
- SU(2);
- periodic, isotropic 4D Wilson measure exp(β Σ_p x_p) with x_p = TrU_p/2, the same β on spatial and temporal faces (each link has six faces, R ≤ 6β);
- L, T ≥ 3;
- cubic spatial box, so that m_sp does not depend on orientation;
- real tests f_ij sampled at **face centers**.

The observable is O_b(t) = (β/b) Σ_{spatial p at t} f_ij(center)(1−x_p), centered. There is no extra b³: β/b·b⁴B² supplies it. No smearing beyond the f-weights.

- (a) Fixed cutoff, exact. Var O_b − Var Õ_b ≥ D_b, and Var O_b − |C_b(n)| ≥ D_b. Any L²-predictor built from links off the slice's spatial links has MSE ≥ D_b. Here Õ is the average over masks of E[O | links outside mask].
- (b) Fixed cutoff, exact. C̃_b(n) = C_b(n) for 2 ≤ n ≤ T−2.
- (c) Limit: β→∞ and L→∞ at fixed physical size (periodic tests, or compact tests with padding), along any trajectory. Then b⁵D_b → (1/36)∫Σ_i(Σ_{j≠i}f)². For one orientation this is ‖f‖²/18. Regime class: **fixed regulator** for (a) and (b); **one limit** for (c). b only scales the Riemann sums, so this is not a continuum construction.
- Inputs for (c), from conditional.md: (6β)²k_β → 3/2 (gamma-law moments); m_sp → 1 uniformly in volume (the Haar-cap bound); Jensen's inequality, which gives E|a_e|² ≥ m²(Σw)².

What "loses" means: a lower bound on the variance removed. The variance itself is bounded below only trivially, by the same D_b.

time.md adds Var(S_b) b⁴ ≥ (1/36)∫∫… for spacetime tests, the six-orientation 1/48 bound (with a kernel), and the tanh(bE/2) spectral bound. These are not checked here.

## 3. Failed predicates
None, in my program or the child's (14 predicates in total, all met). I did not set a predicate that could have caught a defect in the bench's 8.110e-3, because the bench's f is unstated.

## 4. Not checked
- the bench constant against a stated f;
- the free removable formula on a finite lattice by direct simulation (it is derived analytically only, in notes.md step 2);
- non-perturbative validity of the leading-order comparison, including zero modes and torons on the finite torus and the order of the β and L limits;
- dual.md (two-link identity);
- time.md (spectral bounds, 1/48 bound);
- the Lean replay;
- A4's C++ and Python checks (not supplied);
- the location of the K5 quoted sentence.

## 5. Delegated question and outcome
I gave the sub-agent the formulas only. It was to compute c_A = 2Σ_r G₄(r)² (4D lattice, equal time), c_B (Hamiltonian), and G₄(0,1,0). Its control question was the exact value of G₄(0).
- Control: it answered 1/2 by axis symmetry, which is correct.
- Results: c_A = 0.562579733, c_B = 1.456824971, G₄(0,1,0) = −0.0688747458. It converged to 2·10⁻¹⁰ and had 7 of 7 predicates met.
- It could not write child/report.md (blocked), so its report exists only in its message to me.
- I reran both child programs through my register (K2, K3, exit 0). The output is identical, and it agrees with my independent k2_free.py (K1) to 3·10⁻⁹.
- The rerun's result files landed in my root directory (control_result_…014106.txt, sums_result_…014110.txt), because the child writes to the current directory.

## 6. Rerun commands (Git Bash)
```
cd C:/Users/donke/z4-workers/r8-contact && export PYTHONUTF8=1
python -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name k2_free --expect-exit 0 -- python k2_free.py
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name child_control_rerun --expect-exit 0 -- python child/control.py
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name child_sums_rerun --expect-exit 0 -- python child/sums.py
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
```
Verify, last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
