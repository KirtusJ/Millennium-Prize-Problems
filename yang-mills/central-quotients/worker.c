/* One bounded PCP OS user process. Its input is (depth, first axis, second axis).
   The root searches a witness. Its child verifies sign choices and its grandchild
   counts torus sectors. Each node emits the Lean declarations for its own result. */
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

/* Signed labels 1,2,3,4 stand for the Hamilton basis 1,i,j,k. */
static int product(int x, int y) {
    static const int positive[4][4] = {
        {1, 2, 3, 4}, {2, -1, 4, -3}, {3, -4, -1, 2}, {4, 3, -2, -1}
    };
    int sign = 1;
    if (x < 0) { x = -x; sign = -sign; }
    if (y < 0) { y = -y; sign = -sign; }
    return sign * positive[x-1][y-1];
}

static int twist(int x, int y) { return product(x,y) != product(y,x); }

static void request(unsigned depth, unsigned a, unsigned b) {
    emit("NEXT "); number(depth); emit(" "); number(a); emit(" "); number(b); emit("\n");
}

static void root(void) {
    for (int a = 1; a <= 4; ++a) {
        for (int b = 1; b <= 4; ++b) {
            if (!twist(a,b)) continue;
            emit("LEAN-BEGIN\nimport Model\n\nnamespace YangMills.CentralQuotient\n\n");
            emit("theorem product_up_to_sign (a b : Axis) (s t : Bool) :\n"
                 "    let p := mul (lift a s) (lift b t)\n"
                 "    let q := mul (lift b t) (lift a s)\n"
                 "    p = if twisted a b then neg q else q := by\n"
                 "  cases a <;> cases b <;> cases s <;> cases t <;> decide\n\n");
            emit("theorem commute_iff (a b : Axis) (s t : Bool) :\n"
                 "    mul (lift a s) (lift b t) = mul (lift b t) (lift a s) ↔\n"
                 "    twisted a b = false := by\n"
                 "  cases a <;> cases b <;> cases s <;> cases t <;> decide\nLEAN-END\n");
            request(1,a,b);
            return;
        }
    }
    stop(4);
}

static void child(int a, int b) {
    static const char *names[4] = {".e", ".i", ".j", ".k"};
    for (int s = -1; s <= 1; s += 2)
        for (int t = -1; t <= 1; t += 2)
            if (!twist(s*a,t*b)) stop(5);
    emit("LEAN-BEGIN\n\ntheorem witness (s t : Bool) :\n    mul (lift ");
    emit(names[a-1]); emit(" s) (lift "); emit(names[b-1]);
    emit(" t) ≠ mul (lift "); emit(names[b-1]); emit(" t) (lift ");
    emit(names[a-1]); emit(" s) := by\n  cases s <;> cases t <;> decide\n\n");
    emit("theorem flatLift_iff {ι : Type} (hol : ι → Axis) :\n"
         "    HasFlatLift hol ↔ ∀ s t, twisted (hol s) (hol t) = false := by\n"
         "  constructor\n"
         "  · rintro ⟨sign, h⟩ s t\n"
         "    exact (commute_iff _ _ (sign s) (sign t)).mp (h s t)\n"
         "  · intro h\n"
         "    exact ⟨fun _ => false, fun s t => (commute_iff _ _ false false).mpr (h s t)⟩\nLEAN-END\n");
    request(2,a,b);
}

/* An edge starts at the vertex with coordinate 0 in its own direction.
   Its two other coordinates specify its adjacent faces. */
