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
static int verify_count(void) {
#if ROLE == 0
    /* s=j/8, x=i/8: the supporting square dominates the event x>=1. */
    for (long j=1; j<=8; ++j) for (long i=0; i<=32; ++i) {
        long value=(8+j)*i-8*j;
        if (value*value < (i>=8 ? 4096 : 0)) return 0;
    }
#elif ROLE == 1
    /* Integer numerator for the equality law, s=1/n, x_high=1/(n+1). */
    for (long n=1; n<40; ++n) {
        long a=n+1, high=n*n-1;
        if (2*a*(a+high) != (n+1)*(a*a+high)) return 0;
    }
#else
    /* Positive covariance under two independent samples, five unequal weights. */
    long w[5]={2,7,1,8,4}, a[5]={0,2,4,4,7}, b[5]={1,3,5,8,9};
    long n=0,x=0,y=0,xy=0,pair=0;
    for (int i=0;i<5;++i) {
        n+=w[i]; x+=w[i]*a[i]; y+=w[i]*b[i]; xy+=w[i]*a[i]*b[i];
        for (int j=0;j<5;++j) pair+=w[i]*w[j]*(a[i]-a[j])*(b[i]-b[j]);
    }
    if (pair<=0 || pair!=2*(n*xy-x*y)) return 0;
#endif
    return 1;
}
__attribute__((used,noreturn)) static void run(void) {
    if(!verify_count()){sys(60,2,0,0);__builtin_unreachable();}
#if ROLE == 0
    emit("A4 CHILD spectrum\n");
    emit("A4 LEAN import Mathlib.MeasureTheory.Integral.Bochner.Set\n");
    emit("A4 LEAN import Mathlib.Tactic.FieldSimp\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN open MeasureTheory\n");
    emit("A4 LEAN namespace YangMills.GapWeight\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Sharp first/second moment bound from a lower bound on the probability\n");
    emit("A4 LEAN of an event on which x is at least one. The probability space is arbitrary. -/\n");
    emit("A4 LEAN theorem lowMassBound {Ω : Type*} [MeasurableSpace Ω] (μ : Measure Ω)\n");
    emit("A4 LEAN     [IsProbabilityMeasure μ] {A : Set Ω} (hA : MeasurableSet A)\n");
    emit("A4 LEAN     (x : Ω → ℝ) (hx : Integrable x μ)\n");
    emit("A4 LEAN     (hx2 : Integrable (fun i => (x i)^2) μ) {s : ℝ} (hs : 0 ≤ s)\n");
    emit("A4 LEAN     (hp : s^2 ≤ μ.real A) (hfloor : ∀ i ∈ A, 1 ≤ x i) :\n");
    emit("A4 LEAN     2*s*(∫ i, x i ∂μ) ≤ (1+s)*(∫ i, (x i)^2 ∂μ) := by\n");
    emit("A4 LEAN   let g := fun i => (1+s)*((1+s)*(x i)^2-2*s*x i)\n");
    emit("A4 LEAN   have hg : Integrable g μ := ((hx2.const_mul (1+s)).sub (hx.const_mul (2*s))).const_mul _\n");
    emit("A4 LEAN   have hdom (i : Ω) : A.indicator (1 : Ω → ℝ) i ≤ g i + s^2 := by\n");
    emit("A4 LEAN     have hsq : g i + s^2 = ((1+s)*x i-s)^2 := by dsimp [g]; ring\n");
    emit("A4 LEAN     rw [hsq]\n");
    emit("A4 LEAN     by_cases hi : i ∈ A\n");
    emit("A4 LEAN     · rw [Set.indicator_of_mem hi]\n");
    emit("A4 LEAN       change 1 ≤ _\n");
    emit("A4 LEAN       have ht : 1 ≤ (1+s)*x i-s := by\n");
    emit("A4 LEAN         nlinarith [mul_nonneg hs (sub_nonneg.mpr (hfloor i hi)), hfloor i hi]\n");
    emit("A4 LEAN       nlinarith [sq_nonneg ((1+s)*x i-s-1)]\n");
    emit("A4 LEAN     · rw [Set.indicator_of_not_mem hi]\n");
    emit("A4 LEAN       exact sq_nonneg _\n");
    emit("A4 LEAN   have h := integral_mono ((integrable_const (1 : ℝ)).indicator hA)\n");
    emit("A4 LEAN     (hg.add (integrable_const (s^2))) hdom\n");
    emit("A4 LEAN   change (∫ i, A.indicator 1 i ∂μ) ≤ ∫ i, g i + s^2 ∂μ at h\n");
    emit("A4 LEAN   rw [integral_indicator_one hA, integral_add hg (integrable_const _)] at h\n");
    emit("A4 LEAN   simp only [g, integral_const_mul, integral_sub (hx2.const_mul _) (hx.const_mul _),\n");
    emit("A4 LEAN     integral_const, measureReal_univ_eq_one, one_smul] at h\n");
    emit("A4 LEAN   by_contra hn\n");
    emit("A4 LEAN   have hg' := mul_pos (a := 1+s) (by linarith)\n");
    emit("A4 LEAN     (sub_pos.mpr (lt_of_not_ge hn))\n");
    emit("A4 LEAN   nlinarith\n");
    emit("A4 LEAN \n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN /-- Equality for the two-atom law at x=1 and x=s/(1+s). -/\n");
    emit("A4 LEAN theorem twoAtomEquality (s : ℝ) (hs : 0 ≤ s) :\n");
    emit("A4 LEAN     2*s*(s^2+(1-s^2)*(s/(1+s))) =\n");
    emit("A4 LEAN     (1+s)*(s^2+(1-s^2)*(s/(1+s))^2) := by\n");
    emit("A4 LEAN   have h : 1+s ≠ 0 := by linarith\n");
    emit("A4 LEAN   field_simp\n");
    emit("A4 LEAN   ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- The cutoff event under the half-time measure, from bounds on its\n");
    emit("A4 LEAN conditional contributions to the mean transfer weight. -/\n");
    emit("A4 LEAN theorem halfTimeFloor {p a b r : ℝ} (hab : a < b)\n");
    emit("A4 LEAN     (hmean : r ≤ p*b+(1-p)*a) :\n");
    emit("A4 LEAN     (r-a)/(b-a) ≤ p := by\n");
    emit("A4 LEAN   apply (div_le_iff₀ (sub_pos.mpr hab)).mpr\n");
    emit("A4 LEAN   linarith\n");
    emit("A4 LEAN \n");
#elif ROLE == 2
    emit("A4 LEAN /-- Reweighting by an increasing function raises the mean of a comonotone\n");
    emit("A4 LEAN test. Only the three stated integrability hypotheses are used. -/\n");
    emit("A4 LEAN theorem monotoneTilt {Ω : Type*} [MeasurableSpace Ω] (μ : Measure Ω)\n");
    emit("A4 LEAN     [IsProbabilityMeasure μ] (a b : Ω → ℝ) (ha : Integrable a μ)\n");
    emit("A4 LEAN     (hb : Integrable b μ) (hab : Integrable (fun i => a i*b i) μ)\n");
    emit("A4 LEAN     (h : ∀ i j, 0 ≤ (a i-a j)*(b i-b j)) :\n");
    emit("A4 LEAN     (∫ i, a i ∂μ)*(∫ i, b i ∂μ) ≤ ∫ i, a i*b i ∂μ := by\n");
    emit("A4 LEAN   have hr (i : Ω) : a i*(∫ j, b j ∂μ) + b i*(∫ j, a j ∂μ) ≤\n");
    emit("A4 LEAN       a i*b i + ∫ j, a j*b j ∂μ := by\n");
    emit("A4 LEAN     have H := integral_mono ((hb.const_mul (a i)).add (ha.const_mul (b i)))\n");
    emit("A4 LEAN       ((integrable_const (a i*b i)).add hab) (fun j => by\n");
    emit("A4 LEAN         change a i*b j + b i*a j ≤ a i*b i + a j*b j\n");
    emit("A4 LEAN         nlinarith [h i j])\n");
    emit("A4 LEAN     simp only [Pi.add_apply] at H\n");
    emit("A4 LEAN     simpa only [integral_add (hb.const_mul _) (ha.const_mul _),\n");
    emit("A4 LEAN       integral_add (integrable_const _) hab, integral_const_mul, integral_const,\n");
    emit("A4 LEAN       measureReal_univ_eq_one, one_smul] using H\n");
    emit("A4 LEAN   have H := integral_mono ((ha.mul_const _).add (hb.mul_const _))\n");
    emit("A4 LEAN     (hab.add (integrable_const _)) hr\n");
    emit("A4 LEAN   simp only [Pi.add_apply] at H\n");
    emit("A4 LEAN   simp only [integral_add (ha.mul_const _) (hb.mul_const _),\n");
    emit("A4 LEAN     integral_add hab (integrable_const _), integral_mul_const, integral_const,\n");
    emit("A4 LEAN     measureReal_univ_eq_one, one_smul] at H\n");
    emit("A4 LEAN   linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.GapWeight\n");
    emit("A4 LEAN #print axioms YangMills.GapWeight.lowMassBound\n");
    emit("A4 LEAN #print axioms YangMills.GapWeight.twoAtomEquality\n");
    emit("A4 LEAN #print axioms YangMills.GapWeight.halfTimeFloor\n");
    emit("A4 LEAN #print axioms YangMills.GapWeight.monotoneTilt\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
