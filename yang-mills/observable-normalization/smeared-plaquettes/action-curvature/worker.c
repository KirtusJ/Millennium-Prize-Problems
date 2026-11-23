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
    emit("A4 LEAN import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN open MeasureTheory\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.ActionCurvature\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- I is the inverse moment; u is the action per face. -/\n");
    emit("A4 LEAN theorem curvatureBudget {A B : ℝ} (u I du : ℝ → ℝ)\n");
    emit("A4 LEAN     (h : ∀ x ∈ Set.uIcc A B, HasDerivAt u (du x) x)\n");
    emit("A4 LEAN     (hI : ∀ x ∈ Set.uIcc A B, I x = -2 * du x)\n");
    emit("A4 LEAN     (hi : IntervalIntegrable du volume A B) :\n");
    emit("A4 LEAN     (∫ x in A..B, I x) = 2*(u A-u B) := by\n");
    emit("A4 LEAN   rw [intervalIntegral.integral_congr hI, intervalIntegral.integral_const_mul,\n");
    emit("A4 LEAN     intervalIntegral.integral_eq_sub_of_hasDerivAt h hi]\n");
    emit("A4 LEAN   ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem budgetCeiling {r total start finish : ℝ} (hr : 0 < r)\n");
    emit("A4 LEAN     (h : total=2*(start-finish)) (upper : r*start ≤ 5/2) (lower : 0 ≤ finish) :\n");
    emit("A4 LEAN     r*total ≤ 5 := by\n");
    emit("A4 LEAN   rw [h]\n");
    emit("A4 LEAN   nlinarith only [upper,mul_nonneg hr.le lower]\n");
    emit("A4 LEAN \n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN /-- Cauchy–Schwarz between the inverse and first moments of a finite measure. -/\n");
    emit("A4 LEAN theorem inverseInterpolation (μ : Measure ℝ) [IsFiniteMeasure μ]\n");
    emit("A4 LEAN     (hp : ∀ᵐ x ∂μ, 0 < x) (h1 : Integrable (fun x : ℝ => x) μ)\n");
    emit("A4 LEAN     (hinv : Integrable (fun x : ℝ => x⁻¹) μ) (m v j : ℝ)\n");
    emit("A4 LEAN     (hm : (∫ x : ℝ, x ∂μ)=m) (hv : μ.real Set.univ=v)\n");
    emit("A4 LEAN     (hj : (∫ x : ℝ, x⁻¹ ∂μ)=j) (hpos : 0 < m) : v^2 ≤ m*j := by\n");
    emit("A4 LEAN   have hn : 0 ≤ ∫ x : ℝ, (v*x-m)^2/x ∂μ := integral_nonneg_of_ae\n");
    emit("A4 LEAN     (hp.mono fun x hx => div_nonneg (sq_nonneg _) hx.le)\n");
    emit("A4 LEAN   have eq := integral_congr_ae (hp.mono fun x hx => show\n");
    emit("A4 LEAN       (v*x-m)^2/x = v^2*x - 2*v*m + m^2*x⁻¹ by field_simp [hx.ne']; ring)\n");
    emit("A4 LEAN   rw [eq] at hn\n");
    emit("A4 LEAN   have step := integral_add ((h1.const_mul (v^2)).sub (integrable_const (μ := μ) (2*v*m)))\n");
    emit("A4 LEAN     (hinv.const_mul (m^2))\n");
    emit("A4 LEAN   simp only [Pi.sub_apply] at step\n");
    emit("A4 LEAN   rw [step,integral_sub (h1.const_mul _) (integrable_const _),integral_const_mul (v^2),\n");
    emit("A4 LEAN     integral_const_mul (m^2),integral_const,smul_eq_mul,hm,hv,hj] at hn\n");
    emit("A4 LEAN   exact le_of_mul_le_mul_left (a := m) (by nlinarith only [hn]) hpos\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem lowMass (μ : Measure ℝ) [IsFiniteMeasure μ] (hp : ∀ᵐ x ∂μ, 0 < x)\n");
    emit("A4 LEAN     (hi : Integrable (fun x : ℝ => x⁻¹) μ) {E : ℝ} (he : 0 ≤ E) :\n");
    emit("A4 LEAN     μ.real (Set.Ioc 0 E) ≤ E*(∫ x : ℝ, x⁻¹ ∂μ) := by\n");
    emit("A4 LEAN   let s := Set.Ioc 0 E\n");
    emit("A4 LEAN   have hind := (integrable_const (μ := μ) (1:ℝ)).indicator (measurableSet_Ioc (a := 0) (b := E))\n");
    emit("A4 LEAN   have h := integral_mono_ae hind (hi.const_mul E) (hp.mono fun x hx => by\n");
    emit("A4 LEAN     by_cases h : x ∈ s\n");
    emit("A4 LEAN     · rw [Set.indicator_of_mem h]\n");
    emit("A4 LEAN       exact (by simpa [div_eq_mul_inv] using (one_le_div hx).mpr h.2 : 1 ≤ E*x⁻¹)\n");
    emit("A4 LEAN     · rw [Set.indicator_of_not_mem h]\n");
    emit("A4 LEAN       exact mul_nonneg he (inv_nonneg.mpr hx.le))\n");
    emit("A4 LEAN   simpa only [integral_indicator_const _ measurableSet_Ioc, smul_eq_mul, mul_one, integral_const_mul] using h\n");
    emit("A4 LEAN \n");
