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
    emit("A4 LEAN import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN import Mathlib.Tactic.FieldSimp\n");
    emit("A4 LEAN open MeasureTheory Filter\n");
    emit("A4 LEAN namespace YangMills.HamiltonianVariance\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem linkReplacement {K κ frozen original : ℝ} (hκ : 0 < κ)\n");
    emit("A4 LEAN     (trial : κ*K + original ≤ frozen) : K ≤ (frozen-original)/κ := by\n");
    emit("A4 LEAN   exact (le_div_iff₀ hκ).mpr (by linarith only [trial])\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Square of the upper bound on interval probability at the chosen half-width. -/\n");
    emit("A4 LEAN theorem intervalChoice {z : ℝ} (hz : 0 < z) :\n");
    emit("A4 LEAN     2*Real.pi^2*z*(1/(8*Real.pi^2*z)) = (1/2 : ℝ)^2 := by\n");
    emit("A4 LEAN   field_simp [Real.pi_ne_zero, hz.ne']\n");
    emit("A4 LEAN   ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem varianceFloor {v u p : ℝ} (prob : p ≤ 1/2) (sq : u^2*(1-p) ≤ v) :\n");
    emit("A4 LEAN     u^2/2 ≤ v := by\n");
    emit("A4 LEAN   linarith only [mul_le_mul_of_nonneg_left prob (sq_nonneg u), sq]\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem trialKinetic (m : ℝ) (hm : 0 ≤ m) :\n");
    emit("A4 LEAN     3*m^2/(4*(4*m+1)) ≤ 3*m/16 := by\n");
    emit("A4 LEAN   apply (div_le_iff₀ (by linarith : 0 < 4*(4*m+1))).mpr\n");
    emit("A4 LEAN   linarith only [hm]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem fourLinks {r : ℝ} (hr : 0 ≤ r) :\n");
    emit("A4 LEAN     1-r^4 ≤ 4*(1-r) := by\n");
    emit("A4 LEAN   have id : 4*(1-r)-(1-r^4) = (1-r)^2*(r^2+2*r+3) := by ring\n");
    emit("A4 LEAN   have hp : 0 ≤ r^2+2*r+3 := by linarith [sq_nonneg r]\n");
    emit("A4 LEAN   linarith only [id,mul_nonneg (sq_nonneg (1-r)) hp]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem optimizedTrial {g m x : ℝ} (pos : 0 < m) (hx : 0 ≤ x) (root : g=x^2)\n");
    emit("A4 LEAN     (lo : 6*x ≤ m) (hi : m ≤ 6*x+1) :\n");
    emit("A4 LEAN     3*m/16+6*g/m ≤ 17*x/8+3/16 := by\n");
    emit("A4 LEAN   have h : 6*g/m ≤ x := (div_le_iff₀ pos).mpr\n");
    emit("A4 LEAN     (by linarith only [root, mul_le_mul_of_nonneg_left lo hx])\n");
    emit("A4 LEAN   linarith only [hi,h]\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem covarianceToEnergy {M u κ : ℝ} (hκ : 0 ≤ κ) (second mean : ℝ)\n");
    emit("A4 LEAN     (identity : M = 4*κ*(1-second)) (loss : u=1-mean)\n");
    emit("A4 LEAN     (square : 0 ≤ 1-2*mean+second) : M ≤ 8*κ*u := by\n");
    emit("A4 LEAN   rw [identity,loss]\n");
    emit("A4 LEAN   linarith only [mul_nonneg hκ square]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Lift the escape probability to the second moment of the trace law. -/\n");
    emit("A4 LEAN theorem escapeToVariance (μ : Measure ℝ) [IsFiniteMeasure μ] (m u : ℝ) (hu : 0 ≤ u)\n");
    emit("A4 LEAN     (h : 1/2 ≤ μ.real {x | u ≤ |x-m|})\n");
    emit("A4 LEAN     (hi : Integrable (fun x : ℝ => (x-m)^2) μ) :\n");
    emit("A4 LEAN     u^2/2 ≤ ∫ x, (x-m)^2 ∂μ := by\n");
    emit("A4 LEAN   let s : Set ℝ := {x | u ≤ |x-m|}\n");
    emit("A4 LEAN   have hs : MeasurableSet s := measurableSet_le measurable_const\n");
    emit("A4 LEAN     ((continuous_id.sub continuous_const).abs.measurable)\n");
    emit("A4 LEAN   have H := setIntegral_ge_of_const_le (μ := μ) (c := u^2) hs (measure_ne_top μ s)\n");
    emit("A4 LEAN     (f := fun x : ℝ => (x-m)^2) (fun x hx => by\n");
    emit("A4 LEAN       have hx' : u ≤ |x-m| := hx\n");
    emit("A4 LEAN       simpa only [← sq, sq_abs] using mul_self_le_mul_self hu hx') hi.integrableOn\n");
    emit("A4 LEAN   have upper := setIntegral_le_integral (s := s) hi\n");
    emit("A4 LEAN     (Eventually.of_forall fun x => sq_nonneg (x-m))\n");
    emit("A4 LEAN   have ht : (1/2 : ℝ) ≤ μ.real s := h\n");
    emit("A4 LEAN   linarith only [mul_le_mul_of_nonneg_left ht (sq_nonneg u), H, upper]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Jensen's exponential tangent for an arbitrary normalized spectral law. -/\n");
    emit("A4 LEAN theorem normalizedSpectralWitness (μ : Measure ℝ) [IsProbabilityMeasure μ]\n");
    emit("A4 LEAN     {t M : ℝ} (ht : 0 ≤ t) (hi : Integrable (fun x : ℝ => x) μ)\n");
    emit("A4 LEAN     (he : Integrable (fun x : ℝ => Real.exp (-t*x)) μ)\n");
    emit("A4 LEAN     (hm : (∫ x, x ∂μ) ≤ M) :\n");
    emit("A4 LEAN     Real.exp (-t*M) ≤ ∫ x, Real.exp (-t*x) ∂μ := by\n");
    emit("A4 LEAN   let b := Real.exp (-t*M)\n");
    emit("A4 LEAN   have hb : 0 ≤ b := (Real.exp_pos _).le\n");
    emit("A4 LEAN   have tangent (x : ℝ) : b*(1+t*M-t*x) ≤ Real.exp (-t*x) := by\n");
    emit("A4 LEAN     have h := mul_le_mul_of_nonneg_left (Real.add_one_le_exp (t*M-t*x)) hb\n");
    emit("A4 LEAN     change Real.exp (-t*M)*(1+t*M-t*x) ≤ Real.exp (-t*x)\n");
    emit("A4 LEAN     calc\n");
    emit("A4 LEAN       _ ≤ Real.exp (-t*M)*Real.exp (t*M-t*x) := by dsimp [b] at h; linarith only [h]\n");
    emit("A4 LEAN       _ = _ := by rw [← Real.exp_add]; congr 1; ring\n");
    emit("A4 LEAN   have hir : Integrable (fun x : ℝ => 1+t*M-t*x) μ :=\n");
    emit("A4 LEAN     (integrable_const _).sub (hi.const_mul t)\n");
    emit("A4 LEAN   have h := integral_mono (hir.const_mul b) he tangent\n");
    emit("A4 LEAN   rw [integral_const_mul, integral_sub (integrable_const _) (hi.const_mul t),\n");
    emit("A4 LEAN       integral_const_mul, integral_const, measureReal_univ_eq_one, one_smul] at h\n");
    emit("A4 LEAN   have h' : (1:ℝ) ≤ 1+t*M-t*(∫ x, x ∂μ) := by\n");
    emit("A4 LEAN     linarith only [mul_le_mul_of_nonneg_left hm ht]\n");
    emit("A4 LEAN   exact (by simpa only [mul_one] using mul_le_mul_of_nonneg_left h' hb : b ≤ _).trans h\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.HamiltonianVariance\n");
    emit("A4 LEAN #print axioms YangMills.HamiltonianVariance.linkReplacement\n");
    emit("A4 LEAN #print axioms YangMills.HamiltonianVariance.intervalChoice\n");
    emit("A4 LEAN #print axioms YangMills.HamiltonianVariance.varianceFloor\n");
    emit("A4 LEAN #print axioms YangMills.HamiltonianVariance.trialKinetic\n");
    emit("A4 LEAN #print axioms YangMills.HamiltonianVariance.fourLinks\n");
    emit("A4 LEAN #print axioms YangMills.HamiltonianVariance.optimizedTrial\n");
    emit("A4 LEAN #print axioms YangMills.HamiltonianVariance.covarianceToEnergy\n");
    emit("A4 LEAN #print axioms YangMills.HamiltonianVariance.escapeToVariance\n");
    emit("A4 LEAN #print axioms YangMills.HamiltonianVariance.normalizedSpectralWitness\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
