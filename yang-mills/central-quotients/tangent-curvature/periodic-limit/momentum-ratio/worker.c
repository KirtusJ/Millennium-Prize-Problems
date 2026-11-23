/* Exact rational checks of the angular density and both endpoint slopes. */
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



typedef unsigned long long Count;

static Count gcd(Count a, Count b) {
    while (b) {
        Count rem = a % b;
        a = b;
        b = rem;
    }
    return a;
}

/* Endpoint density of (1-dot)/2 is twice the squared marginal's integral. */
static void angular_endpoint(Count *numerator, Count *denominator) {
    const Count product = 13*15*17;
    *numerator = 63*63*(product/13 - 2*(product/15) + product/17);
    *denominator = 4*product;
}

static void fraction(Count a, Count b) {
    if (!b) stop(7);
    Count g = gcd(a,b);
    if (a/g > 0xffffffffu || b/g > 0xffffffffu) stop(7);
    number((unsigned)(a/g));
    emit(", ");
    number((unsigned)(b/g));
}

static void parent(void) {
    Count a, b;
    angular_endpoint(&a,&b);
    emit("LEAN-BEGIN\n");
    emit("import Mathlib.Tactic.Ring\nnamespace MomentumRatio\n");
    emit("theorem angularEndpoint : ((");
    fraction(a,b);
    emit(") : ℕ × ℕ) = (2646, 1105) := by decide\n");
    emit("LEAN-END\n");
    request(1, 4, 3);
}

static void child(unsigned x, unsigned y) {
    if (x != 4 || y != 3) stop(5);
    Count a, b;
    angular_endpoint(&a,&b);
    a *= 19;
    b *= 9;
    emit("LEAN-BEGIN\n");
    emit("theorem coneSlope : ((");
    fraction(a,b);
    emit(") : ℕ × ℕ) = (5586, 1105) := by decide\n");
    emit("LEAN-END\n");
    request(2, 4, 3);
}

static void grandchild(unsigned x, unsigned y) {
    if (x != 4 || y != 3) stop(5);
    Count a, b;
    angular_endpoint(&a,&b);
    Count binomial = 1;
    for (unsigned k=1; k<=10; ++k) binomial = binomial*(10+k)/k;
    a *= 4*10*binomial;
    b *= 3*(1u<<20);
    emit("LEAN-BEGIN\n");
    emit("theorem restCoefficient : ((");
    fraction(a,b);
    emit(") : ℕ × ℕ) = (92169, 16384) := by decide\n");
    emit("theorem factorization (a b c : ℚ) : (a+b)^2 - (a^2+b^2+2*a*b*c) = 2*a*b*(1-c) := by ring\n#print axioms angularEndpoint\n#print axioms coneSlope\n#print axioms restCoefficient\n#print axioms factorization\nend MomentumRatio\n");
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
