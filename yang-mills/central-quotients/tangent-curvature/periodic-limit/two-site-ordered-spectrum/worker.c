/* Three finite checks for the fixed-cube spectral matching. */
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

static void parent(void) {
    /* Exponents in units of 1/24 for h.  Patch r, ball radius ell, s and
       affine loss enter different parts of the two localization estimates. */
    unsigned r=16, ell=27, s=36, affine=18;
    if (!(ell>r && affine>r && 2*r>24 && 2*s-2*r>24)) stop(7);
    if (2*s-2*ell != affine || 4*ell-2*s-affine != affine) stop(7);
    emit("LEAN-BEGIN\nimport Mathlib.Tactic.Ring\nimport Mathlib.Data.Real.Basic\nnamespace TwoSiteOrdered\n");
    emit("theorem outerCost : ("); number(2*s-2*r); emit(" : ℕ) = 40 := by decide\nLEAN-END\n");
    request(1,4,3);
}

static void child(unsigned x, unsigned y) {
    if (x!=4 || y!=3) stop(5);
    /* Among three axial unit probes at least two thirds of the sum
       of their squared cross products survives in the best direction. */
    unsigned checks=0;
    for (int a=-3; a<=3; ++a) for (int b=-3; b<=3; ++b)
        for (int c=-3; c<=3; ++c) {
            int norm=a*a+b*b+c*c;
            int sums[3]={b*b+c*c,a*a+c*c,a*a+b*b};
            int best=sums[0];
            for (unsigned i=1; i<3; ++i) if (sums[i]>best) best=sums[i];
            if (3*best<2*norm || sums[0]+sums[1]+sums[2]!=2*norm) stop(8);
            ++checks;
        }
    emit("LEAN-BEGIN\ntheorem probes : ("); number(checks); emit(" : ℕ) = 343 := by decide\nLEAN-END\n");
    request(2,4,3);
}

static void grandchild(unsigned x, unsigned y) {
    if (x!=4 || y!=3) stop(5);
    /* Check that all seven nonidentity translations of the eight centers
       have no fixed well. */
    for(unsigned z=0; z<8; ++z) for(unsigned k=1; k<8; ++k)
        if ((z^k)==z) stop(9);
    emit("LEAN-BEGIN\ntheorem probeIdentity (a b c : ℝ) : (b^2+c^2)+(a^2+c^2)+(a^2+b^2)=2*(a^2+b^2+c^2) := by ring\n");
    emit("#print axioms outerCost\n#print axioms probes\n#print axioms probeIdentity\nend TwoSiteOrdered\nLEAN-END\n");
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
