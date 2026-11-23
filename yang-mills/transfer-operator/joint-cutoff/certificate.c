/* Emit the physical-energy error theorem from three integer bound coefficients. */
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
    /* Inverting the resolvents costs (2c)(4c); lifting the logarithm
       adds log_error times the square of the defect-energy cap. */
    unsigned defect_error = 8u * job[0], cap = job[1], log_error = job[2];
    unsigned energy_error = defect_error + log_error * cap * cap;
    put("theorem combinedError {a c e m energy : ℝ} (ha : 0 ≤ a)\n"
        "    (hm : 0 ≤ m) (cap : m ≤ ");
    integer(cap);
    put("*c) (defect : |m-e| ≤ ");
    integer(defect_error);
    put("*a*c^2)\n"
        "    (lo : m ≤ energy) (hi : energy ≤ m+");
    integer(log_error);
    put("*a*m^2) : |energy-e| ≤ ");
    integer(energy_error);
    put("*a*c^2 := by\n"
        "  obtain ⟨left, right⟩ := abs_le.mp defect\n"
        "  have sq := mul_self_le_mul_self hm cap\n"
        "  have scaled := mul_le_mul_of_nonneg_left sq ha\n"
        "  apply abs_le.mpr\n"
        "  constructor <;> nlinarith [mul_nonneg ha (sq_nonneg c)]\n");
    flush();
    stop(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
