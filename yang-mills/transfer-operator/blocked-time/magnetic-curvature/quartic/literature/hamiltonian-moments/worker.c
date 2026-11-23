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

__attribute__((used,noreturn)) static void run(void) {
    /* Twice the intermediate electric energies and the connected weights. */
    volatile int energy2[] = {9, 12, 13, 16};
    volatile int weight[] = {6, -26, 18, 1};
#if ROLE == 0
    /* k! times the source coefficient of t^k, k = 3,...,6,
       in (2/g^2)[x^4] Eq. (2.21). */
    volatile int laplace[] = {1, -10, 41, 230};
    for (int k = 0; k < 4; ++k) {
        int expected = -laplace[k];
        if (k >= 1) expected -= 6 * laplace[k-1];
        if (k >= 2) expected -= 9 * laplace[k-2];
        int moment = 0;
        for (int j = 0; j < 4; ++j) {
            int term = weight[j];
            for (int n = 0; n < k; ++n) term *= -energy2[j];
            moment += term;
        }
        require(moment == expected * (1 << k));
    }
    emit("A4 CHILD spectrum\nA4 LEAN Four connected weights reproduce the four published moments\n");
#elif ROLE == 1
    int pole = 0, vacuum = 0;
    for (int j = 0; j < 4; ++j) {
        require(210 % (energy2[j]-6) == 0 && 1872 % energy2[j] == 0);
        pole += 2 * weight[j] * (210 / (energy2[j]-6));
        vacuum += 2 * weight[j] * (1872 / energy2[j]);
    }
    require(pole * 105 == 71 * 210);
    require(vacuum * 104 == -11 * 1872);
    emit("A4 CHILD limit\nA4 LEAN Scalar double pole and vacuum residue agree with the rational values\n");
#else
    volatile int haar2 = 1, haar4 = 2, haar6 = 5;
    int single = haar6 - 15 * haar4 * haar2 + 30 * haar2 * haar2 * haar2;
    int cube = 720 / (3 * 16);
    require(single == 5 && cube == 15);
    require(6 * (single + cube) == 120);
    emit("A4 LEAN Single-face and cube cumulants reproduce the published sixth moment\n");
#endif
    emit("A4 FINISHED\n");
    finish(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
