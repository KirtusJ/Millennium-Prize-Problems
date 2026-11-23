import Mathlib

open Filter Topology

theorem twoSided_cluster (a m : ℕ → ℝ) (c C L : ℝ) (hc : 0 < c) (hcC : c ≤ C)
    (ha : ∀ n, 0 < a n) (hb : ∀ n, c * a n ≤ m n ∧ m n ≤ C * a n)
    (φ : ℕ → ℕ) (hφ : StrictMono φ)
    (hL : Tendsto (fun k => m (φ k) / a (φ k)) atTop (𝓝 L)) :
    c < L ∧ L ≤ C := by
  have h1 : ∀ n, c ≤ m n / a n := fun n => by
    rw [le_div_iff₀ (ha n)]; linarith [hb n]
  have h2 : ∀ n, m n / a n ≤ C := fun n => by
    rw [div_le_iff₀ (ha n)]; linarith [hb n]
  exact ⟨ge_of_tendsto' hL (fun k => h1 (φ k)), le_of_tendsto' hL (fun k => h2 (φ k))⟩

theorem twoSided_cluster_eventually (a m : ℕ → ℝ) (c C L : ℝ) (hc : 0 < c) (hcC : c ≤ C)
    (ha : ∀ n, 0 < a n) (hb : ∀ᶠ n in atTop, c * a n ≤ m n ∧ m n ≤ C * a n)
    (φ : ℕ → ℕ) (hφ : StrictMono φ)
    (hL : Tendsto (fun k => m (φ k) / a (φ k)) atTop (𝓝 L)) :
    c ≤ L ∧ L ≤ C := by
  have hb' : ∀ᶠ k in atTop, c * a (φ k) ≤ m (φ k) ∧ m (φ k) ≤ C * a (φ k) :=
    hφ.tendsto_atTop.eventually hb
  refine ⟨ge_of_tendsto hL ?_, le_of_tendsto hL ?_⟩
  · filter_upwards [hb'] with k hk
    rw [le_div_iff₀ (ha _)]; linarith [hk.1]
  · filter_upwards [hb'] with k hk
    rw [div_le_iff₀ (ha _)]; linarith [hk.2]

theorem twoSided_of_tendsto (a m : ℕ → ℝ) (M : ℝ) (ha : ∀ n, 0 < a n) (hM : 0 < M)
    (h : Tendsto (fun n => m n / a n) atTop (𝓝 M)) :
    ∀ᶠ n in atTop, (M / 2) * a n ≤ m n ∧ m n ≤ 2 * M * a n := by
  have hI : Set.Ioo (M / 2) (2 * M) ∈ 𝓝 M := Ioo_mem_nhds (by linarith) (by linarith)
  filter_upwards [h hI] with n hn
  obtain ⟨h1, h2⟩ := hn
  constructor
  · have := (lt_div_iff₀ (ha n)).1 h1; linarith
  · have := (div_lt_iff₀ (ha n)).1 h2; linarith

#print axioms twoSided_cluster
#print axioms twoSided_cluster_eventually
#print axioms twoSided_of_tendsto
