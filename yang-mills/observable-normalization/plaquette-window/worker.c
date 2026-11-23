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
/* Integer interval for I_n(6), in units of 10^-12, n=1,2. */
typedef unsigned long long U;
static U ceiling(U a,U b){return (a+b-1)/b;}
static void bessel6(int n,U *low,U *high){
    U a=n==1 ? 3000000000000ULL:4500000000000ULL;
    U b=a, sl=a, sh=a;
    for(int j=1;j<=20;++j){
        unsigned den=j*(j+n);
        a=9*a/den; b=ceiling(9*b,den);
        sl+=a; sh+=b;
    }
    *low=sl; *high=sh+b; /* Remaining ratios below one half. */
}
static int verify_count(void){
#if ROLE == 0
    U lo1, hi1, lo2, hi2;
    bessel6(1,&lo1,&hi1); bessel6(2,&lo2,&hi2);
    return (__uint128_t)1000000*hi2 < (__uint128_t)762727*lo1;
#elif ROLE == 1
    /* Each output tuple has at most two predecessors per link. */
    for(int i=0;i<5;++i) for(int j=0;j<5;++j)
    for(int k=0;k<5;++k) for(int l=0;l<5;++l){
        int out[4]={i,j,k,l}, count=0;
        for(int n=0;n<1296;++n){
            int ok=1, q=n;
            for(int a=0;a<4;++a){
                int d=q%6-out[a]; q/=6;
                if(d*d!=1) ok=0;
            }
            count+=ok;
        }
        if(count!=(1+(i>0))*(1+(j>0))*(1+(k>0))*(1+(l>0))) return 0;
    }
    return 1;
#else
    /* 1/39 + (38/39)(1/256+3/400) < 7376/200000 */
    return (1ULL*256*400+38*(400+3*256))*200000 < 7376ULL*39*256*400;
#endif
}
__attribute__((used,noreturn)) static void run(void) {
    if(!verify_count()){sys(60,2,0,0);__builtin_unreachable();}
#if ROLE == 0
    emit("A4 CHILD spectrum\n");
    emit("A4 LEAN import Mathlib.Data.Real.Basic\n");
    emit("A4 LEAN import Mathlib.Tactic.NormNum\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.PlaquetteWindow\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem longitudinalCap {h : ℝ} (ha : 0 ≤ h) (hb : h ≤ 762727/1000000) :\n");
    emit("A4 LEAN     7376/200000 ≤ 1-h^2-h/2 := by\n");
    emit("A4 LEAN   nlinarith [mul_nonneg (sub_nonneg.mpr hb) (show 0 ≤ 762727/1000000+h by linarith)]\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem inverseBudget : (16:ℝ)*(14/(8/25))^4 < 2^26 := by norm_num\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem weightWindow {a w : ℝ} (ha : a ≤ 1/256)\n");
    emit("A4 LEAN     (hd : 7376/200000 ≤ a+w+(1-a-w)/39) : 3/400 ≤ w := by linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem endpointCut : ((1-1/39)/(1+1/39) : ℝ) = 19/20 := by norm_num\n");
    emit("A4 LEAN end YangMills.PlaquetteWindow\n");
    emit("A4 LEAN #print axioms YangMills.PlaquetteWindow.longitudinalCap\n");
    emit("A4 LEAN #print axioms YangMills.PlaquetteWindow.inverseBudget\n");
    emit("A4 LEAN #print axioms YangMills.PlaquetteWindow.weightWindow\n");
    emit("A4 LEAN #print axioms YangMills.PlaquetteWindow.endpointCut\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
