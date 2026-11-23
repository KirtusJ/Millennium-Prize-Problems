/* Native stages use files passed as separate boot modules by the supervisor. */
static long open_input(const char *name) {
    long fd = os(2, (long)name, 0, 0);
    if (fd < 0) finish(1);
    return fd;
}
static void read_exact(long fd, unsigned char *p, size_t n) {
    while (n) {
        long count = os(0, fd, (long)p, (long)n);
        if (count <= 0 || (size_t)count > n) finish(2);
        p += count;
        n -= (size_t)count;
    }
}
static void require_end(long fd) {
    char extra;
    if (os(0, fd, (long)&extra, 1) != 0) finish(2);
}
static void copy_source(const char *name) {
    long fd = open_input(name);
    char block[256];
    for (;;) {
        long n = os(0, fd, (long)block, sizeof(block));
        if (n < 0 || (size_t)n > sizeof(block)) finish(2);
        if (n == 0) break;
        for (long j = 0; j < n; ++j) emit(block[j]);
    }
    if (os(3, fd, 0, 0)) finish(2);
}
#if defined(D4_BOUNDARY_SPECTRUM)
#include "../boundary-spectrum/guest.h"
#elif defined(D4_DUAL_SCALAR)
#include "../dual-scalar/guest.h"
#elif defined(D4_SCALAR_RESPONSE)
#include "../scalar-response/guest.h"
#elif defined(D4_ELECTRIC_SLAB)
#include "../electric-slab/guest.h"
#elif defined(D4_ORDINARY_LOOP)
#include "../ordinary-loop/guest.h"
#elif defined(D4_GRAPH_HOLONOMIES)
#include "../graph-holonomies/guest.h"
#elif defined(D4_ELECTRIC_SCALE)
#include "../electric-scale/guest.h"
#elif defined(D4_FINITE_READINGS)
#include "../finite-readings/guest.h"
#elif defined(D4_ADJOINT_BAND)
#include "../adjoint-band/guest.h"
#else
__attribute__((used,noreturn)) static void run(void) {
    long fd = open_input("request");
    unsigned char stage;
    read_exact(fd, &stage, 1);
    if (stage == 'F') {
        /* The chosen root 1/d gives the linear factor 1-d*q. */
        unsigned char d;
        read_exact(fd, &d, 1);
#ifdef D4_DIFFERENCE
        if (d != 1) finish(4);
#else
        if (d < 2) finish(4);
#endif
        emit(1);
        emit((char)d);
    } else if (stage == 'S') {
        unsigned char factor[2];
        read_exact(fd, factor, sizeof(factor));
        unsigned a = factor[0], d = factor[1];
        if (!a || !d) finish(4);
#ifdef D4_DIFFERENCE
        text("-- BEGIN PCP OS generated time-difference control\n");
        text("noncomputable def differenceShape (q : ℝ) : ℝ := ");
#else
        text("-- BEGIN PCP OS generated signed-spectrum control\n");
        text("noncomputable def signedShape (q : ℝ) : ℝ := ");
#endif
        number(a*a); text(" - "); number(2*a*d); text("*q + ");
        number(d*d); text("*q^2\n\n");
    } else if (stage == 'A') {
        copy_source("analytic");
        copy_source("certificate");
#ifdef D4_DIFFERENCE
        text(
            "/-- The native coefficients preserve positivity and annul only q=1. -/\n"
            "theorem differenceShapeControl (q : ℝ) :\n"
            "    differenceShape q = (1-q)^2 ∧ (differenceShape q = 0 ↔ q = 1) := by\n"
            "  have h : differenceShape q = (1-q)^2 := by unfold differenceShape; ring\n"
            "  constructor\n"
            "  · exact h\n"
            "  · rw [h, sq_eq_zero_iff, sub_eq_zero, eq_comm]\n\n"
            "#print axioms differenceNullSets\n#print axioms differenceCorrelation\n"
            "#print axioms positiveGapAboveKernel\n#print axioms shrinkingFilter\n"
            "#print axioms differenceShapeControl\n\nend Millennium.YangMills.D4\n");
#else
        text(
            "/-- Pointwise nonnegativity coexists with a zero at the late sample. -/\n"
            "theorem signedShapeControl : (∀ q : ℝ, 0 ≤ signedShape q) ∧\n"
            "    signedShape (1/2) = 0 ∧ signedShape 1 = 1 := by\n"
            "  refine ⟨fun q => ?_, by norm_num [signedShape], by norm_num [signedShape]⟩\n"
            "  unfold signedShape\n"
            "  nlinarith only [sq_nonneg (1-2*q)]\n\n"
            "/-- Reflected times T/2 and 3T/2 with the positive energy factor scaled out. -/\n"
            "theorem signedReflectionWitness :\n"
            "    2^2 * signedShape (1/2) + 2*2*(-1) * signedShape (1/4)\n"
            "      + (-1)^2 * signedShape (1/8) = -7/16 := by norm_num [signedShape]\n\n"
            "#print axioms tiltedWindow\n#print axioms positiveTimeTransfer\n"
            "#print axioms subrateOfEnvelope\n#print axioms energySupportOfEnvelope\n"
            "#print axioms supportFromPositiveAnchor\n#print axioms towerAtZero\n"
            "#print axioms towerAtPositiveTime\n#print axioms towerLateBound\n"
            "#print axioms laterMomentBound\n#print axioms collapseAfterPositiveTime\n"
            "#print axioms exteriorPairBound\n#print axioms renormalizedPairVanishes\n"
            "#print axioms scaledLowEnergyBound\n"
            "#print axioms signedShapeControl\n#print axioms signedReflectionWitness\n\n"
            "end Millennium.YangMills.D4\n");
#endif
    } else {
        finish(4);
    }
    require_end(fd);
    if (os(3, fd, 0, 0)) finish(2);
    flush();
    finish(0);
}
#endif
