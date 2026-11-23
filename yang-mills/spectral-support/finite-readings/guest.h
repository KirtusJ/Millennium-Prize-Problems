/* Four-link electric plaquette. The stages exchange two Casimir exponents. */
__attribute__((used,noreturn)) static void run(void) {
    long fd = open_input("request");
    unsigned char stage;
    read_exact(fd, &stage, 1);
    if (stage == 'F') {
        unsigned char links;
        read_exact(fd, &links, 1);
        if (links != 4) finish(4);
        for (unsigned n=1; n<=2; ++n) emit((char)(links*n*(n+2)/4));
    } else if (stage == 'S') {
        unsigned char exponent[2];
        read_exact(fd, exponent, 2);
        if (exponent[0] != 3 || exponent[1] != 8) finish(4);
        unsigned scale = 1u << (exponent[1]-exponent[0]);
        unsigned fundamental = 1, adjoint = 8u*8u;
        text("-- BEGIN PCP OS generated electric readings\n");
        text("def scaledEntries : List (ℤ × ℤ) := [");
        for (unsigned k=0; k<4; ++k) {
            if (k) text(", ");
            text("("); number(fundamental+adjoint); text(", ");
            if (fundamental < adjoint) {
                text("-"); number(adjoint-fundamental);
            } else number(fundamental-adjoint);
            text(")");
            fundamental *= scale;
        }
        text("]\n\n");
        text("theorem generatedReadings : scaledEntries = (List.range 4).map ");
        text("(fun k => (((32:ℤ)^k+64), ((32:ℤ)^k-64))) := by decide\n\n");
    } else if (stage == 'A') {
        copy_source("analytic");
        copy_source("certificate");
        text("#print axioms factorGram\n#print axioms gramTransfer\n");
        text("#print axioms openWindow\n#print axioms softMass\n#print axioms quadraticReadings\n");
        text("#print axioms threeReadingError\n#print axioms recoverDifferences\n");
        text("#print axioms shiftPowers\n#print axioms polynomialChain\n#print axioms oddMomentRecovery\n");
        text("#print axioms endpointSquare\n#print axioms windowMinorant\n#print axioms excludeInterior\n");
        text("#print axioms polarizedSum\n#print axioms diagonalCompletion\n#print axioms freeWitness\n");
        text("#print axioms residualTail\n#print axioms weakMagneticBand\n#print axioms interactingMargin\n");
        text("#print axioms coreKernel\n#print axioms adverseKernel\n#print axioms localLinkKinetic\n");
        text("#print axioms tailProduct\n#print axioms casimirProduct\n#print axioms rayleighCut\n");
        text("#print axioms gapEnclosure\n#print axioms sturmCounts\n#print axioms rotorCutError\n");
        text("#print axioms positiveTimeKernel\n#print axioms positiveTimeMargin\n");
        text("#print axioms generatedReadings\n\nend Millennium.YangMills.D4.FiniteReadings\n");
    } else finish(4);
    require_end(fd);
    if (os(3, fd, 0, 0)) finish(2);
    flush();
    finish(0);
}
