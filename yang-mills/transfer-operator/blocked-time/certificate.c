/* Compute the open coupling threshold from three measured slab incidence counts. */
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
__attribute__((noreturn, used)) static void run(void) {
    unsigned char job[4];
    long fd = os(2, (long)"order", 0, 0);
    if (fd < 0 || os(0, fd, (long)job, sizeof job) != 3 || os(3, fd, 0, 0)) stop(3);
    unsigned magnetic = job[0] + job[1] + job[2];
    /* Solve 2/10 + magnetic*(13/4)*z < 1 for z, reducing the fraction. */
    unsigned numerator = 16, denominator = 5 * magnetic * 13;
    if (!denominator) stop(4);
    unsigned x = numerator, y = denominator;
    while (y) {
        unsigned remainder = x % y;
        x = y;
        y = remainder;
    }
    put("theorem rowAtOne {δ p z : ℝ} (heat : δ ≤ 1/10) (interaction : p ≤ 13*z/4)\n"
        "    (small : z < ");
    integer(numerator/x);
    put("/");
    integer(denominator/x);
    put(") : 2*δ+");
    integer(magnetic);
    put("*p < 1 := by linarith\n");
    put("theorem capError {x J : ℝ} (hx : 0 ≤ x) (hJ : 0 < J) : |x-min x J| ≤ x^2/J := by\n"
        "  by_cases within : x ≤ J\n"
        "  · rw [min_eq_left within, sub_self, abs_zero]\n"
        "    positivity\n"
        "  · rw [min_eq_right (le_of_not_ge within), abs_of_nonneg (by linarith)]\n"
        "    apply (le_div_iff₀ hJ).2\n"
        "    nlinarith [mul_nonneg hx (show 0 ≤ x-J by linarith), sq_nonneg J]\n");
    flush();
    stop(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
