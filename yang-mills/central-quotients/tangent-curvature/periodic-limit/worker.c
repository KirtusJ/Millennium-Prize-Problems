/* Native checks for the isotropic periodic Wilson limit. */
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
    const unsigned side = 4;
    unsigned live = 0, retained = 0;
    for (unsigned site = 0; site < side*side*side*side; ++site) {
        unsigned time = site % side;
        live += 3 + (time + 1 == side);
        if (time + 1 < side) retained += 3;
    }
    emit("LEAN-BEGIN\n");
    emit("import Mathlib.Analysis.SpecificLimits.Basic\n"
         "import Mathlib.Analysis.SpecialFunctions.Log.Basic\n"
         "import Mathlib.Tactic.Linarith\n"
         "import Mathlib.Tactic.Ring\n"
         "import Mathlib.Tactic.NormNum\n"
         "open Filter\n"
         "open scoped Topology\n"
         "namespace PeriodicCriticality\n"
         "\n"
         "theorem seamExponent (v l : ℝ) :\n"
         "    (3/2:ℝ)*((3*v+l)-(3*v-3*l))=6*l := by ring\n"
         "\n");
    emit("theorem forestFour : ((");
    number(live);
    emit(", ");
    number(retained);
    emit(") : ℕ × ℕ) = (832, 576) := by decide\n"
         "\n");
    emit("LEAN-END\n");
    request(1, 4, 2);
}

static void child(unsigned width, unsigned normals) {
    if (width != 4 || normals != 2) stop(5);
    /* A reflected unit face is keyed by its two in-plane cell positions
       and two transverse even boundary coordinates. */
    unsigned hist[4][4][3][3] = {0};
    unsigned unique = 0, max_count = 0;
    for (unsigned x = 0; x < width; ++x)
        for (unsigned y = 0; y < width; ++y)
            for (unsigned z = 0; z < width; ++z)
                for (unsigned t = 0; t < width; ++t) {
                    unsigned count = ++hist[x][y][(z+1)/2][(t+1)/2];
                    if (count == 1) ++unique;
                    if (count > max_count) max_count = count;
                }
    emit("LEAN-BEGIN\n");
    emit("theorem faceMultiplicity (w b : ℝ) (hw : 0 ≤ w) (hb : b ≤ 4) :\n"
         "    b*w/8 ≤ w/2 := by nlinarith\n"
         "\n"
         "theorem dipoleCancels (f g h : ℝ) : (f+h)-(g+h)=f-g := by ring\n"
         "\n"
         "theorem energyIdentity (a v b : ℝ) (hu : a^2+v=1) :\n"
         "    2*b*(1-a) = b*v+b*(1-a)^2 := by nlinarith [congrArg (fun z : ℝ => b*z) hu]\n"
         "\n"
         "theorem pressureMean (Y K S x : ℝ) (hj : 3*Y ≤ S) (hb : S ≤ K+6*x) :\n"
         "    Y ≤ K/3+2*x := by linarith\n"
         "\n");
    emit("theorem faceCensus : ((");
    number(unique);
    emit(", ");
    number(max_count);
    emit(") : ℕ × ℕ) = (144, 4) := by decide\n"
         "\n");
    emit("LEAN-END\n");
    request(2, 4, 2);
}

static void grandchild(unsigned width, unsigned normals) {
    if (width != 4 || normals != 2) stop(5);
    unsigned n = 0, left = 32, right = 1;
    while (left >= right) {
        left *= 2;
        right *= 3;
        ++n;
    }
    emit("LEAN-BEGIN\n");
    emit("theorem slowMoment {q z b : ℝ} (hz : 0 ≤ z) (hzq : z < q) (hb : 0 < b) :\n"
         "    ∃ n : ℕ, z^n < b*q^n := by\n"
         "  have hq : 0 < q := lt_of_le_of_lt hz hzq\n"
         "  have hlim := tendsto_pow_atTop_nhds_zero_of_lt_one (div_nonneg hz hq.le)\n"
         "      ((div_lt_one hq).2 hzq)\n"
         "  obtain ⟨n,hn⟩ := ((tendsto_order.1 hlim).2 b hb).exists\n"
         "  refine ⟨n, ?_⟩\n"
         "  rw [div_pow] at hn\n"
         "  exact (div_lt_iff₀ (pow_pos hq n)).1 hn\n"
         "\n"
         "theorem spectralEdge (r : ℕ → ℝ) (a : ℕ → ℕ → ℝ) (c : ℕ → ℝ)\n"
         "    (hr : ∀ j, 0 ≤ r j ∧ r j ≤ 1)\n"
         "    (ha : ∀ j n, a j n ≤ (r j)^n)\n"
         "    (hl : ∀ n, Tendsto (fun j => a j n) atTop (𝓝 (c n)))\n"
         "    (hs : ∀ q : ℝ, 0 < q → q < 1 → ∃ b > 0, ∀ n : ℕ, b*q^n ≤ c n) :\n"
         "    Tendsto r atTop (𝓝 1) := by\n"
         "  apply tendsto_order.2\n"
         "  constructor\n"
         "  · intro z hz\n"
         "    by_cases hneg : z < 0\n"
         "    · exact Filter.Eventually.of_forall fun j => hneg.trans_le (hr j).1\n"
         "    have hq : z < (z+1)/2 := by linarith\n"
         "    obtain ⟨b,hb,h⟩ := hs ((z+1)/2) (by linarith) (by linarith)\n"
         "    obtain ⟨n,hn⟩ := slowMoment (le_of_not_gt hneg) hq hb\n"
         "    have hev := ((tendsto_order.1 (hl n)).1 _ (hn.trans_le (h n)))\n"
         "    filter_upwards [hev] with j hj\n"
         "    by_contra! hle\n"
         "    exact (not_lt_of_ge (pow_le_pow_left₀ (hr j).1 hle n)) (hj.trans_le (ha j n))\n"
         "  · intro z hz\n"
         "    exact Filter.Eventually.of_forall fun j => (hr j).2.trans_lt hz\n"
         "\n");
    emit("theorem slowExample : 32 * (2 : ℕ)^");
    number(n);
    emit(" < 3^");
    number(n);
    emit(" := by decide\n"
         "\n");
    emit("#print axioms seamExponent\n"
         "#print axioms forestFour\n"
         "#print axioms faceMultiplicity\n"
         "#print axioms dipoleCancels\n"
         "#print axioms energyIdentity\n"
         "#print axioms pressureMean\n"
         "#print axioms faceCensus\n"
         "#print axioms slowMoment\n"
         "#print axioms spectralEdge\n"
         "#print axioms slowExample\n"
         "end PeriodicCriticality\n");
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
