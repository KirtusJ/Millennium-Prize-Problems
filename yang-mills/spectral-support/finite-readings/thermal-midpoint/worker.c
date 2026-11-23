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
    for(int r=2;r<=14;++r)for(int y=1;y<=20;++y){
#if ROLE == 0
        if(2*(r+1)*y-(2*y*y-1)-(2*r+1)!=2*(y-1)*(r-y))return 0;
#elif ROLE == 1
        if(4*(y-1)*(r-y)>(r-1)*(r-1))return 0;
#else
        if(y>=r && (y-1)*(r-y)>0)return 0;
        if(2*y==1+r && 4*(y-1)*(r-y)!=(r-1)*(r-1))return 0;
#endif
    }
    return 1;
}
__attribute__((used,noreturn)) static void run(void) {
    if(!verify_count()){sys(60,2,0,0);__builtin_unreachable();}
#if ROLE == 0
    emit("A4 CHILD spectrum\n");
    emit("A4 LEAN import Mathlib.Data.Real.Basic\n");
    emit("A4 LEAN import Mathlib.Tactic.NormNum\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.ThermalMidpoint\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem cancelStatic (r s : ℝ) : 2*(r+1)*s-s-(2*r+1)*s=0 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem threeReadings (r y : ℝ) :\n");
    emit("A4 LEAN     2*(r+1)*y-(2*y^2-1)-(2*r+1)=2*(y-1)*(r-y) := by ring\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem peak (r y : ℝ) : 4*(y-1)*(r-y) ≤ (r-1)^2 := by\n");
    emit("A4 LEAN   nlinarith only [sq_nonneg (2*y-r-1)]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem above (r y : ℝ) (hy : 1 ≤ y) (hr : r ≤ y) :\n");
    emit("A4 LEAN     (y-1)*(r-y) ≤ 0 := mul_nonpos_of_nonneg_of_nonpos (sub_nonneg.mpr hy) (sub_nonpos.mpr hr)\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem midpointEquality (r : ℝ) :\n");
    emit("A4 LEAN     4*((1+r)/2-1)*(r-(1+r)/2)=(r-1)^2 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem offsetExample : 2*(5/4+1 : ℝ)*(17/16)-(2*(17/16 : ℝ)^2-1)-(2*(5/4 : ℝ)+1)>0 := by\n");
    emit("A4 LEAN   norm_num\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.ThermalMidpoint\n");
    emit("A4 LEAN #print axioms YangMills.ThermalMidpoint.threeReadings\n");
    emit("A4 LEAN #print axioms YangMills.ThermalMidpoint.cancelStatic\n");
    emit("A4 LEAN #print axioms YangMills.ThermalMidpoint.peak\n");
    emit("A4 LEAN #print axioms YangMills.ThermalMidpoint.above\n");
    emit("A4 LEAN #print axioms YangMills.ThermalMidpoint.midpointEquality\n");
    emit("A4 LEAN #print axioms YangMills.ThermalMidpoint.offsetExample\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
