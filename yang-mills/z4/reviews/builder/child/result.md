# Result

## Control
1/2 + 1/3 + 1/6 = 1 (child/control.txt contains `1`)

## Register
`pcp_os.py init pcp --principal principal --principal-name "Kirtus Justus"` -> workspace created, `method: not pinned` (expected), exit 0.

## Theorems (child/TwoSided.lean, `import Mathlib`, `open Filter Topology`)

(A)
```lean
theorem twoSided_cluster (a m : ℕ → ℝ) (c C L : ℝ) (hc : 0 < c) (hcC : c ≤ C)
    (ha : ∀ n, 0 < a n) (hb : ∀ n, c * a n ≤ m n ∧ m n ≤ C * a n)
    (φ : ℕ → ℕ) (hφ : StrictMono φ)
    (hL : Tendsto (fun k => m (φ k) / a (φ k)) atTop (𝓝 L)) :
    c ≤ L ∧ L ≤ C
```
(A')
```lean
theorem twoSided_cluster_eventually (a m : ℕ → ℝ) (c C L : ℝ) (hc : 0 < c) (hcC : c ≤ C)
    (ha : ∀ n, 0 < a n) (hb : ∀ᶠ n in atTop, c * a n ≤ m n ∧ m n ≤ C * a n)
    (φ : ℕ → ℕ) (hφ : StrictMono φ)
    (hL : Tendsto (fun k => m (φ k) / a (φ k)) atTop (𝓝 L)) :
    c ≤ L ∧ L ≤ C
```
(B)
```lean
theorem twoSided_of_tendsto (a m : ℕ → ℝ) (M : ℝ) (ha : ∀ n, 0 < a n) (hM : 0 < M)
    (h : Tendsto (fun n => m n / a n) atTop (𝓝 M)) :
    ∀ᶠ n in atTop, (M / 2) * a n ≤ m n ∧ m n ≤ 2 * M * a n
```

## Compile
`cd C:/Users/donke/z4-lean && PATH=$HOME/.elan/bin:$PATH lake env lean .../child/TwoSided.lean` -> exit 0.
Only warnings: unused variables (hc, hcC in A and A'; hφ in A — these hypotheses are not needed for the proof).

Axioms output:
```
'twoSided_cluster' depends on axioms: [propext, Classical.choice, Quot.sound]
'twoSided_cluster_eventually' depends on axioms: [propext, Classical.choice, Quot.sound]
'twoSided_of_tendsto' depends on axioms: [propext, Classical.choice, Quot.sound]
```

## Register check / verify
The `check ... -- bash -c "..."` form worked as given:
`check K1: exit 0 (expected 0) in 64557 ms | output 3ba2980f1461 | event 2 head 7d924e975829`

verify last line:
`result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
(register: 3 events, chain intact)

## Failures
None.
