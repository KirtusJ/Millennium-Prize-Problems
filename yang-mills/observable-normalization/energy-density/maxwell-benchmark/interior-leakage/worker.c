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
    /* Integer and half-integer momenta, represented in doubled units. */
#if ROLE == 0
    for (int k=1; k<=25; ++k) for (int r=1; r<=50; ++r) {
        if (2*r<=k) continue;
        int low = 2*r-k>k ? 2*r-k : k;
        int q = r<k ? k-r : r-k;
        if (r+q != low || r-q>k || q-r>k) return 0;
    }
#elif ROLE == 1
    for (int k=1; k<=21; ++k) for (int e=k+1; e<=90; ++e) {
        int s = e-k>k ? e-k : k;
        if ((k<s && 2*s<e+k) != (2*k<e && e<3*k)) return 0;
    }
#else
    /* k=2, e=5: doubled logarithmic-time slopes switch at 7/4, 7/2. */
    int t[3]={1,2,4}, winner[3]={0,1,2};
    for (int i=0; i<3; ++i) {
        int cost[3]={10*t[i],7+6*t[i],14+4*t[i]};
        for (int j=0; j<3; ++j)
            if (j!=winner[i] && cost[winner[i]]>=cost[j]) return 0;
    }
#endif
    return 1;
}
__attribute__((used,noreturn)) static void run(void) {
    if(!verify_count()){sys(60,2,0,0);__builtin_unreachable();}
#if ROLE == 0
    emit("A4 CHILD spectrum\n");
    emit("A4 LEAN import Mathlib.Data.Real.Basic\n");
    emit("A4 LEAN import Mathlib.Tactic.FieldSimp\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.NormNum\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.InteriorLeakage\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Fixing either leg within δ of r forces the energy above the one-leg threshold. -/\n");
    emit("A4 LEAN theorem oneLegFloor {k r p q δ : ℝ} (hδ : 0 ≤ δ) (hr : r-δ ≤ p)\n");
    emit("A4 LEAN     (hsum : k ≤ p+q) (hdif : p-q ≤ k) :\n");
    emit("A4 LEAN     max k (2*r-k) - 2*δ ≤ p+q := by\n");
    emit("A4 LEAN   rcases le_total k (2*r-k) with h | h\n");
    emit("A4 LEAN   · rw [max_eq_right h]\n");
    emit("A4 LEAN     linarith\n");
    emit("A4 LEAN   · rw [max_eq_left h]\n");
    emit("A4 LEAN     linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- The closure of the physical momentum triangle attains that floor. -/\n");
    emit("A4 LEAN theorem edgeAttains {k r : ℝ} (hk : 0 ≤ k) (hr : k < 2*r) :\n");
    emit("A4 LEAN     0 ≤ |k-r| ∧ k ≤ r+|k-r| ∧ abs (r - abs (k-r)) ≤ k ∧\n");
    emit("A4 LEAN     r+|k-r| = max k (2*r-k) := by\n");
    emit("A4 LEAN   refine ⟨abs_nonneg _, ?_, ?_, ?_⟩\n");
    emit("A4 LEAN   · linarith [le_abs_self (k-r)]\n");
    emit("A4 LEAN   · rw [abs_le]\n");
    emit("A4 LEAN     rcases le_total r k with h | h\n");
    emit("A4 LEAN     · rw [abs_of_nonneg (sub_nonneg.mpr h)]\n");
    emit("A4 LEAN       constructor <;> linarith\n");
    emit("A4 LEAN     · rw [abs_of_nonpos (sub_nonpos.mpr h)]\n");
    emit("A4 LEAN       constructor <;> linarith\n");
    emit("A4 LEAN   · rcases le_total r k with h | h\n");
    emit("A4 LEAN     · rw [abs_of_nonneg (sub_nonneg.mpr h), max_eq_left (by linarith)]\n");
    emit("A4 LEAN       ring\n");
    emit("A4 LEAN     · rw [abs_of_nonpos (sub_nonpos.mpr h), max_eq_right (by linarith)]\n");
    emit("A4 LEAN       ring\n");
    emit("A4 LEAN \n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN /-- A third affine cost beats both endpoint costs somewhere precisely when its\n");
    emit("A4 LEAN slope is strictly below their mean. Both transitions cost d to lose one leg. -/\n");
    emit("A4 LEAN theorem middlePhase {e s k d : ℝ} (he : s < e) (hk : k ≤ s) (hd : 0 < d) :\n");
    emit("A4 LEAN     (∃ t : ℝ, 0 < t ∧ d+t*s < t*e ∧ d+t*s < 2*d+t*k) ↔ 2*s < e+k := by\n");
    emit("A4 LEAN   constructor\n");
    emit("A4 LEAN   · rintro ⟨t, ht, h₁, h₂⟩\n");
    emit("A4 LEAN     by_contra h\n");
    emit("A4 LEAN     have hx := mul_nonneg ht.le (sub_nonneg.mpr (le_of_not_gt h))\n");
    emit("A4 LEAN     nlinarith\n");
    emit("A4 LEAN   · intro h\n");
    emit("A4 LEAN     have hden : 0 < e-k := by linarith\n");
    emit("A4 LEAN     refine ⟨2*d/(e-k), div_pos (by linarith) hden, ?_, ?_⟩\n");
    emit("A4 LEAN     all_goals\n");
    emit("A4 LEAN       field_simp [hden]\n");
    emit("A4 LEAN       apply (div_lt_div_iff_of_pos_right hden).mpr\n");
    emit("A4 LEAN       nlinarith [mul_pos hd (sub_pos.mpr h)]\n");
    emit("A4 LEAN \n");
#elif ROLE == 2
    emit("A4 LEAN /-- For the magnetic triangle the intermediate slope lies strictly between\n");
    emit("A4 LEAN the endpoint slopes and is exposed exactly in this momentum range. -/\n");
    emit("A4 LEAN theorem interiorRange {k e : ℝ} :\n");
    emit("A4 LEAN     (k < max k (e-k) ∧ 2*max k (e-k) < e+k) ↔\n");
    emit("A4 LEAN       2*k < e ∧ e < 3*k := by\n");
    emit("A4 LEAN   rcases le_total k (e-k) with h | h\n");
    emit("A4 LEAN   · rw [max_eq_right h]\n");
    emit("A4 LEAN     constructor <;> rintro ⟨h₁,h₂⟩ <;> constructor <;> linarith\n");
    emit("A4 LEAN   · rw [max_eq_left h]\n");
    emit("A4 LEAN     constructor <;> rintro ⟨h₁,h₂⟩ <;> constructor <;> linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.InteriorLeakage\n");
    emit("A4 LEAN #print axioms YangMills.InteriorLeakage.oneLegFloor\n");
    emit("A4 LEAN #print axioms YangMills.InteriorLeakage.edgeAttains\n");
    emit("A4 LEAN #print axioms YangMills.InteriorLeakage.middlePhase\n");
    emit("A4 LEAN #print axioms YangMills.InteriorLeakage.interiorRange\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
