/* One-site sector bounds: host-dispatched recursive PCP OS arithmetic checks. */
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
    emit("LEAN-BEGIN\nimport Mathlib.Tactic.NormNum\nimport Mathlib.Tactic.Linarith\n"
         "namespace CenterSectors\n"
         "theorem chebyshev_tail : (2:ℚ)/20000 * (6^19/121645100408832000) "
         "/ (1-6/20) < 1/1000000 := by norm_num\nLEAN-END\n");
    request(1,4,3);
}

static void child(unsigned x, unsigned y) {
    if (x != 4 || y != 3) stop(5);
    emit("LEAN-BEGIN\ntheorem occupation : let s : ℚ := 3*(494/532)^48; "
         "78/1000 < s/(1+s) := by norm_num\nLEAN-END\n");
    request(2,4,3);
}

static void grandchild(unsigned x, unsigned y) {
    if (x != 4 || y != 3) stop(5);
    emit("LEAN-BEGIN\ntheorem contrast_gate : (2730:ℚ)/100000 < 7/100 := by norm_num\n"
         "theorem band_margin : (155:ℚ)/1000 < 278/1000 - (318/1000000)/(3199/100000) "
         "- (708/1000)*(353/1000000)/(226/100000) := by norm_num\n"
         "#print axioms band_margin\n#print axioms chebyshev_tail\n#print axioms occupation\n"
         "#print axioms contrast_gate\nend CenterSectors\nLEAN-END\n");
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
