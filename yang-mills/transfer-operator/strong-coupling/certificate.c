/* Measured PCP OS user program. The order module is the one-byte denominator.
   Search a rational height and emit its Lean statement and proof over the serial ABI. */
#include <stddef.h>

static long os(long n, long a, long b, long c) {
    long r;
    __asm__ volatile ("syscall" : "=a"(r) : "a"(n), "D"(a), "S"(b), "d"(c)
                      : "rcx", "r11", "memory");
    return r;
}
__attribute__((noreturn)) static void finish(int code) {
    os(60, code, 0, 0);
    __builtin_unreachable();
}
static char frame[105] = "LEANHEX ";
static size_t used = 8;
static void flush(void) {
    if (used == 8) return;
    frame[used++] = '\n';
    for (size_t pos = 0; pos < used;) {
        long count = os(1, 1, (long)(frame + pos), used - pos);
        if (count <= 0 || (size_t)count > used - pos) finish(2);
        pos += count;
    }
    used = 8;
}
static void emit_byte(unsigned char b) {
    static const char hex[] = "0123456789abcdef";
    frame[used++] = hex[b >> 4];
    frame[used++] = hex[b & 15];
    if (used == 104) flush();
}
static void emit(const char *p) {
    while (*p) emit_byte((unsigned char)*p++);
}
static void number(unsigned n) {
    if (n >= 10) number(n / 10);
    emit_byte((unsigned char)('0' + n % 10));
}
__attribute__((used, noreturn)) static void run(void) {
    unsigned char order[2];
    long fd = os(2, (long)"order", 0, 0);
    if (fd < 0 || os(0, fd, (long)order, sizeof order) != 1 || os(3, fd, 0, 0)) finish(3);
    unsigned den = order[0];
    if (!den) finish(4);
    for (unsigned num = 1; num <= 2 * den; ++num) {
        if (345 * den + 60 * num > 449 * den || 540 * den > 314 * num) continue;
        emit("def height : ℝ := "); number(num); emit("/"); number(den);
        emit("\n\n/-- R = 3 works for all s,t up to 1/20. The second row is unnormalized. -/\n"
             "theorem rowsThree {s t : ℝ} (hs : s ≤ 1/20) (ht : t ≤ 1/20) :\n"
             "    450*spatial s t 3 height ≤ 449 ∧ 450*temporal t 3 height ≤ 449*height := by\n"
             "  unfold spatial temporal height\n  constructor <;> linarith only [hs, ht]\n");
        flush();
        finish(0);
    }
    finish(5);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
