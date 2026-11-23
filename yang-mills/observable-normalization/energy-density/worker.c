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
    emit("A4 LEAN namespace YangMills.EnergyDensity\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem coordinateCasimir (n : ℝ) :\n");
    emit("A4 LEAN     (((n+1)*(n+3)-n*(n+2))^2 = 2*((n+1)*(n+3)+n*(n+2))+3) ∧\n");
    emit("A4 LEAN     (((n-1)*(n+1)-n*(n+2))^2 = 2*((n-1)*(n+1)+n*(n+2))+3) := by\n");
    emit("A4 LEAN   constructor <;> ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem localDiagonal {κ lam B g S : ℝ} (hl : 0 ≤ lam)\n");
    emit("A4 LEAN     (hg : lam=κ*g) (hs : g*S ≤ 2*B) :\n");
    emit("A4 LEAN     (2*lam*(κ/4)^2*(16*B+9) = κ^2*lam*(2*B+9/8)) ∧\n");
    emit("A4 LEAN     κ*lam^2*S ≤ κ^2*lam*(2*B+9/8) := by\n");
    emit("A4 LEAN   constructor\n");
    emit("A4 LEAN   · ring\n");
    emit("A4 LEAN   · have h := mul_le_mul_of_nonneg_left hs (mul_nonneg (sq_nonneg κ) hl)\n");
    emit("A4 LEAN     have h' : κ*lam^2*S=κ^2*lam*(g*S) := by rw [hg]; ring\n");
    emit("A4 LEAN     nlinarith only [h,h',mul_nonneg (sq_nonneg κ) hl]\n");
    emit("A4 LEAN \n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN /-- The conserved constant mode converts the whole sum into squared spatial differences. -/\n");
    emit("A4 LEAN theorem zeroRowForm {ι : Type*} [Fintype ι] (K : ι → ι → ℝ) (w : ι → ℝ)\n");
    emit("A4 LEAN     (sym : ∀ i j, K i j=K j i) (row : ∀ i, ∑ j, K i j=0) :\n");
    emit("A4 LEAN     2*(∑ i, ∑ j, K i j*w i*w j) = -(∑ i, ∑ j, K i j*(w i-w j)^2) := by\n");
    emit("A4 LEAN   have diag : (∑ i, ∑ j, K i j*(w i)^2) = 0 := by\n");
    emit("A4 LEAN     simp only [← Finset.sum_mul,row,zero_mul,Finset.sum_const_zero]\n");
    emit("A4 LEAN   have other : (∑ i, ∑ j, K i j*(w j)^2) = 0 := by\n");
    emit("A4 LEAN     rw [Finset.sum_comm]\n");
    emit("A4 LEAN     convert diag using 1\n");
    emit("A4 LEAN     exact Finset.sum_congr rfl (fun i _ => Finset.sum_congr rfl (fun j _ => by rw [sym j i]))\n");
    emit("A4 LEAN   have eq (i j : ι) : K i j*(w i-w j)^2 =\n");
    emit("A4 LEAN       K i j*(w i)^2-2*(K i j*w i*w j)+K i j*(w j)^2 := by ring\n");
    emit("A4 LEAN   simp only [eq, Finset.sum_add_distrib, Finset.sum_sub_distrib, ← Finset.mul_sum,diag,other]\n");
    emit("A4 LEAN   ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem bareCoefficient {β b B κ lam : ℝ} (hβ : 1 ≤ β) (hb : 0 < b)\n");
    emit("A4 LEAN     (hk : κ=2/(β*b)) (hl : lam=β/b) (hB : B ≤ 5*β/2) :\n");
    emit("A4 LEAN     b^3*(κ^2*lam*(2*B+9/8)) ≤ 25 := by\n");
    emit("A4 LEAN   have hpos : 0 < β := by linarith\n");
    emit("A4 LEAN   have id : b^3*(κ^2*lam*(2*B+9/8))=(8*B+9/2)/β := by\n");
    emit("A4 LEAN     rw [hk,hl]\n");
    emit("A4 LEAN     field_simp\n");
    emit("A4 LEAN     ring\n");
    emit("A4 LEAN   rw [id]\n");
    emit("A4 LEAN   apply (div_le_iff₀ hpos).mpr\n");
    emit("A4 LEAN   linarith only [hB,hβ]\n");
    emit("A4 LEAN \n");
