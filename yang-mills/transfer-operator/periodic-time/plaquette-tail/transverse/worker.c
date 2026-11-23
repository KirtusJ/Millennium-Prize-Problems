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

/* The parallel faces span axes 0,1. Every transverse edge has four
   distinct side faces, each containing exactly one transverse axis. */
static unsigned char seen[7*7*2*2*6];
static int stored;
static void mark(int x,int y,int z,int w,int orientation) {
    int i=((((w*7+z)*2+y)*2+x)*6+orientation);
    require(i>=0 && i<(int)sizeof seen && !seen[i]);
    seen[i]=1; ++stored;
}

static int absval(int x) { return x<0 ? -x : x; }
static int exact_source(int r,int x,int y) {
    static const int small[2][2]={{19,3},{3,1}};
    static const int large[3][3]={{3763,515,83},{515,137,33},{83,33,11}};
    return r==1 ? small[absval(x)][absval(y)] : large[absval(x)][absval(y)];
}

/* Coefficients of 4cos(j*pi/5) in the basis 1,sqrt(5). */
static const int aa[]={4,1,-1,1,-1,-4}, bb[]={0,1,1,-1,-1,0};
static int equal_min, configurations;
static int nonnegative(int a,int b) {
    if (a>=0 && b>=0) return 1;
    if (a<=0 && b<=0) return a==0 && b==0;
    return a>0 ? a*a>=5*b*b : 5*b*b>=a*a;
}
static void angles(int n,int left,int a,int b) {
    if (!n) {
        if (left) return;
        /* Maximum cosine sum: one pi and five pi/5 = (1+5 sqrt(5))/4. */
        require(nonnegative(1-a,5-b));
        ++configurations;
        if (a==1 && b==5) ++equal_min;
        return;
    }
    for (int j=0;j<=5 && j<=left;++j)
        angles(n-1,left-j,a+aa[j],b+bb[j]);
}

__attribute__((used,noreturn)) static void run(void) {
#if ROLE==0
    for (int z=0;z<7;++z) for (int w=0;w<7;++w) {
        mark(0,0,z,w,0);
        for (int d=0;d<=1;++d) {
            if ((d ? w : z)==6) continue;
            for (int s=0;s<=1;++s) {
                mark(s,0,z,w,1+2*d);
                mark(0,s,z,w,2+2*d);
            }
        }
    }
    require(stored==49+4*84);
    emit("A4 CHILD spectrum\nA4 LEAN parallel squares and unique lateral faces on a transverse patch\n");
#elif ROLE==1
    for (int r=1;r<=2;++r) for (int x=-r;x<=r;++x) for (int y=-r;y<=r;++y) {
        int f=exact_source(r,x,y), a=4*f;
        for (int axis=0;axis<2;++axis) for (int sign=-1;sign<=1;sign+=2) {
            int i=x+(axis==0)*sign, j=y+(axis==1)*sign;
            if (absval(i)<=r && absval(j)<=r) a+=f-exact_source(r,i,j);
        }
        require(a==((x || y) ? 0 : 4*(r==1 ? 35 : 7011)));
    }
    emit("A4 CHILD limit\nA4 LEAN exact free-boundary capacity equations at radii one and two\n");
#else
    angles(6,10,0,0);
    require(equal_min==6 && configurations>1000);
    emit("A4 LEAN charged-cube minimum on the pi-over-five angle grid\n");
#endif
    emit("A4 FINISHED\n");
    finish(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
