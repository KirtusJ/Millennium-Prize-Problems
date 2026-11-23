# m1-agmon report (worker of Director Z4, task T129)

- **Control:** `control.txt` = 0.272341 (−ln tanh 1).
- **Lean:** READY existed. One file was checked: `lean/Tunnel.lean`.
- **Independence:** I share a model family with the director, so my agreement is not independent review.
- **Main deliverable:** TUNNEL_THEOREM.md. Its first line states what is proved.

## 1. Verdict table

| item | verdict | evidence (one line) |
|---|---|---|
| (U) liminf −log m_eo/√β ≥ c*, unconditional | NOT CHECKED (not proved) | Proved only conditional on Lemma F (TUNNEL_THEOREM §4–5). |
| (U) conditional on Lemma F | STANDS (my written proof, not reviewed) | Uses an Agmon weight in a₁ only, T = B*K₁B with B = K₂^{1/2}e^{−V/2}, the Schur step, the fibre bound, and the sign-trial identity. |
| Lemma F: ε_eff(a) ≥ 2 asinh(sin a) − o(1) uniformly | NOT CHECKED (missing proof); numerically supported | ε_eff − ε = −c(a)/β with c ∈ [0.65, 0.98] at β = 64, 256, 1024 for 8 angles (eps_eff.py; child code agrees to 10 digits). |
| Lemma R: fibre top eigenfunction depends only on t; reduction to Legendre P_j(t), V = βs²(1−t) | STANDS | Bi-U(1) symmetry, Perron–Frobenius, Haar pushforward uniform in t. Control E5 (s = 0 gives ε_eff = 0) met. |
| Brief: fibre ground state "concentrated at the two points U₂ = ±1" | DEFECT | V_a vanishes on the whole circle of U₂ commuting with U₁, and the ground state is uniform along it. |
| Brief: needed bound ∫k e^{√β p d(g)} ≤ e^{p²/2(1+O(p/√β))} with radial d | DEFECT | log R_rad/(p²/2) = 13.2 at p = 0.25 for every β (K4). The correct form uses a C² weight, p·X and cosh (Lemma K). |
| Lemma K (Wilson-kernel exponential moment bound, explicit) | STANDS | Hand proof. Core 1 − cos θ ≥ (θ²/2)(1 − 5η²/48) is Lean-checked. Numerically holds in 50/50 cases (K1). |
| 2-D valley: transverse energy 2 asinh(√(sin²a + sin²b)) ≥ ε(a); Agmon minimiser is b = 0 with length c* | STANDS (harmonic level) | Linearisation in TUNNEL_THEOREM §6. Scalar core is Lean `valley_energy_ge`. |
| (L) limsup −log m_eo/√β ≤ c* | NOT CHECKED (missing) | Only A4's e^{−C√β} (C unspecified). The constant is lost in A4's pointwise per-step potential bound. The sharp route is outlined (CLAIMED). |
| λ_ee → 1 | STANDS (sketch) / CITED | Trial bump of radius β^{−1/3}. A4 Setup also states it. |
| Brief's heuristic operator inequality T ≤ e^{−ε_eff/2}K₁e^{−ε_eff/2} | DEFECT (not what is true or needed) | What holds: T = B*K₁B with B*B ≤ e^{−ε_eff(a₁)} fibrewise. Schur then replaces the conjugated K₁ by multiplication by w(U₁). |

Verdict counts over the 11 rows: STANDS 5, DEFECT 3, NOT CHECKED 3.

Predicate counts over my programs (eps_eff run1, kernel_lemma run2, Lean): **met 186, failed 4, measured only 67**.
- **eps_eff run1:** 64 met, 0 failed, 12 measured only.
- **kernel_lemma run2:** 121 met, 4 failed (K2), 55 measured only (50 linear ratios and 5 radial ratios).
- **Lean:** 1 met.

## 2. Hypotheses used, and where they are stated

| # | hypothesis | where |
|---|---|---|
| H1 | Model T = e^{−V/2}K₁K₂e^{−V/2}, k ∝ e^{β cos θ}, eigenvalue I_{n+1}/I₁ | brief; TUNNEL_THEOREM §0 |
| H2 | Lemma F (uniform fibre bound) | TUNNEL_THEOREM §2; MISSING |
| H3 | λ_ee → 1 | TUNNEL_THEOREM §4 (sketch); A4 Setup |
| H4 | λ_eo = λ_oe by link exchange; the odd flip taken on link 1 | TUNNEL_THEOREM §0 |
| H5 | Haar in exponential coordinates ∝ (sin θ/θ)² d³X | Lemma K proof |
| H6 | Lemma R reduction is exact; the numerics rely on it | TUNNEL_THEOREM §1; eps_eff.py docstring |
| H7 | Smooth cutoffs ρ_η and kink smoothing τ exist with the stated properties | TUNNEL_THEOREM §4 (standard, not written in detail) |

