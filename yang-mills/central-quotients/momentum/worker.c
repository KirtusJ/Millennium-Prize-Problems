/* Native PCP proof producer. A task contains the depth, spatial dimension
   and number of incident faces on the selected link. */
#include <stddef.h>

static long syscall3(long number, long a, long b, long c) {
    long result;
    __asm__ volatile ("syscall" : "=a"(result)
                      : "a"(number), "D"(a), "S"(b), "d"(c)
                      : "rcx", "r11", "memory");
    return result;
}

_Noreturn static void stop(int status) {
    syscall3(60, status, 0, 0);
    __builtin_unreachable();
}

static void emit(const char *text) {
    size_t size = 0;
    while (text[size]) ++size;
    while (size) {
        long written = syscall3(1, 1, (long)text, size);
        if (written <= 0 || (size_t)written > size) stop(3);
        text += written;
        size -= written;
    }
}

static void number(unsigned n) {
    char text[12];
    unsigned pos = sizeof text - 1;
    text[pos] = 0;
    do { text[--pos] = '0' + n % 10; n /= 10; } while (n);
    emit(text + pos);
}

static void request(unsigned depth, unsigned a, unsigned b) {
    emit("NEXT "); number(depth); emit(" "); number(a); emit(" "); number(b); emit("\n");
}



static unsigned shift(unsigned n, unsigned site, unsigned axis) {
    unsigned stride = axis == 0 ? 1 : (axis == 1 ? n : n*n);
    unsigned digit = (site/stride)%n;
    return site - stride*digit + stride*((digit+1)%n);
}

static void boundary(unsigned n, unsigned face, unsigned edge[4]) {
    unsigned site = face/3, i = (face%3+1)%3, j = (face%3+2)%3;
    edge[0] = 3*site+i;
    edge[1] = 3*shift(n,site,i)+j;
    edge[2] = 3*shift(n,site,j)+i;
    edge[3] = 3*site+j;
}

static unsigned private_count(unsigned n) {
    unsigned other[4], count = 0;
    for (unsigned p=0; p<3*n*n*n; ++p) {
        unsigned edges[4]; boundary(n,p,edges);
        for (unsigned k=0; k<4; ++k) {
            if (edges[k] != 0) continue;
            unsigned opp = edges[(k+2)%4], found = 0;
            for (unsigned i=0; i<count; ++i) found |= (other[i] == opp);
            if (!found) {
                if (count == 4) stop(6);
                other[count++] = opp;
            }
        }
    }
    return count;
}

static unsigned neighbors(unsigned n, const unsigned char input[375],
                          unsigned char output[375]) {
    unsigned char touched[375];
    unsigned faces = 3*n*n*n, count = 0;
    if (n < 2 || n > 5) stop(6);
    for (unsigned i=0; i<faces; ++i) touched[i] = 0;
    for (unsigned p=0; p<faces; ++p) {
        if (!input[p]) continue;
        unsigned edges[4]; boundary(n,p,edges);
        for (unsigned k=0; k<4; ++k) touched[edges[k]] = 1;
    }
    for (unsigned p=0; p<faces; ++p) {
        unsigned edges[4]; boundary(n,p,edges);
        output[p] = 0;
        for (unsigned k=0; k<4; ++k) output[p] |= touched[edges[k]];
        count += output[p];
    }
    return count;
}

