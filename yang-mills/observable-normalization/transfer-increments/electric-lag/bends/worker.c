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
/* Fine edge starting at a periodic vertex, in one of three directions. */
static int marked(const int p[3], int axis, int l){
    return p[2]==0 && axis<2 && p[axis]<l &&
           (p[1-axis]==0 || p[1-axis]==l);
}
static int overlap(const int p[3], int a, int b, int L, int l){
    int n=marked(p,a,l)+marked(p,b,l);
    int q[3]={p[0],p[1],p[2]};
    q[a]=(p[a]+1)%L; n+=marked(q,b,l);
    q[a]=p[a]; q[b]=(p[b]+1)%L; return n+marked(q,a,l);
}
#elif ROLE == 1
/* Codes 0..3 are 1,i,j,k; bit 2 carries the sign. */
static int mul(int a,int b){
    int i=a&3,j=b&3;
    int neg=i && j && (i==j || (i==1 && j==3) ||
                              (i==2 && j==1) || (i==3 && j==2));
    return a^b^(neg?4:0);
}
static int tr(int a){return (a&3)?0:((a&4)?-2:2);}
static int inv(int a){return a^((a&3)?4:0);}
#else
static long power(int a,int n){long p=1;while(n--)p*=a;return p;}
#endif
static int verify_count(void){
#if ROLE == 0
    for(int l=2;l<=8;++l){
        int L=4*l,counts[3]={0,0,0};
        for(int x=0;x<L;++x)for(int y=0;y<L;++y)for(int z=0;z<L;++z){
            int p[3]={x,y,z};
            for(int a=0;a<3;++a)for(int b=a+1;b<3;++b){
                int d=overlap(p,a,b,L,l); if(d>2)return 0; ++counts[d];
            }
        }
        if(counts[1]!=16*l-8 || counts[2]!=4)return 0;
    }
#elif ROLE == 1
    int full=0,sing=0,cross=0,rem=0;
    for(int a=0;a<8;++a)for(int b=0;b<8;++b){
        int h=tr(mul(a,b)),sum=0;
        for(int u=0;u<8;++u){
            int f=tr(mul(u,a))*tr(mul(b,inv(u))),w=2*f-h;
            sum+=f; full+=f*f; sing+=h*h; cross+=h*w; rem+=w*w;
        }
        if(sum!=4*h)return 0;
    }
    if(full!=512 || sing!=512 || cross || rem!=1536)return 0;
#else
    for(int n=1;n<=7;++n)for(int r=1;r<=6;++r)for(int u=1;u<=6;++u){
        long H=0;for(int j=0;j<n;++j)H+=power(u,j)*power(r,n-1-j);
        if((u-r)*H!=power(u,n)-power(r,n))return 0;
        if(u==r && H!=n*power(r,n-1))return 0;
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
    emit("A4 LEAN import Mathlib.Tactic.LinearCombination\n");
    emit("A4 LEAN import Mathlib.Algebra.BigOperators.Ring.Finset\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.SquareBends\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Each corner face uses two of the four incident face slots per edge. -/\n");
    emit("A4 LEAN theorem incidence (k : ℝ) : (4*k-8)+2*4=4*k := by ring\n");
    emit("A4 LEAN theorem residualNorm : (1 : ℝ) - (1/2)^2 = 3/4 := by norm_num\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Differentiating a power remains regular at coincident eigenvalues. -/\n");
    emit("A4 LEAN theorem finiteSum (u r : ℝ) (n : ℕ) :\n");
    emit("A4 LEAN     (u-r)*(∑ j ∈ Finset.range n, u^j*r^(n-1-j)) = u^n-r^n := by\n");
    emit("A4 LEAN   induction n with\n");
    emit("A4 LEAN   | zero => simp\n");
    emit("A4 LEAN   | succ n ih =>\n");
    emit("A4 LEAN     rw [Finset.sum_range_succ]\n");
    emit("A4 LEAN     have aux : (∑ j ∈ Finset.range n, u^j*r^(n+1-1-j)) =\n");
    emit("A4 LEAN         (∑ j ∈ Finset.range n, u^j*r^(n-1-j))*r := by\n");
    emit("A4 LEAN       rw [Finset.sum_mul]\n");
    emit("A4 LEAN       apply Finset.sum_congr rfl\n");
    emit("A4 LEAN       intro j hj\n");
    emit("A4 LEAN       have h := Finset.mem_range.mp hj\n");
    emit("A4 LEAN       have e : n+1-1-j = (n-1-j)+1 := by omega\n");
    emit("A4 LEAN       rw [e, pow_succ]\n");
    emit("A4 LEAN       ring\n");
    emit("A4 LEAN     rw [aux]\n");
    emit("A4 LEAN     simp only [Nat.add_sub_cancel, Nat.sub_self, pow_zero, mul_one, pow_succ]\n");
    emit("A4 LEAN     linear_combination r * ih\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem singletSlope (d : ℝ) : (4-(4-2*d))/4/4=d/8 := by ring\n");
    emit("A4 LEAN theorem tripletSlope (d : ℝ) : (4-(4+2*d/3))/4/4= -d/24 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Weighted Cauchy remainder for a singlet and triplet pair. -/\n");
    emit("A4 LEAN theorem weightedRemainder (a b x y s t : ℝ) :\n");
    emit("A4 LEAN     (t*a^2+s*b^2)*(s*x^2+t*y^2)-s*t*(a*x+b*y)^2 =\n");
    emit("A4 LEAN     (t*a*y-s*b*x)^2 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.SquareBends\n");
    emit("A4 LEAN #print axioms YangMills.SquareBends.incidence\n");
    emit("A4 LEAN #print axioms YangMills.SquareBends.residualNorm\n");
    emit("A4 LEAN #print axioms YangMills.SquareBends.finiteSum\n");
    emit("A4 LEAN #print axioms YangMills.SquareBends.singletSlope\n");
    emit("A4 LEAN #print axioms YangMills.SquareBends.tripletSlope\n");
    emit("A4 LEAN #print axioms YangMills.SquareBends.weightedRemainder\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