## 3. Failed predicates (all kept)

1. **kernel_lemma run1** was killed by me before writing any result. numpy `leggauss(8000)` is O(n³) and multithreaded. This was my own defect. The run is not recorded in the register as a check, because the kill also ended the wrapper with exit 144. K3 was amended to 2000/4000 nodes, and the amendment is written in the docstring.
2. **kernel_lemma run2, K2 failed in 4/12 cases** (H = 1, p ≤ 0.5, β = 1024 and 4096). This was my own expectation: I treated the Hessian error as multiplicative in p², but it is additive, O(H/√β). It is not a defect of Lemma K, since K1 (the rigorous bound) holds in every case. Because of this, check K3 has exit 1.
3. **Register check K4** (rerun of the child's program): I declared expect-exit 1, but it exited 0. This was my own expectation. The child's program exits 0 even when its predicates H5 and C3 fail.
4. **Child failed predicates** (its own expectations, kept in child/report.md):
   - H5: "min eigenvalue > 0" failed through roundoff underflow.
   - C3: "ε_eff > ε" was false in 21/21 cases. ε_eff is slightly below ε, by about 1/β.

## 4. Not checked

- A proof of Lemma F. This is the only gap in (U).
- The whole of (L), the sharp lower bound on the splitting.
- The details of the smooth cutoff and kink-smoothing constructions.
- Whether eo means flip 1 or flip 2 in the director's convention. This is irrelevant by symmetry.
- Any literature: no network fetch was made, so nothing is cited from papers.
- ε_eff for a < 0.05, and β > 1024.
- The bound E_k e^{√βLθ} = O(1) uniformly in β. It follows from Lemma K's method, but I did not write a separate statement for it.
- A4's own proofs (cited only).

## 5. Delegated questions and outcomes

- **Child T132.** Admitted under T129 (child_admit.log), run as register check K2 `child-run1` (exit 0, 198 s), released (child_release.log). Model: sonnet.
  - Control arccosh(3): it answered 1.762747, which is correct. I graded this first.
  - Question: ε_eff(a) at β = 64, 256, 1024 for 7 angles against 2 asinh(sin a). It was given the reduction hint with an instruction to verify it.
  - Outcome: its values agree with my independent code to 10 printed digits. It found ε_eff − ε = −c(a)/β, and the ratios d(256)/d(1024) are 4.01 to 4.02.
  - I reran its eps_eff.py in rerun_child/ (check K4). The values were identical; only roundoff-noise columns differed.
  - Its reduction check is partly Monte Carlo (t uniform), and it did not numerically test the non-invariant sectors.
- **Grandchild T133.** Admitted and released by the child under T132.
  - Control arccosh(2) = 1.316958, correct.
  - Question: an independent Simpson-quadrature recomputation of ε_eff at β = 64, a = π/2 and a = 0.1.
  - Outcome: 1.75256092 and 0.18402420, which agree with both codes. The child reran it in child/rerun_gc. I did not rerun the grandchild myself.

## 6. Registers

- `python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp`, last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl`, last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

Checks: K1 eps_eff (0/0), K2 child-run1 (0/0), K3 kernel_lemma_run2 (1/0), K4 rerun_child_eps_eff (0/1), K5 lean_tunnel (0/0). Each pair is observed exit / expected exit.

## 7. Exact rerun commands

These are run from /home/user/z4-workers/m1-agmon. Results are written with mode "x", so use a new tag each time.

```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name eps_eff_rerun --expect-exit 0 -- env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 eps_eff.py run2
$P check --ws pcp --name kernel_lemma_rerun --expect-exit 1 -- env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 kernel_lemma.py run3
mkdir -p rerun_child2 && cp child/eps_eff.py rerun_child2/ && $P check --ws pcp --name rerun_child2 --cwd rerun_child2 --expect-exit 0 -- env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 eps_eff.py
$P check --ws pcp --name lean_tunnel_rerun --cwd /home/user/z4-lean --expect-exit 0 -- bash -c 'PATH=$HOME/.elan/bin:$PATH lake env lean /home/user/z4-workers/m1-agmon/lean/Tunnel.lean'
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

The child was run as:

```
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
```
