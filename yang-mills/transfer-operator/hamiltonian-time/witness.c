/* Freestanding PCP OS worker for the variance and energy estimates. */
#include <stddef.h>

static long os(long n, long a, long b, long c) {
    long r;
    __asm__ volatile ("syscall" : "=a"(r) : "a"(n), "D"(a), "S"(b), "d"(c)
                      : "rcx", "r11", "memory");
    return r;
}
__attribute__((noreturn)) static void stop(unsigned code) {
    os(60, code, 0, 0);
    __builtin_unreachable();
}
static char frame[105] = "LEANHEX ";
static size_t used = 8;
static void flush(void) {
    if (used == 8) return;
    frame[used++] = '\n';
    for (size_t off = 0; off < used;) {
        long n = os(1, 1, (long)(frame + off), used - off);
        if (n <= 0 || (size_t)n > used - off) stop(2);
        off += (size_t)n;
    }
    used = 8;
}
static void byte(unsigned char c) {
    static const char hex[] = "0123456789abcdef";
    frame[used++] = hex[c >> 4];
    frame[used++] = hex[c & 15];
    if (used == 104) flush();
}
static void put(const char *s) {
    while (*s) byte((unsigned char)*s++);
}
static void integer(unsigned n) {
    if (n >= 10) integer(n / 10);
    byte((unsigned char)('0' + n % 10));
}
static void fraction(unsigned a, unsigned b) {
    unsigned x = a, y = b;
    while (y) {
        unsigned rem = x % y;
        x = y;
        y = rem;
    }
    integer(a / x); put("/"); integer(b / x);
}
__attribute__((noreturn, used)) static void run(void) {
    unsigned char job[3];
    long fd = os(2, (long)"order", 0, 0);
    if (fd < 0 || os(0, fd, (long)job, sizeof job) != 2 || os(3, fd, 0, 0)) stop(3);
    /* job requests a minimum variance job[0]/9 and maximum scaled energy job[1].
       n is the reciprocal radius. The worst-case squared-mean cost is 16/n². */
    for (unsigned n = 7; n < 256; ++n) {
        unsigned square = n*n, variance = square - 4*n - 16;
        if (9*variance < job[0]*square || 2*(3*square + 4*n) > job[1]*variance) continue;
        put("  have radius : d ≤ "); fraction(1, n);
        put(" := by nlinarith only [small, overlap]\n  obtain ⟨lo, hi⟩ := abs_le.mp mean\n"
            "  have sq : m^2 ≤ "); fraction(16, square);
        put(" := by\n    nlinarith only [mul_nonneg (show 0 ≤ m+"); fraction(4, n);
        put(" by linarith) (show 0 ≤ "); fraction(4, n);
        put("-m by linarith)]\n  have hv : "); fraction(variance, square);
        put(" ≤ v := by linarith\n  refine ⟨hv, (div_le_div_iff₀ (by linarith : 0 < v) hk).2 ?_⟩\n"
            "  linarith [mul_comm κ E]\n");
        flush();
        stop(0);
    }
    stop(4);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
