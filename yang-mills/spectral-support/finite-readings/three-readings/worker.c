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
    for(int q=1;q<10;++q)for(int x=0;x<=10;++x){
#if ROLE == 0
        if(x*(x-q)>(x>q?10*(10-q):0))return 0;
#elif ROLE == 1
        for(int b=q+1;b<=10;++b)
            if((b-q)*(b-q)-(b-x)*(b-x)>(x>q?(b-q)*(b-q):0))return 0;
#else
        for(int a=0;a<=5;++a)for(int w=0;w<=5-a;++w)
            if(a*q*q+w*100-q*(a*q+w*10)!=10*(10-q)*w)return 0;
#endif
    }
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
    emit("A4 LEAN namespace YangMills.TailCertificate\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem lowEndpoint (x q : ℝ) (hx : 0 ≤ x) (hq : x ≤ q) :\n");
    emit("A4 LEAN     x*(x-q) ≤ 0 := mul_nonpos_of_nonneg_of_nonpos hx (sub_nonpos.mpr hq)\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem highEndpoint (x q : ℝ) (hx : x ≤ 1) (hq : q ≤ x) :\n");
    emit("A4 LEAN     x*(x-q) ≤ 1-q := by\n");
    emit("A4 LEAN   nlinarith only [mul_nonneg (sub_nonneg.mpr hx) (sub_nonneg.mpr hq), hx]\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem lowSquare (x q b : ℝ) (hx : x ≤ q) (hb : q ≤ b) :\n");
    emit("A4 LEAN     (b-q)^2-(b-x)^2 ≤ 0 := by\n");
    emit("A4 LEAN   nlinarith only [mul_nonneg (sub_nonneg.mpr hx) (show 0 ≤ (b-q)+(b-x) by linarith)]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem highSquare (x q b : ℝ) : (b-q)^2-(b-x)^2 ≤ (b-q)^2 := by\n");
    emit("A4 LEAN   linarith only [sq_nonneg (b-x)]\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem cornerMoments (a w q : ℝ) :\n");
    emit("A4 LEAN     (a*q^2+w)-q*(a*q+w)=(1-q)*w := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem twoPoint (q b w : ℝ) :\n");
    emit("A4 LEAN     (b-q)^2-(b^2-2*b*((1-w)*q+w*b)+((1-w)*q^2+w*b^2))=w*(b-q)^2 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.TailCertificate\n");
    emit("A4 LEAN #print axioms YangMills.TailCertificate.lowEndpoint\n");
    emit("A4 LEAN #print axioms YangMills.TailCertificate.highEndpoint\n");
    emit("A4 LEAN #print axioms YangMills.TailCertificate.lowSquare\n");
    emit("A4 LEAN #print axioms YangMills.TailCertificate.highSquare\n");
    emit("A4 LEAN #print axioms YangMills.TailCertificate.cornerMoments\n");
    emit("A4 LEAN #print axioms YangMills.TailCertificate.twoPoint\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
