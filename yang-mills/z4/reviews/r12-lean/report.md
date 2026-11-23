# report r12-lean (formalizer), Director Z4

Control: control.txt = 0.272341 (-ln tanh 1). /home/user/z4-lean/READY exists, so Lean was ready.
Compile: `lake env lean R12Analytic.lean` gave **exit code 0** (register K2). The file contains no `sorry` token outside the docstring line 6.

## Verdict table

| item | verdict | evidence |
|---|---|---|
| F1 | STANDS | `R12.F1 (y) (hy : 0 ≤ y) : y - y^3/6 ≤ sin y`, proved in Lean. Axioms: [propext, Classical.choice, Quot.sound] |
| F2 | STANDS | `R12.F2 (y) : \|sin y - y\| ≤ \|y\|^3/6`, proved for all real y. Axioms: [propext, Classical.choice, Quot.sound] |
| F3 | STANDS | `R12.F3 (b k) (hb : 0 < b) : \|(2/b) sin(k b/2) - k\| ≤ b^2 \|k\|^3/24`. Axioms: [propext, Classical.choice, Quot.sound] |
| F3 mutation (24→25) | STANDS (the constant is sharp against 25) | `R12.F3_const_25_false : ¬ ∀ b k, 0<b → … ≤ b^2\|k\|^3/25`, proved in Lean with the witness k=1, b=1/5 and Mathlib `Real.sin_bound`. Axioms: [propext, Classical.choice, Quot.sound]. A float check agrees: lhs 1.66583e-3 > 1.6e-3 (K4) |
| F4 (a: Jordan) | STANDS | `R12.F4a (y) (hy : \|y\| ≤ π/2) : 2/π*\|y\| ≤ \|sin y\| ∧ \|sin y\| ≤ \|y\|`. Axioms: [propext, Classical.choice, Quot.sound] |
| F4 (b: lattice) | STANDS | `R12.F4b (b k) (hb : 0<b) (hkb : \|k*b\| ≤ π) : 2/π*\|k\| ≤ \|(2/b) sin(k b/2)\| ∧ … ≤ \|k\|`. Axioms: [propext, Classical.choice, Quot.sound] |
| F5 | STANDS (the full Gaussian form; the fallback was not needed) | `R12.F5 (c) (hc : 0<c) (M : ℕ) : ∑ m ∈ Finset.Icc 1 M, exp(-c*m^2) ≤ √(π/c)/2`. Proof: `AntitoneOn.sum_le_integral`, then `setIntegral_mono_set`, then `integral_gaussian_Ioi`. Axioms: [propext, Classical.choice, Quot.sound] |
| F6 | STANDS | `R12.F6 (x c) (j : ℕ) (hj : 1 ≤ j) (hc : 0<c) : x^(2j) * exp(-c x^2) ≤ (j/(exp 1 * c))^j`. Axioms: [propext, Classical.choice, Quot.sound] |
| F7 (a: projector) | STANDS | `R12.F7a (p q) (h : 0 < p^2+q^2) : 0 ≤ p^2/(p^2+q^2) ∧ p^2/(p^2+q^2) ≤ 1`. Axioms: [propext, Classical.choice, Quot.sound] |
| F7 (b: square difference) | STANDS | `R12.F7b (A a a') (ha : a ∈ Icc 0 A) (ha' : a' ∈ Icc 0 A) : \|a^2-a'^2\| ≤ 2*A*\|a-a'\|`. Axioms: [propext, Classical.choice, Quot.sound] |

The `#print axioms` output for every theorem, verbatim:
```
'R12.F1' depends on axioms: [propext, Classical.choice, Quot.sound]
'R12.F2' depends on axioms: [propext, Classical.choice, Quot.sound]
'R12.F3' depends on axioms: [propext, Classical.choice, Quot.sound]
'R12.F4a' depends on axioms: [propext, Classical.choice, Quot.sound]
'R12.F4b' depends on axioms: [propext, Classical.choice, Quot.sound]
'R12.F5' depends on axioms: [propext, Classical.choice, Quot.sound]
'R12.F6' depends on axioms: [propext, Classical.choice, Quot.sound]
'R12.F7a' depends on axioms: [propext, Classical.choice, Quot.sound]
'R12.F7b' depends on axioms: [propext, Classical.choice, Quot.sound]
'R12.F3_const_25_false' depends on axioms: [propext, Classical.choice, Quot.sound]
```
There is also an auxiliary lemma, `sin_sub_cubic_monotone`. It says y ↦ sin y − y + y³/6 is monotone on all of ℝ, using `one_sub_sq_div_two_le_cos` for all x. A second auxiliary, `F1_neg`, says sin y ≤ y − y³/6 for y ≤ 0.

Lemmas not proved: none.

