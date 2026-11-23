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
/* Exact row sweep of a doubly charged plane. States track the incoming
   vertical bond, horizontal cuts already used, and pairs of bends. */
#define SIDE (4+ROLE)
static unsigned dp[2][SIDE][1u<<SIDE][SIDE+1];
static unsigned choose(unsigned n,unsigned k){
    unsigned b=1;
    for(unsigned j=1;j<=k;++j) b=b*(n-j+1)/j;
    return b;
}
static int verify_count(void){
    const unsigned l=SIDE, full=(1u<<SIDE)-1;
    unsigned histogram[SIDE+1]={0};
    /* Fix the incoming bond in the first row at x=0; translate it later. */
    dp[0][0][0][0]=1;
    for(unsigned row=0;row<l;++row){
        unsigned cur=row%2,next=1-cur;
        for(unsigned a=0;a<l;++a) for(unsigned used=0;used<=full;++used)
          for(unsigned k=0;k<=l;++k) dp[next][a][used][k]=0;
        for(unsigned a=0;a<l;++a) for(unsigned b=0;b<l;++b){
            unsigned boundary=(1u<<a)^(1u<<b);
            for(unsigned mask=0;mask<=full;++mask){
                unsigned shifted=((mask<<1)&full)|(mask>>(l-1));
                if((mask^shifted)!=boundary) continue;
                for(unsigned used=0;used<=full;++used){
                    if(used&mask) continue;
                    for(unsigned k=0;k<=row;++k)
                        dp[next][b][used|mask][k+(a!=b)]+=dp[cur][a][used][k];
                }
            }
        }
    }
    /* l choices for the initial bond and l for the common z plane. */
    for(unsigned k=0;k<=l;++k) histogram[k]=l*l*dp[l%2][0][full][k];
    if(histogram[0]!=l*l*l || histogram[1]) return 0;
    unsigned rank=2*histogram[0]+l*l*l*(l-1);
    for(unsigned k=2;k<=l;++k){
        unsigned bin=choose(l-1,k-1);
        if(k*histogram[k]!=2*l*l*l*bin*bin) return 0;
        rank+=histogram[k];
    }
    return rank==l*l*choose(2*l,l)+l*l*l*(l-1);
}
__attribute__((used,noreturn)) static void run(void) {
    if(!verify_count()){sys(60,2,0,0);__builtin_unreachable();}
#if ROLE == 0
    emit("A4 CHILD spectrum\n");
    emit("A4 LEAN import Mathlib.Data.Nat.Choose.Basic\n");
    emit("A4 LEAN import Mathlib.Tactic.NormNum\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.WindingCount\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN def rank (l : ℕ) := l^2 * (2*l).choose l + l^3*(l-1)\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem sideFour : rank 4 = 1312 := by decide\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem sideFive : rank 5 = 6800 := by decide\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem sideSix : rank 6 = 34344 := by decide\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.WindingCount\n");
    emit("A4 LEAN #print axioms YangMills.WindingCount.sideFour\n");
    emit("A4 LEAN #print axioms YangMills.WindingCount.sideFive\n");
    emit("A4 LEAN #print axioms YangMills.WindingCount.sideSix\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
