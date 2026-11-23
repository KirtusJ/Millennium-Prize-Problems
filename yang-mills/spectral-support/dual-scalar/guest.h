#include "../scalar-response/box_mod.h"
#include "fourier_mod.h"
static void list_literal(const unsigned char *v,int n) {
    text("[");
    for(int i=0;i<n;++i){if(i)text(", ");number(v[i]);}
    text("]");
}
__attribute__((used,noreturn)) static void run(void) {
    (void)calibrated;
    long fd=open_input("request");
    unsigned char stage;
    read_exact(fd,&stage,1);
    if(stage=='F') {
        unsigned char code,c[9],s[9];read_exact(fd,&code,1);
        if(code!=11)finish(4);
        compute(0,0,c);compute(3,0,s);
        const int indices[3]={8,3,7};
        for(int k=0;k<3;++k){emit((char)c[indices[k]]);emit((char)s[indices[k]]);}
    }else if(stage=='S') {
        unsigned char v[6],t[5],skew[5];read_exact(fd,v,6);fourier_readings(t,0);fourier_readings(skew,1);
        text("-- BEGIN PCP OS generated dual response checks\n");
        text("def boundaryResidues : List Nat := ");list_literal(v,6);text("\n\n");
        text("def twistResidues : List Nat := ");list_literal(t,5);text("\n\n");
        text("def skewResidues : List Nat := ");list_literal(skew,5);text("\n\n");
        text("theorem measuredBoundary : boundaryFractions.length=boundaryResidues.length ∧\n");
        text("    (boundaryFractions.zipWith (agrees 101) boundaryResidues).all id=true := by decide\n\n");
        text("theorem measuredTwist : twistFractions.length=twistResidues.length ∧\n");
        text("    (twistFractions.zipWith (agrees 193) twistResidues).all id=true := by decide\n\n");
        text("theorem measuredSkew : skewFractions.length=skewResidues.length ∧\n");
        text("    (skewFractions.zipWith (agrees 193) skewResidues).all id=true := by decide\n\n");
    }else if(stage=='A') {
        copy_source("analytic");copy_source("certificate");
        text("#print axioms schurReciprocity\n#print axioms sourceComplement\n#print axioms oddCycle\n");
        text("#print axioms complementaryKernel\n#print axioms generalAction\n#print axioms squaredDeficit\n");
        text("#print axioms centeredEven\n#print axioms radialDifference\n#print axioms localMixed\n");
        text("#print axioms halfDiagonal\n#print axioms actionDependence\n#print axioms asymptoticRatio\n");
        text("#print axioms uniqueNumerator\n#print axioms certifiedCube\n#print axioms certifiedStar\n");
        text("#print axioms twistedSignal\n#print axioms measuredBoundary\n#print axioms measuredTwist\n");
        text("#print axioms certifiedSkewCube\n#print axioms certifiedSkewStar\n#print axioms skewSignal\n#print axioms measuredSkew\n");
        text("end Millennium.YangMills.D4.DualScalar\n");
    }else finish(4);
    require_end(fd);if(os(3,fd,0,0))finish(2);
    flush();finish(0);
}
