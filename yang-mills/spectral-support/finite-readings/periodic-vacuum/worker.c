/* Finite-period vacuum test: host-dispatched recursive PCP OS arithmetic checks. */
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
    unsigned vertices = 0;
    for (int x = 0; x <= 1; ++x) {
        for (int y = 0; y <= 1; ++y) {
            for (int z = 0; z <= 1; ++z) {
                int a = x-y, b = x+y-2*z;
                if (3*a*a + b*b > 4) stop(7);
                ++vertices;
            }
        }
    }
    emit("LEAN-BEGIN\nimport Mathlib.Tactic.Ring\nimport Mathlib.Tactic.Linarith\n"
         "import Mathlib.Data.Real.Basic\nnamespace PeriodicVacuum\n"
         "theorem corners : (");
    number(vertices);
    emit(" : ℕ) = 8 := by decide\n"
         "theorem components (x y z : ℝ) : 3*(x-y)^2+(x+y-2*z)^2 = "
         "2*((x-y)^2+(y-z)^2+(z-x)^2) := by ring\nLEAN-END\n");
    request(1,4,3);
}

static void child(unsigned x, unsigned y) {
    if (x != 4 || y != 3) stop(5);
    emit("LEAN-BEGIN\ntheorem pair_rows (p s a h k : ℝ) "
         "(hp : 0 ≤ p) (ha : 0 ≤ a) (hk : k ≤ (1+s)*h) : "
         "p*a*k ≤ (p+p*s)*a*h := by\n"
         "  calc\n    p*a*k ≤ p*a*((1+s)*h) := "
         "mul_le_mul_of_nonneg_left hk (mul_nonneg hp ha)\n"
         "    _ = (p+p*s)*a*h := by ring\nLEAN-END\n");
    request(2,4,3);
}

static void grandchild(unsigned x, unsigned y) {
    if (x != 4 || y != 3) stop(5);
    emit("LEAN-BEGIN\ntheorem occupation (u v : ℝ) (hu : 0 ≤ u) "
         "(hv : u ≤ v) : u/(1+u) ≤ v/(1+v) := by\n"
         "  apply (div_le_div_iff₀ (by linarith : 0 < 1+u) "
         "(by linarith : 0 < 1+v)).2\n  nlinarith\n"
         "#print axioms corners\n#print axioms components\n#print axioms pair_rows\n"
         "#print axioms occupation\nend PeriodicVacuum\nLEAN-END\n");
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
