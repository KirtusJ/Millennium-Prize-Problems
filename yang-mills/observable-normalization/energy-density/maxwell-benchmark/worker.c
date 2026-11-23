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
    emit("A4 LEAN import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN open Real Set MeasureTheory\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.MaxwellEnergy\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- The electric and magnetic amplitudes exchange the two polarizations. -/\n");
    emit("A4 LEAN theorem mixing (a b c : ℝ) :\n");
    emit("A4 LEAN     (a+b*c)^2+(a*c+b)^2 =\n");
    emit("A4 LEAN     ((a+b)/2)^2*(2*(1+c)^2)+((a-b)/2)^2*(2*(1-c)^2) := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- The inverse signs distinguish the total energy and the scalar. -/\n");
    emit("A4 LEAN theorem angleFactors {r s Q c : ℝ} (hr : 0 < r) (hs : 0 < s)\n");
    emit("A4 LEAN     (momentum : Q^2=r^2+s^2+2*r*s*c) :\n");
    emit("A4 LEAN     1+c=(Q^2-(r-s)^2)/(2*r*s) ∧\n");
    emit("A4 LEAN     1-c=((r+s)^2-Q^2)/(2*r*s) := by\n");
    emit("A4 LEAN   constructor <;> field_simp <;> nlinarith only [momentum]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem flatBandIntegral (q : ℝ) :\n");
    emit("A4 LEAN     (∫ z in -q..q, (q^2-z^2)^2) = 16*q^5/15 := by\n");
    emit("A4 LEAN   let G := fun x : ℝ => q^4*x - 2*q^2*x^3/3 + x^5/5\n");
    emit("A4 LEAN   have hd (x : ℝ) : HasDerivAt G ((q^2-x^2)^2) x := by\n");
    emit("A4 LEAN     unfold G\n");
    emit("A4 LEAN     convert (((hasDerivAt_id x).const_mul (q^4)).sub\n");
    emit("A4 LEAN       (((hasDerivAt_pow 3 x).const_mul (2*q^2)).div_const 3)).add\n");
    emit("A4 LEAN       ((hasDerivAt_pow 5 x).div_const 5) using 1\n");
    emit("A4 LEAN     simp\n");
    emit("A4 LEAN     ring\n");
    emit("A4 LEAN   rw [intervalIntegral.integral_eq_sub_of_hasDerivAt (fun x _ => hd x)\n");
    emit("A4 LEAN     ((by fun_prop : Continuous (fun z : ℝ => (q^2-z^2)^2)).intervalIntegrable _ _)]\n");
    emit("A4 LEAN   dsimp [G]\n");
    emit("A4 LEAN   ring\n");
    emit("A4 LEAN \n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN /-- Two-photon spectral densities after the difference of the photon\n");
    emit("A4 LEAN energies has been integrated out. The same Fourier convention is used in both. -/\n");
    emit("A4 LEAN theorem totalDensity {q : ℝ} (hq : 0 < q) :\n");
    emit("A4 LEAN     (∫ z in -q..q, (q^2-z^2)^2)/(128*π^2*q) = q^4/(120*π^2) := by\n");
    emit("A4 LEAN   rw [flatBandIntegral]\n");
    emit("A4 LEAN   field_simp\n");
    emit("A4 LEAN   ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem scalarDensity {q : ℝ} (hq : 0 < q) (E : ℝ) :\n");
    emit("A4 LEAN     (∫ _z in -q..q, (E^2-q^2)^2)/(128*π^2*q) = (E^2-q^2)^2/(64*π^2) := by\n");
    emit("A4 LEAN   rw [intervalIntegral.integral_const]\n");
    emit("A4 LEAN   simp only [smul_eq_mul]\n");
    emit("A4 LEAN   field_simp\n");
    emit("A4 LEAN   ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem thresholdLaplace {t : ℝ} (ht : 0 < t) (q : ℝ) :\n");
    emit("A4 LEAN     (∫ E : ℝ in Ioi q, exp (-t*E)) = exp (-t*q)/t := by\n");
    emit("A4 LEAN   rw [integral_exp_mul_Ioi (neg_lt_zero.mpr ht)]\n");
    emit("A4 LEAN   ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem scalarPolynomial (q y : ℝ) :\n");
    emit("A4 LEAN     ((q+y)^2-q^2)^2=y^4+4*q*y^3+4*q^2*y^2 := by ring\n");
    emit("A4 LEAN \n");
