/* Exact cardinal spline and magnetic tail constants. */
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

static void fraction(Count a, Count b) {
    if (!b) stop(7);
    Count g = gcd(a,b);
    if (a/g > 0xffffffffu || b/g > 0xffffffffu) stop(7);
    number((unsigned)(a/g));
    emit(", ");
    number((unsigned)(b/g));
}


/* Centered cardinal-spline numerator; the denominator is degree factorial. */
static int spline_num(int shift, int degree) {
    int choose = 1, total = 0;
    for (int j=0; j<=8; ++j) {
        int x = shift+4-j, power = 1;
        if (x>0) {
            for (int k=0; k<degree; ++k) power *= x;
            total += (j%2 ? -1 : 1)*choose*power;
        }
        choose = choose*(8-j)/(j+1);
    }
    return total;
}

static void parent(void) {
    Count a = (Count)spline_num(0,7), b = 5040;
    emit("LEAN-BEGIN\n");
    emit("import Mathlib.Tactic.NormNum\nnamespace DirectionalTail\n");
    emit("theorem splineMass : ((");
    fraction(a,b);
    emit(") : ℕ × ℕ) = (151, 315) := by decide\n");
    emit("LEAN-END\n");
    request(1, 4, 3);
}

static void child(unsigned x, unsigned y) {
    if (x != 4 || y != 3) stop(5);
    int series = 0, choose = 1;
    for (int j=0; j<=6; ++j) {
        int k = j-3;
        series += (k%2 ? -1 : 1)*choose*spline_num(k,7);
        choose = choose*(6-j)/(j+1);
    }
    if (series<=0) stop(7);
    Count a = 70ull*(Count)spline_num(0,7)*(Count)series;
    Count b = 6ull*5040*5040;
    emit("LEAN-BEGIN\n");
    emit("theorem fourRays : ((");
    fraction(a,b);
    emit(") : ℕ × ℕ) = (25217, 1620) := by decide\n");
    emit("LEAN-END\n");
    request(2, 4, 3);
}

static void grandchild(unsigned x, unsigned y) {
    if (x != 4 || y != 3) stop(5);
    int second = -spline_num(0,5);
    if (second<=0) stop(7);
    Count a = 3432ull*(Count)spline_num(0,7)*(Count)second;
    Count b = 8ull*5040*120;
    emit("LEAN-BEGIN\n");
    emit("theorem normalAxis : ((");
    fraction(a,b);
    emit(") : ℕ × ℕ) = (43186, 315) := by decide\n");
    emit("#print axioms splineMass\n#print axioms fourRays\n#print axioms normalAxis\nend DirectionalTail\n");
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
