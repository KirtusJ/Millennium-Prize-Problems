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
    for(int w=-4;w<=4;++w)for(int x=-4;x<=4;++x)for(int y=-4;y<=4;++y)for(int z=-4;z<=4;++z)
        if(3*w*w-x*x-y*y-z*z!=4*w*w-(w*w+x*x+y*y+z*z))return 0;
#elif ROLE==1
    if(64*5-48*8+12*16-64!=64)return 0;
#else
    for(int x=0;x<=8;++x)for(int y=0;y<=x;++y)for(int z=0;z<=y;++z)
        if((x+y+z)-(x+y-z)!=2*z)return 0;
#endif
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
    emit("A4 LEAN namespace YangMills.TriadStep\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem isotropicTrace (w x y z : ℝ) (norm : w^2+x^2+y^2+z^2=1) :\n");
    emit("A4 LEAN     (w^2+x^2-y^2-z^2)+(w^2-x^2+y^2-z^2)+(w^2-x^2-y^2+z^2)=4*w^2-1 := by\n");
    emit("A4 LEAN   linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem tracelessMean (s : ℝ) (h : s=1/4) : 4*s-1=0 := by linarith\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem thirdMoment :\n");
    emit("A4 LEAN     64*(5/64 : ℝ)-48*(1/8 : ℝ)+12*(1/4 : ℝ)-1=1 := by norm_num\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem signedLogCubic (c2 c3 : ℝ) :\n");
    emit("A4 LEAN     (c2+c3/6)-(c2-c3/6)=c3/3 := by ring\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem signedMaximum (x y z : ℝ) :\n");
    emit("A4 LEAN     (x+y+z)-(x+y-z)=2*z := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.TriadStep\n");
    emit("A4 LEAN #print axioms YangMills.TriadStep.isotropicTrace\n");
    emit("A4 LEAN #print axioms YangMills.TriadStep.tracelessMean\n");
    emit("A4 LEAN #print axioms YangMills.TriadStep.thirdMoment\n");
    emit("A4 LEAN #print axioms YangMills.TriadStep.signedLogCubic\n");
    emit("A4 LEAN #print axioms YangMills.TriadStep.signedMaximum\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