#elif ROLE == 2
    emit("A4 LEAN /-- At fixed momentum, the three positive readings retain at least one third. -/\n");
    emit("A4 LEAN theorem detectorFraction {a : ℝ} (ha : 0 ≤ a) (hb : a ≤ 1) :\n");
    emit("A4 LEAN     1/3 ≤ 1-a+a^2/3 ∧ 1-a+a^2/3 ≤ 1 := by\n");
    emit("A4 LEAN   constructor\n");
    emit("A4 LEAN   · nlinarith [mul_nonneg (sub_nonneg.mpr hb) (show 0 ≤ 2-a by linarith)]\n");
    emit("A4 LEAN   · nlinarith [mul_nonneg ha (sub_nonneg.mpr hb)]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Two different scalar coefficients at two clocks identify the two squared\n");
    emit("A4 LEAN mixing amplitudes from the rescaled covariance. -/\n");
    emit("A4 LEAN theorem twoClocks {T U g h : ℝ} (distinct : g ≠ h) :\n");
    emit("A4 LEAN     ((T+g*U)-(T+h*U))/(g-h)=U ∧\n");
    emit("A4 LEAN     (g*(T+h*U)-h*(T+g*U))/(g-h)=T := by\n");
    emit("A4 LEAN   have hn : g-h ≠ 0 := sub_ne_zero.mpr distinct\n");
    emit("A4 LEAN   constructor <;> field_simp <;> ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem strictClock {x y q : ℝ} (hy : 0 < y) (hxy : y < x) (hq : 0 ≤ q) :\n");
    emit("A4 LEAN     3*y^4+3*q*y^3+q^2*y^2 < 3*x^4+3*q*x^3+q^2*x^2 := by\n");
    emit("A4 LEAN   have h₂ := pow_lt_pow_left₀ hxy hy.le (by decide : (2:ℕ) ≠ 0)\n");
    emit("A4 LEAN   have h₃ := pow_lt_pow_left₀ hxy hy.le (by decide : (3:ℕ) ≠ 0)\n");
    emit("A4 LEAN   have h₄ := pow_lt_pow_left₀ hxy hy.le (by decide : (4:ℕ) ≠ 0)\n");
    emit("A4 LEAN   nlinarith [mul_nonneg hq (sub_nonneg.mpr h₃.le),\n");
    emit("A4 LEAN     mul_nonneg (sq_nonneg q) (sub_nonneg.mpr h₂.le)]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.MaxwellEnergy\n");
    emit("A4 LEAN #print axioms YangMills.MaxwellEnergy.mixing\n");
    emit("A4 LEAN #print axioms YangMills.MaxwellEnergy.angleFactors\n");
    emit("A4 LEAN #print axioms YangMills.MaxwellEnergy.flatBandIntegral\n");
    emit("A4 LEAN #print axioms YangMills.MaxwellEnergy.totalDensity\n");
    emit("A4 LEAN #print axioms YangMills.MaxwellEnergy.scalarDensity\n");
    emit("A4 LEAN #print axioms YangMills.MaxwellEnergy.thresholdLaplace\n");
    emit("A4 LEAN #print axioms YangMills.MaxwellEnergy.scalarPolynomial\n");
    emit("A4 LEAN #print axioms YangMills.MaxwellEnergy.detectorFraction\n");
    emit("A4 LEAN #print axioms YangMills.MaxwellEnergy.twoClocks\n");
    emit("A4 LEAN #print axioms YangMills.MaxwellEnergy.strictClock\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
