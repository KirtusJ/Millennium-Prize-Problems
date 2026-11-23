/* Freestanding x86-64 PCP OS guest. Each D4 line encodes up to 32 source bytes. */
#include <stddef.h>

static long os(long n, long a, long b, long c) {
    long result;
    __asm__ volatile ("syscall" : "=a"(result) : "a"(n), "D"(a), "S"(b), "d"(c)
                      : "rcx", "r11", "memory");
    return result;
}
static _Noreturn void finish(long code) {
    os(60, code, 0, 0);
    __builtin_unreachable();
}
static char frame[68] = {'D','4',' '};
static unsigned used;
static void flush(void) {
    if (!used) return;
    frame[3 + 2 * used] = '\n';
    long length = 4 + 2 * used;
    if (os(1, 1, (long)frame, length) != length) finish(3);
    used = 0;
}
static void emit(char c) {
    static const char hex[] = "0123456789abcdef";
    unsigned v = (unsigned char)c;
    frame[3 + 2 * used] = hex[v >> 4];
    frame[4 + 2 * used] = hex[v & 15];
    if (++used == 32) flush();
}
static void text(const char *s) { while (*s) emit(*s++); }
#ifndef D4_DIAGONAL
static void number(unsigned n) {
    if (n >= 10) number(n / 10);
    emit((char)('0' + n % 10));
}
#ifndef D4_POSITIVE_TIME
static void weights(const int change[7]) {
    text("[");
    for (int j = 0; j <= 6; ++j) {
        if (j) text(", ");
        int n = (j ? 100 : 0) + change[j];
        if (n < 0) finish(4);
        number((unsigned)n);
    }
    text("]");
}
#endif
#endif
#ifdef D4_POSITIVE_TIME
#include "positive-time/guest.h"
#else
__attribute__((used,noreturn)) static void run(void) {
    char buf[256];
    long fd = os(2, (long)"template", 0, 0);
    if (fd < 0) finish(1);
    for (;;) {
        long count = os(0, fd, (long)buf, sizeof(buf));
        if (count < 0 || count > (long)sizeof(buf)) finish(2);
        if (!count) break;
        for (long i = 0; i < count; ++i) emit(buf[i]);
    }
    if (os(3, fd, 0, 0) != 0) finish(2);
#ifdef D4_DIAGONAL
    /* Append the reviewed array counterexample to the finite-measure argument. */
    text(
        "-- BEGIN PCP OS generated array control\n"
        "/-- A diagonal alone does not constrain an array without a common measure in each row. -/\n"
        "theorem arbitraryArrayControl :\n"
        "    (∀ n : ℕ, Tendsto (fun k : ℕ => if k = n then (0 : ℝ) else 1) atTop (𝓝 1)) ∧\n"
        "    (∀ k : ℕ, (if k = k then (0 : ℝ) else 1) = 0) := by\n"
        "  constructor\n"
        "  · intro n\n"
        "    apply Tendsto.congr' _ (tendsto_const_nhds (x := (1 : ℝ)))\n"
        "    filter_upwards [eventually_gt_atTop n] with k hk\n"
        "    simp [ne_of_gt hk]\n"
        "  · intro k\n"
        "    simp\n"
        "\n"
        "#print axioms nullTailOfWeakLimit\n"
        "#print axioms diagonalSpectralExclusion\n"
        "#print axioms boundedWindow\n"
        "#print axioms disappearingWeight\n"
        "#print axioms arbitraryArrayControl\n"
        "\n"
        "end Millennium.YangMills.D4\n"
    );
#else
    /* Coefficients of (X-1)^4 (2X-1)(4X-1), constant term first. */
    int a[7] = {1}, zero[7] = {0};
    const int scale[6] = {1,1,1,1,2,4};
    for (int d = 0; d < 6; ++d) {
        for (int j = d + 1; j > 0; --j) a[j] = scale[d] * a[j-1] - a[j];
        a[0] = -a[0];
    }
    text("-- BEGIN PCP OS generated finite certificate\n");
    text("def referenceWeights : List Nat := "); weights(zero);
    text("\ndef alternativeWeights : List Nat := "); weights(a);
    text("\n\ntheorem indistinguishableReadings :\n");
    text("    sixReadings referenceWeights = [600, 2100, 9100, 44100, 6300, 136500] ∧\n");
    text("    sixReadings alternativeWeights = sixReadings referenceWeights ∧\n");
    text("    referenceWeights.head? = some 0 ∧ alternativeWeights.head? = some 1 := by decide\n\n");
    text("#print axioms decayAtRoundedTime\n#print axioms noTransferMassAbove\n#print axioms projectionVanishesOfDense\n");
    text("#print axioms denseProjectionOfMomentBounds\n#print axioms endpointAtom\n#print axioms indistinguishableReadings\n\nend Millennium.YangMills.D4\n");
#endif
    flush(); finish(0);
}
#endif
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
