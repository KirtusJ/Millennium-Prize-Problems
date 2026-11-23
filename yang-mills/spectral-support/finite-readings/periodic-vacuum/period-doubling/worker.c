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
#if ROLE==0
    for(int w=0;w<=12;++w)for(int h=0;h<=8;++h)for(int b=0;b<=7;++b)
        if(w*(h*b-1)>h*(w*b))return 0;
#elif ROLE==1
    for(int x=0;x<=6;++x)for(int y=x;y<=6;++y)
        if(x*x*x*y*y>y*y*y*x*x)return 0;
#else
    for(int w=0;w<=8;++w)for(int a=0;a<=9;++a)for(int h=0;h<=4;++h)
        if((w<=h*3+a)!=(w-a<=h*3))return 0;
#endif
    return 1;
}
__attribute__((used,noreturn)) static void run(void) {
    if(!verify_count()){sys(60,2,0,0);__builtin_unreachable();}
#if ROLE == 0
    emit("A4 CHILD spectrum\n");
    emit("A4 LEAN import Mathlib.Data.Real.Basic\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.PeriodPair\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem doubledRow (w z : ℝ) : w^2*z=w*(w*z) := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem weightedBudget (w h k b : ℝ) (hw : 0 ≤ w) (hc : k ≤ h*b) :\n");
    emit("A4 LEAN     w*k ≤ h*(w*b) := by\n");
    emit("A4 LEAN   nlinarith only [mul_nonneg hw (sub_nonneg.mpr hc)]\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem comparePowers (x y : ℝ) (hx : 0 ≤ x) (hxy : x ≤ y) (l n : ℕ)\n");
    emit("A4 LEAN     (h : n ≤ l) :\n");
    emit("A4 LEAN     x^l*y^n ≤ y^l*x^n := by\n");
    emit("A4 LEAN   obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le h\n");
    emit("A4 LEAN   rw [pow_add, pow_add]\n");
    emit("A4 LEAN   have hk := pow_le_pow_left₀ hx hxy k\n");
    emit("A4 LEAN   nlinarith only [mul_nonneg (mul_nonneg (pow_nonneg hx n)\n");
    emit("A4 LEAN     (pow_nonneg (hx.trans hxy) n)) (sub_nonneg.mpr hk)]\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem massFloor (h m w tax : ℝ) (bound : w ≤ h*m+tax) :\n");
    emit("A4 LEAN     w-tax ≤ h*m := by linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.PeriodPair\n");
    emit("A4 LEAN #print axioms YangMills.PeriodPair.doubledRow\n");
    emit("A4 LEAN #print axioms YangMills.PeriodPair.weightedBudget\n");
    emit("A4 LEAN #print axioms YangMills.PeriodPair.comparePowers\n");
    emit("A4 LEAN #print axioms YangMills.PeriodPair.massFloor\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
