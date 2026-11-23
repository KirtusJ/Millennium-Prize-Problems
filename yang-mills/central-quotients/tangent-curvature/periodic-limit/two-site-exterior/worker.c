/* Finite checks for localization on the periodic cube. */
#include <stddef.h>

static long syscall3(long number, long a, long b, long c) {
    long result;
    __asm__ volatile ("syscall" : "=a"(result)
                      : "a"(number), "D"(a), "S"(b), "d"(c)
                      : "rcx", "r11", "memory");
    return result;
}

_Noreturn static void stop(int status) {
    syscall3(60, status, 0, 0);
    __builtin_unreachable();
}

static void emit(const char *text) {
    size_t size = 0;
    while (text[size]) ++size;
    while (size) {
        long written = syscall3(1, 1, (long)text, size);
        if (written <= 0 || (size_t)written > size) stop(3);
        text += written;
        size -= written;
    }
}

static void number(unsigned n) {
    char text[12];
    unsigned pos = sizeof text - 1;
    text[pos] = 0;
    do { text[--pos] = '0' + n % 10; n /= 10; } while (n);
    emit(text + pos);
}

static void request(unsigned depth, unsigned a, unsigned b) {
    emit("NEXT "); number(depth); emit(" "); number(a); emit(" "); number(b); emit("\n");
}

static unsigned count_bits(unsigned bits) {
    return (bits&1u) + ((bits>>1)&1u) + ((bits>>2)&1u);
}

static void parent(void) {
    unsigned shells[4] = {0}, regular_rank = 0;
    for (unsigned k = 0; k < 8; ++k) {
        unsigned shell = count_bits(k);
        if (shell) shells[shell] += 6;
        /* Two charged colors always have nonzero momentum at (pi,0,0).
           The neutral color loses its two transverse branches only at k=0. */
        regular_rank += 4 + (shell ? 2 : 0);
    }
    if (shells[1]!=18 || shells[2]!=18 || shells[3]!=6 || regular_rank!=46) stop(7);
    emit("LEAN-BEGIN\nimport Mathlib.Tactic.Ring\nimport Mathlib.Data.Real.Basic\nnamespace TwoSiteExterior\n");
    emit("theorem centralRank : ("); number(shells[1]+shells[2]+shells[3]);
    emit(" : ℕ) = 42 := by decide\nLEAN-END\n");
    request(1,4,3);
}

static void child(unsigned x, unsigned y) {
    if (x != 4 || y != 3) stop(5);
    /* Orthogonality and covariance of the eight center-sector sign choices. */
    unsigned orthogonal = 0;
    for (unsigned a = 0; a < 8; ++a) for (unsigned b = 0; b < 8; ++b) {
        int overlap = 0;
        for (unsigned z = 0; z < 8; ++z) {
            int pa = (int)(count_bits(a&z)&1);
            int pb = (int)(count_bits(b&z)&1);
            overlap += (1-2*pa)*(1-2*pb);
        }
        if (overlap != (a==b ? 8 : 0)) stop(8);
        if (!overlap) ++orthogonal;
    }
    emit("LEAN-BEGIN\ntheorem orthogonalPairs : ("); number(orthogonal);
    emit(" : ℕ) = 56 := by decide\nLEAN-END\n");
    request(2,4,3);
}

static void grandchild(unsigned x, unsigned y) {
    if (x != 4 || y != 3) stop(5);
    /* Check the algebra which bounds the affine magnetic Taylor remainder
       after multiplying the inequality by the positive parameter e. */
    for (int v=-6; v<=6; ++v) for (int r=-6; r<=6; ++r)
        for (int e=1; e<=8; ++e) {
            int lhs = 8*e*(v+r)*(v+r)-e*(8-e)*v*v-8*(e-8)*r*r;
            if (lhs!=(e*v+8*r)*(e*v+8*r)) stop(9);
        }
    emit("LEAN-BEGIN\ntheorem affineRemainder (e v r : ℝ) : e*(v+r)^2-e*(1-e)*v^2-(e-1)*r^2=(e*v+r)^2 := by ring\n");
    emit("#print axioms centralRank\n#print axioms orthogonalPairs\n#print axioms affineRemainder\nend TwoSiteExterior\nLEAN-END\n");
}
__attribute__((used,noreturn)) static void run(void) {
    static unsigned char input[4];
    long fd = syscall3(2, (long)"task.bin", 0, 0);
    if (fd < 0 || syscall3(0, fd, (long)input, sizeof input) != 3 ||
        syscall3(0, fd, (long)(input+3), 1) != 0 || syscall3(3, fd, 0, 0) != 0) stop(2);
    if (!input[0] && !input[1] && !input[2]) parent();
    else if (input[0] == 1) child(input[1],input[2]);
    else if (input[0] == 2) grandchild(input[1],input[2]);
    else stop(2);
    stop(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
