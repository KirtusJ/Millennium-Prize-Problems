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
    emit("A4 LEAN import Mathlib.Analysis.Complex.AbsMax\n");
    emit("A4 LEAN import Mathlib.MeasureTheory.Integral.Bochner.Set\n");
    emit("A4 LEAN import Mathlib.Analysis.SpecialFunctions.Integrals\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN open MeasureTheory Set Filter\n");
    emit("A4 LEAN namespace YangMills.UniformBand\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- The high-order zero is supplied as a holomorphic quotient g. -/\n");
    emit("A4 LEAN theorem diskPower {g : ℂ → ℂ} {R M : ℝ} (n : ℕ) (hr : 0 < R)\n");
    emit("A4 LEAN     (hg : DiffContOnCl ℂ g (Metric.ball 0 R))\n");
    emit("A4 LEAN     (hb : ∀ z : ℂ, ‖z‖ = R → ‖z^n*g z‖ ≤ M)\n");
    emit("A4 LEAN     {w : ℂ} (hw : w ∈ closure (Metric.ball 0 R)) :\n");
    emit("A4 LEAN     ‖w^n*g w‖ ≤ (‖w‖/R)^n*M := by\n");
    emit("A4 LEAN   have inner : ‖g w‖ ≤ M/R^n := by\n");
    emit("A4 LEAN     apply Complex.norm_le_of_forall_mem_frontier_norm_le Metric.isBounded_ball hg _ hw\n");
    emit("A4 LEAN     rw [frontier_ball (0 : ℂ) hr.ne']\n");
    emit("A4 LEAN     intro z hz\n");
    emit("A4 LEAN     have hz' : ‖z‖ = R := by simpa [Metric.mem_sphere] using hz\n");
    emit("A4 LEAN     have h := hb z hz'\n");
    emit("A4 LEAN     rw [norm_mul, norm_pow, hz'] at h\n");
    emit("A4 LEAN     exact (le_div_iff₀ (pow_pos hr n)).2 (by simpa [mul_comm] using h)\n");
    emit("A4 LEAN   rw [norm_mul, norm_pow, div_pow]\n");
    emit("A4 LEAN   calc\n");
    emit("A4 LEAN     _ ≤ ‖w‖^n*(M/R^n) := mul_le_mul_of_nonneg_left inner (pow_nonneg (norm_nonneg _) _)\n");
    emit("A4 LEAN     _ = _ := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- An arbitrary fixed prefactor disappears when all moment orders are tested. -/\n");
    emit("A4 LEAN theorem zeroTail {m C q : ℝ} (hm : 0 ≤ m) (hq : 1 < q)\n");
    emit("A4 LEAN     (h : ∀ n : ℕ, m*q^n ≤ C) : m = 0 := by\n");
    emit("A4 LEAN   by_contra ne\n");
    emit("A4 LEAN   have hp : 0 < m := lt_of_le_of_ne hm (Ne.symm ne)\n");
    emit("A4 LEAN   obtain ⟨n, hn⟩ := pow_unbounded_of_one_lt (C/m) hq\n");
    emit("A4 LEAN   have hn' := (div_lt_iff₀ hp).mp hn\n");
    emit("A4 LEAN   linarith [h n, mul_comm m (q^n)]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem momentTail {X : Type*} [MeasurableSpace X] (μ : Measure X) [IsFiniteMeasure μ]\n");
    emit("A4 LEAN     (f : X → ℝ) (s : Set X) (hs : MeasurableSet s) {q C : ℝ} (hq : 1 < q)\n");
    emit("A4 LEAN     (hf : ∀ x, 0 ≤ f x) (lower : ∀ x ∈ s, q ≤ f x)\n");
    emit("A4 LEAN     (hi : ∀ n : ℕ, Integrable (fun x => f x ^ n) μ)\n");
    emit("A4 LEAN     (bound : ∀ n : ℕ, ∫ x, f x^n ∂μ ≤ C) : μ.real s = 0 := by\n");
    emit("A4 LEAN   apply zeroTail measureReal_nonneg hq\n");
    emit("A4 LEAN   intro n\n");
    emit("A4 LEAN   have le := setIntegral_mono_on (μ := μ)\n");
    emit("A4 LEAN     (f := fun _ : X => q^n) (integrable_const _).integrableOn (hi n).integrableOn hs\n");
    emit("A4 LEAN     (fun x hx => pow_le_pow_left₀ (by linarith : 0 ≤ q) (lower x hx) n)\n");
    emit("A4 LEAN   simpa [setIntegral_const, smul_eq_mul] using\n");
    emit("A4 LEAN     le.trans ((setIntegral_le_integral (hi n)\n");
    emit("A4 LEAN       (Filter.Eventually.of_forall fun x => pow_nonneg (hf x) n)).trans (bound n))\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Apply the two alternatives to the vacuum-subtracted scaled transfer. -/\n");
    emit("A4 LEAN theorem split {x b e : ℝ} (hb : 3/4 ≤ b)\n");
    emit("A4 LEAN     (h : |x^2*(x-b)| ≤ e) :\n");
    emit("A4 LEAN     x^2 ≤ 4*e ∨ |x-b| ≤ 4*e := by\n");
    emit("A4 LEAN   rw [abs_mul, abs_of_nonneg (sq_nonneg x)] at h\n");
    emit("A4 LEAN   by_cases small : x ≤ 1/2\n");
    emit("A4 LEAN   · left\n");
    emit("A4 LEAN     have ht : 1/4 ≤ |x-b| := by rw [abs_of_nonpos (by linarith)]; linarith\n");
    emit("A4 LEAN     nlinarith [mul_le_mul_of_nonneg_left ht (sq_nonneg x)]\n");
    emit("A4 LEAN   · right\n");
    emit("A4 LEAN     have ht : (1/2:ℝ)^2 ≤ x^2 := pow_le_pow_left₀ (by norm_num) (le_of_not_ge small) 2\n");
    emit("A4 LEAN     nlinarith [mul_le_mul_of_nonneg_right ht (abs_nonneg (x-b))]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem seedCoefficient : (4*(-1/24)-2*(1/4)^2 : ℝ) = -7/24 := by norm_num\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem nearSimpleRoot {x a b c e d : ℝ} (hd : 0 < d)\n");
    emit("A4 LEAN     (hb : d ≤ |x-b|) (hc : d ≤ |x-c|) (h : |(x-a)*(x-b)*(x-c)| ≤ e) :\n");
    emit("A4 LEAN     |x-a| ≤ e/d^2 := by\n");
    emit("A4 LEAN   rw [abs_mul, abs_mul] at h\n");
    emit("A4 LEAN   apply (le_div_iff₀ (sq_pos_of_pos hd)).2\n");
    emit("A4 LEAN   calc\n");
    emit("A4 LEAN     _ ≤ |x-a| * (|x-b| * |x-c|) := by\n");
    emit("A4 LEAN       apply mul_le_mul_of_nonneg_left _ (abs_nonneg _)\n");
    emit("A4 LEAN       simpa [pow_two] using mul_le_mul hb hc hd.le (abs_nonneg _)\n");
    emit("A4 LEAN     _ ≤ e := by simpa [mul_assoc] using h\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem quarticCoefficient (θ : ℝ) :\n");
    emit("A4 LEAN     (1/48 + 1/96 + 1/128 + 1/48 + θ/256 : ℝ) = 23/384 + θ/256 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem secondLagUpper {y d : ℝ} (hy : |y-1| ≤ d) :\n");
    emit("A4 LEAN     |1-y^2| ≤ d*(2+d) := by\n");
    emit("A4 LEAN   rw [show 1-y^2 = -(y-1)*(y+1) by ring, abs_mul, abs_neg]\n");
    emit("A4 LEAN   have hb : |y+1| ≤ 2+d := by\n");
    emit("A4 LEAN     calc\n");
    emit("A4 LEAN       |y+1| = |(y-1)+2| := by ring_nf\n");
    emit("A4 LEAN       _ ≤ |y-1|+|2| := abs_add_le _ _\n");
    emit("A4 LEAN       _ ≤ 2+d := by rw [abs_of_nonneg (by norm_num : (0:ℝ) ≤ 2)]; linarith\n");
    emit("A4 LEAN   exact mul_le_mul hy hb (abs_nonneg _) ((abs_nonneg _).trans hy)\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem secondLagLower {y d : ℝ} (hy : 0 ≤ y) (hd : y ≤ d) :\n");
    emit("A4 LEAN     |y^2| ≤ d^2 := by\n");
    emit("A4 LEAN   rw [abs_of_nonneg (sq_nonneg _)]\n");
    emit("A4 LEAN   exact pow_le_pow_left₀ hy hd 2\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Two centered atoms and a centered atom split into a wider pair agree\n");
    emit("A4 LEAN through the third raw moment. -/\n");
    emit("A4 LEAN noncomputable def mix (a d : ℝ) (n : ℕ) : ℝ := 1-a+a*((1-d)^n+(1+d)^n)/2\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem matched (a w : ℝ) :\n");
    emit("A4 LEAN     ∀ n ∈ Finset.range 4, mix a (w/2) n = mix (a/16) (2*w) n := by\n");
    emit("A4 LEAN   intro n hn\n");
    emit("A4 LEAN   have hn' := Finset.mem_range.mp hn\n");
    emit("A4 LEAN   interval_cases n <;> unfold mix <;> ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.UniformBand\n");
    emit("A4 LEAN #print axioms YangMills.UniformBand.zeroTail\n");
    emit("A4 LEAN #print axioms YangMills.UniformBand.momentTail\n");
    emit("A4 LEAN #print axioms YangMills.UniformBand.split\n");
    emit("A4 LEAN #print axioms YangMills.UniformBand.seedCoefficient\n");
    emit("A4 LEAN #print axioms YangMills.UniformBand.matched\n");
    emit("A4 LEAN #print axioms YangMills.UniformBand.diskPower\n");
    emit("A4 LEAN #print axioms YangMills.UniformBand.nearSimpleRoot\n");
    emit("A4 LEAN #print axioms YangMills.UniformBand.quarticCoefficient\n");
    emit("A4 LEAN #print axioms YangMills.UniformBand.secondLagUpper\n");
    emit("A4 LEAN #print axioms YangMills.UniformBand.secondLagLower\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