static void parent(void) {
    unsigned wide = private_count(3), short_box = private_count(2);
    emit("LEAN-BEGIN\n"
         "import Mathlib.MeasureTheory.Integral.Bochner.Set\n"
         "import Mathlib.Tactic.Linarith\n"
         "import Mathlib.Tactic.NormNum\n"
         "import Mathlib.Tactic.Positivity\n"
         "\n"
         "open MeasureTheory Set\n"
         "open scoped BigOperators\n"
         "\n"
         "namespace YangMills.Momentum\n"
         "\n"
         "/-- Squaring a bound on the extremal ground-state amplitudes gives the density bound. -/\n"
         "theorem densityComparison {lo hi r x normal : ℝ}\n"
         "    (hr : 0 ≤ r) (hx : lo ≤ x) (hu : hi ≤ r*lo)\n"
         "    (hh : 0 ≤ hi) (hn : normal ≤ hi^2) : normal ≤ r^2*x^2 := by\n"
         "  have h : hi ≤ r*x := hu.trans (mul_le_mul_of_nonneg_left hx hr)\n"
         "  have hsq := mul_self_le_mul_self hh h\n"
         "  nlinarith\n"
         "\n"
         "/-- Private Haar integrations remove cross terms if their means vanish. -/\n"
         "theorem privateIntegrals {ι α : Type*} [MeasurableSpace α] (μ : Measure α) (s : Finset ι)\n"
         "    (term : ι → ι → α → ℝ) (a : ι → ℝ) (j : ℝ)\n"
         "    (hi : ∀ i ∈ s, ∀ k ∈ s, Integrable (term i k) μ)\n"
         "    (diag : ∀ i ∈ s, ∫ x, term i i x ∂μ = j*a i)\n"
         "    (off : ∀ i ∈ s, ∀ k ∈ s, i ≠ k → ∫ x, term i k x ∂μ = 0) :\n"
         "    (∫ x, ∑ i ∈ s, ∑ k ∈ s, term i k x ∂μ) = j * ∑ i ∈ s, a i := by\n"
         "  classical\n"
         "  rw [integral_finset_sum s (fun i hi' => integrable_finset_sum _ (fun k hk => hi i hi' k hk)),\n"
         "      Finset.mul_sum]\n"
         "  apply Finset.sum_congr rfl\n"
         "  intro i hi'\n"
         "  rw [integral_finset_sum s (fun k hk => hi i hi' k hk)]\n"
         "  exact (Finset.sum_eq_single_of_mem i hi' (fun k hk hki => off i hi' k hk (Ne.symm hki))).trans (diag i hi')\n"
         "\n"
         "\n"
         "theorem haarFloor {α : Type*} [MeasurableSpace α] (μ : Measure α) (ρ f : α → ℝ)\n"
         "    (r : ℝ) (floor : ∀ᵐ x ∂μ, 1 ≤ r^2 * ρ x) (pos : ∀ᵐ x ∂μ, 0 ≤ f x)\n"
         "    (hf : Integrable f μ) (hp : Integrable (fun x => ρ x * f x) μ) :\n"
         "    (∫ x, f x ∂μ) ≤ r^2 * ∫ x, ρ x * f x ∂μ := by\n"
         "  rw [← integral_const_mul]\n"
         "  apply integral_mono_ae hf (hp.const_mul _)\n"
         "  filter_upwards [floor, pos] with x h hx\n"
         "  simpa only [one_mul, mul_assoc] using mul_le_mul_of_nonneg_right h hx\n"
         "\n"
         "/-- Sites are encoded as x+n*(y+n*z). An edge uses its direction, a face its normal. -/\n"
         "private def shiftSite (n site axis : ℕ) (forward : Bool) : ℕ :=\n"
         "  let stride := n^axis\n"
         "  let u := site / stride % n\n"
         "  site - u*stride + ((u + (if forward then 1 else n-1)) % n)*stride\n"
         "\n"
         "private def faceEdges (n face : ℕ) : List ℕ :=\n"
         "  let x := face / 3\n"
         "  let i := (face%3+1)%3\n"
         "  let j := (face%3+2)%3\n"
         "  [3*x+i, 3*shiftSite n x i true+j, 3*shiftSite n x j true+i, 3*x+j]\n"
         "\n"
         "private def edgeFaces (n edge : ℕ) : List ℕ :=\n"
         "  let x := edge / 3\n"
         "  let i := edge % 3\n"
         "  [1,2].flatMap fun k =>\n"
         "    let j := (i+k)%3\n"
         "    let normal := 3-i-j\n"
         "    [3*x+normal, 3*shiftSite n x j false+normal]\n"
         "\n"
         "private def nearFaces (n face : ℕ) : List ℕ :=\n"
         "  ((faceEdges n face).flatMap (edgeFaces n)).eraseDups\n"
         "\n"
         "def nearCounts (n : ℕ) : ℕ × ℕ :=\n"
         "  let first := nearFaces n 0\n"
         "  (first.length, (first.flatMap (nearFaces n)).eraseDups.length)\n"
         "\n"
         "def privateEdgeCount (n : ℕ) : ℕ :=\n"
         "  (((edgeFaces n 0).map fun face =>\n"
         "      let es := faceEdges n face\n"
         "      es[(es.idxOf 0 + 2) % 4]!).eraseDups).length\n"
         "\n"
         "theorem privateEdges : privateEdgeCount 3 = ");
    number(wide);
    emit(" ∧ privateEdgeCount 2 = ");
    number(short_box);
    emit(" := by decide +kernel\n"
         "\n"
         "LEAN-END\n");

    request(1,3,wide);
}

