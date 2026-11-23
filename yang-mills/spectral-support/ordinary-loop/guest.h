/* Enumerate Wick pairings on labeled slots. No edge joins two slots from
   the same normal-ordered factor. */
static unsigned count_pairs(unsigned mask) {
    if (!mask) return 1;
    unsigned a=0, sum=0;
    while (!(mask & (1u<<a))) ++a;
    unsigned rest=mask ^ (1u<<a);
    for (unsigned b=a+1; b<6; ++b)
        if ((rest & (1u<<b)) && a/2 != b/2)
            sum+=count_pairs(rest ^ (1u<<b));
    return sum;
}
/* A pairing across two radial vertices permutes 2n labeled slots.
   Each connected color component has three choices. */
static unsigned radial_pairings(unsigned n, unsigned depth, unsigned used, unsigned *p) {
    if (depth < 2*n) {
        unsigned sum=0;
        for (unsigned j=0;j<2*n;++j) if (!(used & (1u<<j))) {
            p[depth]=j;
            sum+=radial_pairings(n,depth+1,used|(1u<<j),p);
        }
        return sum;
    }
    unsigned labels[6], weight=1;
    for (unsigned i=0;i<2*n;++i) labels[i]=i;
    for (unsigned i=0;i<2*n;++i) {
        unsigned a=labels[i/2], b=labels[n+p[i]/2];
        for (unsigned j=0;j<2*n;++j) if (labels[j]==b) labels[j]=a;
    }
    for (unsigned i=0;i<2*n;++i) if (labels[i]==i) weight*=3;
    return weight;
}
__attribute__((used,noreturn)) static void run(void) {
    long fd=open_input("request");
    unsigned char stage;
    read_exact(fd,&stage,1);
    if (stage=='F') {
        unsigned char code;
        read_exact(fd,&code,1);
        if (code!=8) finish(4);
        emit((char)count_pairs(15));
        emit((char)count_pairs(63));
        for (unsigned i=0;i<3;++i) for (unsigned j=0;j<3;++j) for (unsigned k=0;k<3;++k) {
            if (i==j || i==k || j==k) continue;
            emit((char)(((i>j)+(i>k)+(j>k))%2));
            emit((char)i); emit((char)j); emit((char)k);
        }
        unsigned p[6];
        for (unsigned n=1;n<=3;++n) {
            unsigned count=radial_pairings(n,0,0,p);
            emit((char)(count & 255)); emit((char)(count>>8));
        }
    } else if (stage=='S') {
        unsigned char input[32];
        read_exact(fd,input,sizeof(input));
        text("-- BEGIN PCP OS generated trace contractions\n");
        text("def terms : List Term := [");
        for (unsigned i=2;i<26;i+=4) {
            if (i!=2) text(", ");
            text("⟨"); text(input[i] ? "-1, " : "1, ");
            number(input[i+1]); text(", "); number(input[i+2]); text(", "); number(input[i+3]); text("⟩");
        }
        text("]\n\ntheorem determinantWick (K : ℕ → ℕ → ℝ) : wick K terms=6*detCov K := by\n");
        text("  simp [wick,terms,detCov]\n  ring\n\n");
        text("theorem squarePairings : matchings 2 (List.range 4)="); number(input[0]);
        text(" ∧ matchings 3 (List.range 6)="); number(input[1]); text(" := by decide\n\n");
        text("theorem colorWeights : 3*(matchings 2 (List.range 4):ℚ)/4=");
        number(3*input[0]/2); text("/2 ∧ 3*(matchings 3 (List.range 6):ℚ)/8=");
        number(3*input[1]/8); text(" := by norm_num [squarePairings.1,squarePairings.2]\n\n");
        text("theorem radialCounts : ");
        for (unsigned n=1;n<=3;++n) {
            if (n!=1) text(" ∧ ");
            text("Nat.factorial "); number(2*n+1); text("=");
            number(input[24+2*n]+256u*input[25+2*n]);
        }
        text(" := by decide\n\n");
    } else if (stage=='A') {
        copy_source("analytic"); copy_source("certificate");
        text("#print axioms dotWord\n#print axioms orientedWord\n#print axioms ordinaryProduct\n");
        text("#print axioms scalarDefect\n#print axioms productRemainder\n#print axioms normalizedReading\n");
        text("#print axioms integrableLater\n#print axioms tiltedTail\n#print axioms determinantWick\n");
        text("#print axioms radialCounts\n#print axioms twiceWound\n#print axioms windingGram\n#print axioms windingCalibration\n");
        text("#print axioms squareDilation\n#print axioms degreeBudget\n");
        text("#print axioms triangleRatio\n#print axioms orientedRatio\n");
        text("#print axioms squarePairings\n#print axioms colorWeights\n\nend Millennium.YangMills.D4.OrdinaryLoop\n");
    } else finish(4);
    require_end(fd);
    if (os(3,fd,0,0)) finish(2);
    flush(); finish(0);
}
