/* A bounded proof-template worker for the PCP OS user ABI. ROLE selects a subgoal. */
#ifndef ROLE
#error ROLE required
#endif
__attribute__((used)) static volatile int worker_role = ROLE + 1;
static long sys(long n,long a,long b,long c) {
    long result;
    __asm__ volatile("syscall":"=a"(result):"a"(n),"D"(a),"S"(b),"d"(c):"rcx","r11","memory");
    return result;
}
static void emit(const char *s) {
    unsigned len=0;
    while(s[len]) ++len;
    while(len){
        long k=sys(1,1,(long)s,len);
        if(k<=0 || (unsigned long)k>len){sys(60,1,0,0);__builtin_unreachable();}
        len-=(unsigned)k;s+=k;
    }
}
__attribute__((used,noreturn)) static void run(void) {
#if ROLE == 0
    emit("A4 CHILD spectrum\n");
    emit("A4 LEAN import Mathlib.MeasureTheory.Integral.Bochner.Set\n");
    emit("A4 LEAN import Mathlib.Analysis.SpecialFunctions.Exp\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN open MeasureTheory\n");
    emit("A4 LEAN open scoped BigOperators\n");
    emit("A4 LEAN namespace YangMills.SmearedMoments\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Convert the integrated divergence estimate to a shift-independent spread. -/\n");
    emit("A4 LEAN theorem vectorSpread {k y : ℝ} (score : 2 ≤ (3+4*k)*y) :\n");
    emit("A4 LEAN     4 ≤ 25*(1+k^2)*y^2 := by\n");
    emit("A4 LEAN   have h := mul_self_le_mul_self (by norm_num : (0:ℝ) ≤ 2) score\n");
    emit("A4 LEAN   nlinarith only [h,mul_nonneg (sq_nonneg (4-3*k)) (sq_nonneg y)]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Sum the four private-link estimates for one electric link. -/\n");
    emit("A4 LEAN theorem edgeBound (u v w z e τ : ℝ)\n");
    emit("A4 LEAN     (hu : τ*u^2 ≤ e) (hv : τ*v^2 ≤ e)\n");
    emit("A4 LEAN     (hw : τ*w^2 ≤ e) (hz : τ*z^2 ≤ e) :\n");
    emit("A4 LEAN     τ*(u^2+v^2+w^2+z^2) ≤ 4*e := by\n");
    emit("A4 LEAN   linarith only [hu,hv,hw,hz]\n");
    emit("A4 LEAN \n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN /-- Symmetric nonnegative majorants with bounded row sums act boundedly on ℓ². -/\n");
    emit("A4 LEAN theorem rowBound {ι : Type*} [Fintype ι] (w : ι → ι → ℝ) (c : ι → ℝ) (D : ℝ)\n");
    emit("A4 LEAN     (hw : ∀ i j, 0 ≤ w i j) (sym : ∀ i j, w j i = w i j)\n");
    emit("A4 LEAN     (rows : ∀ i, ∑ j, w i j ≤ D) :\n");
    emit("A4 LEAN     ∑ i, ∑ j, w i j*c i*c j ≤ D * ∑ i, (c i)^2 := by\n");
    emit("A4 LEAN   have single (i j : ι) : w i j*c i*c j ≤\n");
    emit("A4 LEAN       (w i j*(c i)^2 + w i j*(c j)^2)/2 := by\n");
    emit("A4 LEAN     nlinarith only [mul_nonneg (hw i j) (sq_nonneg (c i-c j))]\n");
    emit("A4 LEAN   have hs := Finset.sum_le_sum (s := Finset.univ) (fun i _ =>\n");
    emit("A4 LEAN     Finset.sum_le_sum (s := Finset.univ) (fun j _ => single i j))\n");
    emit("A4 LEAN   have swap : (∑ i, ∑ j, w i j*(c j)^2) = ∑ i, ∑ j, w i j*(c i)^2 := by\n");
    emit("A4 LEAN     rw [Finset.sum_comm]\n");
    emit("A4 LEAN     exact Finset.sum_congr rfl (fun i _ => Finset.sum_congr rfl (fun j _ => by rw [sym j i]))\n");
    emit("A4 LEAN   have side : (∑ i, ∑ j, w i j*(c i)^2) ≤ D*∑ i,(c i)^2 := by\n");
    emit("A4 LEAN     rw [Finset.mul_sum]\n");
    emit("A4 LEAN     apply Finset.sum_le_sum\n");
    emit("A4 LEAN     intro i _\n");
    emit("A4 LEAN     rw [← Finset.sum_mul]\n");
    emit("A4 LEAN     exact mul_le_mul_of_nonneg_right (rows i) (sq_nonneg _)\n");
    emit("A4 LEAN   simp only [← Finset.sum_div, Finset.sum_add_distrib] at hs\n");
    emit("A4 LEAN   linarith only [hs,swap,side]\n");
    emit("A4 LEAN \n");
#elif ROLE == 2
    emit("A4 LEAN theorem secondCeiling {m₂ m₁ m₃ S B κ n : ℝ}\n");
    emit("A4 LEAN     (hn : 0 ≤ n) (hk : 0 ≤ κ) (hs : 0 ≤ S)\n");
    emit("A4 LEAN     (h₃ : 0 ≤ m₃) (loss : S*(1+B) ≤ 18)\n");
    emit("A4 LEAN     (first : m₁ ≤ 16*κ*S*n) (third : m₃ ≤ 145*103681537*κ^3*(1+B)*n)\n");
    emit("A4 LEAN     (interp : m₂^2 ≤ m₁*m₃) : m₂ ≤ 2100000*κ^2*n := by\n");
    emit("A4 LEAN   have hp : 0 ≤ 16*κ*S*n := by positivity\n");
    emit("A4 LEAN   have ha := mul_le_mul_of_nonneg_right first h₃\n");
    emit("A4 LEAN   have hb := mul_le_mul_of_nonneg_left third hp\n");
    emit("A4 LEAN   have hx := mul_le_mul_of_nonneg_right loss\n");
    emit("A4 LEAN     (mul_nonneg (pow_nonneg hk 4) (sq_nonneg n))\n");
    emit("A4 LEAN   by_contra! bad\n");
    emit("A4 LEAN   have upper : 0 ≤ 2100000*κ^2*n := by positivity\n");
    emit("A4 LEAN   have hc := mul_self_lt_mul_self upper bad\n");
    emit("A4 LEAN   nlinarith only [ha,hb,hx,interp,hc,mul_nonneg (pow_nonneg hk 4) (sq_nonneg n)]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- The moments of a finite measure bound its mass through a genuine integral. -/\n");
    emit("A4 LEAN theorem massInterpolation (μ : Measure ℝ) [IsFiniteMeasure μ] (a v d : ℝ)\n");
    emit("A4 LEAN     (hv : v=μ.real Set.univ) (ha : a=∫ x : ℝ, x ∂μ)\n");
    emit("A4 LEAN     (hd : d=∫ x : ℝ, x^2 ∂μ) (hp : 0 < v)\n");
    emit("A4 LEAN     (h1 : Integrable (fun x : ℝ => x) μ) (h2 : Integrable (fun x : ℝ => x^2) μ) :\n");
    emit("A4 LEAN     a^2 ≤ v*d := by\n");
    emit("A4 LEAN   have H := integral_nonneg (μ := μ) (fun x : ℝ => sq_nonneg (v*x-a))\n");
    emit("A4 LEAN   have eq (x : ℝ) : (v*x-a)^2=v^2*x^2-(2*v*a)*x+a^2 := by ring\n");
    emit("A4 LEAN   simp only [eq] at H\n");
    emit("A4 LEAN   have step := integral_add ((h2.const_mul (v^2)).sub (h1.const_mul (2*v*a)))\n");
    emit("A4 LEAN     (integrable_const (μ := μ) (a^2))\n");
    emit("A4 LEAN   simp only [Pi.sub_apply] at step\n");
    emit("A4 LEAN   rw [step,integral_sub (h2.const_mul _) (h1.const_mul _),integral_const_mul,\n");
    emit("A4 LEAN     integral_const_mul,integral_const,smul_eq_mul,← hv,← ha,← hd] at H\n");
    emit("A4 LEAN   exact le_of_mul_le_mul_left (a := v) (by nlinarith only [H]) hp\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem varianceAndRate {a d n m₁ m₂ v : ℝ} (hn : 0 < n) (ha : 0 < a) (hd : 0 < d)\n");
    emit("A4 LEAN     (hv : 0 ≤ v) (first : a*n ≤ m₁) (second : m₂ ≤ d*n)\n");
    emit("A4 LEAN     (interp : m₁^2 ≤ v*m₂) :\n");
    emit("A4 LEAN     a^2*n/d ≤ v ∧ m₁ ≤ (d/a)*v := by\n");
    emit("A4 LEAN   have h := mul_le_mul_of_nonneg_left second hv\n");
    emit("A4 LEAN   have mx := mul_self_le_mul_self (mul_nonneg ha.le hn.le) first\n");
    emit("A4 LEAN   have mpos := (mul_pos ha hn).trans_le first\n");
    emit("A4 LEAN   have scale : a*m₁*n ≤ v*d*n := by\n");
    emit("A4 LEAN     nlinarith only [mul_le_mul_of_nonneg_right first mpos.le,interp,h]\n");
    emit("A4 LEAN   constructor\n");
    emit("A4 LEAN   · apply (div_le_iff₀ hd).mpr\n");
    emit("A4 LEAN     apply le_of_mul_le_mul_right (a := n) _ hn\n");
    emit("A4 LEAN     nlinarith only [mx,interp,h]\n");
    emit("A4 LEAN   · have g := le_of_mul_le_mul_right scale hn\n");
    emit("A4 LEAN     rw [div_mul_eq_mul_div,(le_div_iff₀ ha)]\n");
    emit("A4 LEAN     linarith only [g]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Low energies of the energy-weighted law are bounded by the unweighted mass. -/\n");
    emit("A4 LEAN theorem lowFirst (μ : Measure ℝ) [IsFiniteMeasure μ] {E : ℝ} (hE : 0 ≤ E)\n");
    emit("A4 LEAN     (h1 : Integrable (fun x : ℝ => x) μ) :\n");
    emit("A4 LEAN     (∫ x in Set.Icc 0 E, x ∂μ) ≤ E*μ.real Set.univ := by\n");
    emit("A4 LEAN   let s := Set.Icc 0 E\n");
    emit("A4 LEAN   have h := integral_mono_ae (h1.restrict (s := s)) (integrable_const E)\n");
    emit("A4 LEAN     ((ae_restrict_mem (μ := μ) (s := s) measurableSet_Icc).mono (fun x hx => hx.2))\n");
    emit("A4 LEAN   rw [integral_const, Measure.real, Measure.restrict_apply_univ, smul_eq_mul] at h\n");
    emit("A4 LEAN   have m := measureReal_mono (μ := μ) (Set.subset_univ s)\n");
    emit("A4 LEAN   exact h.trans (by change (μ.real s)*E ≤ E*μ.real Set.univ\n");
    emit("A4 LEAN                     linarith only [mul_le_mul_of_nonneg_right m hE])\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem weightedEscape {ell m n k B E u Z : ℝ} (he : 0 ≤ E) (hu : 0 ≤ u)\n");
    emit("A4 LEAN     (hB : 0 ≤ B) (hZ : 0 ≤ Z) (hn : 0 < n) (hk : 0 < k)\n");
    emit("A4 LEAN     (mass : ell ≤ 8*E*u*Z) (first : 4*k*n ≤ 25*(1+B)*m)\n");
    emit("A4 LEAN     (bounded : u*(1+B) ≤ 9) :\n");
    emit("A4 LEAN     ell*(k*n) ≤ 450*E*Z*m := by\n");
    emit("A4 LEAN   have hm : 0 ≤ m := by\n");
    emit("A4 LEAN     by_contra! bad\n");
    emit("A4 LEAN     nlinarith only [first,mul_pos hk hn,mul_nonpos_of_nonneg_of_nonpos hB bad.le,bad]\n");
    emit("A4 LEAN   have hp : 0 ≤ 8*E*u*Z := by positivity\n");
    emit("A4 LEAN   have H := mul_le_mul_of_nonneg_left first hp\n");
    emit("A4 LEAN   have H' := mul_le_mul_of_nonneg_right mass (mul_nonneg hk.le hn.le)\n");
    emit("A4 LEAN   have K := mul_le_mul_of_nonneg_right bounded (mul_nonneg (mul_nonneg he hZ) hm)\n");
    emit("A4 LEAN   nlinarith only [H,H',K]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.SmearedMoments\n");
    emit("A4 LEAN #print axioms YangMills.SmearedMoments.vectorSpread\n");
    emit("A4 LEAN #print axioms YangMills.SmearedMoments.edgeBound\n");
    emit("A4 LEAN #print axioms YangMills.SmearedMoments.rowBound\n");
    emit("A4 LEAN #print axioms YangMills.SmearedMoments.secondCeiling\n");
    emit("A4 LEAN #print axioms YangMills.SmearedMoments.massInterpolation\n");
    emit("A4 LEAN #print axioms YangMills.SmearedMoments.varianceAndRate\n");
    emit("A4 LEAN #print axioms YangMills.SmearedMoments.lowFirst\n");
    emit("A4 LEAN #print axioms YangMills.SmearedMoments.weightedEscape\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