#elif ROLE == 2
    emit("A4 LEAN /-- Dominate a window integral by a constant multiple of its curvature budget. -/\n");
    emit("A4 LEAN theorem windowAverage {A B c : ℝ} (P I : ℝ → ℝ) (hab : A ≤ B)\n");
    emit("A4 LEAN     (hp : IntervalIntegrable P volume A B) (hi : IntervalIntegrable I volume A B)\n");
    emit("A4 LEAN     (bound : ∀ x ∈ Set.Icc A B, P x ≤ c*I x) :\n");
    emit("A4 LEAN     (∫ x in A..B, P x) ≤ c*(∫ x in A..B, I x) := by\n");
    emit("A4 LEAN   have h := intervalIntegral.integral_mono_on hab hp (hi.const_mul c) bound\n");
    emit("A4 LEAN   simpa only [intervalIntegral.integral_const_mul] using h\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem rmsBound {G r total sqAvg : ℝ} (hr : 0 < r) (hG : G=r^2)\n");
    emit("A4 LEAN     (budget : r*total ≤ 5) (interpolated : sqAvg ≤ G*(80/r)*total) :\n");
    emit("A4 LEAN     sqAvg ≤ 400 := by\n");
    emit("A4 LEAN   have h : G*(80/r)=80*r := by rw [hG]; field_simp; ring\n");
    emit("A4 LEAN   rw [h] at interpolated\n");
    emit("A4 LEAN   linarith only [interpolated,budget]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem scaledTail {r v V J ε m : ℝ} (hr : 0 < r) (hv : 0 < v)\n");
    emit("A4 LEAN     (hV : 0 < V) (hJ : 0 ≤ J) (he : 0 ≤ ε)\n");
    emit("A4 LEAN     (floor : v ≤ r^2*V) (low : m ≤ ε*r*J) :\n");
    emit("A4 LEAN     m/V ≤ ε*r^3*J/v := by\n");
    emit("A4 LEAN   apply (div_le_div_iff₀ hV hv).mpr\n");
    emit("A4 LEAN   nlinarith only [mul_le_mul_of_nonneg_left floor (mul_nonneg (mul_nonneg he hr.le) hJ),\n");
    emit("A4 LEAN      mul_le_mul_of_nonneg_right low hv.le]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Raw probabilities of a measurable family of finite spectral laws on a dyadic window. -/\n");
    emit("A4 LEAN theorem dyadicRawLow (μ : ℝ → Measure ℝ) [∀ g, IsFiniteMeasure (μ g)]\n");
    emit("A4 LEAN     (J : ℝ → ℝ) {G r v ε : ℝ} (hr : 0 < r) (hg : G=r^2) (hv : 0 < v) (he : 0 ≤ ε)\n");
    emit("A4 LEAN     (posEnergy : ∀ g ∈ Set.Icc G (2*G), ∀ᵐ x ∂(μ g), 0 < x)\n");
    emit("A4 LEAN     (inverse : ∀ g ∈ Set.Icc G (2*G), Integrable (fun x : ℝ => x⁻¹) (μ g))\n");
    emit("A4 LEAN     (moment : ∀ g ∈ Set.Icc G (2*G), (∫ x : ℝ, x⁻¹ ∂(μ g)) = J g)\n");
    emit("A4 LEAN     (floor : ∀ g ∈ Set.Icc G (2*G), v ≤ r^2*(μ g).real Set.univ)\n");
    emit("A4 LEAN     (hi : IntervalIntegrable J volume G (2*G))\n");
    emit("A4 LEAN     (hprob : IntervalIntegrable (fun g => (μ g).real (Set.Ioc 0 (ε*r)) /\n");
    emit("A4 LEAN       (μ g).real Set.univ) volume G (2*G))\n");
    emit("A4 LEAN     (budget : r*(∫ g in G..2*G, J g) ≤ 5) :\n");
    emit("A4 LEAN     (∫ g in G..2*G, (μ g).real (Set.Ioc 0 (ε*r))/(μ g).real Set.univ)/G ≤ 5*ε/v := by\n");
    emit("A4 LEAN   have hG : 0 < G := hg ▸ sq_pos_of_pos hr\n");
    emit("A4 LEAN   have hab : G ≤ 2*G := by linarith\n");
    emit("A4 LEAN   have bound (g : ℝ) (hx : g ∈ Set.Icc G (2*G)) :\n");
    emit("A4 LEAN       (μ g).real (Set.Ioc 0 (ε*r))/(μ g).real Set.univ ≤ (ε*r^3/v)*J g := by\n");
    emit("A4 LEAN     have h := lowMass (μ g) (posEnergy g hx) (inverse g hx) (mul_nonneg he hr.le)\n");
    emit("A4 LEAN     rw [moment g hx] at h\n");
    emit("A4 LEAN     have hV : 0 < (μ g).real Set.univ := by\n");
    emit("A4 LEAN       by_contra! z\n");
    emit("A4 LEAN       linarith only [floor g hx,hv,mul_nonpos_of_nonneg_of_nonpos (sq_nonneg r) z]\n");
    emit("A4 LEAN     have hJ : 0 ≤ J g := by\n");
    emit("A4 LEAN       rw [← moment g hx]\n");
    emit("A4 LEAN       exact integral_nonneg_of_ae ((posEnergy g hx).mono fun x h => (inv_pos.mpr h).le)\n");
    emit("A4 LEAN     have res := scaledTail hr hv hV hJ he (floor g hx) h\n");
    emit("A4 LEAN     convert res using 1\n");
    emit("A4 LEAN     ring\n");
    emit("A4 LEAN   have HW := windowAverage _ J hab hprob hi bound\n");
    emit("A4 LEAN   apply (div_le_iff₀ hG).mpr\n");
    emit("A4 LEAN   rw [div_mul_eq_mul_div]\n");
    emit("A4 LEAN   apply (le_div_iff₀ hv).mpr\n");
    emit("A4 LEAN   have H := mul_le_mul_of_nonneg_right HW hv.le\n");
    emit("A4 LEAN   have id : ((ε*r^3/v)*(∫ g in G..2*G, J g))*v = (ε*r^3)*(∫ g in G..2*G, J g) := by\n");
    emit("A4 LEAN     field_simp\n");
    emit("A4 LEAN   rw [id] at H\n");
    emit("A4 LEAN   rw [hg] at H budget ⊢\n");
    emit("A4 LEAN   nlinarith only [H,mul_le_mul_of_nonneg_left budget (mul_nonneg he (sq_nonneg r))]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.ActionCurvature\n");
    emit("A4 LEAN #print axioms YangMills.ActionCurvature.curvatureBudget\n");
    emit("A4 LEAN #print axioms YangMills.ActionCurvature.budgetCeiling\n");
    emit("A4 LEAN #print axioms YangMills.ActionCurvature.inverseInterpolation\n");
    emit("A4 LEAN #print axioms YangMills.ActionCurvature.lowMass\n");
    emit("A4 LEAN #print axioms YangMills.ActionCurvature.windowAverage\n");
    emit("A4 LEAN #print axioms YangMills.ActionCurvature.rmsBound\n");
    emit("A4 LEAN #print axioms YangMills.ActionCurvature.scaledTail\n");
    emit("A4 LEAN #print axioms YangMills.ActionCurvature.dyadicRawLow\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
