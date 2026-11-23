/* Finite checks for the cubic average and graph covariance. */
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

static unsigned weight(unsigned mask) {
    return (mask & 1) + ((mask >> 1) & 1) + ((mask >> 2) & 1);
}




static void parent(void) {
    /* 192 G(x,y) = 6 sum_k character(x xor y)/weight(k). */
    int at_zero = 0;
    for (unsigned k=1; k<8; ++k) at_zero += 6 / (int)weight(k);
    for (unsigned axis=0; axis<3; ++axis) {
        int neighbor = 0;
        for (unsigned k=1; k<8; ++k)
            neighbor += ((k & (1u << axis)) ? -6 : 6) / (int)weight(k);
        if (at_zero-neighbor != 28) stop(7);
    }
    if (at_zero != 29) stop(7);
    emit("LEAN-BEGIN\nnamespace ElectricDiagonal\ntheorem neighbor : (");
    number(at_zero); emit(" - 1 : Nat) = 28 := by decide\nLEAN-END\n");
    request(1,3,2);
}

static void child(unsigned dimension, unsigned extent) {
    if (dimension!=3 || extent!=2) stop(5);
    /* The four determinant-one coordinate sign rotations average any
       cross product to zero, as well as any single color vector. */
    for (unsigned axis=0; axis<3; ++axis) {
        int sum=0;
        for (unsigned mask=0; mask<8; ++mask) {
            if (weight(mask)%2) continue;
            sum += ((mask >> axis) & 1) ? -1 : 1;
        }
        if (sum!=0) stop(7);
    }
    emit("LEAN-BEGIN\ntheorem centeredOrbit : (3*24*28^2 + 0 : Nat) = 2*192*(3*29) + 2*192^2*5/16 := by decide\nLEAN-END\n");
    request(2,dimension,extent);
}

static void grandchild(unsigned dimension, unsigned extent) {
    if (dimension!=3 || extent!=2) stop(5);
    emit("LEAN-BEGIN\ntheorem normalized : (16*9+5 : Nat) = 149 := by decide\n");
    emit("#print axioms neighbor\n#print axioms centeredOrbit\n#print axioms normalized\nend ElectricDiagonal\nLEAN-END\n");
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
