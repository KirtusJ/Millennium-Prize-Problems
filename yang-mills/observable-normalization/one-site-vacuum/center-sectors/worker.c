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
    for(int w=1;w<=8;++w)for(int v=1;v<=8;++v)
    for(int g=0;g<=6;++g)for(int f=0;f<=6;++f){
        int delta=w*g-v*f;
        if(delta*delta-(g-f)*(w*w*g-v*v*f)!=g*f*(w-v)*(w-v))return 0;
    }
#elif ROLE == 1
    /* On a 64-vertex meridian a short edge crossing either equator has
       both endpoints at least 8 edges from the nearer center. */
    for(int x=0;x<64;++x)for(int y=0;y<64;++y){
        int sx=(x>=16&&x<48),sy=(y>=16&&y<48);
        int d=x>y?x-y:y-x; if(d>32)d=64-d;
        int ax=x%32,ay=y%32;if(ax>16)ax=32-ax;if(ay>16)ay=32-ay;
        if(sx!=sy&&d<8&&(ax<8||ay<8))return 0;
    }
#else
    for(unsigned k=2;k<=3;++k)for(unsigned mask=1;mask<(1U<<k);++mask){
        int signed_sum=0;
        for(unsigned corner=0;corner<(1U<<k);++corner){
            int sign=1;
            for(unsigned i=0;i<k;++i)if((mask&corner)&(1U<<i))sign=-sign;
            signed_sum+=sign;
        }
        if(signed_sum)return 0;
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
    emit("A4 LEAN import Mathlib.Tactic.Positivity\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.CenterSectors\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Pairwise remainder from testing the kinetic equation with w²g. -/\n");
    emit("A4 LEAN theorem weightedPair (g f w v : ℝ) :\n");
    emit("A4 LEAN     (w*g-v*f)^2-(g-f)*(w^2*g-v^2*f) = g*f*(w-v)^2 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem absorbExterior (q t inside outside err : ℝ) (h : q*outside ≤ err*(inside+outside))\n");
    emit("A4 LEAN     (gap : t ≤ q-err) (pos : 0 ≤ outside) : t*outside ≤ err*inside := by\n");
    emit("A4 LEAN   nlinarith only [h, mul_nonneg (sub_nonneg.mpr gap) pos]\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Undoing the positive ground state when a sign is attached to it. -/\n");
    emit("A4 LEAN theorem signLoss (s t a b : ℝ) (hs : s^2=1) (ht : t^2=1) :\n");
    emit("A4 LEAN     a*b*(s-t)^2=2*a*b*(1-s*t) := by\n");
    emit("A4 LEAN   have eq : (s-t)^2 = 2*(1-s*t) := by nlinarith only [hs,ht]\n");
    emit("A4 LEAN   rw [eq]; ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Cancellation on a center-stable corner set after minorization. -/\n");
    emit("A4 LEAN theorem cornerLoss (absMass signedMass : ℝ) (hz : signedMass=0) :\n");
    emit("A4 LEAN     absMass^2-signedMass^2=absMass^2 := by rw [hz]; ring\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Recover a one-step separation from a separation of transfer powers. -/\n");
    emit("A4 LEAN theorem powerLoss (a b : ℝ) (hb : 0 ≤ b) (hab : b ≤ a) (ha : a ≤ 1) (n : ℕ) :\n");
    emit("A4 LEAN     a^n-b^n ≤ (n:ℝ)*(a-b) := by\n");
    emit("A4 LEAN   induction n with\n");
    emit("A4 LEAN   | zero => simp\n");
    emit("A4 LEAN   | succ n ih =>\n");
    emit("A4 LEAN     have cap : b^n ≤ 1 := pow_le_one₀ hb (hab.trans ha)\n");
    emit("A4 LEAN     have order : 0 ≤ a^n-b^n := sub_nonneg.mpr (pow_le_pow_left₀ hb hab n)\n");
    emit("A4 LEAN     have first := mul_nonneg (sub_nonneg.mpr ha) order\n");
    emit("A4 LEAN     have second := mul_nonneg (sub_nonneg.mpr hab) (sub_nonneg.mpr cap)\n");
    emit("A4 LEAN     rw [pow_succ, pow_succ, Nat.cast_succ]\n");
    emit("A4 LEAN     nlinarith only [first, second, ih]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.CenterSectors\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN #print axioms YangMills.CenterSectors.weightedPair\n");
    emit("A4 LEAN #print axioms YangMills.CenterSectors.absorbExterior\n");
    emit("A4 LEAN #print axioms YangMills.CenterSectors.signLoss\n");
    emit("A4 LEAN #print axioms YangMills.CenterSectors.cornerLoss\n");
    emit("A4 LEAN #print axioms YangMills.CenterSectors.powerLoss\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
