/* Enumerate actual oriented faces of a 4 x 3 x 3 x 3 periodic box. */
static unsigned advance(unsigned site, unsigned axis) {
    static const unsigned stride[4]={1,4,12,36};
    unsigned size=axis==0?4:3, d=stride[axis];
    return (site/d)%size+1==size?site-(size-1)*d:site+d;
}
static unsigned incidence(unsigned site, unsigned mu, unsigned nu, unsigned bond) {
    unsigned x=bond/4, a=bond%4;
    return (a==mu && (x==site || x==advance(site,nu))) ||
           (a==nu && (x==site || x==advance(site,mu)));
}
/* Match the two labeled slots at each quadratic vertex along a given cycle,
   using each undirected edge of that cycle exactly once. */
static unsigned cycle_count(unsigned vertices, unsigned slots, unsigned edges) {
    if (!slots) return edges==(1u<<vertices)-1;
    unsigned first=0,total=0;
    while (!(slots & (1u<<first))) ++first;
    unsigned tail=slots^(1u<<first), a=first/2;
    for (unsigned j=first+1;j<2*vertices;++j) if (tail & (1u<<j)) {
        unsigned b=j/2, edge;
        if ((a+1)%vertices==b) edge=a;
        else if ((b+1)%vertices==a) edge=b;
        else continue;
        if (!(edges & (1u<<edge)))
            total+=cycle_count(vertices,tail^(1u<<j),edges|(1u<<edge));
    }
    return total;
}
__attribute__((used,noreturn)) static void run(void) {
    long fd=open_input("request");
    unsigned char stage;
    read_exact(fd,&stage,1);
    if (stage=='F') {
        unsigned char code;
        read_exact(fd,&code,1);
        if (code!=9) finish(4);
        unsigned cells=0, adjacent=0, spatial=0;
        for (unsigned s=0;s<108;++s) for (unsigned mu=0;mu<4;++mu)
          for (unsigned nu=mu+1;nu<4;++nu) if (incidence(s,mu,nu,0)) {
              ++cells;
              adjacent+=incidence(s,mu,nu,4*advance(0,0));
              spatial+=incidence(s,mu,nu,4*advance(0,1));
          }
        emit((char)cells); emit((char)adjacent); emit((char)spatial);
        /* Integers for the two-particle polynomial from even angular moments.
           Its k^4 coefficient is the average of (4 - 4 z^2 + 2 z^4)/2. */
        unsigned coeff=(4*15-4*5+2*3)/2;
        emit((char)coeff);
        unsigned radial=35-42+coeff;  /* common denominator 105 */
        emit((char)radial);
        emit((char)cycle_count(3,63,0)); emit((char)cycle_count(4,255,0));
    } else if (stage=='S') {
        unsigned char v[7];
        read_exact(fd,v,7);
        text("-- BEGIN PCP OS generated slab controls\n");
        text("theorem latticeIncidence : faceCount 0="); number(v[0]);
        text(" ∧ faceCount 4="); number(v[1]); text(" ∧ faceCount 16="); number(v[2]);
        text(" := by decide\n\n");
        text("theorem marginalPolynomial (z : ℝ) : z^2*phase 1 z=z^2-2*z^4+(");
        number(v[3]); text("/15)*z^6 := by unfold phase; ring\n\n");
        text("theorem marginalConstant : (1:ℝ)/3-2/5+(23/15)/7=");
        number(v[4]); text("/105 := by norm_num\n\n");
        text("theorem marginalIntegral : (∫ z in (0:ℝ)..1, z^2*phase 1 z)=");
        number(v[4]); text("/105 := by\n  simp_rw [marginalPolynomial]\n");
        text("  rw [intervalIntegral.integral_add,intervalIntegral.integral_sub,");
        text("intervalIntegral.integral_const_mul,intervalIntegral.integral_const_mul,integral_pow,integral_pow,integral_pow]\n");
        text("  · norm_num\n  all_goals apply Continuous.intervalIntegrable; fun_prop\n\n");
        text("theorem collinearWeights : ("); number(v[5]); text("*9:ℚ)^2/(2*9)^3=8/9 ∧ (");
        number(v[6]); text("*18:ℚ)/(2*18)^2=2/9 := by norm_num\n\n");
    } else if (stage=='A') {
        copy_source("analytic"); copy_source("certificate");
        text("#print axioms oddTrace\n#print axioms collinearWeights\n");
        text("#print axioms scalarOrientation\n#print axioms tensorInverse\n#print axioms splitChannels\n#print axioms mixedConeValue\n");
        text("#print axioms slabCenter\n#print axioms cutoffLaplacian\n#print axioms momentStep\n");
        text("#print axioms angularExpansion\n#print axioms angularIntegral\n#print axioms phasePositive\n");
        text("#print axioms threshold\n#print axioms restReading\n#print axioms latticeIncidence\n");
        text("#print axioms marginalPolynomial\n#print axioms marginalConstant\n#print axioms marginalIntegral\n");
        text("end Millennium.YangMills.D4.ElectricSlab\n");
    } else finish(4);
    require_end(fd);
    if (os(3,fd,0,0)) finish(2);
    flush(); finish(0);
}
