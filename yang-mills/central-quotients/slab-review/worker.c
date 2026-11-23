/* Finite controls for the center projection and two-slice prediction. */
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

static unsigned sign_bit(unsigned mask, unsigned site) {
    return (mask >> site) & 1;
}

static unsigned ring_sum(unsigned twist) {
    unsigned sum = 0;
    for (unsigned spins = 0; spins < 16; ++spins) {
        unsigned weight = 1;
        for (unsigned x = 0; x < 4; ++x) {
            unsigned different = sign_bit(spins, x) ^ sign_bit(spins, (x + 1) % 4);
            if (x == 3) different ^= twist;
            weight *= different ? 1 : 9;
        }
        sum += weight;
    }
    return sum;
}

static void parent(void) {
    unsigned even = ring_sum(0), odd = ring_sum(1);
    if (even <= odd) stop(4);
    emit("LEAN-BEGIN\nimport Mathlib.Data.Real.Basic\nimport Mathlib.Tactic.Ring\nimport Mathlib.Tactic.Linarith\nimport Mathlib.Tactic.NormNum\n\nnamespace SlabReview\n"
         "theorem ringSums : (");
    number(even);
    emit(" : Nat) = 10^4 + 8^4 ∧ (");
    number(odd);
    emit(" : Nat) = 10^4 - 8^4 := by decide\n"
         "theorem denominator : (256 : Nat)*9^4 < 625*8^4 ∧ 369*8^4 < 256*9^4 := by decide\n"
         "LEAN-END\n");
    request(1, 4, 2);
}

static int phase(unsigned twist, const unsigned site[3]) {
    int value = 0;
    for (unsigned axis = 0; axis < 3; ++axis)
        value += (int)(sign_bit(twist, axis) * site[axis]);
    return value;
}

static void child(unsigned initial_side, unsigned stride) {
    if (initial_side != 4 || stride != 2) stop(5);
    unsigned good = 0, missing_seam = 0;
    for (unsigned side = initial_side; side <= 8; side += stride) {
        for (unsigned twist = 0; twist < 8; ++twist) {
            for (unsigned index = 0; index < side*side*side; ++index) {
                unsigned xyz[] = {index % side, (index / side) % side, index / (side*side)};
                for (unsigned axis = 0; axis < 3; ++axis) {
                    unsigned next[] = {xyz[0], xyz[1], xyz[2]};
                    next[axis] = (next[axis] + 1) % side;
                    int bit = (int)sign_bit(twist, axis);
                    int raw = phase(twist, next) - phase(twist, xyz);
                    int corrected = raw + (next[axis] == 0 ? (int)side * bit : 0);
                    if (corrected != bit) stop(6);
                    ++good;
                    if (raw != bit) ++missing_seam;
                }
            }
        }
    }
    emit("LEAN-BEGIN\ntheorem liftedEdges : 8*3*(4^3+6^3+8^3) = (");
    number(good);
    emit(" : Nat) := by decide\ntheorem lostSeams : 4*3*(4^2+6^2+8^2) = (");
    number(missing_seam);
    emit(" : Nat) := by decide\nLEAN-END\n");
    request(2, initial_side, stride);
}

static void grandchild(unsigned side, unsigned stride) {
    if (side != 4 || stride != 2) stop(5);
    unsigned error = 0, weight_sum = 0;
    for (int left = -1; left <= 1; left += 2)
        for (int here = -1; here <= 1; here += 2)
            for (int right = -1; right <= 1; right += 2) {
                unsigned weight = (left == here ? 3u : 1u) * (here == right ? 3u : 1u);
                int residual = 5*here - 2*(left + right);
                error += weight * (unsigned)(residual * residual);
                weight_sum += weight;
            }
    emit("LEAN-BEGIN\ntheorem interpolation : (");
    number(error);
    emit(" : Nat)*5 = 3*");
    number(25*weight_sum);
    emit(" := by decide\n"
         "theorem interpolationSquare (x g : ℝ) : (1+x^2)*(1-4*x*g+2*(1+x^2)*g^2) - (1-x^2) = 2*((1+x^2)*g-x)^2 := by ring\n"
         "theorem windowMass {low central high : ℝ} (a : low ≤ 1/512) (b : high ≤ 71/12800) (c : 3/200 ≤ low+central+high) : 3/400 ≤ central := by linarith\n"
         "theorem endpointRatio : (1-(12729:ℚ)/12871)/(1+12729/12871) = 71/12800 := by norm_num\n"
         "#print axioms interpolationSquare\n#print axioms windowMass\n#print axioms endpointRatio\n"
         "#print axioms ringSums\n#print axioms denominator\n#print axioms liftedEdges\n"
         "#print axioms lostSeams\n#print axioms interpolation\nend SlabReview\nLEAN-END\n");
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
