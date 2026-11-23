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
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN import Mathlib.Tactic.NormNum\n");
    emit("A4 LEAN namespace YangMills.BlockVariance\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN noncomputable def pureStep (x : ℝ) := (1-x)/3\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Three orthogonal pure directions acting on a unit quaternion. -/\n");
    emit("A4 LEAN theorem oneAxisAverage {a b c d : ℝ} (unit : a^2+b^2+c^2+d^2=1) :\n");
    emit("A4 LEAN     ((-b)^2+(-c)^2+(-d)^2)/3 = pureStep (a^2) := by\n");
    emit("A4 LEAN   unfold pureStep\n");
    emit("A4 LEAN   linarith only [unit]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem twoAxes (x : ℝ) : pureStep (pureStep x) = (2+x)/9 := by\n");
    emit("A4 LEAN   unfold pureStep\n");
    emit("A4 LEAN   ring\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem traceSquareFloor (a : ℝ) :\n");
    emit("A4 LEAN     8/9 ≤ 4 * pureStep (pureStep (a^2)) := by\n");
    emit("A4 LEAN   rw [twoAxes]\n");
    emit("A4 LEAN   linarith only [sq_nonneg a]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Two independent evaluations along a fair sign yield the Walsh energy identity. -/\n");
    emit("A4 LEAN theorem splitSign (plus minus : ℝ) :\n");
    emit("A4 LEAN     (plus^2+minus^2)/2 = ((plus+minus)/2)^2+((plus-minus)/2)^2 := by ring\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Assemble a conditional bound from an independent color carrying a fraction of the weights. -/\n");
    emit("A4 LEAN theorem assemble {total block cond variance c : ℝ}\n");
    emit("A4 LEAN     (color : total ≤ 11*block) (cost : 0 ≤ c)\n");
    emit("A4 LEAN     (localBound : c*block ≤ cond) (varianceBound : cond ≤ variance) :\n");
    emit("A4 LEAN     (c/11)*total ≤ variance := by\n");
    emit("A4 LEAN   have h := mul_le_mul_of_nonneg_left color cost\n");
    emit("A4 LEAN   linarith only [h,localBound,varianceBound]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Cost of a shift on the good-score event after scaling the angular step. -/\n");
    emit("A4 LEAN theorem localCost {b u : ℝ} (h₁ : b*u ≤ 1/4) (h₂ : b^2*u^2 ≤ 1/16) :\n");
    emit("A4 LEAN     12*b*u + 12*b^2*u^2 ≤ 15/4 := by\n");
    emit("A4 LEAN   linarith only [h₁,h₂]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.BlockVariance\n");
    emit("A4 LEAN #print axioms YangMills.BlockVariance.oneAxisAverage\n");
    emit("A4 LEAN #print axioms YangMills.BlockVariance.twoAxes\n");
    emit("A4 LEAN #print axioms YangMills.BlockVariance.traceSquareFloor\n");
    emit("A4 LEAN #print axioms YangMills.BlockVariance.splitSign\n");
    emit("A4 LEAN #print axioms YangMills.BlockVariance.assemble\n");
    emit("A4 LEAN #print axioms YangMills.BlockVariance.localCost\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
