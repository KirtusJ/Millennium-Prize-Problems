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
    emit("A4 LEAN open MeasureTheory Filter\n");
    emit("A4 LEAN namespace YangMills.ExcitedBand\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- s = E(1-x²), with y = sqrt s and k = sqrt K. -/\n");
    emit("A4 LEAN theorem scoreFloor {s y K k : ℝ} (hy : 0 ≤ y)\n");
    emit("A4 LEAN     (ys : y^2=s) (ks : k^2=K) (ysmall : y ≤ 1)\n");
    emit("A4 LEAN     (score : 3 ≤ 4*s + 4*k*y) :\n");
    emit("A4 LEAN     9 ≤ 32*s*(1+K) := by\n");
    emit("A4 LEAN   have h : 3 ≤ 4*y*(1+k) := by\n");
    emit("A4 LEAN     nlinarith only [score, ys, mul_le_mul_of_nonneg_left ysmall hy]\n");
    emit("A4 LEAN   have hs := mul_self_le_mul_self (by norm_num : (0:ℝ) ≤ 3) h\n");
    emit("A4 LEAN   nlinarith only [hs, mul_nonneg (sq_nonneg y) (sq_nonneg (k-1)),\n");
    emit("A4 LEAN     congrArg (fun v : ℝ => v*(1+K)) ys, congrArg (fun v : ℝ => y^2*v) ks]\n");
    emit("A4 LEAN \n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN /-- The indicator bound works on the entire real line. -/\n");
    emit("A4 LEAN theorem pointBand (x L U : ℝ) (hL : 0 ≤ L) (hU : 0 < U) :\n");
    emit("A4 LEAN     x ≤ L + x^2/U + (Set.Icc L U).indicator (fun _ => U) x := by\n");
    emit("A4 LEAN   by_cases hx : x ∈ Set.Icc L U\n");
    emit("A4 LEAN   · rw [Set.indicator_of_mem hx]\n");
    emit("A4 LEAN     linarith only [hx.2, div_nonneg (sq_nonneg x) hU.le, hL]\n");
    emit("A4 LEAN   · rw [Set.indicator_of_not_mem hx, add_zero]\n");
    emit("A4 LEAN     by_cases lo : x ≤ L\n");
    emit("A4 LEAN     · linarith only [lo, div_nonneg (sq_nonneg x) hU.le]\n");
    emit("A4 LEAN     · have hi : U < x := lt_of_not_ge (fun h => hx ⟨(lt_of_not_ge lo).le,h⟩)\n");
    emit("A4 LEAN       have hs : x ≤ x^2/U := (le_div_iff₀ hU).mpr (by\n");
    emit("A4 LEAN         nlinarith only [mul_nonneg (hU.le.trans hi.le) (sub_nonneg.mpr hi.le)])\n");
    emit("A4 LEAN       linarith only [hs,hL]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem momentWindow (μ : Measure ℝ) [IsFiniteMeasure μ] {L U : ℝ}\n");
    emit("A4 LEAN     (hL : 0 ≤ L) (hU : 0 < U) (h1 : Integrable (fun x : ℝ => x) μ)\n");
    emit("A4 LEAN     (h2 : Integrable (fun x : ℝ => x^2) μ) :\n");
    emit("A4 LEAN     (∫ x, x ∂μ) ≤ L*μ.real Set.univ + (∫ x : ℝ, x^2 ∂μ)/U\n");
    emit("A4 LEAN       + U*μ.real (Set.Icc L U) := by\n");
    emit("A4 LEAN   have ha := (integrable_const L (μ := μ)).add (h2.div_const U)\n");
    emit("A4 LEAN   have hb := (integrable_const U (μ := μ)).indicator (measurableSet_Icc (a := L) (b := U))\n");
    emit("A4 LEAN   have h := integral_mono h1 (ha.add hb) (fun x => pointBand x L U hL hU)\n");
    emit("A4 LEAN   have step := integral_add ha hb\n");
    emit("A4 LEAN   have step' := integral_add (integrable_const L (μ := μ)) (h2.div_const U)\n");
    emit("A4 LEAN   simp only [Pi.add_apply] at step step' h\n");
    emit("A4 LEAN   rw [step, step',\n");
    emit("A4 LEAN       integral_const, integral_div, integral_indicator_const _ measurableSet_Icc,\n");
    emit("A4 LEAN       smul_eq_mul, mul_comm (μ.real Set.univ) L] at h\n");
    emit("A4 LEAN   simpa only [smul_eq_mul, mul_comm (μ.real (Set.Icc L U)) U] using h\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem windowWeight {A L U V S W : ℝ} (hu : 0 < U)\n");
    emit("A4 LEAN     (moment : A ≤ L*V + S/U + U*W)\n");
    emit("A4 LEAN     (low : L*V ≤ A/4) (high : S/U ≤ A/4) : A/(2*U) ≤ W := by\n");
    emit("A4 LEAN   apply (div_le_iff₀ (by linarith : 0 < 2*U)).mpr\n");
    emit("A4 LEAN   linarith only [moment,low,high]\n");
    emit("A4 LEAN \n");
