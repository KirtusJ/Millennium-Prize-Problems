# report — p9-rev3 (third revision, small), task T62

Control: control.txt = `0.272341` (−ln tanh 1).

## Verdict table

| Item | Verdict | Evidence |
|---|---|---|
| Original `\theta_aS` in the chessboard proof | DEFECT (of the target) | `\theta_a` is defined nowhere in the file; only `\theta_r` (`x_j↦2r−x_j`) and the index action `t'_j=2r−1−t_j` are defined. Now replaced by `\theta_rS`, defined explicitly. |
| Corrected doubling and iteration with `\theta_r` | STANDS | check_rev3.py P1: S_i⊂H_+, θ_rS_i = [−2^{i+1}+1, −2^i], the two are disjoint, and after k steps the union is Z/LZ. 14/14 cases (k=2..5). P2: θ_r∘ϑ_t = ϑ_{t'} on sites, 1360/1360 cases. |
| Original τ, `F(U_{·−e0})` | DEFECT (of the target) | It sends a function of time-0 links to time −1, outside A_+ (P3; the child's C4 gives supp={5} on Z/6). |
| Corrected τ, `F(U_{·+e0})`, maps A_+ into A_+ | STANDS | P3: 9/9 cases. Child, rerun by me: 63/63 supports shift by +1, and 7/7 supports in {0,1,2} stay in A_+. |
| θτ = τ^{-1}θ under the corrected convention | STANDS | P4: 30000 evaluations, difference 0 (tolerance 1e-12). Child: 4000 evaluations, difference 0. |
| ⟨v,T^n v⟩ = Cov(O_{p0},O_{p_n}) | STANDS | Under the corrected τ, τ^n O_{p0} = O_{p_n} literally (P5: 15/15). The old convention gave O_{p_{−n}}, which is equal only by reflection symmetry. |
| Proof of Lemma pf:lem-transfer | STANDS (it does not depend on the sign) | It uses only translation invariance and θτ = τ^{-1}θ. I read it and left it unchanged. |
| N5: preprint Lemma 139 / Thm 140 are as the reviewer describes | STANDS | I read pp. 77–78. The torus has L=2^m≥4 (I checked the superscript on the page image). It uses site-hyperplane reflection positivity plus the chessboard estimate for cube events, and "a plaquette lies in exactly four unit cubes" (≥L^4/4 bad plaquettes). It sets q = min(1, exp(6(log β_W+C0) − β_W ρ²/16)) per cube, which is 6(log β_W+C0) − t/4 when t = β_W ρ²/4. |
| N4: Wilson T ≥ 0 on the site-reflection space | NOT CHECKED | Inserted as reported, marked as not proved and not used. |
| N5: joint-event bound | NOT CHECKED | Inserted as reported. |
| N3: dissemination for even L ≥ 4 | NOT CHECKED | Inserted as "not read". |
| V7: second-lineage verification of the chessboard estimate and the tail | NOT CHECKED | Quoted from NEW_REVIEW_POINTS.md (comments 7105946691, 7105949912). |
| Build | STANDS | 3× pdflatex exit 0; 0 errors, 0 LaTeX warnings, no undefined references; **53 pages**. |
| Alias grep (A4,B4,C4,D4,G4,Z4, Director, group A/B/C/G) | STANDS | 0 hits, case-sensitive. A case-insensitive search finds lowercase "director" in pre-existing role descriptions (main.tex:58, sec_provenance.tex:6, :31) and the repository path `yang-mills/z4/attempt` in refs.tex. I left these unchanged. |

Predicate counts:
- My own (check_rev3.py): 5 met, 0 failed, 0 measured only.
- Child's N=6 program, rerun by me: 5 met, 0 failed.
- Page count: 1 measured only.
- Child's extra N=2 run: 2 failed. These are the child's own expectations, not defects (see below).

## Hypotheses each statement uses, and where they are stated
- **Chessboard lemma**: L=2^k, k≥2, f≥0 bounded measurable on block 0 (sec_proof.tex, Lemma pf:lem-chess). It also uses site-plane reflection positivity on the torus, Lemma pf:lem-rp (§pf:sec-rp).
- **τ / transfer matrix**: μ∈L_β is translation invariant and reflection positive in the site plane {x_0=0}. This is Lemma pf:lem-limit(1),(2); A_+ is defined at the start of §pf:sec-transfer.
- **Cov identity**: θO_{p0}=O_{p0}, because p_0 lies in {x_0=0}, and p_n := p_0+ne_0 (sec_proof.tex l.47).
- **Preprint Thm 140**: β_W≥1, 0<ρ≤1, a torus of side 2^m≥4, and an arbitrary set A of unit cubes (preprint p.77). For the C0 of Lemma 139, text extraction gives "12 + 23 log(24π3)". I read this as 1/2 + (3/2)·log(24π^3) but did not check it against the page image.

## Failed predicates
- My programs: none.
- Child: its N=2 boundary run failed P2b and P4. At N=2 the closed half A_+={0,1} is the whole ring, so nothing can leave it. This is the child's own expectation, not a defect of the target, and the child says so too.

## What I did not check
- **N4 positivity, the joint bound, and even-L dissemination**: not checked.
- **The second lineage's verification (V7)**: I did not check it. I also did not re-derive the chessboard estimate beyond the index bookkeeping, and I did not check Corollary pf:cor-tail or the free-energy constants.
- **Tension for the director**: N1 says its group checked the "temporal-chain integration", which is the upper-bound proof of Lemma pf:lem-free. sec_provenance still lists "the free-energy bounds beyond the arithmetic of the constant" as not verified. The brief asked me to move only the chessboard estimate and the tail, so I left that line as it was.
- **The reviewer's Y_p**: in the joint bound I wrote the reviewer's Y_p as O_p. I took Y_p = O_p because the tail e^{60.2−t/8} is the paper's tail for O_p. The reviewer's definition of Y_p was not available to me.
- **Preprint version**: the title-page footnote of v6 says "version 5". This is an inconsistency in the preprint itself. The bib entry cites v6 as fetched.
- **arXiv**: I did not consult arxiv.org; the hexagonmath PDF supplied all the bibliographic fields.
- **Lean**: READY exists, but I did not use Lean.

## Delegated questions and outcomes
- **Child, T64** (admitted under T62, released; event 133). Question: on Z/6 with a toy one-variable-per-slice configuration, does the corrected τ shift support forward, keep A_+ invariant except for supports that contain slice 3, satisfy θτ=τ^{-1}θ, and does the old convention leave A_+?
  - Control answer: 0. Correct, and graded first.
  - Outcome: C1–C4 STANDS.
  - I reread check.py; its definitions match mine. I reran it in child_rerun/ under my register (K3), and the result is byte-identical to the child's result_N6.txt.
- **Grandchild, T66** (admitted by the child under T64; the child reports it as released). Question: the boundary case N=2. Is θ the identity on slices, does C3 hold, and is τ²=id?
  - Reported: all True, and its control is 0.
  - I did not rerun the grandchild myself. The child reports that it reran it.

## Records
- PCP register `pcp`:
  - K1 child-run1 (exit 0, 69.8 s)
  - K2 check-rev3
  - K3 child-rerun-N6
- `python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp` → `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl` → `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

## Rerun commands
```
cd /home/user/z4-workers/p9-rev3
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name check-rev3-again --expect-exit 0 -- python3 check_rev3.py   # first move check_rev3_result.txt aside (mode "x")
$P check --ws pcp --name child-rerun-again --cwd child_rerun --expect-exit 0 -- python3 -I check.py 6 rerun2_N6.txt
cd paper && for i in 1 2 3; do pdflatex -interaction=nonstopmode -halt-on-error main.tex; done; pdfinfo main.pdf | grep Pages; grep -i undefined main.log
cd .. && grep -nE "\b(A4|B4|C4|D4|G4|Z4)\b|Director|[Gg]roup [ABCG]\b" paper/*.tex
(cd orig && for f in *.tex; do diff -u $f ../paper/$f; done)
$P verify --ws pcp; /home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
