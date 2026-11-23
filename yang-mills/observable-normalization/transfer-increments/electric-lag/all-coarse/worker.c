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
static int onmesh(int axis,const int *p,int l){
    return p[(axis+1)%3]%l==0 && p[(axis+2)%3]%l==0;
}
static int edgeid(int axis,const int *p,int L){
    return 3*((p[0]*L+p[1])*L+p[2])+axis;
}
static void face(const int *p,int a,int b,int L,int ids[4],int mesh[4],int l){
    int u[3]={p[0],p[1],p[2]},v[3]={p[0],p[1],p[2]};
    u[b]=(u[b]+1)%L;v[a]=(v[a]+1)%L;
    ids[0]=edgeid(a,p,L);ids[1]=edgeid(a,u,L);
    ids[2]=edgeid(b,p,L);ids[3]=edgeid(b,v,L);
    mesh[0]=onmesh(a,p,l);mesh[1]=onmesh(a,u,l);
    mesh[2]=onmesh(b,p,l);mesh[3]=onmesh(b,v,l);
}
#endif
static int verify_count(void){
#if ROLE == 0
    for(int l=2;l<=4;++l){
        int L=4*l;
        for(int x=0;x<L;++x)for(int y=0;y<L;++y)for(int z=0;z<L;++z){
            int p[3]={x,y,z};
            for(int a=0;a<3;++a)for(int b=a+1;b<3;++b){
                int ids[4],m[4];face(p,a,b,L,ids,m,l);
                if(m[0]+m[1]>1||m[2]+m[3]>1)return 0;
                /* Every face through the first private a-link is a candidate. */
                int u[3]={x,y,z},found=0;
                if(m[0])u[b]=(u[b]+1)%L;
                for(int c=0;c<3;++c)if(c!=a)for(int side=0;side<2;++side){
                    int q[3]={u[0],u[1],u[2]},other[4],dummy[4];
                    q[c]=(q[c]+L-side)%L;
                    face(q,a,c,L,other,dummy,l);
                    int hit=1;
                    for(int i=0;i<4;++i)if(!m[i]){
                        int seen=0;for(int j=0;j<4;++j)seen+=(ids[i]==other[j]);
                        if(seen!=1)hit=0;
                    }
                    found+=hit;
                }
                if(found!=1)return 0;
            }
        }
    }
#elif ROLE == 1
    /* A face changes at most one label on each of the touched segments. */
    for(int l=2;l<=8;++l)for(int place=0;place<l;++place)
    for(int initial=0;initial<=8;++initial)for(int delta=-1;delta<=1;++delta){
        if(initial+delta<0)continue;
        int recovered=-1;
        for(int j=0;j<l;++j){
            int value=(j==place)?initial+delta:initial;
            if(j!=place)recovered=value;
        }
        if(recovered!=initial)return 0;
    }
#else
    for(int e=4;e<=100;++e)for(int m=0;m<=2;++m)
    for(int occupied=0;occupied<=m;++occupied)
        if(e-occupied+4-m<e)return 0;
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
    emit("A4 LEAN namespace YangMills.CoarseResponse\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- A face can erase at most two occupied edges and contributes four\n");
    emit("A4 LEAN minus the number of mesh edges as private fundamental links. -/\n");
    emit("A4 LEAN theorem supportCount (E occupied mesh : ℤ) (ha : occupied ≤ mesh)\n");
    emit("A4 LEAN     (hm : mesh ≤ 2) : E ≤ E-occupied+(4-mesh) := by omega\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Difference of endpoint powers plus the remaining geometric sum,\n");
    emit("A4 LEAN without division by a spectral difference. -/\n");
    emit("A4 LEAN theorem telescopes (r t : ℝ) (n : ℕ) :\n");
    emit("A4 LEAN     (t-r)*(∑ j ∈ Finset.range n, t^j*r^(n-1-j))=t^n-r^n := by\n");
    emit("A4 LEAN   induction n with\n");
    emit("A4 LEAN   | zero => simp\n");
    emit("A4 LEAN   | succ n ih =>\n");
    emit("A4 LEAN     rw [Finset.sum_range_succ]\n");
    emit("A4 LEAN     have aux : (∑ j ∈ Finset.range n, t^j*r^(n+1-1-j)) =\n");
    emit("A4 LEAN         (∑ j ∈ Finset.range n, t^j*r^(n-1-j))*r := by\n");
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
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem derivativeSplit (t r l h : ℝ) :\n");
    emit("A4 LEAN     (t-l*r)*h=(t-r)*h+(1-l)*r*h := by ring\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem endpoints (T R Q : ℝ) (ht : 0 ≤ T) (hr : 0 ≤ R)\n");
    emit("A4 LEAN     (hT : T ≤ Q) (hR : R ≤ Q) : |T-R| ≤ Q := by\n");
    emit("A4 LEAN   rw [abs_le]; constructor <;> linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem squaredNorm (N u : ℝ) : (2*u)^2*N=4*N*u^2 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.CoarseResponse\n");
    emit("A4 LEAN #print axioms YangMills.CoarseResponse.supportCount\n");
    emit("A4 LEAN #print axioms YangMills.CoarseResponse.telescopes\n");
    emit("A4 LEAN #print axioms YangMills.CoarseResponse.derivativeSplit\n");
    emit("A4 LEAN #print axioms YangMills.CoarseResponse.endpoints\n");
    emit("A4 LEAN #print axioms YangMills.CoarseResponse.squaredNorm\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
