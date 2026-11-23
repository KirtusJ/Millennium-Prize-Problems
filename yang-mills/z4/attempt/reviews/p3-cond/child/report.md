# T27 report (p3-cond child). Principal: Kirtus Justus

**Control:** dim so(4) = **6** (control.txt). Same-family model as the sources, so not independent review.

## Q1. Rewriting vs sources (sec_reduction.tex vs THEOREM_S.md / CHALLENGE_S.md)

| Line | Statement | Source | Direction |
|---|---|---|---|
| 3 | "Both theorems are proved in full" | THEOREM_S §4: steps 2 and 11 "PROVED (sketch)"; step 7 "CITED-2nd"/CLAIMED; tex l.183 itself says the OS description "was not read" | **stronger** |
| 15, 39, 328 | "For the Wilson action T_β ≥ 0 is a theorem of [Lu77]" | CHALLENGE_S header: Lüscher 1977 CLAIMED from memory, not read | **stronger** (CLAIMED -> theorem; cited but unread) |
| 397 | H2: "proved (Theorem thm:main)" | THEOREM_S l.1, §8: "Theorem B′ (one model family, not independently reviewed)" | **stronger** (qualifier dropped) |
| 395, 405 | H0 "proved"; RP of periodic Wilson states from [OS78] | THEOREM_S l.40, 121: Osterwalder–Seiler CLAIMED (snippets only); proof was THEOREM_B Lemma 1, 1′ | **stronger** (CLAIMED citation used as a known result) |
| 15, 18 | "‖T_β‖ ≤ 1" stated without proof (needed for m ∈ [0,∞]) | not in sources | **stronger** (added claim) |
| 52-55 | (C) for any c ∈ (0,1) (source c = 1/2); R′ (R1)-(R5) | Theorem R′ source (A1_REDUCTION.md) not among my files, so only the c-generalisation can be seen | **stronger** (more general; unverifiable against source) |
| 108-118 | Observation red:twomass (C fails for two decoupled fields) | no source in my files | new claim; not comparable. I rechecked the inequality, it is correct |
| 241 | P = 4k+2 (Taylor lemma) | THEOREM_S step 2: P = 4k+1 | number differs (not stronger or weaker; tex gives an extra min(1,r) factor) |
| 157 | "take D ≥ 1" | not in source | harmless w.l.o.g. (increasing D weakens H3(b)) |

Weaker (tex more cautious than source):

| Line | Statement | Source | Direction |
|---|---|---|---|
| 310-313, 325 | gap lemma \|B(s)\| ≤ e^{-s}F_f^{1/2}F_g^{1/2}, \|F(s)\| ≤ e^{-s}F(0) | step 8: monotone F(t+s) ≤ e^{-s}F(t) | **weaker** (CHALLENGE_S repair (a); statement of Theorem S unchanged) |
| 262 | σ_k ≤ 7αe^Γ (k!)^{b+1} | step 2: σ_k ≤ α′(k!)^{b+ε} | **weaker** exponent |
| 360, 362, 384 | free field is an "analogue", numbers "not proofs", H0/H3(b)/H4 qualified | THEOREM_S §6 "holds", "Theorem S is not mis-stated" | **weaker** (matches CHALLENGE_S item 12, 15) |
| 177, 183 | E4 formula "written by us"; OS §4 description "not read" | step 7 tags | weaker/honest |
| 405 | (C) open for SU(2); omission of (E2) asymptotic-freedom text | THEOREM_S §2 | weaker (omission) |

Checked and equal: Theorem S hypotheses H0, H1=(A), H2=(B), H3, H4; conclusions 1-4; E0′-E4; table statuses of H1, H3, H4 (open) and every free-field number in the table (match THEOREM_S §6 and CHALLENGE_S item 10, 14). I also reread the constants in l.241-265 (A_k, I_k, Γ, 7α bound): they are correct.

## Q2. Lemma red:dense
(i) Kronecker: follows (ϑ/π irrational => ϑ/2π irrational; positive multiples are dense mod 2π; K closed). (ii) conjugation: follows (σ L12 σ^T = L_μν; such a permutation exists for each pair; tex indices run 0..3 so "e1,e2" are the 2nd and 3rd axes). (iii) span + inverse function theorem: follows (differential of the product of exponentials at 0 is Σφ_p L_p, an isomorphism onto so(4), dim 6). (iv) connectedness: follows (open subgroup is closed; SO(4) connected). (v) reflection: follows (diag(-1,1,1,1) ∈ W4, det -1). No gap found.

Numerical program `q2b.py` (output `out_q2b.txt`): (a) rank 6 met; (b) 6 of 6 planes err 0.0 (< 1e-12) met; (c) W4 has 384 elements, 192 with det -1, met. Exit 0.

## Failed predicates
- `q2.py` (b): failed in 5 of 6 planes, err 0.84. **My own bug** (a vacuous `all(())` clause made the sigma search return W4[0]). Kept as `out_q2.run1_failed.txt`; `q2b.py` is the fix. Not a target defect.
- PCP check `grandchild-rerun` (K2): I expected exit 1, but diff exit 0 means identical. **My own expectation error**; the content is identical.
- Grandchild G1 (closure of {R12(n·1.0)} within 1e-3 of R12(0.5), n ≤ 10000): **failed**, best n = 9752, distance 3.6e-3. This is **my suggested bound being too tight, not a lemma defect** (I reproduced 3.597e-3 independently; with n ≤ 100000 the best is 2.06e-5 at n = 52352). The lemma needs the infinite set, not a bound.
- Tolerance sources: 1e-12 (task, float64 eps ≈ 1e-16 with O(1) entries); 1e-3 (task); Frobenius tol for rotation blocks ≈ √2·d.

## Counts (met, failed, measured only)
Mine (q2b): 3 met (a, b, c; b as 6 of 6 cases), 0 failed, 0 measured only. q2 run 1: 2 met, 1 failed (b, own bug). Grandchild: G2 met (group size 384, 0.5 rotation not in group), G1 failed, 0 measured only. "For all" check (b): hypothesis tested per case, 6 of 6 planes had a σ.

## Grandchild
Task id **T28** (label p3-cond-grandchild, parent T27), released by me (event 55). Control 2+2 = 4 correct. Question: Kronecker closure at φ = 0.5, n ≤ 10000, and θ = π/2 boundary. Outcome: G1 failed (3.6e-3 at n = 9752, see above), G2 met (384 = |W4|, finite). I reread gc.py and reran it: byte-identical (diff = SAME). Files in grandchild/.

## Rerun (from this directory; outputs open with mode "x", so move old ones first)
```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name q2b --expect-exit 0 -- python3 q2b.py
$P check --ws pcp --name gc-rerun --expect-exit 0 -- bash -c "python3 -I grandchild/gc.py | diff - grandchild/out.txt"
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

## Verify, last lines
- `$P verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl`: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
