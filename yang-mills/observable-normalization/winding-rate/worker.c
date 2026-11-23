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
/* Count eight-step continuations of an initial directed edge in Z^3. */
#define STEPS 8
static const int increment[6]={1,-1,32,-32,1024,-1024};
static int visited[STEPS+2];
static unsigned histogram[2*STEPS+1];
static void enumerate(int depth,int projection) {
    if(depth==STEPS){ ++histogram[projection+STEPS]; return; }
    for(int d=0;d<6;++d){
        int next=visited[depth+1]+increment[d], seen=0;
        for(int j=0;j<=depth+1;++j) if(visited[j]==next) seen=1;
        if(seen) continue;
        visited[depth+2]=next;
        enumerate(depth+1,projection+(d/2<=ROLE ? (d%2 ? -1:1):0));
    }
}
static __uint128_t power(unsigned a,unsigned n){
    __uint128_t r=1; while(n--) r*=a; return r;
}
static int verify_count(void){
    for(int incoming=0;incoming<6;++incoming){
        for(int j=0;j<=2*STEPS;++j) histogram[j]=0;
        visited[0]=-increment[incoming]; visited[1]=0;
        enumerate(0,0);
        unsigned total=0;
        __uint128_t tilted=0;
        for(int j=0;j<=2*STEPS;++j){
            total+=histogram[j];
            __uint128_t weight=power(9,j)*power(8,16-j);
            tilted+=weight*histogram[j];
        }
        if(total!=308981 || 10*tilted>=9*power(5,8)*power(9,8)*power(8,8)) return 0;
    }
    return 1;
}
__attribute__((used,noreturn)) static void run(void) {
    if(!verify_count()){sys(60,2,0,0);__builtin_unreachable();}
#if ROLE == 0
    emit("A4 CHILD spectrum\n");
    emit("A4 LEAN import Mathlib.Data.Real.Basic\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN import Mathlib.Tactic.NormNum\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.WindingRate\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem renewal (p s : ℝ) :\n");
    emit("A4 LEAN     (1-s*p+5*p^2)*(1+s*p)+(s^2-6)*p^2 =\n");
    emit("A4 LEAN       1-p^2+5*s*p^3 := by ring\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem denominator (p m c : ℝ) :\n");
    emit("A4 LEAN     1-2*(3+m*(c-1))*p+5*p^2 =\n");
    emit("A4 LEAN     (1-p)*(1-5*p)-2*m*p*(c-1) := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem strictGain (p m : ℝ) (hp : 0 < p) (hq : 5*p < 1) (hm : m ≤ 3) :\n");
    emit("A4 LEAN     m*(1-5*p) < 5*(1-p) := by\n");
    emit("A4 LEAN   have h := mul_le_mul_of_nonneg_right hm (by linarith : 0 ≤ 1-5*p)\n");
    emit("A4 LEAN   linarith\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem blockAllowance : (9/10:ℝ)*(101/100)^8 < 1 := by norm_num\n");
    emit("A4 LEAN theorem unweightedAllowance : (308981:ℝ)*(41/200)^8 < 1 := by norm_num\n");
    emit("A4 LEAN end YangMills.WindingRate\n");
    emit("A4 LEAN #print axioms YangMills.WindingRate.renewal\n");
    emit("A4 LEAN #print axioms YangMills.WindingRate.denominator\n");
    emit("A4 LEAN #print axioms YangMills.WindingRate.strictGain\n");
    emit("A4 LEAN #print axioms YangMills.WindingRate.blockAllowance\n");
    emit("A4 LEAN #print axioms YangMills.WindingRate.unweightedAllowance\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
