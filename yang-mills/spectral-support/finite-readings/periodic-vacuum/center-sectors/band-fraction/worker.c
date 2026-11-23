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
static int verify_count(void){
#if ROLE == 0
    for(int width=0;width<=40;width++)for(int x=0;x<=width;x++)
        if(2*x-width < -width || 2*x-width > width)return 0;
#elif ROLE == 1
    for(int x=-5;x<=5;x++)for(int y=-5;y<=5;y++)
        if(y*y!=x*x+y*y-x*x)return 0;
#else
    for(int x=-5;x<=5;x++)for(int y=-5;y<=5;y++)
        if(x*y<-(x<0?-x:x)*(y<0?-y:y))return 0;
#endif
    return 1;
}
__attribute__((used,noreturn)) static void run(void) {
    if(!verify_count()){sys(60,2,0,0);__builtin_unreachable();}
#if ROLE == 0
    emit("A4 CHILD spectrum\n");
    emit("A4 LEAN import Mathlib.Analysis.InnerProductSpace.Basic\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN import Mathlib.Tactic.NormNum\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.VacuumBand\n");
    emit("A4 LEAN open scoped RealInnerProductSpace\n");
    emit("A4 LEAN variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℝ H]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- A positive tail with a known upper endpoint can be centered at half its width. -/\n");
    emit("A4 LEAN theorem centeredTail (r ε : ℝ) (lower : 0 ≤ r) (upper : r ≤ ε) :\n");
    emit("A4 LEAN     |r - ε / 2| ≤ ε / 2 := by\n");
    emit("A4 LEAN   apply abs_le.mpr\n");
    emit("A4 LEAN   constructor <;> linarith\n");
    emit("A4 LEAN \n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN /-- Squared length after removal of the component along a unit trial vector. -/\n");
    emit("A4 LEAN theorem perpendicularSquare (f x : H) (unit : ⟪f,f⟫ = 1) :\n");
    emit("A4 LEAN     ‖x - ⟪f,x⟫ • f‖ ^ 2 = ‖x‖ ^ 2 - ⟪f,x⟫ ^ 2 := by\n");
    emit("A4 LEAN   rw [← real_inner_self_eq_norm_sq, ← real_inner_self_eq_norm_sq]\n");
    emit("A4 LEAN   simp only [inner_sub_left, inner_sub_right, real_inner_smul_left, real_inner_smul_right, unit]\n");
    emit("A4 LEAN   rw [real_inner_comm x f]\n");
    emit("A4 LEAN   ring\n");
    emit("A4 LEAN \n");
#elif ROLE == 2
    emit("A4 LEAN /-- Lower bound on a band direction's overlap using both perpendicular lengths. -/\n");
    emit("A4 LEAN theorem projectedDirection (f h x : H) (unit : ⟪f,f⟫ = 1) :\n");
    emit("A4 LEAN     ⟪f,h⟫ * ⟪f,x⟫ - ‖h-⟪f,h⟫ • f‖ * ‖x-⟪f,x⟫ • f‖ ≤ ⟪h,x⟫ := by\n");
    emit("A4 LEAN   have lower := (abs_le.mp (abs_real_inner_le_norm (h-⟪f,h⟫ • f) (x-⟪f,x⟫ • f))).1\n");
    emit("A4 LEAN   simp only [inner_sub_left, inner_sub_right, real_inner_smul_left, real_inner_smul_right,\n");
    emit("A4 LEAN     unit] at lower\n");
    emit("A4 LEAN   rw [real_inner_comm h f] at lower ⊢\n");
    emit("A4 LEAN   nlinarith only [lower]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem polynomialDegree : 2 * 6 + 2 * 18 + 4 ≤ 2 * 32 - 1 := by decide\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- A band whose weights decay more slowly preserves its share at positive lag. -/\n");
    emit("A4 LEAN theorem bandShareAtLag (w r wt rt k : ℝ) (hw : 0 ≤ w) (hr : 0 ≤ r)\n");
    emit("A4 LEAN     (inside : k*w ≤ wt) (outside : rt ≤ k*r) : w*rt ≤ wt*r := by\n");
    emit("A4 LEAN   calc\n");
    emit("A4 LEAN     w*rt ≤ w*(k*r) := mul_le_mul_of_nonneg_left outside hw\n");
    emit("A4 LEAN     _ = (k*w)*r := by ring\n");
    emit("A4 LEAN     _ ≤ wt*r := mul_le_mul_of_nonneg_right inside hr\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.VacuumBand\n");
    emit("A4 LEAN #print axioms YangMills.VacuumBand.centeredTail\n");
    emit("A4 LEAN #print axioms YangMills.VacuumBand.perpendicularSquare\n");
    emit("A4 LEAN #print axioms YangMills.VacuumBand.projectedDirection\n");
    emit("A4 LEAN #print axioms YangMills.VacuumBand.polynomialDegree\n");
    emit("A4 LEAN #print axioms YangMills.VacuumBand.bandShareAtLag\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
