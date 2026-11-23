# e2-chalBgen (T47): challenge of THEOREM_B_GENERAL.md / general.tex

Control: control.txt = 0.272341 (-ln tanh 1).

**Plain verdict.** The extension is proved, relative to the SU(2) proof, for **every compact Lie group G with dim G >= 1 and a faithful unitary rho, connected or not.** I found no line that fails for that class. The first line that fails outside it is Lemma Wick / Assembly ("Var X_0 >= d/8 > 0"). For d = 0 (finite groups) the limit field is 0, and the builder says so. general.tex has one statement-level defect: it defines d := dim G and says "otherwise replace G by rho(G)", but it never requires dim rho(G) >= 1 and never says that d then means dim rho(G). With a non-faithful rho, "Var X_0 >= d/8" with d = dim G is false. For example, take G = U(1)xSU(2) with rho = the SU(2) fundamental only: the field has 3 colours, not 4. With rho trivial the theorem is false outright. The .md file states this correctly (H2: "effective condition dim rho(G) >= 1"). The ratio bound itself is unaffected.

## 1. Verdict table

| Item | Verdict | Evidence |
|---|---|---|
| Main claim, all compact Lie G with dim >= 1, faithful rho | STANDS | Every changed step re-derived by hand (sections 2 and 3 below); no failing line found |
| A1(i) disconnected G: zero of the action, Laplace near/far split | STANDS | The box gauge fixes T_int (the time link at x0 is set to 1) and a shell tree. This kills the residual gauge copy at x0 by a reflection, and Cor zero(1) holds for any group. ratio_check QB1: with h_{+0}=1, exactly 1 of 128 O(2) component patterns has min S=0. QB2: the next minimum is 6 |
| A1(i) without gauge fixing (child T49) | STANDS (as expected) | Exactly 2 of 256 patterns have S=0: all det +1, and all det -1 (the gauge copy). The other minima are 6, 10, 12, 14, 16 (= number of odd plaquettes, 256/256). Rerun byte-identical (K3) |
| A1(ii) O(2): Ad acts as -1 on so(2); background law | STANDS | Ad(G) enters only in the base-point step (Haar on all of G) and (c). Lemma Wick uses only E\|f\|^2 and Var\|f\|^2, so a symmetric or correlated f law changes nothing. QA2: 0 violations in 3000 cases |
| A2 no group factor; U(1)xSU(2) with charge 3 + fund | STANDS | Hessian of s = (1/2)\|X\|_rho^2 equals the observable's form. QA3: ratio = c(1) exactly for d = 1, 3, 4, 8, 248. QA2: mismatched forms A ≠ B, worst ratio = c(1) = 1.897490e-2 (reached at f=0). MC: U1xSU2 0.58357±0.00096 vs 7/12. Note: charge 3 + fund is **not faithful** (kernel Z_3); rho(G) ≅ U(1)xSU(2), so d = 4 is unchanged |
| A3 Lemma V constants, counterexample | STANDS | Hand check: c_V via Jordan on \|X\| <= pi/(2 sqrt N), and monotonicity for t <= 1. C_V via (C2) and eta_*. U(1) with charge 1 + charge k: lim V/sqrt t = 2/(pi sqrt(1+k^2)) and V(1) ≈ 1/2, so the ratio is ≈ pi k/4 (39 at k=50). eta_* depends only on (G, rho), not on beta or the box. Vol_rho(SU(3)) = sqrt3 (2pi)^5/(2·81) agrees with Macdonald's formula rescaled by 3^{-4}, giving 9 sqrt3/(8 pi) |
| A3 charge 1 + charge 5 (deep local minima) | STANDS | The far region is covered by eta_* > 0 (local minimum at t=2pi/5 has s ≈ 0.345). MC U1_15: 0.14602±0.00031 vs 7/48 |
| A3 "replace G by rho(G)" for the conclusion | STANDS | Pushforward of L_beta(G) lies in L_beta(rho(G)). The rho(G)-Hilbert space embeds isometrically in the G one, so m_mu(G) <= m(rho(G)): the direction is correct |
| general.tex hypothesis statement for non-faithful rho | DEFECT (minor, statement) | d := dim G, with no dim rho(G) >= 1. Var X_0 >= d/8 is false when ker rho has positive dimension; the theorem is false when rho is trivial |
| A4 chart: injectivity on Omega, radius pi/sqrt N, Jacobian | STANDS | Principal log is unique for normal matrices with spectrum in i(-pi,pi). Eigenvalues of ad X are i(theta_j - theta_k). Minimal-geodesic argument correct. (C1)-(C3) re-derived. No beta appears in any chart constant |
| A5 RP / chessboard | STANDS | Needs only s(U^{-1}) = s(U), inversion-invariant Haar, and a real action. Chessboard and free-energy steps are group-free; the Haar lower bound for {a <= beta^{-1/2}} holds with the same c_V for beta >= 1 |
| (N1) far region, (N2) near region, (E3) general | STANDS | Constants 12 sqrt(nu_s) M, 2N delta e^{4 sqrt N delta}, 48 N^2 delta^2 e^{8 sqrt N delta}, and N s_p^2 e^{sqrt N s_p} re-derived |
| (N4) normalisation E O_p -> 7d/48 on R_1 | STANDS | C_pp = 7/24 re-derived: R_1 is the cocktail-party graph K_{2,2,2,2} on 8 arms, and by Foster the 24 edge resistances sum to 7. MC (box_mc, beta=300) for U1, U1_15, O2, U1xSU2, SU3: all within tolerance (table below) |
| A6 finite groups fail at Assembly | STANDS | F ≡ 0, so Var X_0 -> 0 and the argument gives nothing |
| A6 Z_2 gapped at weak coupling (mass ~ beta); consistency with Adhikari–Cao | NOT CHECKED | No network. It is consistent with the program's citation of Adhikari–Cao (decay of correlations for finite-group LGT at weak coupling), which I recall from memory and did not verify |
| A7 general.tex vs proved hypotheses | DEFECT (minor), else STANDS | Only the non-faithful/d issue above. It does not overclaim connectedness-freeness: that is proved. The "Check" line agrees with my MC |
| Nit: "a satisfies the four relations verbatim" with a = ∞ off G_0 | STANDS with a nit | \|a(AVB) - a(AB)\| is ∞ - ∞ when AB ∉ G_0. The builder actually uses chi wherever this matters |
| Builder's B1–B7, Lean L1–L5 | NOT CHECKED | Their programs and Lean file are not in my directory. I ran no Lean (READY exists; no Lean claim made) |

