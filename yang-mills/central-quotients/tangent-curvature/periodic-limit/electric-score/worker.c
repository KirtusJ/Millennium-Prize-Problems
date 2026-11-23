/* Finite quaternion-group controls for the two-slice plaquette score. */
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



/* Labels 0..3 are 1,i,j,k. Bit 2 denotes an overall minus sign. */
static int trace_product(unsigned a, unsigned b, int inverse_b) {
    if ((a & 3) != (b & 3)) return 0;
    int negative = ((a ^ b) & 4) != 0;
    if ((a & 3) && !inverse_b) negative = !negative;
    return negative ? -2 : 2;
}

/* Kernel on Q8: keep the link with probability 1/d, else redraw Haar.
   After three links the retention probability is 1/d^3. */
static void parent(void) {
    unsigned cases = 0;
    for (int d = 2; d <= 9; ++d) {
        int h = d*d*d;
        for (unsigned u = 0; u < 8; ++u) {
            for (unsigned w = 0; w < 8; ++w) {
                int sum = 0;
                for (unsigned a = 0; a < 8; ++a) {
                    for (unsigned b = 0; b < 8; ++b) {
                        int weight = h-1 + 8*(a==b);
                        sum += weight*trace_product(u,a,0)*trace_product(w,b,0);
                    }
                }
                if (2*sum != 64*trace_product(u,w,1)) stop(7);
                ++cases;
            }
        }
    }
    emit("LEAN-BEGIN\nimport Mathlib.Tactic.Ring\nimport Mathlib.Data.Real.Basic\nnamespace ElectricScore\n");
    emit("theorem sharedLinkCases : ("); number(cases); emit(" : ℕ) = 512 := by decide\nLEAN-END\n");
    request(1,4,3);
}

static int character(unsigned a) {
    return (a & 3) ? 0 : ((a & 4) ? -2 : 2);
}

static void child(unsigned x,unsigned y) {
    if (x!=4 || y!=3) stop(5);
    unsigned cases = 0;
    for (int d=2; d<=9; ++d) {
        int k=d*d*d*d, first=0, second=0, common=0;
        for (unsigned a=0; a<8; ++a) {
            for (unsigned b=0; b<8; ++b) {
                int f=character(a)*character(b);
                int face_weight=k-1+8*(a==b);
                first += face_weight*f;
                second += face_weight*f*f;
                int tr=trace_product(a,b,1);
                common += (d-1+8*(a==b))*tr*tr;
            }
        }
        /* Denominators are 64k for a face and 64d for the common edge. */
        if (first!=64 || second!=64*(k+3) || common!=64*(d+3)) stop(8);
        ++cases;
    }
    emit("LEAN-BEGIN\ntheorem secondMomentCases : ("); number(cases); emit(" : ℕ) = 8 := by decide\nLEAN-END\n");
    request(2,4,3);
}

static void grandchild(unsigned x,unsigned y) {
    if (x!=4 || y!=3) stop(5);
    emit("LEAN-BEGIN\ntheorem scoreVariance (a b : ℝ) : (1+b^4-a^8)+12*(a^6*(1+3*b)/4-a^8)=1+b^4+3*a^6*(1+3*b)-13*a^8 := by ring\n");
    emit("theorem squaredDifference (x y : ℝ) : (x-y)^2=x^2-2*x*y+y^2 := by ring\n");
    emit("#print axioms sharedLinkCases\n#print axioms secondMomentCases\n#print axioms scoreVariance\n#print axioms squaredDifference\nend ElectricScore\nLEAN-END\n");
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
