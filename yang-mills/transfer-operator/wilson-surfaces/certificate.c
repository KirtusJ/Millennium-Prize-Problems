/* Enumerate planar cubical fillings and emit checked area and counting constants. */
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
static unsigned perimeter(unsigned mask, unsigned side) {
    unsigned p = 0;
    for (unsigned j = 0; j < side*side; ++j) {
        if (!(mask & (1u << j))) continue;
        unsigned x = j % side, y = j / side;
        p += !x || !(mask & (1u << (j-1)));
        p += x+1 == side || !(mask & (1u << (j+1)));
        p += !y || !(mask & (1u << (j-side)));
        p += y+1 == side || !(mask & (1u << (j+side)));
    }
    return p;
}
static unsigned minimum(unsigned side, unsigned lag) {
    unsigned cells = side*side, best = 2*cells;
    for (unsigned mask = 0; mask < (1u << cells); ++mask) {
        unsigned missing = cells;
        for (unsigned x = mask; x; x &= x-1) --missing;
        unsigned cost = 2*missing + lag*perimeter(mask,side);
        if (cost < best) best = cost;
    }
    return best;
}
__attribute__((noreturn, used)) static void run(void) {
    unsigned char job[4];
    long fd = os(2, (long)"order", 0, 0);
    if (fd < 0 || os(0, fd, (long)job, sizeof job) != 3 || os(3, fd, 0, 0)) stop(3);
    unsigned vertex = job[0], corners = job[1], side = job[2];
    if (!vertex || !corners || side != 3) stop(4);
    unsigned animals = 4*vertex*corners, caps = 2*side*side, walls = 4*side;
    unsigned first = minimum(side,1), second = minimum(side,2);
    if (first != walls || second != caps) stop(5);
    put("theorem animalRate {p : ℝ} (hp : 0 ≤ p) (small : ");
    integer(animals);
    put("*p ≤ 1/4) :\n    0 ≤ ");
    integer(2*animals);
    put("*p ∧ ");
    integer(2*animals);
    put("*p ≤ 1/2 := by constructor <;> linarith\n"
        "theorem threeSquare (k : ℕ) (hk : 0 < k) :\n    min ");
    integer(caps);
    put(" ("); integer(walls);
    put("*k) = if k = 1 then "); integer(first);
    put(" else "); integer(second);
    put(" := by split <;> omega\n");
    flush();
    stop(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