Box MC (results_box_mc.txt, 64 chains, seeds 1000+10·i, beta=300 is the predicate, beta=1200 is measured only):

| G | d | pred 7d/48 | beta=300 | beta=1200 |
|---|---|---|---|---|
| U(1) | 1 | 0.14583 | 0.14619±0.00030 | 0.14553±0.00037 |
| U(1), charge 1+5 | 1 | 0.14583 | 0.14602±0.00031 | 0.14569±0.00041 |
| O(2) | 1 | 0.14583 | 0.14649±0.00031 | 0.14569±0.00037 |
| U(1)xSU(2), 3+fund | 4 | 0.58333 | 0.58357±0.00096 | 0.58608±0.00167 |
| SU(3) | 8 | 1.16667 | 1.16496±0.00202 | 1.17054±0.00313 |

Predicate counts (met, failed, measured only): **16 met, 0 failed, 6 measured only.**
- box_mc: P1×5 met, P2 met; measured: 5 beta=1200 runs.
- ratio_check: QA1, QA2, QA3×5, QB0, QB1, QB2 met; measured: the distinct-minima list.

Item verdicts: **STANDS 15, DEFECT 2 (both the same minor statement issue in general.tex: the hypothesis row and A7), NOT CHECKED 2.**

## 2. Hypotheses each statement uses, and where they are stated
- (H1) G compact Lie, d = dim G >= 1, connectedness not needed: md §1 H1; general.tex line 4.
- (H2) rho faithful, continuous, unitary (used for positivity of <,>_rho, the unique zero of s, and eta_* > 0); otherwise pass to rho(G): md §1 H2 (with dim rho(G) >= 1); general.tex line 4 (**without** dim rho(G) >= 1).
- (H3) d=4, Wilson action, periodic boxes of side 2^k, weak limit points: md §1 H3; sec_proof_SU2.tex lines 5–8.
- Compactness gives eta_*, eta(delta), and K_N: md §2, §5 N1; tex lines 12 and 26.
- Unimodularity/inversion invariance (RP): md table, Lemma rp.
- Cited facts: Haar density in exponential coordinates, Hopf–Rinow and bi-invariant geodesics, null level sets of real-analytic functions, Z_2 gap, U(1) Coulomb phase: md §6.