static void cube_proofs(void) {
    unsigned incident[12], position = 0;
    for (unsigned vertex = 0; vertex < 8; ++vertex) {
        for (unsigned direction = 0; direction < 3; ++direction) {
            if (vertex & (1u << direction)) continue;
            unsigned faces = 0;
            for (unsigned axis = 0; axis < 3; ++axis) {
                if (axis == direction) continue;
                unsigned side = (vertex >> axis) & 1u;
                faces |= 1u << (2*axis + side);
            }
            incident[position++] = faces;
        }
    }
    unsigned h[64] = {0};
    for (unsigned signs = 0; signs < 4096; ++signs) {
        unsigned mask = 0;
        for (unsigned edge = 0; edge < 12; ++edge)
            if (signs & (1u << edge)) mask ^= incident[edge];
        ++h[mask];
    }
    unsigned sum = 0;
    for (unsigned m = 0; m < 64; ++m) {
        unsigned negative = 0;
        for (unsigned i = 0; i < 6; ++i) negative += (m >> i) & 1u;
        if (h[m] != ((negative & 1u) ? 0 : h[0])) stop(7);
        sum += h[m] * (1u << (12 - 2*negative));
    }
    emit("theorem closed_cube_surfaces : closedFaceMasks = [0, 63] := by decide +kernel\n\n"
         "set_option maxRecDepth 20000 in\nset_option maxHeartbeats 0 in\n"
         "theorem cube_face_fibres :\n"
         "    ((List.range 64).all fun m => faceMultiplicities[m]! ==\n"
         "      (if negativeFaces m % 2 == 0 then ");
    number(h[0]);
    emit(" else 0)) = true := by decide +kernel\n\n"
         "set_option maxRecDepth 20000 in\nset_option maxHeartbeats 0 in\n"
         "theorem cube_weight_at_identity : scaledCubeSum = ");
    number(sum);
    emit(" := by decide +kernel\n\n");
}

static void leaf(void) {
    unsigned histogram[64] = {0};
    for (unsigned code = 0; code < 256; ++code) {
        int axis[4];
        for (unsigned k = 0; k < 4; ++k) axis[k] = 1 + ((code >> (2*k)) & 3);
        unsigned mask = 0, bit = 0;
        for (unsigned i = 0; i < 4; ++i)
            for (unsigned j = i+1; j < 4; ++j)
                mask |= (unsigned)twist(axis[i], axis[j]) << bit++;
        ++histogram[mask];
    }
    unsigned nonzero_masks = 0, multiplicity = 0;
    for (unsigned mask = 1; mask < 64; ++mask) {
        if (!histogram[mask]) continue;
        ++nonzero_masks;
        if (!multiplicity) multiplicity = histogram[mask];
        if (multiplicity != histogram[mask]) stop(6);
    }
    emit("LEAN-BEGIN\n\nset_option maxRecDepth 100000 in\n"
         "set_option maxHeartbeats 0 in\n"
         "theorem four_cycle_census :\n"
         "    fluxes.length = 256 ∧ fluxes.count 0 = ");
    number(histogram[0]);
    emit(" ∧\n    (fluxes.eraseDups.erase 0).length = "); number(nonzero_masks);
    emit(" ∧\n    ((fluxes.eraseDups.erase 0).all (fun m => fluxes.count m == ");
    number(multiplicity);
    emit(")) = true := by decide +kernel\n\n");
    emit("theorem pfaffian_zero (a b c d : Axis) :\n"
         "    ((twisted a b && twisted c d) ^^ (twisted a c && twisted b d)) =\n"
         "      (twisted a d && twisted b c) := by\n"
         "  cases a <;> cases b <;> cases c <;> cases d <;> decide\n\n");
    cube_proofs();
    emit("end YangMills.CentralQuotient\n\n");
    static const char *theorems[] = {"product_up_to_sign","commute_iff","witness","flatLift_iff",
                                    "four_cycle_census","pfaffian_zero","closed_cube_surfaces",
                                    "cube_face_fibres","cube_weight_at_identity"};
    for (unsigned i = 0; i < sizeof theorems/sizeof theorems[0]; ++i) {
        emit("#print axioms YangMills.CentralQuotient."); emit(theorems[i]); emit("\n");
    }
    emit("LEAN-END\n");
}

__attribute__((used,noreturn)) static void run(void) {
    static unsigned char input[4];
    long fd = syscall3(2, (long)"task.bin", 0, 0);
    if (fd < 0 || syscall3(0, fd, (long)input, sizeof input) != 3 ||
        syscall3(0, fd, (long)(input+3), 1) != 0 || syscall3(3, fd, 0, 0) != 0) stop(2);
    if (!input[0] && !input[1] && !input[2]) root();
    else if ((input[0] == 1 || input[0] == 2) &&
             input[1] >= 1 && input[1] <= 4 && input[2] >= 1 && input[2] <= 4) {
        if (!twist(input[1],input[2])) stop(5);
        if (input[0] == 1) child(input[1],input[2]); else leaf();
    } else stop(2);
    stop(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