#elif ROLE == 2
    emit("A4 LEAN theorem filterPoint {s E : ℝ} (hs : 0 ≤ s) (he : 0 ≤ E) :\n");
    emit("A4 LEAN     0 ≤ (1-Real.exp (-s*E)) ∧ (1-Real.exp (-s*E)) ≤ 1 ∧\n");
    emit("A4 LEAN       (1-Real.exp (-s*E)) ≤ s*E := by\n");
    emit("A4 LEAN   have h := Real.exp_le_one_iff.mpr (mul_nonpos_of_nonpos_of_nonneg (neg_nonpos.mpr hs) he)\n");
    emit("A4 LEAN   have h' := Real.add_one_le_exp (-s*E)\n");
    emit("A4 LEAN   exact ⟨by linarith, by linarith only [Real.exp_pos (-s*E)],by linarith⟩\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem lowFilter {s E ε : ℝ} (hs : 0 ≤ s) (he : 0 ≤ E) (low : E ≤ ε) :\n");
    emit("A4 LEAN     (1-Real.exp (-s*E))^2 ≤ s^2*ε*E := by\n");
    emit("A4 LEAN   have h := filterPoint hs he\n");
    emit("A4 LEAN   have h2 := mul_self_le_mul_self h.1 h.2.2\n");
    emit("A4 LEAN   have h3 := mul_le_mul_of_nonneg_left low (mul_nonneg (sq_nonneg s) he)\n");
    emit("A4 LEAN   nlinarith only [h2,h3]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem highFilter {s E R : ℝ} (hs : 0 ≤ s) (hr : 0 < R) (high : R ≤ E) :\n");
    emit("A4 LEAN     (1-Real.exp (-s*E))^2 ≤ E/R := by\n");
    emit("A4 LEAN   have h := filterPoint hs (hr.le.trans high)\n");
    emit("A4 LEAN   have h2 := mul_self_le_mul_self h.1 h.2.1\n");
    emit("A4 LEAN   have : 1 ≤ E/R := (one_le_div hr).mpr high\n");
    emit("A4 LEAN   nlinarith only [this,h2]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Integrate a local spectral majorant using only the first moment. -/\n");
    emit("A4 LEAN theorem restrictedFilter (μ : Measure ℝ) {s c : ℝ} (A : Set ℝ) (hA : MeasurableSet A)\n");
    emit("A4 LEAN     (hc : 0 ≤ c) (supp : ∀ᵐ E ∂μ, 0 ≤ E) (h1 : Integrable (fun E : ℝ => E) μ)\n");
    emit("A4 LEAN     (hi : IntegrableOn (fun E : ℝ => (1-Real.exp (-s*E))^2) A μ)\n");
    emit("A4 LEAN     (bound : ∀ E ∈ A, 0 ≤ E → (1-Real.exp (-s*E))^2 ≤ c*E) :\n");
    emit("A4 LEAN     (∫ E in A, (1-Real.exp (-s*E))^2 ∂μ) ≤ c * ∫ E : ℝ, E ∂μ := by\n");
    emit("A4 LEAN   have hs := ae_restrict_of_ae supp (s := A)\n");
    emit("A4 LEAN   have hm := (ae_restrict_mem (μ := μ) hA).and hs\n");
    emit("A4 LEAN   have h := integral_mono_ae hi ((h1.const_mul c).restrict (s := A))\n");
    emit("A4 LEAN     (hm.mono fun x hx => bound x hx.1 hx.2)\n");
    emit("A4 LEAN   rw [integral_const_mul] at h\n");
    emit("A4 LEAN   exact h.trans (mul_le_mul_of_nonneg_left (setIntegral_le_integral h1 supp) hc)\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Uniform first moments bound the mass of both tails of the filtered measure. -/\n");
    emit("A4 LEAN theorem filteredTails (μ : Measure ℝ) {s ε R C : ℝ}\n");
    emit("A4 LEAN     (hs : 0 ≤ s) (he : 0 ≤ ε) (hr : 0 < R)\n");
    emit("A4 LEAN     (supp : ∀ᵐ E ∂μ, 0 ≤ E) (h1 : Integrable (fun E : ℝ => E) μ)\n");
    emit("A4 LEAN     (hi : Integrable (fun E : ℝ => (1-Real.exp (-s*E))^2) μ)\n");
    emit("A4 LEAN     (moment : (∫ E : ℝ, E ∂μ) ≤ C) :\n");
    emit("A4 LEAN     (∫ E in Set.Icc 0 ε, (1-Real.exp (-s*E))^2 ∂μ) ≤ s^2*ε*C ∧\n");
    emit("A4 LEAN     (∫ E in Set.Ici R, (1-Real.exp (-s*E))^2 ∂μ) ≤ C/R := by\n");
    emit("A4 LEAN   have lo := restrictedFilter μ (Set.Icc 0 ε) measurableSet_Icc\n");
    emit("A4 LEAN     (mul_nonneg (sq_nonneg s) he) supp h1 hi.integrableOn\n");
    emit("A4 LEAN     (fun E hE hpos => lowFilter hs hpos hE.2)\n");
    emit("A4 LEAN   have upper := restrictedFilter μ (Set.Ici R) measurableSet_Ici\n");
    emit("A4 LEAN     (inv_nonneg.mpr hr.le) supp h1 hi.integrableOn (fun E hE _ => by\n");
    emit("A4 LEAN       simpa only [div_eq_inv_mul] using highFilter hs hr hE)\n");
    emit("A4 LEAN   constructor\n");
    emit("A4 LEAN   · exact lo.trans (mul_le_mul_of_nonneg_left moment (mul_nonneg (sq_nonneg s) he))\n");
    emit("A4 LEAN   · rw [div_eq_inv_mul]\n");
    emit("A4 LEAN     exact upper.trans (mul_le_mul_of_nonneg_left moment (inv_nonneg.mpr hr.le))\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.EnergyDensity\n");
    emit("A4 LEAN #print axioms YangMills.EnergyDensity.coordinateCasimir\n");
    emit("A4 LEAN #print axioms YangMills.EnergyDensity.localDiagonal\n");
    emit("A4 LEAN #print axioms YangMills.EnergyDensity.zeroRowForm\n");
    emit("A4 LEAN #print axioms YangMills.EnergyDensity.bareCoefficient\n");
    emit("A4 LEAN #print axioms YangMills.EnergyDensity.filterPoint\n");
    emit("A4 LEAN #print axioms YangMills.EnergyDensity.lowFilter\n");
    emit("A4 LEAN #print axioms YangMills.EnergyDensity.highFilter\n");
    emit("A4 LEAN #print axioms YangMills.EnergyDensity.restrictedFilter\n");
    emit("A4 LEAN #print axioms YangMills.EnergyDensity.filteredTails\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
