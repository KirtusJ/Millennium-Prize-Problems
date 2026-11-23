#include "box_mod.h"
static void print_list(const unsigned char *v, int length) {
    text("[");
    for (int i=0;i<length;++i) { if (i) text(", "); number(v[i]); }
    text("]");
}
__attribute__((used,noreturn)) static void run(void) {
    long fd=open_input("request");
    unsigned char stage;
    read_exact(fd,&stage,1);
    if (stage=='F') {
        unsigned char code,out[9],cal[5];
        read_exact(fd,&code,1);
        if (code!=10) finish(4);
        compute(0,0,out);
        calibrated(1,cal);
        for (int i=0;i<8;++i) emit((char)out[i]);
        for (int i=0;i<5;++i) emit((char)cal[i]);
    } else if (stage=='S') {
        unsigned char v[13],space[5];
        read_exact(fd,v,13);
        calibrated(2,space);
        text("-- BEGIN PCP OS generated Wilson response residues\n");
        text("def residues : List Nat := "); print_list(v,8); text("\n\n");
        text("def timeResidues : List Nat := "); print_list(v+8,5); text("\n\n");
        text("def spaceResidues : List Nat := "); print_list(space,5); text("\n\n");
        text("theorem boxResidues : boxFractions.length = residues.length ∧\n");
        text("    (boxFractions.zipWith agrees residues).all id = true := by decide\n\n");
        text("theorem triangleResidues : residues[3]? = some "); number(v[3]);
        text(" ∧ residues[7]? = some "); number(v[7]);
        text(" ∧ residues[3]? ≠ residues[7]? := by decide\n\n");
        text("theorem nullResidues : (timeCalibration.zipWith agrees timeResidues).all id = true ∧\n");
        text("    (spaceCalibration.zipWith agrees spaceResidues).all id = true ∧\n");
        text("    timeCalibration.length = timeResidues.length ∧ spaceCalibration.length = spaceResidues.length := by decide\n\n");
    } else if (stage=='A') {
        copy_source("analytic"); copy_source("certificate");
        text("#print axioms tilt\n#print axioms tiltCovariance\n#print axioms radialDerivative\n");
        text("#print axioms integratedResponse\n#print axioms firstRadialTerm\n#print axioms relativeSquare\n");
        text("#print axioms singleRadial\n#print axioms radialMatch\n#print axioms sphereAtUnit\n");
        text("#print axioms wilsonRelative\n#print axioms matchedRelative\n#print axioms separatedSign\n");
        text("#print axioms boxResidues\n#print axioms triangleResidues\n");
        text("#print axioms crossNull\n#print axioms timeFilter\n#print axioms spaceFilter\n#print axioms nullResidues\n");
        text("end Millennium.YangMills.D4.ScalarResponse\n");
    } else finish(4);
    require_end(fd);
    if (os(3,fd,0,0)) finish(2);
    flush(); finish(0);
}
