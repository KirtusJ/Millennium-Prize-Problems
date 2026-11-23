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
static int counts[512], blocked;
static int filled(int state, int side, int x, int y) {
    if (x<0 || x>=side || y<0 || y>=side) return 0;
    return (state >> (x + side*y)) & 1;
}
static void walk(int side, int state, int depth) {
    if (depth == side) { ++counts[state]; return; }
    for (int y=0; y<side; ++y) for (int x=0; x<side; ++x) {
        int value = filled(state,side,x,y);
        int h = (filled(state,side,x+1,y)!=value) + (filled(state,side,x-1,y)!=value);
        int v = (filled(state,side,x,y+1)!=value) + (filled(state,side,x,y-1)!=value);
        if (h+v==3) { require(depth==side-1); ++blocked; }
        else if (h+v>=2) {
            require(h==1 && v==1);
            walk(side,state^(1<<(x+side*y)),depth+1);
        }
    }
}
#elif ROLE == 1
/* Unit quaternions encoded as signed 1, i, j, k by indices 1,...,4. */
static int mul(int a, int b) {
    static const int product[4][4] = {
        {1,2,3,4},{2,-1,4,-3},{3,-4,-1,2},{4,3,-2,-1}};
    int sign = 1;
    if (a<0) { sign=-sign; a=-a; }
    if (b<0) { sign=-sign; b=-b; }
    return sign * product[a-1][b-1];
}
static int tr(int a) { return a==1 ? 2 : a==-1 ? -2 : 0; }
#endif

__attribute__((used,noreturn)) static void run(void) {
#if ROLE == 0
    for (int side=2; side<=3; ++side) {
        for (int i=0; i<512; ++i) counts[i]=0;
        blocked=0;
        walk(side,(1<<(side*side))-1,0);
        int norm=0;
        for (int i=0; i<512; ++i) norm+=counts[i]*counts[i];
        require(norm==(side==2 ? 24 : 880));
        require(blocked==4*(1<<(side-1)));
    }
    emit("A4 CHILD spectrum\nA4 LEAN Physical occupancy walks at sides two and three\n");
#elif ROLE == 1
    for (int a=1; a<=4; ++a) for (int b=1; b<=4; ++b) {
        int sum=0;
        for (int h=-4; h<=4; ++h) if (h) {
            int inverse=(h==1 || h==-1) ? h : -h;
            sum+=tr(mul(a,h))*tr(mul(inverse,b));
        }
        require(sum==4*tr(mul(a,b)));
    }
    emit("A4 CHILD limit\nA4 LEAN Singlet averaging control on the defining quaternion representation\n");
#else
    long row[25]={1};
    for (int side=1; side<=12; ++side) {
        for (int k=side; k>0; --k) row[k]+=row[k-1];
        long mass=0, middle=1;
        for (int k=0; k<=side; ++k) mass+=row[k]*row[k];
        for (int k=1; k<=side; ++k) middle=middle*(side+k)/k;
        require(mass==middle);
    }
    emit("A4 LEAN Missing row amplitudes square to the central binomial count\n");
#endif
    emit("A4 FINISHED\n"); finish(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
