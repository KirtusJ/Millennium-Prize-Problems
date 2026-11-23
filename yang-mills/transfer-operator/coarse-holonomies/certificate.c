/* Compute the sharp scalar floor entailed by the translation-overlap comparison. */
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
    unsigned overlap_inv = job[0], terms = job[1], haar = job[2];
    if (!overlap_inv || !terms || !haar) stop(4);
    unsigned variance_factor = overlap_inv * terms * terms;
    unsigned floor = 1;
    while (floor * haar < variance_factor) ++floor;
    if (floor * haar != variance_factor) stop(5);
    put("theorem displacementFloor {D s k : ℝ} (propagate : ");
    integer(haar);
    put(" ≤ k^2*s)\n    (overlap : s ≤ ");
    integer(variance_factor);
    put("*D) : 1 ≤ ");
    integer(floor);
    put("*k^2*D := by\n  have h := mul_le_mul_of_nonneg_left overlap (sq_nonneg k)\n"
        "  linarith only [propagate, h]\n");
    flush();
    stop(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
