/* Periodic center signs and contact coefficients of the raw odd clover. */
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


/* On the four-torus of side four, coordinates use two bits per axis. */
static unsigned step(unsigned x, unsigned i) {
    unsigned shift=2*i;
    return (x & ~(3u<<shift)) | (((((x>>shift)&3u)+1)&3u)<<shift);
}
static unsigned sign_bit(unsigned x, unsigned axis) {
    unsigned bit=0;
    for (unsigned i=0;i<axis;++i) bit^=(x>>(2*i))&1u;
    return bit;
}
static void parent(void) {
    unsigned count=0;
    for (unsigned x=0;x<256;++x) for (unsigned i=0;i<4;++i)
        for (unsigned j=i+1;j<4;++j) {
            unsigned bit=sign_bit(x,i)^sign_bit(step(x,i),j)
                       ^sign_bit(step(x,j),i)^sign_bit(x,j);
            if (!bit) stop(7);
            ++count;
        }
    emit("LEAN-BEGIN\nimport Mathlib.Tactic.NormNum\nnamespace HaarClover\n");
    emit("theorem centerCount : ("); number(count);
    emit(" : ℕ) = 1536 := by decide\nLEAN-END\n");
    request(1,4,3);
}
static void child(unsigned x,unsigned y) {
    if (x!=4 || y!=3) stop(5);
    unsigned count=0;
    for (unsigned partner=1;partner<4;++partner)
        for (unsigned corners=0;corners<16;++corners) ++count;
    emit("LEAN-BEGIN\ntheorem siteCount : (");number(count);
    emit(" : ℕ) = 48 := by decide\n");
    emit("theorem contact : (48:ℚ)*3/4096 = 9/256 := by norm_num\nLEAN-END\n");
    request(2,4,3);
}
static void grandchild(unsigned x,unsigned y) {
    if (x!=4 || y!=3) stop(5);
    emit("LEAN-BEGIN\ntheorem quadratic : (48:ℚ)*((1/4-1/8)/(4*256)-(3/4096)/4) = -3/1024 := by norm_num\n");
    emit("#print axioms centerCount\n#print axioms siteCount\n#print axioms contact\n#print axioms quadratic\nend HaarClover\nLEAN-END\n");
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
