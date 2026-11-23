/* Emit the three-reading thermal error from the coefficients of X(1-X)^2. */
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
    unsigned l1 = job[0] + job[1] + job[2];
    put("theorem threeThermalErrors {u v w b : ℝ} (hu : |u| ≤ 2*b) (hv : |v| ≤ 2*b)\n"
        "    (hw : |w| ≤ 2*b) : |u-");
    integer(job[1]);
    put("*v+w| ≤ ");
    integer(2*l1);
    put("*b := by\n"
        "  have U := abs_le.mp hu\n"
        "  have V := abs_le.mp hv\n"
        "  have W := abs_le.mp hw\n"
        "  apply abs_le.mpr\n"
        "  constructor <;> linarith\n");
    flush();
    stop(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
