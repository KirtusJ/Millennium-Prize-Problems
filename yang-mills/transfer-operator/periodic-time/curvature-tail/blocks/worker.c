/* Exact finite controls. Each guest issues the next role through the shared runner. */
#ifndef ROLE
#error ROLE required
#endif
__attribute__((used)) static volatile int worker_role = ROLE + 1;

static long syscall3(long nr, long a, long b, long c) {
    long out;
    __asm__ volatile("syscall" : "=a"(out) : "a"(nr), "D"(a), "S"(b), "d"(c)
                     : "rcx", "r11", "memory");
    return out;
}

static __attribute__((noreturn)) void finish(int result) {
    syscall3(60, result, 0, 0);
    __builtin_unreachable();
}

static void require(int condition) {
    if (!condition) finish(1);
}

static void emit(const char *str) {
    int len = 0;
    while (str[len]) ++len;
    while (len > 0) {
        long wrote = syscall3(1, 1, (long)str, len);
        require(wrote > 0 && wrote <= len);
        str += wrote;
        len -= wrote;
    }
}

#if ROLE == 0
/* Three paths between two vertices. The first fixes the tree; the other
   two give an ordered pair of loops, subject to one common conjugation. */
static int mul(int a,int b) { return (a%3+(a<3?b%3:3-b%3))%3+3*((a/3)^(b/3)); }
static int inv(int a) { return a<3?(3-a)%3:a; }
static int rot(int g,int u) { return mul(mul(g,u),inv(g)); }
static int label(int a,int b,int c) {
    int best=36;
    for(int g=0;g<6;++g) {
        int code=6*rot(g,mul(b,inv(a)))+rot(g,mul(c,inv(a)));
        if(code<best) best=code;
    }
    return best;
}
#elif ROLE == 1
/* 48 times the potential solving the radius-one star Laplacian. */
static int source(int x,int a,int b) { return (x==a)-(x==b); }
static int potential(int x,int a,int b) {
    return 7*source(x,a,b)-source(x^1,a,b);
}
static int gram(int a,int b,int c,int d) {
    return potential(a,c,d)-potential(b,c,d);
}
#endif

__attribute__((used,noreturn)) static void run(void) {
#if ROLE == 0
    for(int a=0;a<6;++a) for(int b=0;b<6;++b) for(int c=0;c<6;++c) {
        int orbit=label(a,b,c);
        /* Generate every vertex-gauge transform from the tree-fixed tuple;
           compare full canonical labels for generator pairs of the groups. */
        for(int g=0;g<6;++g) for(int k=0;k<6;++k) {
            int x=mul(mul(g,a),inv(k)),y=mul(mul(g,b),inv(k)),z=mul(mul(g,c),inv(k));
            require(label(x,y,z)==orbit);
        }
    }
    require(label(0,3,3)!=label(0,3,4));
    emit("A4 CHILD spectrum\nA4 LEAN 7776 vertex gauge transforms preserve the joint two-loop orbit\n");
#elif ROLE == 1
    int count=0;
    for(int a=0;a<8;++a) for(int b=a+1;b<8;++b) if(a/2!=b/2) {
        for(int c=0;c<8;++c) for(int d=c+1;d<8;++d) if(c/2!=d/2) {
            int cross=gram(a,b,c,d);
            require(gram(a,b,a,b)==14 && cross==gram(c,d,a,b));
            require(a==c && b==d ? cross==14 : cross*cross<196);
            ++count;
        }
    }
    require(count==576 && gram(0,2,0,4)==7);
    emit("A4 CHILD limit\nA4 LEAN 576 two-face covariance minors checked with a shared-edge cross term\n");
#else
    int rotations=0, mean[3]={0}, moment[3][3]={{0}};
    for(int i=0;i<3;++i) for(int j=0;j<3;++j) if(i!=j) {
        int k=3-i-j, perm[3]={i,j,k};
        int parity=(j==(i+1)%3)?1:-1;
        for(int a=-1;a<=1;a+=2) for(int b=-1;b<=1;b+=2) {
            int sign[3]={a,b,a*b*parity}, x[3]={0};
            for(int l=0;l<3;++l) x[perm[l]]=sign[l]*(l+1);
            require(parity*sign[0]*sign[1]*sign[2]==1);
            for(int l=0;l<3;++l) {
                mean[l]+=x[l];
                for(int n=0;n<3;++n) moment[l][n]+=x[l]*x[n];
            }
            ++rotations;
        }
    }
    require(rotations==24);
    for(int i=0;i<3;++i) for(int j=0;j<3;++j)
        require(mean[i]==0 && moment[i][j]==(i==j?112:0));
    emit("A4 LEAN 24 proper color rotations cancel linear readings and preserve oriented volume\n");
#endif
    emit("A4 FINISHED\n");
    finish(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
