/* Enumerate actual permutations on three letters. Index the three rotations
   first, followed by their products with the reflection fixing letter zero. */
static unsigned action(unsigned p, unsigned x) {
    return (p%3u + (p<3u ? x : 3u-x))%3u;
}
__attribute__((used,noreturn)) static void run(void) {
    long fd = open_input("request");
    unsigned char stage;
    read_exact(fd, &stage, 1);
    if (stage == 'F') {
        unsigned char degree;
        read_exact(fd, &degree, 1);
        if (degree != 7) finish(4);
        for (unsigned a=0; a<6; ++a) for (unsigned b=0; b<6; ++b) {
            unsigned candidate=0;
            for (; candidate<6; ++candidate) {
                unsigned k=0;
                while (k<3 && action(candidate,k)==action(a,action(b,k))) ++k;
                if (k==3) break;
            }
            if (candidate==6) finish(4);
            emit((char)candidate);
        }
    } else if (stage == 'S') {
        unsigned char table[36], inv[6];
        unsigned hist[6] = {0};
        read_exact(fd, table, sizeof(table));
        for (unsigned k=0; k<36; ++k) if (table[k]>=6) finish(4);
        for (unsigned a=0; a<6; ++a) {
            unsigned b=0;
            while (b<6 && (table[6*a+b] || table[6*b+a])) ++b;
            if (b==6) finish(4);
            inv[a]=(unsigned char)b;
        }
        for (unsigned a=0; a<6; ++a) for (unsigned b=0; b<6; ++b) {
            unsigned ab=table[6*a+b];
            unsigned aba=table[6*ab+inv[a]];
            hist[table[6*aba+inv[b]]]++;
        }
        text("-- BEGIN PCP OS generated shared-path control\n");
        text("def table : List Nat := [");
        for (unsigned k=0; k<36; ++k) { if (k) text(", "); number(table[k]); }
        text("]\n\ndef histogram : List Nat := [");
        for (unsigned k=0; k<6; ++k) { if (k) text(", "); number(hist[k]); }
        text("]\n\ntheorem tableComposes : table = (List.range 6).flatMap ");
        text("(fun a => (List.range 6).map (compose a)) := by decide\n\n");
        text("theorem sharedWord : histogram = [18,9,9,0,0,0] ∧ ");
        text("histogram = (List.range 6).map (fun g => ((List.range 6).flatMap ");
        text("(fun a => (List.range 6).map (commutator a))).count g) := by decide\n\n");
    } else if (stage == 'A') {
        copy_source("analytic");
        copy_source("certificate");
        text("#print axioms reciprocalSecant\n#print axioms reciprocalMean\n#print axioms reverseTest\n");
        text("#print axioms explainedVariance\n#print axioms independentChannels\n#print axioms spectralThreshold\n");
        text("#print axioms casimirLoss\n#print axioms goodClock\n#print axioms discardedClock\n");
        text("#print axioms varianceBudget\n#print axioms reflectionDoubling\n#print axioms sixStapleTime\n");
        text("#print axioms survivalAtMostOne\n");
        text("#print axioms lossExpansion\n#print axioms stapleDispersion\n#print axioms reciprocalDispersion\n");
        text("#print axioms limitingBias\n");
        text("#print axioms productError\n#print axioms tableComposes\n#print axioms sharedWord\n");
        text("\nend Millennium.YangMills.D4.GraphHolonomies\n");
    } else finish(4);
    require_end(fd);
    if (os(3, fd, 0, 0)) finish(2);
    flush();
    finish(0);
}
