# report — a9-chalL34 (challenger of L3_L4.md), Director Z4, principal Kirtus Justus

Control: control.txt = 0.272341 (−ln tanh 1). I share a model family with the author and the director, so my agreement is not independent review. Lean: /home/user/z4-lean/READY exists, but I did not use Lean. The author's L34.lean is not in this folder, so its Lean claims (`one_sub_cos_ge`, `half_pos_part_sq`, `norm_add_sq_ge`, `exp_rem`) were **not rerun**. I checked them by hand only.

## 1. Verdict table

| item | verdict | evidence (one line) |
|---|---|---|
| A1 zero set / global lower bound (L3 §1, §2b) | STANDS | Lemma A's axial-tree induction is correct. A centre flip at the interior site changes the T_int link, so the gauge kills it. prog_a1: N=1, 400/400 cooled Haar starts end at U=1 (S=0) and no other stationary end state exists. One free link forced to −1 gives min S = 11.834. N=2: 4/4 starts end at U=1. |
| A2 constants of the near region | STANDS | Recomputed by hand: ¼(½λ−…) gives (λ/8 − 48δ²e^{8δ})\|φ\|² − (6+48δ²e^{8δ})\|ψ\|² ≥ (λ/16)\|φ\|² − 7\|ψ\|². Also correct: the HS-norm √2 factors, the count of 6 plaquettes per link, and \|dψ_p\|² ≤ 4Σ. Linearisation is used only where s_p ≤ 4δ, and the far region uses only compactness, so the class-angle vs curl issue does not arise. J ≤ 1/(2π²) and J vanishing at \|x\|=π only lowers the density. λ(1)=0.83772234 and λ(2)=0.14712176 reproduced. η(0.03)/δ² ≈ 1.50 (proxy) > 0. |
| A2 η(δ) explicit | DEFECT (acknowledged by author, not fatal) | The author's c is not explicit: c = min(λ/16, η/(2nπ²)), and η is obtained by compactness only. My proxy gives c ≈ 1.35e−3/(2·7·π²) ≈ 1e−5 for N=1. Positivity is all that L3 needs. |
| A3 shell simple connectivity (Lemma B) | STANDS | The gluing proof is correct. I checked that every shell plaquette lies in a face x_i=±N, which the proof uses silently. Child (rerun identically): H₁=0 over GF(2), Q and Z for N=1 (V80 E208 F192) and N=2 (V544 E1568 F1536). |
| L3 (c),(d) uniform Laplace limit | STANDS | (E3) gives the pointwise O((r+M)³/√β) error. Domination is (2π²)^{−n}e^{7M²}e^{−c\|φ\|²}. Uniform L¹ convergence of the densities gives the TV statement for bounded measurable W, and z_M>0 by compactness. |
| A4 L4(a) path/base independence, colour, translation | STANDS | The random-gauge argument in (iii) is correct: V(Ũ)=g_oVg_b^{−1} is Haar and independent of G(Ũ) because g_o is independent of everything else. ‖Ad V − I‖ ≤ 2α(V) holds. Translation invariance is claimed only for the LIMIT law, through (i). |
| A4 Bianchi (iv) | STANDS (terse) | The cube word identity (six transported faces multiply to 1) is asserted, not written out: neither the order nor the transports are given. It is the standard identity for ∂(cube) ≅ S². I did not check it by program. |
| A4 moments / UI | STANDS | E O_p²O_q² ≤ (E O_p⁴ E O_q⁴)^{1/2} is bounded uniformly, by S3a. That gives UI of O_pO_q, so Var and Cov converge. |
| A5 DLR in the limit | STANDS | ψ^β = L(dψ^β) exactly (L is a left inverse of d on T_s-gauge shell forms, and d is injective there). dψ^β − F_sh^β → 0 in probability. F_sh is 𝒢_R-measurable because shell plaquettes ∉ P_R. Cylinder w_out generate 𝒢_R, and bounded-Lipschitz w_in determine the regular conditional law. |
| A6 standard facts | STANDS, list incomplete | The six facts are used within their hypotheses. Also used but not listed: existence of regular conditional distributions (Polish), Kolmogorov / product Haar on infinitely many sites (L4 (iii)), Scheffé / dominated convergence for TV in L3, and Lévy's downward theorem (v2 Lemma R). All are textbook. None is non-standard. |
| A7 interface repairs | STANDS (terse) | §3(b) works along an arbitrary sequence (β_k, μ_k) with bounds uniform in μ ∈ 𝓛_β. v2's undefined Φ^b_out and Ψ̃ are no longer used. L4 is still not stated as one theorem with explicit quantifiers. |
| A8 minimal-box Monte Carlo | STANDS | My own heatbath, N=1, flat shell, 10⁵ sweeps. β=500: mean O = 0.437354 ± 0.000423 against (3/2)C_pp = 0.4375, and X = 0.291507 ± 0.000709 against C_pp = 7/24. β=50: O = 0.437709 ± 0.000457. |
| L3_L4 §4 claim "Theorem B′ proved modulo §6 and L=2^k" | STANDS for the L3/L4 part; NOT CHECKED for all of v2 | No failing line found. I spot-checked these steps of v2 (see §4): Lemma 3's constant 60.19, the chessboard doubling ranges, the image count, the Cov formula, and d*h = 0 despite T_int pinning. |

Counts (rows of the table): 11 STANDS, 1 DEFECT (non-fatal, η not explicit, already declared by the author), 0 NOT CHECKED. One row is also partly NOT CHECKED (the rest of v2).

