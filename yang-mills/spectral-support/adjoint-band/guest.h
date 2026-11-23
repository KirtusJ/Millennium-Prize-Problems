/* Spherical divergence on S^d, with d passed in the measured boot request. */
__attribute__((used,noreturn)) static void run(void) {
    long fd = open_input("request");
    unsigned char stage;
    read_exact(fd, &stage, 1);
    if (stage == 'F') {
        unsigned char d;
        read_exact(fd, &d, 1);
        if (d < 2 || d > 20) finish(4);
        /* The two endpoint divergences of (a*x-b*x^3) grad(x) are
           a and d*(b-a). Equating them fixes a=d, b=d+1. */
        emit((char)d);
        emit((char)d);
        emit((char)(d+1));
    } else if (stage == 'S') {
        unsigned char c[3];
        read_exact(fd, c, sizeof(c));
        unsigned d=c[0], a=c[1], b=c[2];
        if (d < 2 || d > 20 || a != d || b != d+1) finish(4);
        unsigned second = a*(d+1)+3*b, fourth = b*(d+3);
        if (second != fourth || second % a != 0) finish(5);
        text("-- BEGIN PCP OS generated spherical divergence\n");
        text("theorem sphericalDivergence (x : ℝ) :\n    (1-x^2)*(1-");
        number(3*b); text("*x^2/"); number(a); text(") - ");
        number(d); text("*x*(x-"); number(b); text("*x^3/"); number(a);
        text(") = 1-"); number(second/a); text("*x^2*(1-x^2) := by ring\n\n");
    } else if (stage == 'A') {
        copy_source("analytic");
        copy_source("certificate");
        text("#print axioms scoreMultiplier\n#print axioms adjointFirstMoment\n");
        text("#print axioms crossCharacterIdentity\n#print axioms squareCommutator\n");
        text("#print axioms adjointGraphNorm\n#print axioms magneticCount\n");
        text("#print axioms quadraticMinorant\n#print axioms quadraticBand\n#print axioms massCapBand\n#print axioms improvedBand\n");
        text("#print axioms jointSelection\n#print axioms prescribedDiagonalFails\n");
        text("#print axioms sphericalDivergence\n\nend Millennium.YangMills.D4.Adjoint\n");
    } else {
        finish(4);
    }
    require_end(fd);
    if (os(3, fd, 0, 0)) finish(2);
    flush();
    finish(0);
}
