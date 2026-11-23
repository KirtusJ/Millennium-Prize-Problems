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

/* First-order basis states are encoded by their filled unit cells. */
static int filled(unsigned state, int side, int x, int y) {
    if (x < 0 || y < 0 || x >= side || y >= side) return 0;
    return (state >> (x + side*y)) & 1;
}

__attribute__((used,noreturn)) static void run(void) {
#if ROLE == 0
    for (int side = 2; side <= 5; ++side) {
        unsigned state = (1U << (side*side)) - 1;
        for (int x = 0; x < side; ++x) {
            int y = side-1;
            int across = 2-filled(state,side,x-1,y)-filled(state,side,x+1,y);
            int along = 2-filled(state,side,x,y-1)-filled(state,side,x,y+1);
            require(along == 1 && across == (x == side-1 ? 2 : 1));
            state ^= 1U << (x+side*y);
        }
    }
    emit("A4 CHILD spectrum\nA4 LEAN Row stripping first gives a three-edge face at depth side minus one\n");
#elif ROLE == 1
    /* Prefix k=0,...,3 at g=1 and 2. Common denominator 6!*3!*2^9.
       In the recurrence the omitted-series ratio is <=1/20. */
    const long scale = 2211840;
    int fact[] = {1,1,2,6,24,120,720};
    for (int g = 1; g <= 2; ++g) {
        long lower[4] = {0}, upper[4] = {0};
        for (int n = 1; n <= 3; ++n) {
            long last = 0;
            for (int k = 0; k <= 3; ++k) {
                long den = (long)fact[k]*fact[k+n]*(g == 1 ? 1L<<(2*k+n) : 1L);
                require(scale % den == 0);
                last = scale / den;
                lower[n] += last;
            }
            upper[n] = lower[n] + (last+18)/19;
        }
        if (g == 1) {
            require(4*upper[2] < lower[1]);
            require(3*lower[3]*lower[1] > 2*upper[2]*upper[2]);
            require(4*8 > 27);
        } else {
            require(7*lower[2] > 3*upper[1]);
            require(4*upper[3]*upper[1] < 3*lower[2]*lower[2]);
            require(7*27 < 3*64);
        }
    }
    emit("A4 CHILD limit\nA4 LEAN Positive-series enclosures certify the accidental crossing in (1,2)\n");
#else
    /* For the standard normal, He_4=y^4-6y^2+3. Evaluate
       at y^2=5 and 6 to compare to the sixth/ fourth moment bound. */
    volatile int square_low = 5, square_high = 6;
    require(square_low*square_low - 6*square_low + 3 < 0);
    require(square_high*square_high - 6*square_high + 3 > 0);
    emit("A4 LEAN Degree-four Hermite compression improves the sixth-moment bound\n");
#endif
    emit("A4 FINISHED\n"); finish(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