static void child(unsigned dimension, unsigned valence) {
    if (dimension != 3 || valence != private_count(dimension)) stop(5);
    const unsigned energies[4] = {0,1,4,8}, masses[4] = {100,6,3,1};
    unsigned first = 0, third = 0, window = 0;
    for (unsigned i=0; i<4; ++i) {
        unsigned e = energies[i], m = masses[i];
        first += e*m;
        third += e*e*e*m;
        if (e >= 1 && e <= 4) window += m;
    }
    emit("LEAN-BEGIN\n"
         "/-- A real spectral energy is dominated by the low, window and cubic terms. -/\n"
         "theorem cubicWindowPoint {e l R : ℝ} (he : 0 ≤ e) (hl : 0 ≤ l) (hR : 0 < R) :\n"
         "    R^2 * e ≤ R^2*l + R^3 * (Icc l R).indicator (fun _ => (1:ℝ)) e + e^3 := by\n"
         "  by_cases low : e < l\n"
         "  · rw [indicator_of_not_mem (show e ∉ Icc l R from fun h => (not_lt.mpr h.1) low)]\n"
         "    have t := mul_le_mul_of_nonneg_left (le_of_lt low) (sq_nonneg R)\n"
         "    nlinarith [pow_nonneg he 3]\n"
         "  by_cases upper : e ≤ R\n"
         "  · rw [indicator_of_mem (show e ∈ Icc l R from ⟨le_of_not_gt low,upper⟩)]\n"
         "    have t := mul_le_mul_of_nonneg_left upper (sq_nonneg R)\n"
         "    nlinarith [mul_nonneg (sq_nonneg R) hl, pow_nonneg he 3]\n"
         "  · rw [indicator_of_not_mem (show e ∉ Icc l R from fun h => upper h.2)]\n"
         "    have t := mul_nonneg (sub_nonneg.mpr (le_of_not_ge upper)) (by positivity : 0 ≤ e*(e+R))\n"
         "    nlinarith [mul_nonneg (sq_nonneg R) hl]\n"
         "\n"
         "/-- Window estimate for an actual finite Borel measure, allowing an atom at zero. -/\n"
         "theorem cubicWindowMeasure (μ : Measure ℝ) [IsFiniteMeasure μ] {l R : ℝ}\n"
         "    (hl : 0 ≤ l) (hR : 0 < R) (he : ∀ᵐ e ∂μ, 0 ≤ e)\n"
         "    (h1 : Integrable (fun e : ℝ => e) μ) (h3 : Integrable (fun e : ℝ => e^3) μ) :\n"
         "    R^2 * (∫ e, e ∂μ) ≤ R^2*l*μ.real univ + R^3*μ.real (Icc l R) + ∫ e, e^3 ∂μ := by\n"
         "  let band := (Icc l R).indicator (fun _ : ℝ => (1:ℝ))\n"
         "  have hb : Integrable band μ := (integrable_const 1).indicator measurableSet_Icc\n"
         "  have hv : (∫ e, band e ∂μ) = μ.real (Icc l R) := integral_indicator_one measurableSet_Icc\n"
         "  have h := integral_mono_ae (h1.const_mul (R^2))\n"
         "    (((integrable_const (R^2*l)).add (hb.const_mul (R^3))).add h3)\n"
         "    (he.mono fun e ho => cubicWindowPoint ho hl hR)\n"
         "  change (∫ x, R^2*x ∂μ) ≤ (∫ x, (R^2*l + R^3*band x) + x^3 ∂μ) at h\n"
         "  have hab : Integrable (fun x : ℝ => R^2*l + R^3*band x) μ :=\n"
         "    (integrable_const (R^2*l)).add (hb.const_mul (R^3))\n"
         "  rw [integral_add hab h3, integral_add (integrable_const (R^2*l)) (hb.const_mul (R^3)),\n"
         "      integral_const, integral_const_mul, integral_const_mul, hv] at h\n"
         "  simpa only [smul_eq_mul, mul_comm (μ.real univ)] using h\n"
         "\n"
         "theorem positiveWindow {a M l R mass window : ℝ} (hr : 0 < R)\n"
         "    (low : 4*l*mass ≤ a) (tail : 4*M ≤ a*R^2)\n"
         "    (control : R^2*a ≤ R^2*l*mass + R^3*window + M) :\n"
         "    a ≤ 2*R*window := by\n"
         "  have ht := mul_le_mul_of_nonneg_left low (sq_nonneg R)\n"
         "  by_contra! h\n"
         "  have contra := mul_lt_mul_of_pos_left h (sq_pos_of_pos hr)\n"
         "  nlinarith\n"
         "\n"
         "/-- Counts exceptional momenta through the trace of the static structure factor. -/\n"
         "theorem exceptionalCount {ι : Type*} (all bad : Finset ι) (sub : bad ⊆ all)\n"
         "    (mass : ι → ℝ) (h0 : ∀ k ∈ all, 0 ≤ mass k) {a l C : ℝ} (hl : 0 ≤ l)\n"
         "    (badMass : ∀ k ∈ bad, a ≤ 4*l*mass k)\n"
         "    (parseval : ∑ k ∈ all, mass k ≤ (all.card : ℝ)*C) :\n"
         "    (bad.card : ℝ)*a ≤ 4*l*((all.card : ℝ)*C) := by\n"
         "  have first := Finset.sum_le_sum badMass\n"
         "  have second := Finset.sum_le_sum_of_subset_of_nonneg sub (fun i hi _ => h0 i hi)\n"
         "  simpa only [Finset.sum_const, nsmul_eq_mul, ← Finset.mul_sum] using\n"
         "    first.trans (by rw [← Finset.mul_sum]; exact mul_le_mul_of_nonneg_left (second.trans parseval) (by positivity))\n"
         "\n"
         "\n"
         "private def spectralAtoms : List (ℕ × ℕ) := [(0,100), (1,6), (4,3), (8,1)]\n"
         "private def atomicMoment (n : ℕ) := (spectralAtoms.map fun (e,m) => m*e^n).sum\n"
         "private def atomicWindow := (spectralAtoms.map fun (e,m) => if 1 ≤ e ∧ e ≤ 4 then m else 0).sum\n"
         "\n"
         "theorem closedWindowFixture : (atomicMoment 1, atomicMoment 3, atomicWindow) = (");
    number(first);
    emit(",");
    number(third);
    emit(",");
    number(window);
    emit(") := by decide +kernel\n"
         "\n"
         "/-- Sum of squared derivatives for the adjoint gradient map q ↦ x Im(q). -/\n"
         "theorem adjointDifferentialFloor (x : ℝ) :\n"
         "    (3/4 : ℝ) ≤ 1-2*x^2+4*x^4 := by\n"
         "  nlinarith [sq_nonneg (2*x^2-1/2)]\n"
         "\n"
         "theorem shiftedResidual {k s : ℝ} (parts : 3/4 ≤ (4+4*k)*s) :\n"
         "    9 ≤ 256*(1+k)^2*s^2 := by\n"
         "  have h := mul_self_le_mul_self (by norm_num : (0:ℝ) ≤ 3/4) parts\n"
         "  nlinarith\n"
         "\n"
         "/-- D4's quadratic window majorant, including both endpoints. -/\n"
         "theorem quadraticWindowPoint {l R : ℝ} (ordered : l ≤ R) (e : ℝ) :\n"
         "    (e-l)*(R-e) ≤ (R-l)^2/4 * (Icc l R).indicator (fun _ => (1:ℝ)) e := by\n"
         "  by_cases h : e ∈ Icc l R\n"
         "  · rw [indicator_of_mem h]\n"
         "    nlinarith [sq_nonneg (e-(R+l)/2)]\n"
         "  · rw [indicator_of_not_mem h, mul_zero]\n"
         "    by_cases he : e < l\n"
         "    · exact mul_nonpos_of_nonpos_of_nonneg (by linarith) (by linarith)\n"
         "    · have hu : R < e := lt_of_not_ge (fun le => h ⟨le_of_not_gt he, le⟩)\n"
         "      exact mul_nonpos_of_nonneg_of_nonpos (by linarith) (by linarith)\n"
         "\n"
         "LEAN-END\n");

    request(2,dimension,valence);
}

