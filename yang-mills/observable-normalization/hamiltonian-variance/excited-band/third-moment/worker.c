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
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN open MeasureTheory Filter\n");
    emit("A4 LEAN namespace YangMills.CubicMoment\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem kineticDouble {d p r a : ℝ} (h : r ≤ a) (h' : p ≤ a)\n");
    emit("A4 LEAN     (term : ℝ) (ht : term ≤ r + d + 2*p) : term ≤ 3*a+d := by\n");
    emit("A4 LEAN   linarith only [ht,h,h']\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem localThird {κ B lam S C M : ℝ} (hk : 0 ≤ κ) (hb : 0 ≤ B) (hc : 0 ≤ C)\n");
    emit("A4 LEAN     (magnetic : lam*S ≤ 2*κ*B)\n");
    emit("A4 LEAN     (form : M ≤ κ^2/8*(κ/4*C*(1+16*B)+6144*lam*S)) :\n");
    emit("A4 LEAN     M ≤ (C+1536)*κ^3*(1+B) := by\n");
    emit("A4 LEAN   have h := mul_le_mul_of_nonneg_left magnetic (sq_nonneg κ)\n");
    emit("A4 LEAN   nlinarith only [form,h,mul_nonneg (pow_nonneg hk 3) hc,\n");
    emit("A4 LEAN     mul_nonneg (mul_nonneg (pow_nonneg hk 3) hc) hb, pow_nonneg hk 3]\n");
    emit("A4 LEAN \n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN /-- Nonnegative energy makes the weighted square nonnegative. -/\n");
    emit("A4 LEAN theorem momentInterpolation (μ : Measure ℝ) (hs : ∀ᵐ x ∂μ, 0 ≤ x)\n");
    emit("A4 LEAN     (h1 : Integrable (fun x : ℝ => x) μ) (h2 : Integrable (fun x : ℝ => x^2) μ)\n");
    emit("A4 LEAN     (h3 : Integrable (fun x : ℝ => x^3) μ)\n");
    emit("A4 LEAN     (a b c : ℝ) (ha : a=∫ x : ℝ, x ∂μ) (hb : b=∫ x : ℝ, x^2 ∂μ)\n");
    emit("A4 LEAN     (hc : c=∫ x : ℝ, x^3 ∂μ) (pos : 0 < a) :\n");
    emit("A4 LEAN     b^2 ≤ a*c := by\n");
    emit("A4 LEAN   have eq (x : ℝ) : x*(a*x-b)^2 = a^2*x^3-(2*a*b)*x^2+b^2*x := by ring\n");
    emit("A4 LEAN   have hp : 0 ≤ ∫ x : ℝ, x*(a*x-b)^2 ∂μ :=\n");
    emit("A4 LEAN     integral_nonneg_of_ae (hs.mono fun x hx => mul_nonneg hx (sq_nonneg _))\n");
    emit("A4 LEAN   simp only [eq] at hp\n");
    emit("A4 LEAN   have addstep := integral_add ((h3.const_mul (a^2)).sub (h2.const_mul (2*a*b))) (h1.const_mul (b^2))\n");
    emit("A4 LEAN   have substep := integral_sub (h3.const_mul (a^2)) (h2.const_mul (2*a*b))\n");
    emit("A4 LEAN   simp only [Pi.sub_apply] at addstep\n");
    emit("A4 LEAN   rw [addstep,substep, integral_const_mul,\n");
    emit("A4 LEAN     integral_const_mul, integral_const_mul, ← ha, ← hb, ← hc] at hp\n");
    emit("A4 LEAN   apply (le_of_mul_le_mul_left (a := a) (by nlinarith only [hp]) pos)\n");
    emit("A4 LEAN \n");
#elif ROLE == 2
    emit("A4 LEAN theorem smallLoss {S B : ℝ} (hS : S ≤ 1) (hb : 0 ≤ B) (hB : B ≤ 1) :\n");
    emit("A4 LEAN     S*(1+B) ≤ 18 := by\n");
    emit("A4 LEAN   nlinarith only [hS,hB,mul_le_mul_of_nonneg_right hS hb]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem largeLoss {S B u : ℝ} (hu : 1 ≤ u) (hS : 0 ≤ S)\n");
    emit("A4 LEAN     (hB : B ≤ 5*u/2) (loss : S*u^2 ≤ 2*B) : S*(1+B) ≤ 18 := by\n");
    emit("A4 LEAN   have hu' : 0 < u := by linarith only [hu]\n");
    emit("A4 LEAN   have hsu : S*u ≤ 5 := le_of_mul_le_mul_right\n");
    emit("A4 LEAN     (a := u) (by nlinarith only [hB,loss]) hu'\n");
    emit("A4 LEAN   have hb' : 1+B ≤ 7*u/2 := by linarith only [hu,hB]\n");
    emit("A4 LEAN   nlinarith only [mul_le_mul_of_nonneg_left hb' hS, hsu]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem uniformSecond {M₁ M₂ M₃ C κ S B : ℝ} (hc : 0 ≤ C) (hk : 0 ≤ κ)\n");
    emit("A4 LEAN     (hm : M₁=4*κ*S) (hS : 0 ≤ S) (h3 : M₃ ≤ C*κ^3*(1+B))\n");
    emit("A4 LEAN     (hi : M₂^2 ≤ M₁*M₃) (h : S*(1+B) ≤ 18) :\n");
    emit("A4 LEAN     M₂^2 ≤ 72*C*κ^4 := by\n");
    emit("A4 LEAN   rw [hm] at hi\n");
    emit("A4 LEAN   have hp : 0 ≤ 4*κ*S := mul_nonneg (by linarith only [hk]) hS\n");
    emit("A4 LEAN   have hx := mul_le_mul_of_nonneg_left h (mul_nonneg hc (pow_nonneg hk 4))\n");
    emit("A4 LEAN   nlinarith only [hi,mul_le_mul_of_nonneg_left h3 hp,hx]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem numericCeiling {M κ : ℝ} (h : M^2 ≤ 72*((72*1200^2+1)+1536)*κ^4) :\n");
    emit("A4 LEAN     M ≤ 86401*κ^2 := by\n");
    emit("A4 LEAN   by_contra! bad\n");
    emit("A4 LEAN   have hs := mul_self_lt_mul_self (a := 86401*κ^2)\n");
    emit("A4 LEAN     (mul_nonneg (by norm_num) (sq_nonneg κ)) bad\n");
    emit("A4 LEAN   nlinarith only [hs,h,sq_nonneg (κ^2)]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.CubicMoment\n");
    emit("A4 LEAN #print axioms YangMills.CubicMoment.kineticDouble\n");
    emit("A4 LEAN #print axioms YangMills.CubicMoment.localThird\n");
    emit("A4 LEAN #print axioms YangMills.CubicMoment.momentInterpolation\n");
    emit("A4 LEAN #print axioms YangMills.CubicMoment.smallLoss\n");
    emit("A4 LEAN #print axioms YangMills.CubicMoment.largeLoss\n");
    emit("A4 LEAN #print axioms YangMills.CubicMoment.uniformSecond\n");
    emit("A4 LEAN #print axioms YangMills.CubicMoment.numericCeiling\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
