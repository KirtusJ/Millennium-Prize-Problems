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
static int id(int L,int x,int y,int z){return (x%L*L+y%L)*L+z%L;}
static int edge(int L,int x,int y,int z,int a){return 3*id(L,x,y,z)+a;}
static void face(int L,int x,int y,int z,int i,int j,int e[4]) {
    e[0]=edge(L,x,y,z,i);
    e[1]=edge(L,x,y,z,j);
    e[2]=edge(L,x+(j==0),y+(j==1),z+(j==2),i);
    e[3]=edge(L,x+(i==0),y+(i==1),z+(i==2),j);
}
#endif
static int verify_count(void){
#if ROLE == 0
    for(int L=4;L<=10;L+=2) for(int a=0;a<3;++a) for(int b=a+1;b<3;++b){
        int base[4],self=0,single=0;
        face(L,0,0,0,a,b,base);
        for(int x=0;x<L;++x) for(int y=0;y<L;++y) for(int z=0;z<L;++z)
        for(int i=0;i<3;++i) for(int j=i+1;j<3;++j){
            int e[4],k=0;face(L,x,y,z,i,j,e);
            for(int s=0;s<4;++s) for(int t=0;t<4;++t) k+=(base[s]==e[t]);
            if(k==4) ++self;
            else if(k==1) ++single;
            else if(k!=0) return 0;
        }
        if(self!=1 || single!=12) return 0;
    }
#elif ROLE == 1
    for(int n=1;n<=16;++n){
        int total=0;
        for(int a=0;a<n;++a) for(int b=0;b<n;++b)
        for(int c=0;c<n;++c) for(int d=0;d<n;++d){
            if(a==b && b==c && c==d) total+=4;
            else if((a==b && c==d)||(a==c && b==d)||(a==d && b==c)) ++total;
        }
        if(total!=3*n*n+n) return 0;
    }
#else
    for(int a=1;a<=16;++a) for(int b=0;b<a;++b) for(int s=-20;s<=20;++s)
        if((2*a*s-a*a>2*b*s-b*b)!=(2*s>a+b)) return 0;
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
    emit("A4 LEAN import Mathlib.Tactic.FieldSimp\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.ElectricLag\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- The square characters have fourth moment four; distinct doubled\n");
    emit("A4 LEAN faces give three pairings. -/\n");
    emit("A4 LEAN theorem fourthCount (N : ℝ) : 4*N+3*N*(N-1)=3*N^2+N := by ring\n");
    emit("A4 LEAN theorem fourthNormalized (N : ℝ) (h : N ≠ 0) :\n");
    emit("A4 LEAN     (3*N^2+N)/N^2=3+1/N := by field_simp; ring\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- The likelihood comparison for two distinct normal shifts\n");
    emit("A4 LEAN changes sign at their midpoint. -/\n");
    emit("A4 LEAN theorem logDifference (a b s : ℝ) :\n");
    emit("A4 LEAN     (a*s-a^2/2)-(b*s-b^2/2)=(a-b)*(s-(a+b)/2) := by ring\n");
    emit("A4 LEAN theorem midpointTest (a b s : ℝ) (hab : b<a) :\n");
    emit("A4 LEAN     b*s-b^2/2 < a*s-a^2/2 ↔ (a+b)/2 < s := by\n");
    emit("A4 LEAN   rw [← sub_pos, logDifference]\n");
    emit("A4 LEAN   exact (mul_pos_iff_of_pos_left (sub_pos.mpr hab)).trans sub_pos\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Tilting the standard normal changes the mean while keeping the\n");
    emit("A4 LEAN quadratic part of its density the same. -/\n");
    emit("A4 LEAN theorem gaussianTilt (s h : ℝ) : -s^2/2+h*s-h^2/2=-(s-h)^2/2 := by ring\n");
    emit("A4 LEAN theorem informationMean (h : ℝ) : h*h-h^2/2=h^2/2 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.ElectricLag\n");
    emit("A4 LEAN #print axioms YangMills.ElectricLag.fourthCount\n");
    emit("A4 LEAN #print axioms YangMills.ElectricLag.fourthNormalized\n");
    emit("A4 LEAN #print axioms YangMills.ElectricLag.logDifference\n");
    emit("A4 LEAN #print axioms YangMills.ElectricLag.midpointTest\n");
    emit("A4 LEAN #print axioms YangMills.ElectricLag.gaussianTilt\n");
    emit("A4 LEAN #print axioms YangMills.ElectricLag.informationMean\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
