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

/* Signed basis units 1,i,j,k of Q8. */
static int mult(int a, int b) {
    static const int m[4][4] = {
        {1,2,3,4}, {2,-1,4,-3}, {3,-4,-1,2}, {4,3,-2,-1}
    };
    int s = 1;
    if (a < 0) { a = -a; s = -s; }
    if (b < 0) { b = -b; s = -s; }
    return s * m[a-1][b-1];
}
static int inv(int a) { return a == 1 || a == -1 ? a : -a; }
static int cube(int a) { return a*a*a; }

__attribute__((used,noreturn)) static void run(void) {
#if ROLE == 0
    for (int L=2; L<=32; ++L) {
        int side = cube(L+1)-cube(L-1);
        int vertices = (L+1)*cube(L+1)-(L-1)*cube(L-1);
        int edges = cube(L+1)-1 + L*side + cube(L-1);
        require(edges+1 == vertices);
    }
    emit("A4 CHILD spectrum\nA4 LEAN shell vertex and tree edge counts through side 32\n");
#elif ROLE == 1
    int wrong=0;
    for (int a=-4; a<=4; ++a) for (int b=-4; b<=4; ++b)
    for (int c=-4; c<=4; ++c) for (int d=-4; d<=4; ++d) {
        if (!a || !b || !c || !d) continue;
        int h=mult(mult(a,b),mult(inv(c),inv(d)));
        require(mult(mult(inv(a),h),mult(d,c))==b);
        require(mult(mult(inv(d),inv(h)),mult(a,b))==c);
        if (mult(mult(inv(a),h),mult(c,d))!=b) ++wrong;
    }
    require(wrong>0);
    emit("A4 CHILD limit\nA4 LEAN both ordered square inverses on 4096 quaternion assignments\n");
#else
    for (int L=2; L<=128; ++L) {
        int edge=3*L+(L-1)*(1+6*L);
        int seam=3*L+(L-1)*(1+7*L)+3*L*(L-1);
        require(edge<=16*(L+1)*(L+1) && seam<=16*(L+1)*(L+1));
        int frame=0;
        for (int x=0; x<L-1; ++x) frame+=L;
        require(frame+L==L*L);
    }
    emit("A4 LEAN quadratic word budget and Cartan seam accumulation through side 128\n");
#endif
    emit("A4 FINISHED\n");
    finish(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
