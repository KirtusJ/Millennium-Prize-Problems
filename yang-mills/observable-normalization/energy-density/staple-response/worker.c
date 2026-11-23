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
    emit("A4 LEAN import Mathlib.MeasureTheory.Integral.Prod\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.FieldSimp\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN open MeasureTheory Filter\n");
    emit("A4 LEAN open scoped Topology\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.StapleResponse\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Squared innovations on two distinct product fibers have the same mixed\n");
    emit("A4 LEAN moment as their exterior second moments, even when the fiber laws vary. -/\n");
    emit("A4 LEAN theorem squaredFiber {E A B : Type*} [MeasurableSpace E] [MeasurableSpace A]\n");
    emit("A4 LEAN     [MeasurableSpace B] (ρ : Measure E) (μ : E → Measure A) (ν : E → Measure B)\n");
    emit("A4 LEAN     [∀ e, SFinite (μ e)] [∀ e, SFinite (ν e)] (f : E → A → ℝ) (g : E → B → ℝ) :\n");
    emit("A4 LEAN     (∫ e, ∫ z : A × B, f e z.1 ^ 2 * g e z.2 ^ 2 ∂(μ e).prod (ν e) ∂ρ) =\n");
    emit("A4 LEAN       ∫ e, (∫ u, (f e u)^2 ∂(μ e))*(∫ v, (g e v)^2 ∂(ν e)) ∂ρ := by\n");
    emit("A4 LEAN   apply integral_congr_ae\n");
    emit("A4 LEAN   filter_upwards with e\n");
    emit("A4 LEAN   exact integral_prod_mul (fun u => (f e u)^2) (fun v => (g e v)^2)\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Multiplication by an arbitrary boundary or spectator weight commutes with\n");
    emit("A4 LEAN integrating out the one temporal link at fixed remaining links. -/\n");
    emit("A4 LEAN theorem boundaryInsertion {E A : Type*} [MeasurableSpace E] [MeasurableSpace A]\n");
    emit("A4 LEAN     (ρ : Measure E) (μ : E → Measure A) (w : E → ℝ) (f : E → A → ℝ) :\n");
    emit("A4 LEAN     (∫ e, ∫ a, w e * f e a ∂(μ e) ∂ρ) = ∫ e, w e * (∫ a, f e a ∂(μ e)) ∂ρ := by\n");
    emit("A4 LEAN   apply integral_congr_ae\n");
    emit("A4 LEAN   filter_upwards with e\n");
    emit("A4 LEAN   exact integral_const_mul (w e) (f e)\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Multiply through by the squared normalizer to compare the three Taylor\n");
    emit("A4 LEAN polynomials for the raw tilted-gamma moments. -/\n");
    emit("A4 LEAN theorem tiltedVariance (x : ℝ) :\n");
    emit("A4 LEAN     let a := 1-3*x/8-15*x^2/128\n");
    emit("A4 LEAN     let b := 3/2-15*x/16-105*x^2/256\n");
    emit("A4 LEAN     let c := 15/4-105*x/32-945*x^2/512\n");
    emit("A4 LEAN     c*a-b^2-(3/2-3*x/4-9*x^2/8)*a^2 =\n");
    emit("A4 LEAN       x^3*(2025*x^3/131072+7155*x^2/65536-99*x/8192-189/256) := by\n");
    emit("A4 LEAN   dsimp\n");
    emit("A4 LEAN   ring\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem reciprocalRemainder (β R : ℝ) (h : R ≠ 0) :\n");
    emit("A4 LEAN     β^2/R-β/6-(6*β-R)/36=(6*β-R)^2/(36*R) := by\n");
    emit("A4 LEAN   field_simp\n");
    emit("A4 LEAN   ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem reciprocalSquare (β R : ℝ) (h : R ≠ 0) :\n");
    emit("A4 LEAN     β^2/R^2-1/36=(6*β-R)*(6*β+R)/(36*R^2) := by\n");
    emit("A4 LEAN   field_simp\n");
    emit("A4 LEAN   ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem environmentExpansion (β R : ℝ) (h : R ≠ 0) :\n");
    emit("A4 LEAN     β^2*(-3/(4*R)-9/(8*R^2))+β/8+(6*β-R)/48+1/32 =\n");
    emit("A4 LEAN       -(6*β-R)^2/(48*R)-(6*β-R)*(6*β+R)/(32*R^2) := by\n");
    emit("A4 LEAN   field_simp\n");
    emit("A4 LEAN   ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem secondMean : -(3:ℝ)/48-1/32 = -3/32 := by norm_num\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Covariance of two centered quadratic energies in three independent colors\n");
    emit("A4 LEAN after the Gaussian fourth-moment contraction has been supplied. -/\n");
    emit("A4 LEAN theorem wickContraction {ι : Type*} (s : Finset ι) (K : ι → ℝ) (cov : ℝ)\n");
    emit("A4 LEAN     (wick : cov = (3/2)*∑ i ∈ s, (K i)^2) :\n");
    emit("A4 LEAN     cov / 48^2 = (∑ i ∈ s, (K i)^2)/1536 := by rw [wick]; ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem projectedSignal {ι : Type*} (s : Finset ι) (K : ι → ℝ)\n");
    emit("A4 LEAN     {j : ι} (hj : j ∈ s) (h : K j ≠ 0) : 0 < (∑ i ∈ s, (K i)^2)/1536 := by\n");
    emit("A4 LEAN   have h₁ := Finset.single_le_sum (f := fun i => (K i)^2)\n");
    emit("A4 LEAN     (fun i (_ : i ∈ s) => sq_nonneg (K i)) hj\n");
    emit("A4 LEAN   exact div_pos ((sq_pos_of_ne_zero h).trans_le h₁) (by norm_num)\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Pass from convergence of each rescaled projected cross entry to convergence\n");
    emit("A4 LEAN of the rescaled squared Frobenius reading. -/\n");
    emit("A4 LEAN theorem transferTail {ι : Type*} (s : Finset ι) (K : ℕ → ι → ℝ) (c : ι → ℝ)\n");
    emit("A4 LEAN     (h : ∀ i ∈ s, Tendsto (fun n : ℕ => (n:ℝ)^4*K n i) atTop (𝓝 (c i))) :\n");
    emit("A4 LEAN     Tendsto (fun n : ℕ => (n:ℝ)^8*(∑ i ∈ s, (K n i)^2)/1536) atTop\n");
    emit("A4 LEAN       (𝓝 ((∑ i ∈ s, (c i)^2)/1536)) := by\n");
    emit("A4 LEAN   have z := tendsto_finset_sum s (fun i hi => (h i hi).pow 2)\n");
    emit("A4 LEAN   convert z.div_const 1536 using 1\n");
    emit("A4 LEAN   ext n\n");
    emit("A4 LEAN   rw [Finset.mul_sum]\n");
    emit("A4 LEAN   congr 1\n");
    emit("A4 LEAN   apply Finset.sum_congr rfl\n");
    emit("A4 LEAN   intro i _\n");
    emit("A4 LEAN   ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem spatialCoefficient (p : ℝ) (hp : p ≠ 0) :\n");
    emit("A4 LEAN     12*(1/p^2)^2/1536=1/(128*p^4) := by field_simp; ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.StapleResponse\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN #print axioms YangMills.StapleResponse.boundaryInsertion\n");
    emit("A4 LEAN #print axioms YangMills.StapleResponse.squaredFiber\n");
    emit("A4 LEAN #print axioms YangMills.StapleResponse.tiltedVariance\n");
    emit("A4 LEAN #print axioms YangMills.StapleResponse.reciprocalRemainder\n");
    emit("A4 LEAN #print axioms YangMills.StapleResponse.reciprocalSquare\n");
    emit("A4 LEAN #print axioms YangMills.StapleResponse.environmentExpansion\n");
    emit("A4 LEAN #print axioms YangMills.StapleResponse.secondMean\n");
    emit("A4 LEAN #print axioms YangMills.StapleResponse.wickContraction\n");
    emit("A4 LEAN #print axioms YangMills.StapleResponse.projectedSignal\n");
    emit("A4 LEAN #print axioms YangMills.StapleResponse.transferTail\n");
    emit("A4 LEAN #print axioms YangMills.StapleResponse.spatialCoefficient\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
