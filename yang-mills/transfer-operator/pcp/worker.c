/* Freestanding user program for the PCP OS x86-64 read/write/exit ABI.
   Two leaves synthesize Lean proof scripts. An assembly guest combines them
   with the supplied basis. Hex framing preserves UTF-8 on the serial console. */
#include <stddef.h>
#include <stdint.h>

static long sys(long n, long a, long b, long c) {
    long out;
    __asm__ volatile ("syscall" : "=a"(out) : "a"(n), "D"(a), "S"(b), "d"(c)
                      : "rcx", "r11", "memory");
    return out;
}
static void stop(int status) {
    sys(60, status, 0, 0);
    __builtin_unreachable();
}
static void write_all(const char *p, size_t len) {
    while (len) {
        long n = sys(1, 1, (long)p, len);
        if (n <= 0 || (unsigned long)n > len) stop(11);
        p += n;
        len -= n;
    }
}
static const char digits[] = "0123456789abcdef";
static char line[108] = "LEANHEX ";
static size_t used = 8;
static void flush(void) {
    if (used == 8) return;
    line[used++] = '\n';
    write_all(line, used);
    used = 8;
}
static void byte(unsigned char c) {
    line[used++] = digits[c >> 4];
    line[used++] = digits[c & 15];
    if (used == 104) flush();
}
static void emit(const char *s) {
    while (*s) byte((unsigned char)*s++);
}
static size_t load(const char *name, unsigned char *dst, size_t size) {
    long fd = sys(2, (long)name, 0, 0);
    if (fd < 0) stop(12);
    size_t pos = 0;
    while (pos < size) {
        long n = sys(0, fd, (long)(dst + pos), size - pos);
        if (n < 0 || (size_t)n > size - pos) stop(13);
        if (n == 0) break;
        pos += (size_t)n;
    }
    if (pos == size || sys(3, fd, 0, 0) != 0) stop(14);
    return pos;
}

static void comparison(void) {
    /* At (sign*c, A), the square (A*x-c*y)^2 vanishes identically
       exactly when the coefficient of A*c is zero. */
    int sign;
    for (sign = -1; sign <= 1; sign += 2)
        if (sign - 1 == 0) break;
    if (sign > 1) stop(20);
    const char *probe = sign < 0 ? "(-c)" : "c";
    emit("  constructor\n  · intro h\n    have key := sub_nonneg.mpr (h ");
    emit(probe);
    emit(" (u-m))\n    have id := pivot_identity u v c m ");
    emit(probe);
    emit(" (u-m)\n"
         "    rw [mul_comm (u-m) c, sub_self, zero_pow (by decide), zero_add] at id\n"
         "    have hp : 0 ≤ ((u-m)*(v-m)-c^2)*(u-m)^2 := id ▸ mul_nonneg (sub_nonneg.mpr hu.le) key\n"
         "    have := nonneg_of_mul_nonneg_left hp (sq_pos_of_pos (sub_pos.mpr hu))\n"
         "    linarith\n"
         "  · intro h x y\n"
         "    have hsum := add_nonneg (sq_nonneg ((u-m)*x - c*y))\n"
         "      (mul_nonneg (sub_nonneg.mpr h) (sq_nonneg y))\n"
         "    rw [← pivot_identity] at hsum\n"
         "    exact sub_nonneg.mp (nonneg_of_mul_nonneg_right hsum (sub_pos.mpr hu))\n");
}

static void collapse(void) {
    /* In the bound E(a) <= 2a, a <= m/k contradicts E(a) >= m
       only when 2/k < 1. Select the first acceptable integer. */
    unsigned k;
    for (k = 1; k <= 9; ++k) if (2 < k) break;
    if (k > 9) stop(21);
    emit("  rintro ⟨m, hm, hall⟩\n  let a := min (m/");
    byte('0' + k);
    emit(") (1/4)\n  have ha : 0 < a := lt_min (by linarith) (by norm_num)\n"
         "  have hfirst : a ≤ m/");
    byte('0' + k);
    emit(" := min_le_left _ _\n"
         "  have hsecond : a ≤ 1/4 := min_le_right _ _\n"
         "  have hsmall : a ≤ 1/2 := by linarith\n"
         "  linarith only [hm, hfirst, hall a ha hsmall, (soft_energy a ha hsmall).2]\n");
}
static unsigned char basis[32768], parts[2][4096];
static void assemble(void) {
    size_t n = load("basis", basis, sizeof basis);
    size_t sizes[] = {load("comparison", parts[0], sizeof parts[0]),
                      load("collapse", parts[1], sizeof parts[1])};
    unsigned seen = 0;
    for (size_t i = 0; i < n; ++i) {
        unsigned c = basis[i];
        if (c != 1 && c != 2) { byte(c); continue; }
        unsigned j = c - 1;
        if (!sizes[j] || (seen & (1u << j))) stop(22);
        seen |= 1u << j;
        for (size_t k = 0; k < sizes[j]; ++k) byte(parts[j][k]);
    }
    if (seen != 3) stop(23);
}
__attribute__((used, noreturn)) static void run(void) {
    unsigned char job[2];
    if (load("order", job, sizeof job) != 1) stop(24);
    if (job[0] == 'C') comparison();
    else if (job[0] == 'W') collapse();
    else if (job[0] == 'A') assemble();
    else stop(25);
    flush();
    stop(0);
    __builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
