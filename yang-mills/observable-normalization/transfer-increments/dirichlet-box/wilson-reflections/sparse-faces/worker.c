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
static int verify_count(void) {
#if ROLE == 0
    /* Each reflected tile's central face and all four cubes avoid its boundary. */
    for (int mask=0; mask<16; ++mask) {
        for (int axis=0; axis<4; ++axis) {
            int tangent=axis<2, reflected=(mask>>axis)&1;
            int lo=tangent ? 1 : 2, hi=lo+tangent;
            int left=reflected ? 4-hi : lo, right=reflected ? 4-lo : hi;
            if (left-!tangent<1 || right+!tangent>3) return 0;
        }
    }
#elif ROLE == 1
    /* Face (i,j) encoded by its axis mask and base vertex in a 5^4 cell. */
    int faces[21], used=0, stride[4]={1,5,25,125};
    int center=1+5+2*25+2*125;
    for (int k=2; k<4; ++k) for (int side=0; side<2; ++side) {
        int base=center-side*stride[k], axes[3]={0,1,k};
        for (int skip=0; skip<3; ++skip) for (int end=0; end<2; ++end) {
            int omitted=axes[skip], mask=(3|(1<<k))^(1<<omitted);
            int pos=base+end*stride[omitted];
            if (pos==center && mask==3) continue;
            int id=16*pos+mask;
            for (int j=0;j<used;++j) if (id==faces[j]) return 0;
            if (used>=20) return 0;
            faces[used++]=id;
        }
    }
    if (used!=20) return 0;
#else
    for (int L=8; L<=128; L*=2) {
        int blocks=L/4, copies=1;
        for (int j=0;j<4;++j) copies*=blocks;
        if (256LL*copies!=1LL*L*L*L*L) return 0;
    }
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
    emit("A4 LEAN namespace YangMills.SparseFaces\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Cauchy for the chord lengths of the five complementary faces. -/\n");
    emit("A4 LEAN theorem fiveChord (a b c d e : ℝ) :\n");
    emit("A4 LEAN     (a+b+c+d+e)^2 ≤ 5*(a^2+b^2+c^2+d^2+e^2) := by\n");
    emit("A4 LEAN   nlinarith only [sq_nonneg (a-b), sq_nonneg (a-c), sq_nonneg (a-d),\n");
    emit("A4 LEAN     sq_nonneg (a-e), sq_nonneg (b-c), sq_nonneg (b-d), sq_nonneg (b-e),\n");
    emit("A4 LEAN     sq_nonneg (c-d), sq_nonneg (c-e), sq_nonneg (d-e)]\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Each of four complementary disks pays one fifth of the central deficit. -/\n");
    emit("A4 LEAN theorem cubeBudget (s A B C D : ℝ) (ha : s ≤ 5*A) (hb : s ≤ 5*B)\n");
    emit("A4 LEAN     (hc : s ≤ 5*C) (hd : s ≤ 5*D) :\n");
    emit("A4 LEAN     9*s ≤ 5*(s+A+B+C+D) := by linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem pressureReserve (S P l : ℝ) (hl : 0 ≤ l) (h : 9*P ≤ 5*S) :\n");
    emit("A4 LEAN     (1-5*l/9)*S ≤ S-l*P := by\n");
    emit("A4 LEAN   nlinarith only [mul_nonneg hl (sub_nonneg.mpr h)]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem positiveReserve (l : ℝ) (h : l < 9/5) : 0 < 1-5*l/9 := by\n");
    emit("A4 LEAN   linarith\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem endpointSlack : (1 : ℝ) < 3/2 ∧ (3/2 : ℝ) < 9/5 := by\n");
    emit("A4 LEAN   constructor <;> linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem densityExponent : (4:ℕ)^4*9=2*1152 := by decide\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.SparseFaces\n");
    emit("A4 LEAN #print axioms YangMills.SparseFaces.fiveChord\n");
    emit("A4 LEAN #print axioms YangMills.SparseFaces.cubeBudget\n");
    emit("A4 LEAN #print axioms YangMills.SparseFaces.pressureReserve\n");
    emit("A4 LEAN #print axioms YangMills.SparseFaces.positiveReserve\n");
    emit("A4 LEAN #print axioms YangMills.SparseFaces.endpointSlack\n");
    emit("A4 LEAN #print axioms YangMills.SparseFaces.densityExponent\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