#elif ROLE == 2
    emit("A4 LEAN /-- Positive time differences test mass away from the entire zero eigenspace. -/\n");
    emit("A4 LEAN theorem differenceKernel {s t L U E : ℝ} (hs : 0 ≤ s) (ht : 0 ≤ t)\n");
    emit("A4 LEAN     (hl : 0 ≤ L) (he : E ∈ Set.Icc L U) :\n");
    emit("A4 LEAN     Real.exp (-t*U)*(1-Real.exp (-s*L))^2 ≤\n");
    emit("A4 LEAN       Real.exp (-t*E)*(1-Real.exp (-s*E))^2 := by\n");
    emit("A4 LEAN   have hb := Real.exp_le_exp.mpr (mul_le_mul_of_nonpos_left he.2 (neg_nonpos.mpr ht))\n");
    emit("A4 LEAN   have hc := Real.exp_le_exp.mpr (mul_le_mul_of_nonpos_left he.1 (neg_nonpos.mpr hs))\n");
    emit("A4 LEAN   have hp : 0 ≤ 1-Real.exp (-s*L) := by\n");
    emit("A4 LEAN     have := Real.exp_le_one_iff.mpr (mul_nonpos_of_nonpos_of_nonneg (neg_nonpos.mpr hs) hl)\n");
    emit("A4 LEAN     linarith\n");
    emit("A4 LEAN   exact mul_le_mul hb (by\n");
    emit("A4 LEAN     simpa only [← sq] using (mul_self_le_mul_self hp (sub_le_sub_left hc 1)))\n");
    emit("A4 LEAN     (sq_nonneg _) (Real.exp_pos _).le\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem integratedDifference (μ : Measure ℝ) [IsFiniteMeasure μ] {s t L U : ℝ}\n");
    emit("A4 LEAN     (hs : 0 ≤ s) (ht : 0 ≤ t) (hl : 0 ≤ L)\n");
    emit("A4 LEAN     (hi : Integrable (fun E : ℝ => Real.exp (-t*E)*(1-Real.exp (-s*E))^2) μ) :\n");
    emit("A4 LEAN     (Real.exp (-t*U)*(1-Real.exp (-s*L))^2)*μ.real (Set.Icc L U) ≤\n");
    emit("A4 LEAN       ∫ E : ℝ, Real.exp (-t*E)*(1-Real.exp (-s*E))^2 ∂μ := by\n");
    emit("A4 LEAN   have hw := setIntegral_ge_of_const_le (μ := μ) measurableSet_Icc\n");
    emit("A4 LEAN     (measure_ne_top μ (Set.Icc L U)) (fun E hE => differenceKernel hs ht hl hE) hi.integrableOn\n");
    emit("A4 LEAN   have up := setIntegral_le_integral (s := Set.Icc L U) hi (Eventually.of_forall\n");
    emit("A4 LEAN     fun E => mul_nonneg (Real.exp_pos _).le (sq_nonneg _))\n");
    emit("A4 LEAN   linarith only [hw,up]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.ExcitedBand\n");
    emit("A4 LEAN #print axioms YangMills.ExcitedBand.scoreFloor\n");
    emit("A4 LEAN #print axioms YangMills.ExcitedBand.pointBand\n");
    emit("A4 LEAN #print axioms YangMills.ExcitedBand.momentWindow\n");
    emit("A4 LEAN #print axioms YangMills.ExcitedBand.windowWeight\n");
    emit("A4 LEAN #print axioms YangMills.ExcitedBand.differenceKernel\n");
    emit("A4 LEAN #print axioms YangMills.ExcitedBand.integratedDifference\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
