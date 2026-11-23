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
#if ROLE == 0
static int inside(int x,int y,int l,int hole){
    return x>=0 && y>=0 && x<l && y<l && x+l*y!=hole;
}
static int count(int x,int y,int l,int hole){
    int v=inside(x,y,l,hole);
    return (inside(x-1,y,l,hole)!=v)+(inside(x+1,y,l,hole)!=v)
        +(inside(x,y-1,l,hole)!=v)+(inside(x,y+1,l,hole)!=v);
}
#elif ROLE == 1
static int ideal(int mask){
    for(int y=0;y<4;++y)for(int x=0;x<4;++x)if(mask&(1<<(4*y+x))){
        if(x && !(mask&(1<<(4*y+x-1))))return 0;
        if(y && !(mask&(1<<(4*y+x-4))))return 0;
    }
    return 1;
}
#endif
static int verify_count(void){
#if ROLE == 0
    for(int l=4;l<=10;++l){
        int outcomes[32],n=0,first=0;
        for(int a=0;a<l*l;++a)if(count(a%l,a/l,l,-1)==2){
            ++first;
            for(int y=-1;y<=l;++y)for(int x=-1;x<=l;++x){
                int d=count(x,y,l,a);
                if(d>2)return 0;
                if(d==2){
                    int b=x+l*y;
                    if(x<0||y<0||x>=l||y>=l||n>=32)return 0;
                    outcomes[n++]=(a==b)?0:1+(a<b?a*l*l+b:b*l*l+a);
                }
            }
        }
        int norm=0;
        for(int i=0;i<n;++i)for(int j=0;j<n;++j)norm+=outcomes[i]==outcomes[j];
        if(first!=4 || n!=24 || norm!=48)return 0;
    }
#elif ROLE == 1
    /* For size at most three all addable cells lie in the 4 by 4 box. */
    for(int m=0;m<(1<<16);++m){
        int bits=0;for(int v=m;v;v&=v-1)++bits;
        if(bits>3 || !ideal(m))continue;
        int excess=0;
        for(int i=0;i<16;++i)if(ideal(m^(1<<i)))excess+=(m&(1<<i))?-1:1;
        if(excess!=1)return 0;
        for(int i=0;i<16;++i)if(m&(1<<i))for(int j=0;j<16;++j)if(!(m&(1<<j))){
            int final=m^(1<<i)^(1<<j);
            if(ideal(final)&&ideal(m^(1<<i))!=ideal(m^(1<<j)))return 0;
        }
    }
#else
    long v[14]={1},expected=1;
    for(int n=1;n<=12;++n){
        long w[14]={0};
        for(int i=0;i<n;++i){
            w[i+1]+=v[i];
            if(i)w[i-1]+=4*i*v[i];
        }
        for(int i=0;i<=n;++i)v[i]=w[i];
        if(n%2){if(v[0])return 0;}
        else{expected*=4*(n-1);if(v[0]!=expected)return 0;}
    }
#endif
    return 1;
}
__attribute__((used,noreturn)) static void run(void) {
    if(!verify_count()){sys(60,2,0,0);__builtin_unreachable();}
#if ROLE == 0
    emit("A4 CHILD spectrum\n");
    emit("A4 LEAN import Mathlib.Data.Real.Basic\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.CornerSpectrum\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Moments of four additions/removals, with plaquette amplitude one fourth. -/\n");
    emit("A4 LEAN noncomputable def evenMoment : ℕ → ℝ\n");
    emit("A4 LEAN   | 0 => 1\n");
    emit("A4 LEAN   | n+1 => ((2*(n:ℝ)+1)/4) * evenMoment n\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem momentsDetermined (m : ℕ → ℝ) (h0 : m 0=1)\n");
    emit("A4 LEAN     (h : ∀ n : ℕ, m (n+1)=((2*(n:ℝ)+1)/4)*m n) :\n");
    emit("A4 LEAN     ∀ n, m n=evenMoment n := by\n");
    emit("A4 LEAN   intro n\n");
    emit("A4 LEAN   induction n with\n");
    emit("A4 LEAN   | zero => exact h0\n");
    emit("A4 LEAN   | succ n ih => rw [h, ih, evenMoment]\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem secondFourth : evenMoment 1 = 1/4 ∧ evenMoment 2 = 3/16 := by\n");
    emit("A4 LEAN   norm_num [evenMoment]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem twoStepWalks :\n");
    emit("A4 LEAN     ((4:ℝ)^2+6*2^2+8)/4^4 = 3/16 := by norm_num\n");
    emit("A4 LEAN /-- D applied to a power of W on the empty state, using [D,W]=4I. -/\n");
    emit("A4 LEAN theorem lowerPowers {V : Type*} [AddCommMonoid V] (W D : V →+ V) (v : ℕ → V)\n");
    emit("A4 LEAN     (step : ∀ n, D (v (n+1)) = W (D (v n)) + 4 • v n)\n");
    emit("A4 LEAN     (zero : D (v 0) = 0) (powers : ∀ n, W (v n) = v (n+1)) :\n");
    emit("A4 LEAN     ∀ n : ℕ, D (v (n+1)) = (n+1) • (4 • v n) := by\n");
    emit("A4 LEAN   intro n\n");
    emit("A4 LEAN   induction n with\n");
    emit("A4 LEAN   | zero => simp [step, zero]\n");
    emit("A4 LEAN   | succ n ih =>\n");
    emit("A4 LEAN     rw [step, ih, map_nsmul, map_nsmul, powers]\n");
    emit("A4 LEAN     exact (succ_nsmul _ _).symm\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Evaluation in the empty state converts the ladder identity into\n");
    emit("A4 LEAN the unscaled Gaussian moment recurrence. -/\n");
    emit("A4 LEAN theorem returnRecurrence {V : Type*} [AddCommMonoid V] (W D : V →+ V)\n");
    emit("A4 LEAN     (v : ℕ → V) (read : V →+ ℝ)\n");
    emit("A4 LEAN     (step : ∀ n, D (v (n+1)) = W (D (v n)) + 4 • v n)\n");
    emit("A4 LEAN     (zero : D (v 0) = 0) (powers : ∀ n, W (v n) = v (n+1))\n");
    emit("A4 LEAN     (empty : ∀ x, read (W x) = read (D x)) (n : ℕ) :\n");
    emit("A4 LEAN     read (v (n+2)) = 4*((n:ℝ)+1)*read (v n) := by\n");
    emit("A4 LEAN   rw [← powers (n+1), empty, lowerPowers W D v step zero powers n,\n");
    emit("A4 LEAN       map_nsmul, map_nsmul]\n");
    emit("A4 LEAN   simp only [nsmul_eq_mul, Nat.cast_add, Nat.cast_one, Nat.cast_ofNat]\n");
    emit("A4 LEAN   ring\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- A bound on the support of a positive measure bounds its moment ratio. -/\n");
    emit("A4 LEAN theorem supportRatio (v M s h : ℝ) (hv : 0 < v)\n");
    emit("A4 LEAN     (hs : M = s*v) (hb : M ≤ h^2*v) : s ≤ h^2 := by\n");
    emit("A4 LEAN   exact (le_of_mul_le_mul_right (hs ▸ hb) hv)\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.CornerSpectrum\n");
    emit("A4 LEAN #print axioms YangMills.CornerSpectrum.momentsDetermined\n");
    emit("A4 LEAN #print axioms YangMills.CornerSpectrum.secondFourth\n");
    emit("A4 LEAN #print axioms YangMills.CornerSpectrum.twoStepWalks\n");
    emit("A4 LEAN #print axioms YangMills.CornerSpectrum.supportRatio\n");
    emit("A4 LEAN #print axioms YangMills.CornerSpectrum.lowerPowers\n");
    emit("A4 LEAN #print axioms YangMills.CornerSpectrum.returnRecurrence\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
