/* Form the signed six-face curl Gram matrix from oriented cube holonomies. */
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
static int incidence[6][64];
__attribute__((noreturn, used)) static void run(void) {
    unsigned char face[25];
    long fd=os(2,(long)"order",0,0);
    if (fd<0 || os(0,fd,(long)face,sizeof face)!=24 || os(3,fd,0,0)) stop(3);
    for (unsigned i=0;i<6;++i) for (unsigned j=0;j<4;++j) {
        unsigned a=face[4*i+j], b=face[4*i+(j+1)%4], diff=a^b;
        if (a>7 || b>7 || !(diff==1 || diff==2 || diff==4)) stop(4);
        unsigned edge=a<b?8*a+b:8*b+a;
        if (incidence[i][edge]) stop(5);
        incidence[i][edge]=a<b?1:-1;
    }
    unsigned trace=0, second=0;
    put("def cubeA : Matrix (Fin 6) (Fin 6) ℤ := !![");
    for (unsigned i=0;i<6;++i) {
        for (unsigned j=0;j<6;++j) {
            int x=0;
            for (unsigned e=0;e<64;++e) x+=incidence[i][e]*incidence[j][e];
            if (i==j) trace+=(unsigned)x;
            second+=(unsigned)(x*x);
            if (j) put(",");
            if (x<0) {put("-"); integer((unsigned)(-x));} else integer((unsigned)x);
        }
        put(i==5?"]\n":"; ");
    }
    put("\nset_option maxRecDepth 10000 in\nset_option maxHeartbeats 3000000 in\n");
    put("theorem cubePolynomial : cubeA*(cubeA-4•1)*(cubeA-6•1)=0 := by decide\n\n");
    put("theorem cubeSpectrum (a b : ℝ) (tr : 4*a+6*b="); integer(trace);
    put(") (tr₂ : 16*a+36*b="); integer(second);
    put(") :\n    a=3 ∧ b=2 := by constructor <;> linarith\n");
    flush();
    stop(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
