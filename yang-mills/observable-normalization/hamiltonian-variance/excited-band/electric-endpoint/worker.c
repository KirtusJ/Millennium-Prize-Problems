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
    emit("A4 LEAN import Mathlib.Analysis.SpecialFunctions.Integrals\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.ElectricEndpoint\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem varianceIdentity (u S : ℝ) :\n");
    emit("A4 LEAN     4*((1-S)-(1-u)^2)=4*(2*u-u^2-S) := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Keep the kinetic and potential energies in the same trial budget. -/\n");
    emit("A4 LEAN theorem jointBudget {K u g : ℝ} (hu : 0 ≤ u) (hg : 0 ≤ g)\n");
    emit("A4 LEAN     (budget : K+g*u ≤ 17*Real.sqrt g/8+3/16) :\n");
    emit("A4 LEAN     u*K ≤ 289/256+3*u/16 := by\n");
    emit("A4 LEAN   have h := mul_le_mul_of_nonneg_right budget hu\n");
    emit("A4 LEAN   have sq : (Real.sqrt g*u)^2=g*u^2 := by rw [mul_pow, Real.sq_sqrt hg]\n");
    emit("A4 LEAN   nlinarith only [h, sq, sq_nonneg (Real.sqrt g*u-17/16)]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem sphereLower {K S : ℝ} (hK : 0 ≤ K) (hS : 0 ≤ S)\n");
    emit("A4 LEAN     (sphere : 3-4*S ≤ 4*Real.sqrt (K*S)) : 9 ≤ (16*K+24)*S := by\n");
    emit("A4 LEAN   have h := Real.sq_sqrt (mul_nonneg hK hS)\n");
    emit("A4 LEAN   by_cases hs : 0 ≤ 3-4*S\n");
    emit("A4 LEAN   · have p := mul_nonneg (sub_nonneg.mpr sphere)\n");
    emit("A4 LEAN       (add_nonneg (mul_nonneg (show (0:ℝ) ≤ 4 by norm_num) (Real.sqrt_nonneg (K*S))) hs)\n");
    emit("A4 LEAN     nlinarith only [p,h,sq_nonneg S]\n");
    emit("A4 LEAN   · nlinarith [mul_nonneg hK hS]\n");
    emit("A4 LEAN \n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN theorem envelope (u : ℝ) : (2-u)*(289/256+27*u/16) ≤ 99/32 := by\n");
    emit("A4 LEAN   nlinarith only [sq_nonneg (864*u-575)]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem productBound {K u : ℝ} (hu : u ≤ 2)\n");
    emit("A4 LEAN     (joint : u*K ≤ 289/256+3*u/16) :\n");
    emit("A4 LEAN     (2*u-u^2)*(K+3/2) ≤ 99/32 := by\n");
    emit("A4 LEAN   have h := mul_le_mul_of_nonneg_left joint (sub_nonneg.mpr hu)\n");
    emit("A4 LEAN   linarith only [h,envelope u]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem normBound {K S u : ℝ} (hK : 0 ≤ K)\n");
    emit("A4 LEAN     (sphere : 9 ≤ (16*K+24)*S) (prod : (2*u-u^2)*(K+3/2) ≤ 99/32) :\n");
    emit("A4 LEAN     4*(2*u-u^2-S) ≤ 18*S := by\n");
    emit("A4 LEAN   by_contra hn\n");
    emit("A4 LEAN   have h := mul_pos (sub_pos.mpr (lt_of_not_ge hn))\n");
    emit("A4 LEAN     (show 0 < K+3/2 by linarith)\n");
    emit("A4 LEAN   nlinarith only [h,sphere,prod]\n");
    emit("A4 LEAN \n");
#elif ROLE == 2
    emit("A4 LEAN theorem endpoint {K S u g κ : ℝ} (hK : 0 ≤ K) (hS : 0 ≤ S)\n");
    emit("A4 LEAN     (hu : 0 ≤ u) (hu₂ : u ≤ 2) (hg : 0 ≤ g) (hκ : 0 ≤ κ)\n");
    emit("A4 LEAN     (budget : K+g*u ≤ 17*Real.sqrt g/8+3/16)\n");
    emit("A4 LEAN     (sphere : 3-4*S ≤ 4*Real.sqrt (K*S)) :\n");
    emit("A4 LEAN     κ/18*(4*(2*u-u^2-S)) ≤ (4*κ*S)/4 := by\n");
    emit("A4 LEAN   have hv := normBound hK (sphereLower hK hS sphere)\n");
    emit("A4 LEAN     (productBound hu₂ (jointBudget hu hg budget))\n");
    emit("A4 LEAN   nlinarith only [mul_nonneg hκ (sub_nonneg.mpr hv)]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem retainWeight {A D U M low band : ℝ} (ha : 0 < A) (hd : 0 < D)\n");
    emit("A4 LEAN     (hu : U=4*D/A) (first : A ≤ M) (lower : low ≤ M/4)\n");
    emit("A4 LEAN     (extraction : M ≤ low+D/U+U*band) : A^2/(8*D) ≤ band := by\n");
    emit("A4 LEAN   have u_pos : 0 < U := by rw [hu]; positivity\n");
    emit("A4 LEAN   have d_u : D/U=A/4 := by rw [hu]; field_simp; ring\n");
    emit("A4 LEAN   rw [d_u] at extraction\n");
    emit("A4 LEAN   have hb : A/2 ≤ U*band := by linarith only [lower,first,extraction]\n");
    emit("A4 LEAN   calc\n");
    emit("A4 LEAN     A^2/(8*D)=(A/2)/U := by rw [hu]; field_simp; ring\n");
    emit("A4 LEAN     _ ≤ band := (div_le_iff₀ u_pos).2 (by simpa [mul_comm] using hb)\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.ElectricEndpoint\n");
    emit("A4 LEAN #print axioms YangMills.ElectricEndpoint.varianceIdentity\n");
    emit("A4 LEAN #print axioms YangMills.ElectricEndpoint.jointBudget\n");
    emit("A4 LEAN #print axioms YangMills.ElectricEndpoint.sphereLower\n");
    emit("A4 LEAN #print axioms YangMills.ElectricEndpoint.envelope\n");
    emit("A4 LEAN #print axioms YangMills.ElectricEndpoint.productBound\n");
    emit("A4 LEAN #print axioms YangMills.ElectricEndpoint.normBound\n");
    emit("A4 LEAN #print axioms YangMills.ElectricEndpoint.endpoint\n");
    emit("A4 LEAN #print axioms YangMills.ElectricEndpoint.retainWeight\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
