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
typedef struct { int r, i, j, k; } Quaternion;
static Quaternion product(Quaternion a, Quaternion b) {
    return (Quaternion){a.r*b.r-a.i*b.i-a.j*b.j-a.k*b.k,
        a.r*b.i+a.i*b.r+a.j*b.k-a.k*b.j,
        a.r*b.j-a.i*b.k+a.j*b.r+a.k*b.i,
        a.r*b.k+a.i*b.j-a.j*b.i+a.k*b.r};
}
static Quaternion conjugate(Quaternion a) { return (Quaternion){a.r,-a.i,-a.j,-a.k}; }
static Quaternion word(int code) {
    int w[4]={0};
    int a=code/12, b=(a+1+code/4%3)%4;
    w[a]=code&1 ? 4 : -4;
    w[b]=code&2 ? 3 : -3;
    return (Quaternion){w[0],w[1],w[2],w[3]};
}
#elif ROLE == 1
static int abs_int(int a) { return a<0 ? -a : a; }
static int compose(int a,int b) {
    return ((a%3+(a<3 ? b%3 : 3-b%3))%3)+3*((a/3)^(b/3));
}
static int inverse(int a) { return a<3 ? (3-a)%3 : a; }
static int orbit(int a) { return a==0 ? 0 : (a<3 ? 1 : 2); }
static int check_partition(int code) {
    int counts[4][6]={{0}}, classes[4][3]={{0}}, total[6]={0}, ctotal[3]={0};
    for (int b=0; b<4; ++b) {
        const int rep[3]={0,1,3};
        int v=rep[code%3]; code/=3;
        for (int g=0; g<6; ++g) {
            int value=compose(compose(g,v),inverse(g));
            ++counts[b][value]; ++total[value];
            ++classes[b][orbit(value)]; ++ctotal[orbit(value)];
        }
    }
    int fine=0, coarse=0, classified=0;
    for (int b=0; b<4; ++b) {
        for (int g=0; g<6; ++g) {
            fine+=abs_int(4*counts[b][g]-total[g]);
            if (b%2==0) coarse+=abs_int(4*(counts[b][g]+counts[b+1][g])-2*total[g]);
        }
        for (int c=0;c<3;++c) classified+=abs_int(4*classes[b][c]-ctotal[c]);
    }
    require(fine==classified && coarse<=fine);
    return coarse<fine;
}
#endif

__attribute__((used,noreturn)) static void run(void) {
#if ROLE == 0
    int noncommuting=0;
    for (int i=0;i<48;++i) for (int j=0;j<48;++j) {
        Quaternion a=word(i),b=word(j),v=product(a,b),rev=product(b,a);
        int delta=product(a,conjugate(b)).r-v.r;
        require(delta==2*(a.i*b.i+a.j*b.j+a.k*b.k));
        require(product(a,conjugate(a)).r==25);
        if (v.i!=rev.i || v.j!=rev.j || v.k!=rev.k) ++noncommuting;
    }
    require(noncommuting>100);
    emit("A4 CHILD spectrum\nA4 LEAN 2304 rational quaternion pairs recover the shell dot product from traces\n");
#elif ROLE == 1
    int strict=0;
    for (int code=0; code<81; ++code) strict+=check_partition(code);
    require(strict>0 && strict<81);
    emit("A4 CHILD limit\nA4 LEAN 81 boundary laws preserve orbit TV and contract when exterior data are discarded\n");
#else
    /* Sum the second-order density term over six directions. Their first and
       second moments reproduce the sphere moments used in the radial proof. */
    for (int a=-2; a<=2; ++a) for (int b=-2; b<=2; ++b) for (int c=-2;c<=2;++c)
        for (int r=0;r<=4;++r) {
            int h[3]={a,b,c}, hh=a*a+b*b+c*c, x=r*r, linear=0, twice_second=0;
            for (int i=0;i<3;++i) for (int sign=-1;sign<=1;sign+=2) {
                int dot=sign*r*h[i];
                linear+=dot; twice_second+=3-hh-x+dot*dot;
            }
            require(linear==0 && twice_second==2*(hh-3)*(x-3));
        }
    emit("A4 LEAN 625 angular controls cancel the linear term and reproduce the radial score\n");
#endif
    emit("A4 FINISHED\n");
    finish(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
