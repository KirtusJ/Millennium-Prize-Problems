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
    for(int c=0;c<=9;++c)for(int z=1;z<=9;++z)for(int r=1;r<=9;++r)
        if((r*c)*z!=r*(c*z))return 0;
#elif ROLE == 1
    for(int x=0;x<=10;++x)for(int q=1;q<10;++q)
        if(x-q>(x>q?10-q:0))return 0;
#else
    if(4*4<=5*3 || 4*5*2!=5*8)return 0;
#endif
    return 1;
}
__attribute__((used,noreturn)) static void run(void) {
    if(!verify_count()){sys(60,2,0,0);__builtin_unreachable();}
#if ROLE == 0
    emit("A4 CHILD spectrum\n");
    emit("A4 LEAN import Mathlib.Data.Real.Basic\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.NormNum\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.OpenSlab\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem normalization (n z c r : ℝ) (hc : c*z=n) :\n");
    emit("A4 LEAN     (r*c)*z=r*n := by rw [mul_assoc,hc]\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem tail (low high total next q : ℝ) (h : total=low+high)\n");
    emit("A4 LEAN     (bound : next ≤ low+q*high) :\n");
    emit("A4 LEAN     next-q*total ≤ (1-q)*low := by rw [h]; linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem calibratedRatio (c k cmin kmin : ℝ) (hc : cmin ≤ c)\n");
    emit("A4 LEAN     (hk : kmin ≤ k) (hp : 0 ≤ cmin) (hk0 : 0 ≤ k) :\n");
    emit("A4 LEAN     cmin*kmin ≤ c*k := by\n");
    emit("A4 LEAN   calc\n");
    emit("A4 LEAN     cmin*kmin ≤ cmin*k := mul_le_mul_of_nonneg_left hk hp\n");
    emit("A4 LEAN     _ ≤ c*k := mul_le_mul_of_nonneg_right hc hk0\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem falseSignal : (4/5 : ℝ) > 3/4 := by norm_num\n");
    emit("A4 LEAN theorem correctedSignal : (4/5 : ℝ)*(5/8)=1/2 := by norm_num\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.OpenSlab\n");
    emit("A4 LEAN #print axioms YangMills.OpenSlab.normalization\n");
    emit("A4 LEAN #print axioms YangMills.OpenSlab.tail\n");
    emit("A4 LEAN #print axioms YangMills.OpenSlab.calibratedRatio\n");
    emit("A4 LEAN #print axioms YangMills.OpenSlab.falseSignal\n");
    emit("A4 LEAN #print axioms YangMills.OpenSlab.correctedSignal\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
