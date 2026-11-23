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

static long square(long x) {
    return x*x;
}

__attribute__((used,noreturn)) static void run(void) {
#if ROLE == 0
    /* Count points in a shifted rational interval of length L/4. Taking
       four independent coordinates preserves a uniform volume fraction. */
    for (long length=16; length<=128; ++length) {
        for (long shift=0; shift<8; ++shift) {
            long count=0;
            for (long j=-2; j<=length; ++j)
                if (8*j>=shift && 8*j<=shift+2*length) ++count;
            require(8*count >= length && 2*count <= length);
            require(square(square(8*count)) >= square(square(length)));
        }
    }
    emit("A4 CHILD spectrum\nA4 LEAN displaced mesh boxes retain a positive fraction of four-volume\n");
#elif ROLE == 1
    /* Exact four-frequency Plancherel, including the weighted spatial ledger
       for a first frequency difference. Fourier numerators omit 1/4. */
    for (long a=0; a<9; ++a) for (long b=0; b<9; ++b)
        for (long c=0; c<9; ++c) {
            long g0=a+2*b+c, g1=a-c, g2=a-2*b+c;
            require(square(g0)+2*square(g1)+square(g2)
                    == 4*(square(a)+2*square(b)+square(c)));
            require(4*square(g1)+4*square(g2)
                    == 8*(square(a-b)+square(b-c)));
        }
    emit("A4 CHILD limit\nA4 LEAN exact spatial Plancherel and frequency-difference identities\n");
#else
    for (long center=1; center<=64; ++center) {
        for (long y=1; y<=4*center; ++y) {
            long cost=2*square(y)+2*square(center)-4*center*y;
            require(cost==2*square(y-center));
            require((cost==0)==(y==center));
        }
    }
    /* a=p/q; compare 2 and 2 sqrt(2a), including equality. */
    for (long q=1; q<=24; ++q) for (long p=1; p<=q; ++p) {
        long difference=4*q-8*p;
        require((difference>0)==(q>2*p));
        require((difference==0)==(q==2*p));
    }
    emit("A4 LEAN exact saddle cost identity and critical exponent sign\n");
#endif
    emit("A4 FINISHED\n");
    finish(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