static void grandchild(unsigned dimension, unsigned valence) {
    if (dimension != 3 || valence != private_count(dimension)) stop(5);
    static unsigned char seed[375], one[375], two[375];
    seed[0] = 1;
    unsigned small_one = neighbors(3,seed,one), small_two = neighbors(3,one,two);
    unsigned large_one = neighbors(5,seed,one), large_two = neighbors(5,one,two);
    emit("LEAN-BEGIN\n"
         "/-- A uniform row and column sum bounds the spatial moment form on coefficient norms. -/\n"
         "theorem finiteSchur {ι : Type*} (s : Finset ι) (w : ι → ι → ℝ) (x : ι → ℝ) (K : ℝ)\n"
         "    (nonnegative : ∀ i ∈ s, ∀ j ∈ s, 0 ≤ w i j)\n"
         "    (row : ∀ i ∈ s, ∑ j ∈ s, w i j ≤ K) (col : ∀ j ∈ s, ∑ i ∈ s, w i j ≤ K) :\n"
         "    (∑ i ∈ s, ∑ j ∈ s, w i j * (x i*x j)) ≤ K * ∑ i ∈ s, x i^2 := by\n"
         "  have diagonal (a : ι → ι → ℝ) (b : ∀ i ∈ s, ∑ j ∈ s, a i j ≤ K) :\n"
         "      (∑ i ∈ s, ∑ j ∈ s, a i j * x i^2) ≤ K * ∑ i ∈ s, x i^2 := by\n"
         "    rw [Finset.mul_sum]\n"
         "    apply Finset.sum_le_sum\n"
         "    intro i hi\n"
         "    rw [← Finset.sum_mul]\n"
         "    exact mul_le_mul_of_nonneg_right (b i hi) (sq_nonneg _)\n"
         "  have other : (∑ i ∈ s, ∑ j ∈ s, w i j * x j^2) ≤ K * ∑ i ∈ s, x i^2 := by\n"
         "    rw [Finset.sum_comm]\n"
         "    exact diagonal (fun j i => w i j) col\n"
         "  have both : (∑ i ∈ s, ∑ j ∈ s, 2*(w i j*(x i*x j))) ≤\n"
         "      ∑ i ∈ s, ∑ j ∈ s, (w i j*x i^2 + w i j*x j^2) := by\n"
         "    apply Finset.sum_le_sum\n"
         "    intro i hi\n"
         "    apply Finset.sum_le_sum\n"
         "    intro j hj\n"
         "    nlinarith [mul_nonneg (nonnegative i hi j hj) (sq_nonneg (x i-x j))]\n"
         "  simp only [← Finset.mul_sum, Finset.sum_add_distrib] at both\n"
         "  linarith [diagonal w row]\n"
         "\n"
         "set_option maxRecDepth 25000 in\n"
         "set_option maxHeartbeats 0 in\n"
         "theorem periodicSupport : nearCounts 3 = (");
    number(small_one);
    emit(",");
    number(small_two);
    emit(") ∧ nearCounts 5 = (");
    number(large_one);
    emit(",");
    number(large_two);
    emit(") := by decide +kernel\n"
         "\n"
         "/-- A bounded first/third moment permits an exceptional Fourier mode with divergent mass. -/\n"
         "theorem softAtom (x : ℝ) (hx : 1 ≤ x) : x*(1/x) = 1 ∧ x*(1/x)^3 ≤ 1 := by\n"
         "  have pos : 0 < x := by linarith\n"
         "  have h : x*(1/x) = 1 := by field_simp\n"
         "  have small : 1/x ≤ 1 := (div_le_one pos).mpr hx\n"
         "  have u : 0 ≤ 1/x := by positivity\n"
         "  constructor\n"
         "  · exact h\n"
         "  · calc x*(1/x)^3 = (x*(1/x)) * ((1/x)*(1/x)) := by ring\n"
         "         _ ≤ 1 := by rw [h, one_mul]; exact (mul_le_mul_of_nonneg_right small u).trans (by simpa using small)\n"
         "\n"
         "/-- Recover a positive aligned vacuum vector distance from the rank-one projection distance. -/\n"
         "theorem alignedVacuum {z v p : ℝ} (h0 : 0 ≤ z) (h1 : z ≤ 1)\n"
         "    (hv : v^2 = 2*(1-z)) (hp : p^2 = 1-z^2) : v^2 ≤ 2*p^2 := by\n"
         "  nlinarith [mul_nonneg h0 (sub_nonneg.mpr h1)]\n"
         "\n"
         "private theorem rmsProduct {ι : Type*} (s : Finset ι) (f g : ι → ℝ) {A B : ℝ}\n"
         "    (hA : 0 ≤ A) (hB : 0 ≤ B)\n"
         "    (hf : ∑ i ∈ s, f i^2 ≤ A^2) (hg : ∑ i ∈ s, g i^2 ≤ B^2) :\n"
         "    ∑ i ∈ s, f i*g i ≤ A*B := by\n"
         "  have hfa := (Real.sqrt_le_sqrt hf).trans_eq (Real.sqrt_sq hA)\n"
         "  have hgb := (Real.sqrt_le_sqrt hg).trans_eq (Real.sqrt_sq hB)\n"
         "  exact (Real.sum_mul_le_sqrt_mul_sqrt s f g).trans\n"
         "    (mul_le_mul hfa hgb (Real.sqrt_nonneg _) hA)\n"
         "\n"
         "/-- Sum pointwise trace-norm errors using the squared norms returned by Parseval. -/\n"
         "theorem summedGramError {ι : Type*} (s : Finset ι) (err left right delta : ι → ℝ)\n"
         "    {A D h : ℝ} (hA : 0 ≤ A) (hD : 0 ≤ D) (hh : 0 ≤ h)\n"
         "    (hl : ∑ i ∈ s, left i^2 ≤ A^2) (hr : ∑ i ∈ s, right i^2 ≤ A^2)\n"
         "    (hd : ∑ i ∈ s, delta i^2 ≤ D^2)\n"
         "    (terms : ∀ i ∈ s, err i ≤ delta i*left i + delta i*right i + h*right i^2) :\n"
         "    ∑ i ∈ s, err i ≤ 2*D*A + h*A^2 := by\n"
         "  have hsum := Finset.sum_le_sum terms\n"
         "  simp only [Finset.sum_add_distrib, ← Finset.mul_sum] at hsum\n"
         "  linarith [rmsProduct s delta left hD hA hd hl,\n"
         "    rmsProduct s delta right hD hA hd hr, mul_le_mul_of_nonneg_left hr hh]\n"
         "\n"
         "end YangMills.Momentum\n"
         "\n"
         "open YangMills.Momentum\n"
         "#print axioms densityComparison\n"
         "#print axioms privateIntegrals\n"
         "#print axioms cubicWindowPoint\n"
         "#print axioms cubicWindowMeasure\n"
         "#print axioms positiveWindow\n"
         "#print axioms exceptionalCount\n"
         "#print axioms periodicSupport\n"
         "#print axioms softAtom\n"
         "#print axioms haarFloor\n"
         "#print axioms closedWindowFixture\n"
         "#print axioms privateEdges\n"
         "#print axioms finiteSchur\n"
         "#print axioms adjointDifferentialFloor\n"
         "#print axioms shiftedResidual\n"
         "#print axioms quadraticWindowPoint\n"
         "#print axioms alignedVacuum\n"
         "#print axioms summedGramError\n"
         "LEAN-END\n");
}

__attribute__((used,noreturn)) static void run(void) {
    static unsigned char input[4];
    long fd = syscall3(2, (long)"task.bin", 0, 0);
    if (fd < 0 || syscall3(0, fd, (long)input, sizeof input) != 3 ||
        syscall3(0, fd, (long)(input+3), 1) != 0 || syscall3(3, fd, 0, 0) != 0) stop(2);
    if (!input[0] && !input[1] && !input[2]) parent();
    else if (input[0] == 1) child(input[1],input[2]);
    else if (input[0] == 2) grandchild(input[1],input[2]);
    else stop(2);
    stop(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
