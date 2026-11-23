/* One-site static floor: host-dispatched recursive PCP OS arithmetic checks. */
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
    emit("LEAN-BEGIN\nimport Mathlib.Tactic.NormNum\nimport Mathlib.Tactic.Ring\n"
         "namespace StaticFloor\ntheorem odd_orbit (d : ℚ) : "
         "d^2+(-d)^2+0^2 = 2*d^2 := by ring\nLEAN-END\n");
    request(1,4,3);
}

static void child(unsigned x, unsigned y) {
    if (x != 4 || y != 3) stop(5);
    emit("LEAN-BEGIN\ntheorem share : let floor : ℚ := 250/1000000; "
         "let rem : ℚ := 2/10000000000; 999999/1000000 < floor/(floor+rem) "
         ":= by norm_num\nLEAN-END\n");
    request(2,4,3);
}

static void grandchild(unsigned x, unsigned y) {
    if (x != 4 || y != 3) stop(5);
    emit("LEAN-BEGIN\ntheorem constant_cancels (d : ℚ) : "
         "-d+(13/3)*d-(13/3)*d+d=0 := by ring\n"
         "theorem signed_share : (74:ℚ)/100 < 1132/(1132+391) := by norm_num\n"
         "#print axioms signed_share\n#print axioms odd_orbit\n#print axioms share\n"
         "#print axioms constant_cancels\nend StaticFloor\nLEAN-END\n");
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
