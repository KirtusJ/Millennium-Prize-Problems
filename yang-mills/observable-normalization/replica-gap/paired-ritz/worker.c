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
    /* Every block is either a constant or [[2+eps,2-eps],[2-eps,2+eps]]/2.
       Scale the latter by 64. Its squared Frobenius loss is four. */
    int v[4]={65,63,63,65}, norm=0,loss=0;
    for(int i=0;i<4;++i){norm+=v[i]*v[i]; loss+=(v[i]-64)*(v[i]-64);}
    return loss==4 && 4096*loss<norm;
#elif ROLE == 1
    /* Prove b_i/B <= 1/3+1/16000 from sqrt(4+eps^2) <= 2+eps^2/4. */
    return (8193L-4096)*48000 <= (8193L+4096)*16003;
#else
    /* Schur test with all quantities converted to a common scale. */
    long unit=6144000;
    long cap=669*unit/2000, c=unit/3+unit/16000+unit/4096, w=unit/64;
    return cap>c && (cap-c)*(cap-w)>w*w;
#endif
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
    emit("A4 LEAN namespace YangMills.PairedRitz\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- A scalar Schur test majorizes the Rayleigh quotient on the split trial space. -/\n");
    emit("A4 LEAN theorem blockCap (a b t c y w : ℝ) (hy : y < t)\n");
    emit("A4 LEAN     (hg : w^2 ≤ (t-c)*(t-y)) :\n");
    emit("A4 LEAN     c*a^2+2*w*a*b+y*b^2 ≤ t*(a^2+b^2) := by\n");
    emit("A4 LEAN   have h := mul_le_mul_of_nonneg_right hg (sq_nonneg a)\n");
    emit("A4 LEAN   by_contra hn\n");
    emit("A4 LEAN   have hp := mul_pos (sub_pos.mpr hy) (sub_pos.mpr (lt_of_not_ge hn))\n");
    emit("A4 LEAN   nlinarith [sq_nonneg ((t-y)*b-w*a)]\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem rankTwo (s : ℝ) :\n");
    emit("A4 LEAN     (s-1)*3-(s+1)=2*(s-2) := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem thermalExampleSchur :\n");
    emit("A4 LEAN     (1/64:ℝ)^2 ≤ (669/2000-(1/3+1/16000+1/4096))*(669/2000-1/64) := by norm_num\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem ratioEnclosure :\n");
    emit("A4 LEAN     (333/1000:ℝ) ≤ 1/3-1/4096 ∧\n");
    emit("A4 LEAN     (669/2000)/(1-1/4096) ≤ 335/1000 := by constructor <;> norm_num\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.PairedRitz\n");
    emit("A4 LEAN #print axioms YangMills.PairedRitz.blockCap\n");
    emit("A4 LEAN #print axioms YangMills.PairedRitz.rankTwo\n");
    emit("A4 LEAN #print axioms YangMills.PairedRitz.thermalExampleSchur\n");
    emit("A4 LEAN #print axioms YangMills.PairedRitz.ratioEnclosure\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
