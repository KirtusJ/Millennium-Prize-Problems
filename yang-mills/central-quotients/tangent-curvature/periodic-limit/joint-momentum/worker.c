/* Checks of signed paths, momentum aliases, and two-leg kinematics. */
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


static unsigned magnitude(int a) { return (unsigned)(a < 0 ? -a : a); }

static void decode(unsigned code, int v[3]) {
    for (unsigned j = 0; j < 3; ++j) {
        v[j] = (int)(code % 3) - 1;
        code /= 3;
    }
}

/* Sort distinct axes by elementary face swaps. Cancel opposite same-axis steps. */
static void parent(void) {
    unsigned affected = 0, swaps = 0;
    for (unsigned a = 0; a < 27; ++a)
        for (unsigned b = 0; b < 27; ++b) {
            int u[3], v[3], word[6], reduced[6];
            decode(a,u);
            decode(b,v);
            unsigned length = 0, used = 0, box = 0;
            for (unsigned pass = 0; pass < 2; ++pass)
                for (int j = 0; j < 3; ++j) {
                    int sign = pass ? v[j] : u[j];
                    if (sign) word[length++] = sign*(j+1);
                }
            for (unsigned i = 1; i < length; ++i) {
                unsigned j = i;
                while (j && magnitude(word[j-1]) > magnitude(word[j])) {
                    int tmp = word[j-1];
                    word[j-1] = word[j];
                    word[j] = tmp;
                    ++box;
                    --j;
                }
            }
            for (unsigned j = 0; j < length; ++j) {
                if (used && reduced[used-1] == -word[j]) --used;
                else reduced[used++] = word[j];
            }
            unsigned pos = 0, area = 0;
            for (int j = 0; j < 3; ++j) {
                int net = u[j]+v[j];
                for (unsigned k = 0; k < magnitude(net); ++k) {
                    if (pos == used || reduced[pos++] != (net>0 ? j+1 : -j-1)) stop(7);
                }
                for (int i = j+1; i < 3; ++i) area += magnitude(u[i]*v[j]);
            }
            if (pos != used || area != box || (!u[1] && !u[2] && box)) stop(7);
            affected += box > 0;
            swaps += box;
        }
    emit("LEAN-BEGIN\n");
    emit("import Mathlib.Analysis.SpecialFunctions.Sqrt\n"
         "import Mathlib.Tactic.Linarith\n"
         "import Mathlib.Tactic.Ring\n"
         "\n"
         "namespace JointMomentum\n"
         "\n");
    emit("theorem signedPathCounts : ((");
    number(affected);
    emit(", ");
    number(swaps);
    emit(") : ℕ × ℕ) = (540,972) := by decide\n"
         "\n");
    emit("theorem wickExcess (r b v : ℝ) (hr : 0 < r) (h1 : r < 1)\n"
         "    (hb : 0 < b) (hv : 0 ≤ v) :\n"
         "    0 < b*(r-r^2)+v*(1-r^2) := by\n"
         "  have h : 0 < r*(1-r) := mul_pos hr (sub_pos.mpr h1)\n"
         "  have k : 0 < (1-r)*(1+r) := mul_pos (sub_pos.mpr h1) (by linarith)\n"
         "  nlinarith [mul_pos hb h, mul_nonneg hv k.le]\n"
         "\n");
    emit("LEAN-END\n");
    request(1, 4, 3);
}

static void child(unsigned step, unsigned dimension) {
    if (step != 4 || dimension != 3) stop(5);
    unsigned aliased = 0, still_aliased = 0;
    for (unsigned p = 0; p < 16; ++p)
        for (unsigned q = p+1; q < 16; ++q) {
            int coarse = 1, full = 1;
            for (unsigned j = 0; j < 16; ++j) {
                if ((j*p)%16 != (j*q)%16) {
                    full = 0;
                    if (j%step == 0) coarse = 0;
                }
            }
            aliased += coarse;
            still_aliased += full;
        }
    emit("LEAN-BEGIN\n");
    emit("theorem foldedPairs : ((");
    number(aliased);
    emit(", ");
    number(still_aliased);
    emit(") : ℕ × ℕ) = (24,0) := by decide\n"
         "\n");
    emit("theorem budget (signal approximation moment : ℝ)\n"
         "    (hs : 0 < signal) (ha : approximation ≤ signal/4)\n"
         "    (hm : moment ≤ signal/4) :\n"
         "    0 < signal - approximation - moment := by linarith\n"
         "\n");
    emit("LEAN-END\n");
    request(2, 4, 3);
}

static void grandchild(unsigned step, unsigned dimension) {
    if (step != 4 || dimension != 3) stop(5);
    unsigned count = 0, invariant = 0;
    for (unsigned x = 1; x <= 20; ++x)
        for (unsigned y = 1; y <= 20; ++y)
            for (unsigned h = 1; h <= 29; ++h) {
                if (h*h != x*x+y*y) continue;
                unsigned energy = 2*h, total = 2*x;
                if (energy <= total || energy*energy-total*total != 4*y*y) stop(7);
                ++count;
                invariant += energy*energy-total*total;
            }
    emit("LEAN-BEGIN\n");
    emit("theorem twoLegChecks : ((");
    number(count);
    emit(", ");
    number(invariant);
    emit(") : ℕ × ℕ) = (14,7332) := by decide\n"
         "\n");
    emit("theorem transverseRadius (e p : ℝ) (hp : 0 ≤ p) (he : p < e) :\n"
         "    (p/2)^2 + (Real.sqrt (e^2-p^2)/2)^2 = (e/2)^2 := by\n"
         "  have h : 0 ≤ (e-p)*(e+p) := mul_nonneg (by linarith) (by linarith)\n"
         "  have hs := Real.sq_sqrt (show 0 ≤ e^2-p^2 by nlinarith)\n"
         "  nlinarith\n"
         "\n"
         "#print axioms signedPathCounts\n"
         "#print axioms wickExcess\n"
         "#print axioms foldedPairs\n"
         "#print axioms budget\n"
         "#print axioms twoLegChecks\n"
         "#print axioms transverseRadius\n"
         "end JointMomentum\n");
    emit("LEAN-END\n");
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
