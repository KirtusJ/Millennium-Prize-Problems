/* Link bits 2*j and 2*j+1 meet the vertex on opposite sides of axis j. */
static unsigned parity6(unsigned n) {
    unsigned odd = 0;
    for (unsigned i = 0; i < 6; ++i) odd ^= (n >> i) & 1;
    return odd;
}
__attribute__((used,noreturn)) static void run(void) {
    long fd = open_input("request");
    unsigned char stage;
    read_exact(fd, &stage, 1);
    if (stage == 'F') {
        unsigned char degree;
        read_exact(fd, &degree, 1);
        if (degree != 6) finish(4);
        for (unsigned i = 0; i < degree; ++i)
            for (unsigned j = i+1; j < degree; ++j)
                if (i/2 != j/2) emit((char)((1u<<i) | (1u<<j)));
    } else if (stage == 'S') {
        unsigned char rows[12], flat[64];
        read_exact(fd, rows, sizeof(rows));
        text("-- BEGIN PCP OS generated star flux\n");
        text("def starRows : List Nat := [");
        for (unsigned i = 0; i < 12; ++i) {
            if (i) text(", ");
            number(rows[i]);
        }
        text("]\n\ndef starFlat : List Nat := [");
        unsigned count = 0;
        for (unsigned z = 0; z < 64; ++z) {
            unsigned seen = 0;
            for (unsigned j = 0; j < 12; ++j) seen |= parity6(rows[j] & z);
            if (!seen) {
                if (count) text(", ");
                number(z);
                flat[count++] = (unsigned char)z;
            }
        }
        text("]\n\ndef starFlux : List Nat := [");
        unsigned emitted = 0;
        for (unsigned b = 0; b < 64; ++b) {
            unsigned seen = 0;
            for (unsigned i = 0; i < count; ++i) seen |= parity6(b & flat[i]);
            if (!seen) {
                if (emitted++) text(", ");
                number(b);
            }
        }
        text("]\n\nset_option maxRecDepth 8192\nset_option maxHeartbeats 1600000\n");
        text("theorem starCalculation : faceKernel starRows = starFlat ∧ starFlat = [0,63] ∧ ");
        text("annihilator starFlat = starFlux ∧ starFlux = (List.range 64).filter ");
        text("(fun b => bitParity b == 0) ∧ starFlux.length = 32 := by decide\n\n");
        /* One representative per flat-twist coset: the high bit is clear. */
        unsigned counts[25] = {0};
        for (unsigned z = 0; z < 32; ++z) {
            unsigned energy = 0;
            for (unsigned j = 0; j < 12; ++j) energy += 2*parity6(z & rows[j]);
            counts[energy]++;
        }
        text("def energyHistogram : List (Nat × Nat) := [");
        unsigned first = 1;
        for (unsigned e = 0; e <= 24; ++e) {
            if (!counts[e]) continue;
            if (!first) text(", ");
            text("("); number(e); text(", "); number(counts[e]); text(")");
            first = 0;
        }
        text("]\n\ntheorem starSpectrum : energyHistogram = [(0,1),(8,6),(12,16),(16,9)] ∧ ");
        text("((List.range 25).map (fun e => (e, ((List.range 32).map ");
        text("(twistEnergy starRows)).count e))).filter (fun p => p.2 != 0) = energyHistogram ");
        text(":= by decide\n\n");
    } else if (stage == 'A') {
        copy_source("analytic");
        copy_source("certificate");
        text("#print axioms edgeTransform\n#print axioms chainForm\n#print axioms interiorRow\n");
        text("#print axioms collectRows\n#print axioms prefixBound\n");
        text("#print axioms freeEnd\n#print axioms shellVariation\n#print axioms scaledEnergy\n");
        text("#print axioms centerDisk\n#print axioms centerError\n#print axioms wrongEndpoint\n");
        text("#print axioms lowTwistMass\n#print axioms twistLeakage\n#print axioms starSpectrum\n");
        text("#print axioms meshTangent\n#print axioms meshSurvival\n");
        text("#print axioms starCalculation\n\nend Millennium.YangMills.D4.ElectricScale\n");
    } else finish(4);
    require_end(fd);
    if (os(3, fd, 0, 0)) finish(2);
    flush();
    finish(0);
}