**Plain answer to the brief.** I found no line of L3_L4.md that fails. Given textbook measure theory (the six listed facts plus the four unlisted ones in A6) and L = 2^k, the L3/L4 gap of PROOF_B_v2 is closed. Theorem B′ is then proved in this folder's sense, with two provisos:
- I did not re-audit Lemma D (identification of lim C^R with P and P_{p0pn} = G(n)) or Lemma G (the n^{−5} lower bound).
- The Lean lemmas the text relies on were not rerun, because L34.lean is absent here.

What is merely terse:
- the Bianchi word identity;
- the unlisted standard facts;
- L4 not being stated as a single theorem;
- "inf ≥ 0.1738" in §2(b). That number comes from 120 random samples, so it is a sampled minimum, not an infimum. It is labelled as measured, but it is not evidence for the bound.

## 2. Hypotheses each statement uses (and where stated)

- **Lemma A:**
  - the box 2-complex (all links and plaquettes of R);
  - U flat on all plaquettes;
  - for uniqueness, shell links = 1 and T_int links = 1 (L3_L4 §1);
  - shell graph connected (prog1 Q2, and my child's c=1).
- **Lemma B:**
  - the shell 2-complex;
  - faces are 3-boxes;
  - every shell plaquette lies in a face (used, not stated; verified by me);
  - the order of gluing (§1).
- **L3:**
  - box R, N ≥ 1;
  - T_s, T_int gauge (§2a);
  - Lemma H (λ>0; v2 §3);
  - zero set (Lemma A);
  - |ψ| ≤ M with β ≥ β₀(M) (§2b);
  - δ chosen with 48δ²e^{8δ} ≤ min(λ/16, 1);
  - (E1)–(E3), with (E3) needing α(U_p) < π (§0);
  - S3a for the tails of ψ (v2 §2).
- **L4:**
  - μ_k ∈ 𝓛_{β_k} (gauge invariant, translation invariant, DLR per v2 Lemma 1′);
  - S3a uniform in β ≥ 1 and μ;
  - path choices: paths for q ∉ P_R avoiding Λ′_R, paths for p ∈ P_R inside R (§3c step 1);
  - the six facts (§6).

## 3. Failed predicates

None of mine failed:
- prog_a1 Q1–Q8: 8 met, 0 failed, 3 measured only (the list of distinct end values, the −1-forced minima, the η proxy).
- prog_a8 M1–M3: 3 met, 0 failed, 1 measured only (X at β=50, 2.7 SE above C_pp, which is consistent with an O(1/β) correction).

Child: 7 met (P0–P6), 0 failed.

Tolerance sources:
- 1e−6 for λ: the author's printed decimals.
- 1e−12: float round-off.
- 1e−10 and 1e−4: cooling convergence levels.
- 0.5 rad: my own choice, near-region threshold.
- MC: 4 SE from batch means (100 batches), plus 0.5/β. The 0.5/β allowance is my own guess of the O(1/β) scale and is not derived. The β=500 values are within 0.4 SE without it.
- Child: exact integer arithmetic.

## 4. What I did not check

- v2 Lemma D (lim C^R = P and the Fourier formula for G(n)) and Lemma G (the explicit lower bound c₀ n^{−10}).
- v2 Lemma 1 site-plane RP in full detail.
- S2's Lean check.
- The author's Lean file L34.lean: absent, not rerun.
- The cube word identity behind Bianchi: not written out by the author, not checked by me.
- π₁ of the shell by computation. The child computed H₁ only. π₁ = 1 rests on Lemma B's proof, which I checked by hand.
- The global bound βS ≥ c|φ|² − 7M² was not sampled by me. I checked its ingredients instead: unique zero, min S with a −1 link = 11.83, η proxy > 0.
- N=2 minima: only 4 starts were run.
- No literature source was read for the standard facts.

## 5. Delegated questions and outcomes

- **Child** (sonnet, child/, register child/pcp; run recorded as check K1, exit 0, 56 s).
  - Question: homology H₁ of the shell 2-complex for N = 1, 2 over GF(2), Q, Z.
  - Control (sites of Z⁴ with sup-norm 1): answered 80. Correct; graded before reading anything else.
  - Returned: H₁ = 0 over GF(2), mod 2³¹−1, and Z (unit-pivot elimination exhausts the boundary matrix; rank 129 = E−V+1 for N=1, 1025 for N=2; d₁d₂ = 0).
  - I reread shell_h1.py. The boundary map and the unimodular elimination are correct. I reran it in rerun_child/ (checks K2, K3): byte-identical output.
- **Grandchild** (child's sub-agent, child/grandchild/).
  - Question: independent recomputation of V, E, F, b₁ over GF(2) for N=1.
  - Control: 26 sites of Z³ with sup-norm 1, correct per the child.
  - Returned: V80 E208 F192, c=1, rank 129, b₁ = 0. This agrees with the child, and the child reports that it reran it.
  - I did not rerun the grandchild's code myself. Its numbers are superseded by my rerun of the child's program.

## 6. Exact commands to rerun

The result files are opened with mode "x", so delete or move the old ones first.

```
cd /home/user/z4-workers/a9-chalL34
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"            # control
rm -f a1_results_N1.txt a1_results_N2.txt a8_results.txt rerun_child/res_1.txt rerun_child/res_2.txt
$P check --ws pcp --name a1-zeroset --expect-exit 0 -- python3 prog_a1.py      # ~3 min, 1 core
$P check --ws pcp --name a8-mc --expect-exit 0 -- python3 prog_a8.py           # ~4 min, 1 core
$P check --ws pcp --name rerun-child-N1 --cwd rerun_child --expect-exit 0 -- python3 shell_h1.py 1
$P check --ws pcp --name rerun-child-N2 --cwd rerun_child --expect-exit 0 -- python3 shell_h1.py 2
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Last lines:
- `$P verify --ws pcp`: `Result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- Rust `pcpos verify pcp/register.jsonl`: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
