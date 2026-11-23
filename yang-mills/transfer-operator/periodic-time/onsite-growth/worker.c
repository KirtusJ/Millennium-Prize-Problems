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
static int terminal_count;
static int least_edges = 7;
static int most_edges;

static void differentiate(int step, int edges, int degree[3], int unused[3]) {
    if (step == 6) {
        for (int i = 0; i < 3; ++i) {
            require(degree[i] >= 2 && degree[i] - unused[i] == 2);
        }
        require(edges >= 3 && edges <= 6);
        if (edges < least_edges) least_edges = edges;
        if (edges > most_edges) most_edges = edges;
        ++terminal_count;
        return;
    }
    int i = step / 2;
    if (unused[i] > 0) {
        --unused[i];
        differentiate(step + 1, edges, degree, unused);
        ++unused[i];
    }
    for (int j = 0; j < 3; ++j) {
        if (j == i) continue;
        ++degree[i];
        ++degree[j];
        ++unused[j];
        differentiate(step + 1, edges + 1, degree, unused);
        --degree[i];
        --degree[j];
        --unused[j];
    }
}
#elif ROLE == 2
/* Pair two labeled legs at each site. A closed color cycle has 3 choices. */
static int matching[12];
static long contractions(int sites, int mask) {
    if (!mask) {
        int seen = 0;
        long colors = 1;
        for (int leg = 0; leg < 2 * sites; ++leg) {
            if (seen & (1 << leg)) continue;
            colors *= 3;
            int current = leg;
            do {
                seen |= (1 << current) | (1 << (current ^ 1));
                current = matching[current ^ 1];
            } while (current != leg);
        }
        return colors;
    }
    int first = 0;
    while (!(mask & (1 << first))) ++first;
    int rest = mask ^ (1 << first);
    long sum = 0;
    for (int j = first + 1; j < 2 * sites; ++j) {
        if (!(rest & (1 << j)) || j / 2 == first / 2) continue;
        matching[first] = j;
        matching[j] = first;
        sum += contractions(sites, rest ^ (1 << j));
    }
    return sum;
}
#endif

__attribute__((used,noreturn)) static void run(void) {
#if ROLE == 0
    int degree[3] = {0}, unused[3] = {0};
    differentiate(0, 0, degree, unused);
    require(terminal_count > 0 && least_edges == 3 && most_edges == 6);
    emit("A4 CHILD spectrum\nA4 LEAN interpolation derivatives consume two distinct endpoints at each of three sites\n");
#elif ROLE == 1
    /* Endpoint factors are powers of 1/2. Enumerate exact exponent inequalities
       on all three-vertex graphs with multiplicities 0,1,2. */
    int witnesses = 0;
    for (int a = 0; a <= 2; ++a) for (int b = 0; b <= 2; ++b)
        for (int c = 0; c <= 2; ++c) {
            if (a + b < 2 || a + c < 2 || b + c < 2) continue;
            for (int x = 0; x < 6; ++x) for (int y = 0; y < 6; ++y)
                for (int z = 0; z < 6; ++z) {
                    int bound = 2 * (a * (x > y ? x : y) + b * (x > z ? x : z)
                                   + c * (y > z ? y : z));
                    require(bound >= 2 * (x + y + z));
                    ++witnesses;
                }
        }
    require(witnesses >= 216);
    emit("A4 CHILD limit\nA4 LEAN two-endpoint bounds survive nonuniform capped site weights\n");
#else
    /* Independent centered chi-square(3) moment recurrence from its mgf. */
    long moments[7] = {1, 0};
    for (int k = 1; k < 6; ++k) {
        moments[k + 1] = 2 * k * (moments[k] + 3 * moments[k - 1]);
        require(contractions(k + 1, (1 << (2 * (k + 1))) - 1) == moments[k + 1]);
    }
    emit("A4 LEAN no-self Wick pairings and three-color cycles at orders two through six\n");
#endif
    emit("A4 FINISHED\n");
    finish(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
