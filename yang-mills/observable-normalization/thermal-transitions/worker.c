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
    emit("A4 LEAN import Mathlib.Data.Real.Basic\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN import Mathlib.Tactic.FieldSimp\n");
    emit("A4 LEAN import Mathlib.Tactic.Positivity\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.ThermalTransitions\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- A forward or backward geometric contribution has the same multiplier. -/\n");
    emit("A4 LEAN theorem geometricStep (v z : ℝ) :\n");
    emit("A4 LEAN     v*z - 2*v + v/z = (z+1/z-2)*v := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem positiveMultiplier (z : ℝ) (hz : 0 < z) :\n");
    emit("A4 LEAN     0 ≤ z+1/z-2 := by\n");
    emit("A4 LEAN   have h : z+1/z-2 = (z-1)^2/z := by field_simp [ne_of_gt hz]; ring\n");
    emit("A4 LEAN   rw [h]\n");
    emit("A4 LEAN   positivity\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem determinantPair (a b x y : ℝ) :\n");
    emit("A4 LEAN     (a+b)*(a*x^2+b*y^2)-(a*x+b*y)^2 = a*b*(x-y)^2 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem shiftedPair (a b x y : ℝ) :\n");
    emit("A4 LEAN     (a*x+b*y)*(a*x^3+b*y^3)-(a*x^2+b*y^2)^2 = a*b*x*y*(x-y)^2 := by ring\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem stationaryAndMoving (a b x : ℝ) :\n");
    emit("A4 LEAN     (a+b)*(b*x^2)-(b*x)^2 = a*b*x^2 ∧\n");
    emit("A4 LEAN     (b*x)*(b*x^3)-(b*x^2)^2 = 0 := by constructor <;> ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.ThermalTransitions\n");
    emit("A4 LEAN #print axioms YangMills.ThermalTransitions.geometricStep\n");
    emit("A4 LEAN #print axioms YangMills.ThermalTransitions.positiveMultiplier\n");
    emit("A4 LEAN #print axioms YangMills.ThermalTransitions.determinantPair\n");
    emit("A4 LEAN #print axioms YangMills.ThermalTransitions.shiftedPair\n");
    emit("A4 LEAN #print axioms YangMills.ThermalTransitions.stationaryAndMoving\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