## 3. Failed predicates
None of mine. The child had one, K1: scipy was missing. That is an environment defect, not a target defect; the child used its own BFGS. The child also had a wrong expectation of its own (48 plaquettes instead of 24), which was not coded as a predicate.

## 4. What I did not check
- The Z_2 / finite-group literature (no network).
- The builder's numerics B1–B7 and Lean L1–L5.
- The Monte Carlo covers only the minimal box R_1 with trivial shell. It does not cover the infinite-volume limit or nontrivial shell data.
- The statement "Haar density = prod (sin(l/2)/(l/2))^2 / Vol" was checked only against the formula's structure, not re-derived.
- Real-analyticity / null level sets on non-identity cosets (N3): accepted as standard.
- K_N, eta(delta), eta_*: no numerical values.
- Within my 35-minute budget the proof check is a careful read plus spot re-derivations, not a line-by-line formal audit. We share a model family, so this is not independent review.

## 5. Delegated questions and outcomes
- **Child T49** (admitted under T47, ran in my register as child-run1/K1, exit 0, released). Question: the O(2) minimal-box minimization, all 2^8 component patterns, without gauge fixing. I graded the control first: child/control.txt = 2, which is correct. Result: zero set = the gauge orbit at x0 (2 patterns: all +, all −). The other minima are 6, 10, 12, 14, 16, equal to the number of odd plaquettes (s = 1 exactly there). The smallest nonzero minimum is 6. Its "DEFECT in the claim's wording" refers to the phrasing of my own prompt (I asked whether shell data force g = 1), not to the target. In the paper's box gauge, T_int removes the copy; my QB1/QB2 confirm this independently. I reran its scan.py (K3) and its grandchild's gc.py (K4): outputs identical apart from the timing line.
- **Grandchild T50** (admitted by the child under T49, released). Question: recompute S for the configuration gauge-transformed by a reflection (expected 0) and for a single reflected link (expected 6, in 6 plaquettes). Result: 0, 0, 6, 6. Control passed. I reran it: identical.

## 6. Rerun commands (from /home/user/z4-workers/e2-chalBgen; move existing results_* files first, since outputs use mode "x")
```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name box_mc --expect-exit 0 --timeout 300 -- env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 box_mc.py
$P check --ws pcp --name ratio_check --expect-exit 0 --timeout 280 -- env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 ratio_check.py
mkdir -p rerun_child && cp child/scan.py child/grandchild/gc.py rerun_child/
$P check --ws pcp --name rerun-child-scan --cwd rerun_child --expect-exit 0 --timeout 280 -- env OMP_NUM_THREADS=1 python3 scan.py 3
$P check --ws pcp --name rerun-grandchild-gc --cwd rerun_child --expect-exit 0 --timeout 120 -- python3 gc.py
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos task-admit /home/user/z4-work/graph/attempt.jsonl --by principal --label e2-chalBgen-child --parent T47
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos task-release /home/user/z4-work/graph/attempt.jsonl --by principal --id T49
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
Last lines:
- `$P verify --ws pcp`: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- `pcpos verify pcp/register.jsonl`: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."