## Hypotheses: where each is stated, and which were added or could be dropped
- **F1:** needs y ≥ 0. It is used, since for y<0 the inequality reverses (`F1_neg`).
- **F2:** needs no hypothesis.
- **F3:** needs b > 0. It is used for |2/b| = 2/b and |kb/2| = |k| b/2.
- **F4a:** needs |y| ≤ π/2, which only the lower bound uses. The upper bound |sin y| ≤ |y| holds for all y.
- **F4b:** needs b > 0 and |k b| ≤ π. Again only the lower bound needs |kb| ≤ π.
- **F5:** needs c > 0 and M : ℕ, with no other hypothesis. For M = 0 the sum is empty.
- **F6:** needs j ≥ 1 and c > 0.
  - The hypothesis x ≥ 0 was **dropped**: the theorem holds for all real x, because x^(2j) = (x²)^j.
  - j ≥ 1 is used, since the proof divides by j. The case j = 0 (1·exp(-cx²) ≤ 1) is also true but I did not prove it.
- **F7a:** needs p² + q² > 0.
- **F7b:** needs a, a' ∈ [0, A]. The proof only uses 0 ≤ a + a' ≤ 2A.
- **Formulation choices:**
  - In the Lean statements e is `Real.exp 1`.
  - The sum ∑_{m=1}^{M} is written as `Finset.Icc 1 M`.
  - In F6, (j/(e c))^j is written as `(j/(exp 1 * c))^j`.
- **Hypotheses added:** none.

## Failed predicates
- **First compile, exit 1.** There were two errors: the F5 index-shift rewrite, and two `field_simp` closures in F6. Both were defects of my own proof script, not of the statements. I fixed them, and the second compile gave exit 0.
- **K3 `no-sorry` (expected grep exit 1, got 0).** The only match is line 6, which is my own docstring text "No `sorry` in this file". The predicate was badly designed (my expectation); the target is fine.
- **K7 (expected exit 1, got 0).** My own error: I excluded line 7 instead of line 6.
  - K8, which excludes line 6, met its expectation (exit 1, no other match).
  - The binding evidence is still the axioms output: there is no `sorryAx` anywhere.
- **The brief's suggested mutation (edit a copy with 25 and see the proof fail):** I did not do it as a file edit. I replaced it with the stronger Lean theorem `F3_const_25_false`, which proves that the 25 version is false, so no proof of it can exist.

Register counts (K1–K8): 6 met, 2 failed (K3, K7, both my own predicates), 0 measured only.

## Not checked
- Whether 24 is the optimal constant: I only showed it cannot be 25. It is the limit k b → 0, but that is not formalised.
- F6 for j = 0.
- I did not use the child's float tolerance analysis for anything except corroboration. In F2 and F3 the child's float test is weak where cancellation dominates (relative slack around −1, absorbed by its 8-ulp tolerance). The Lean proofs are the evidence.
- Whether these lemmas are the ones the downstream theta-function and Yang-Mills arguments actually need, with matching hypotheses. Only the statements as given in the brief were formalised.

## Delegated questions and outcomes
- **Child** (sonnet, run as child-run1 = K1, exit 0). Question: a Python check of F1–F6 on 10^5 random points each, with seed 20240607.
  - Control: 0.008138, which is correct. I graded it before reading anything else.
  - It reported 0 fails for all items. Points meeting the hypothesis per case: F1 50188, F2 100000, F3 90038, F4a 76329, F4b 89604, F5 98020, F6 98080.
  - I reread check.py (predicates in its docstring, mode "x", fixed seed) and reran it as K5. The output was identical (first 400 characters of every line).
- **Grandchild** (started by the child). Question: a 50-digit decimal recomputation of F6 at the equality point x² = j/c and at ±1e-3 around it.
  - Control 0.008138 was correct.
  - Maximum relative difference at the equality point: 9.4e-48. All 42 perturbed cases were strict, with minimum slack 5.0e-7.
  - I reran it in gc_rerun/ (K6) and got identical results.txt.
  - This confirms that the F6 constant is attained, so it is sharp.

## Rerun commands
```
cd /home/user/z4-workers/r12-lean
python3 -c "import math;print('%.6f'%(-math.log(math.tanh(1))))"
cd /home/user/z4-lean && PATH=$HOME/.elan/bin:$PATH lake env lean /home/user/z4-workers/r12-lean/R12Analytic.lean; echo $?
cd /home/user/z4-workers/r12-lean
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name lean-compile --expect-exit 0 --cwd /home/user/z4-lean -- bash -c 'PATH=$HOME/.elan/bin:$PATH lake env lean /home/user/z4-workers/r12-lean/R12Analytic.lean'
$P check --ws pcp --name no-sorry-outside-line6 --expect-exit 1 -- bash -c "grep -n sorry R12Analytic.lean | grep -v '^6:'"
$P check --ws pcp --name witness --expect-exit 0 -- python3 witness.py witness_results2.txt
$P check --ws pcp --name child-rerun --expect-exit 0 --cwd child -- python3 check.py results_parent_rerun2.txt
mkdir -p gc_rerun2 && cp child/grandchild/check_f6.py gc_rerun2/ && $P check --ws pcp --name grandchild-rerun --expect-exit 0 --cwd gc_rerun2 -- python3 check_f6.py
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
Last line of `$P verify --ws pcp`: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
Last line of Rust `pcpos verify`: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."

The director and I share a model family, so this is not independent review. The Lean kernel check is the independent part.
