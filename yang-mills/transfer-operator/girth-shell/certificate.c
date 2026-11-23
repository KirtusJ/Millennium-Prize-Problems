/* Contract the twelve oriented SU(2) Schur integrals on six cube faces. */
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
static unsigned parent[24];
static unsigned root(unsigned i) {
    while (parent[i] != i) i = parent[i];
    return i;
}
static unsigned next(unsigned i) {
    return 4*(i/4)+(i+1)%4;
}
__attribute__((noreturn, used)) static void run(void) {
    unsigned char face[25];
    long fd = os(2, (long)"order", 0, 0);
    if (fd < 0 || os(0, fd, (long)face, sizeof face) != 24 || os(3, fd, 0, 0)) stop(3);
    for (unsigned i=0; i<24; ++i) parent[i]=i;
    unsigned edges=0, colors=0;
    for (unsigned i=0; i<24; ++i) {
        unsigned a=face[i], b=face[next(i)], diff=a^b, matches=0;
        if (a>7 || b>7 || !(diff==1 || diff==2 || diff==4)) stop(4);
        for (unsigned j=0; j<24; ++j) {
            if (face[j]!=b || face[next(j)]!=a) continue;
            ++matches;
            if (i<j) {
                ++edges;
                parent[root(i)]=root(next(j));
                parent[root(next(i))]=root(j);
            }
        }
        if (matches!=1) stop(5);
    }
    for (unsigned i=0; i<24; ++i) if (root(i)==i) ++colors;
    if (edges!=12 || colors!=8) stop(6);
    unsigned faces=24/4;
    unsigned denominator=(1u << (edges+faces-colors))/4;
    put("theorem cubeHessian : (4:ℝ)*2^"); integer(colors); put("/(2^");
    integer(edges); put("*2^"); integer(faces); put(") = 1/"); integer(denominator);
    put(" := by norm_num\n");
    flush();
    stop(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
