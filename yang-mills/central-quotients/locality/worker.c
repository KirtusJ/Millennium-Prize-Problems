/* Measured PCP worker for compact-link locality. Task bytes are depth, dimension and face count. */
#include <stddef.h>

static long syscall3(long number, long a, long b, long c) {
    long result;
    __asm__ volatile ("syscall" : "=a"(result)
                      : "a"(number), "D"(a), "S"(b), "d"(c)
                      : "rcx", "r11", "memory");
    return result;
}

_Noreturn static void stop(int status) {
    syscall3(60, status, 0, 0);
    __builtin_unreachable();
}

static void emit(const char *text) {
    size_t size = 0;
    while (text[size]) ++size;
    while (size) {
        long written = syscall3(1, 1, (long)text, size);
        if (written <= 0 || (size_t)written > size) stop(3);
        text += written;
        size -= written;
    }
}

static void number(unsigned n) {
    char text[12];
    unsigned pos = sizeof text - 1;
    text[pos] = 0;
    do { text[--pos] = '0' + n % 10; n /= 10; } while (n);
    emit(text + pos);
}

static void request(unsigned depth, unsigned a, unsigned b) {
    emit("NEXT "); number(depth); emit(" "); number(a); emit(" "); number(b); emit("\n");
}



static unsigned shift(unsigned n, unsigned site, unsigned axis) {
    unsigned stride = axis == 0 ? 1 : (axis == 1 ? n : n*n);
    unsigned digit = (site/stride)%n;
    return site - stride*digit + stride*((digit+1)%n);
}

static void boundary(unsigned n, unsigned face, unsigned edge[4]) {
    unsigned site = face/3, i = (face%3+1)%3, j = (face%3+2)%3;
    edge[0] = 3*site+i;
    edge[1] = 3*shift(n,site,i)+j;
    edge[2] = 3*shift(n,site,j)+i;
    edge[3] = 3*site+j;
}


/* Scan the four-link boundaries with multiplicity and group neighboring link
   midpoints by squared doubled distance from the x link at the origin. */
static unsigned scan(unsigned bins[5], unsigned *return_paths) {
    enum { side=5, links=3*side*side*side };
    unsigned weights[links], count=0;
    for (unsigned a=0; a<links; ++a) weights[a]=0;
    for (unsigned p=0; p<links; ++p) {
        unsigned edges[4]; boundary(side,p,edges);
        unsigned incident=0;
        for (unsigned k=0; k<4; ++k) incident += edges[k]==0;
        if (!incident) continue;
        ++count;
        for (unsigned k=0; k<4; ++k) ++weights[edges[k]];
    }
    *return_paths=0;
    for (unsigned i=0; i<5; ++i) bins[i]=0;
    for (unsigned e=0; e<links; ++e) {
        if (!weights[e]) continue;
        unsigned site=e/3, distance=0;
        for (unsigned i=0; i<3; ++i) {
            int delta=2*(int)(site%side)+(int)(e%3==i)-(int)(i==0);
            site/=side;
            if (delta>side) delta-=2*side;
            if (delta< -side) delta+=2*side;
            distance+=(unsigned)(delta*delta);
        }
        if (distance>4) stop(6);
        bins[distance]+=weights[e];
        *return_paths+=weights[e]*weights[e];
    }
    return count;
}
static unsigned factorial(unsigned n) {
    unsigned out=1;
    for (unsigned j=2;j<=n;++j) out*=j;
    return out;
}
static void parent(void) {
    unsigned bins[5], diagonal;
    unsigned faces=scan(bins,&diagonal);
    emit("LEAN-BEGIN\n"
         "import Mathlib.Tactic.NoncommRing\n"
         "import Mathlib.Tactic.Linarith\n"
         "import Mathlib.Tactic.NormNum\n"
         "import Mathlib.Tactic.Positivity\n"
         "import Mathlib.Tactic.FieldSimp\n"
         "import Mathlib.Analysis.SpecialFunctions.Integrals\n"
         "import Mathlib.Analysis.SpecialFunctions.Exp\n"
         "\n"
         "open scoped BigOperators\n"
         "open Filter Topology\n"
         "\n"
         "namespace YangMills.Locality\n"
         "\n"
         "/-- Product rule for the commutator of a word. -/\n"
         "theorem wordStep {R : Type*} [Ring R] (u v b : R) :\n"
         "    u*v*b-b*(u*v) = u*(v*b-b*v)+(u*b-b*u)*v := by noncomm_ring\n"
         "\n"
         "/-- The derivative and inverse derivative cancel the homogeneous transport. -/\n"
         "theorem conjugateForce {R : Type*} [Ring R] (u z b v : R) :\n"
         "    (u*z)*b*v + u*b*(-z*v) = u*(z*b-b*z)*v := by noncomm_ring\n"
         "\n"
         "theorem inverseCommutator {R : Type*} [Ring R] (u v b : R)\n"
         "    (h : v*u=1) (k : u*v=1) :\n"
         "    v*b-b*v = -(v*(u*b-b*u)*v) := by\n"
         "  have a : v*(u*b)*v = b*v := by simp [← mul_assoc, h]\n"
         "  have c : v*(b*u)*v = v*b := by simp [mul_assoc, k]\n"
         "  rw [mul_sub, sub_mul, a, c]\n"
         "  abel\n"
         "\n"
         "/-- Squared-distance classes in doubled midpoint coordinates for the faces incident to an x link. -/\n"
         "private def pattern : List (ℤ × ℤ × ℤ) :=\n"
         "  [(-1,-1,0),(1,-1,0),(-1,1,0),(1,1,0),\n"
         "   (-1,0,-1),(1,0,-1),(-1,0,1),(1,0,1),\n"
         "   (0,2,0),(0,-2,0),(0,0,2),(0,0,-2)] ++ List.replicate 4 (0,0,0)\n"
         "\n"
         "private def countDist (n : ℤ) : ℕ :=\n"
         "  (pattern.filter fun v => v.1^2 + v.2.1^2 + v.2.2^2 == n).length\n"
         "\n"
         "theorem midpointCounts : (countDist 0, countDist 2, countDist 4) = (");
    number(bins[0]);
    emit(",");
    number(bins[2]);
    emit(",");
    number(bins[4]);
    emit(") := by decide\n"
         "LEAN-END\n");

    request(1,3,faces);
}
static void child(unsigned dimension, unsigned faces) {
    unsigned bins[5], diagonal;
    if (dimension!=3 || faces!=scan(bins,&diagonal)) stop(5);
    emit("LEAN-BEGIN\n"
         "\n"
         "/-- Successive weighted face-incidence steps, beginning with a source on links. -/\n"
         "def walks {ι : Type*} [Fintype ι] (A : ι → ι → ℝ) (g : ι → ℝ) : ℕ → ι → ℝ\n"
         "  | 0 => g\n"
         "  | n+1 => fun i => ∑ j, A i j * walks A g n j\n"
         "\n"
         "theorem tiltedWalks {ι : Type*} [Fintype ι] (A : ι → ι → ℝ) (g v : ι → ℝ)\n"
         "    (K M : ℝ) (ha : ∀ i j, 0 ≤ A i j) (hk : 0 ≤ K) (hm : 0 ≤ M)\n"
         "    (hrow : ∀ i, (∑ j, A i j * v j) ≤ K * v i) (hg : ∀ i, g i ≤ M*v i)\n"
         "    (n : ℕ) (i : ι) : walks A g n i ≤ (M * K^n) * v i := by\n"
         "  induction n generalizing i with\n"
         "  | zero => simpa [walks] using hg i\n"
         "  | succ n ih =>\n"
         "    have hn : 0 ≤ M*K^n := mul_nonneg hm (pow_nonneg hk n)\n"
         "    calc\n"
         "      walks A g (n+1) i ≤ ∑ j, A i j * ((M*K^n)*v j) :=\n"
         "        Finset.sum_le_sum fun j _ => mul_le_mul_of_nonneg_left (ih j) (ha i j)\n"
         "      _ = (M*K^n) * ∑ j, A i j * v j := by\n"
         "        rw [Finset.mul_sum]\n"
         "        apply Finset.sum_congr rfl\n"
         "        intro j _\n"
         "        ring\n"
         "      _ ≤ (M*K^n) * (K*v i) := mul_le_mul_of_nonneg_left (hrow i) hn\n"
         "      _ = _ := by ring\n"
         "\n"
         "theorem noShortPaths {ι : Type*} [Fintype ι] (A : ι → ι → ℝ) (g : ι → ℝ)\n"
         "    (d : ι → ℕ) (hstep : ∀ i j, A i j ≠ 0 → d i ≤ d j + 1)\n"
         "    (hsource : ∀ i, 0 < d i → g i = 0) (n : ℕ) (i : ι) (hlt : n < d i) :\n"
         "    walks A g n i = 0 := by\n"
         "  induction n generalizing i with\n"
         "  | zero => exact hsource i hlt\n"
         "  | succ n ih =>\n"
         "    apply Finset.sum_eq_zero\n"
         "    intro j _\n"
         "    by_cases h : A i j = 0\n"
         "    · simp [h]\n"
         "    · have := hstep i j h\n"
         "      rw [ih j (by omega), mul_zero]\n"
         "\n"
         "private def diagonalTwo : ℕ := 4^2 + 8*1^2 + 4*1^2\n"
         "theorem twoStepReturn : diagonalTwo = ");
    number(diagonal);
    emit(" := by decide\n"
         "LEAN-END\n");

    request(2,dimension,faces);
}
static void grandchild(unsigned dimension, unsigned faces) {
    unsigned bins[5], diagonal;
    if (dimension!=3 || faces!=scan(bins,&diagonal)) stop(5);
    emit("LEAN-BEGIN\n"
         "\n"
         "private noncomputable def term (x : ℝ) (n : ℕ) : ℝ := x^n / (n.factorial : ℝ)\n"
         "\n"
         "/-- The twice-integrated Volterra kernel occupies only the even Taylor indices\n"
         "after factoring out the initial time. This bound holds for every truncation. -/\n"
         "theorem evenMajorant (x : ℝ) (hx : 0 ≤ x) (N : ℕ) :\n"
         "    (∑ n ∈ Finset.range N, x^(2*n) / ((2*n+1).factorial : ℝ)) ≤ Real.exp x := by\n"
         "  have H (k : ℕ) : (∑ n ∈ Finset.range k, x^(2*n) / ((2*n+1).factorial : ℝ))\n"
         "      ≤ ∑ n ∈ Finset.range (2*k), term x n := by\n"
         "    induction k with\n"
         "    | zero => simp\n"
         "    | succ k ih =>\n"
         "      rw [show 2*(k+1)=2*k+1+1 by omega, Finset.sum_range_succ, Finset.sum_range_succ]\n"
         "      rw [Finset.sum_range_succ] at *\n"
         "      have df : ((2*k).factorial : ℝ) ≤ ((2*k+1).factorial : ℝ) := by\n"
         "        exact_mod_cast Nat.factorial_le (by omega : 2*k ≤ 2*k+1)\n"
         "      have hd : (0:ℝ) < (2*k).factorial := by positivity\n"
         "      have hbase : x^(2*k) / ((2*k+1).factorial : ℝ) ≤ term x (2*k) :=\n"
         "        div_le_div_of_nonneg_left (pow_nonneg hx _) hd df\n"
         "      have hpos : 0 ≤ term x (2*k+1) := by unfold term; positivity\n"
         "      linarith\n"
         "  exact (H N).trans (Real.sum_le_exp_of_nonneg hx _)\n"
         "\n"
         "\n"
         "/-- Integration from zero shifts the factorial kernel by one degree, including across zero. -/\n"
         "theorem integrateTerm (n : ℕ) (t : ℝ) : (∫ x in (0:ℝ)..t, term x n) = term t (n+1) := by\n"
         "  unfold term\n"
         "  rw [intervalIntegral.integral_div, integral_pow]\n"
         "  simp only [zero_pow (Nat.succ_ne_zero n), sub_zero, Nat.factorial_succ, Nat.cast_mul,\n"
         "    Nat.cast_add, Nat.cast_one]\n"
         "  rw [div_div]\n"
         "\n"
         "theorem twoIntegrations (n : ℕ) (t : ℝ) :\n"
         "    (∫ s in (0:ℝ)..t, ∫ x in (0:ℝ)..s, term x n) = term t (n+2) := by\n"
         "  simp_rw [integrateTerm]\n"
         "\n"
         "/-- For a real-time phase error bounded by 2 and y²/2, its squared error costs\n"
         "at most 2y; this is the energy-tail interpolation in the Wilson comparison. -/\n"
         "theorem phaseInterpolation {r y : ℝ} (hr : 0 ≤ r) (hy : 0 ≤ y)\n"
         "    (h2 : r ≤ 2) (hquad : r ≤ y^2/2) : r^2 ≤ 2*y := by\n"
         "  by_cases h : y ≤ 2\n"
         "  · have h1 : y^2 ≤ 2*y := by nlinarith [mul_nonneg hy (sub_nonneg.mpr h)]\n"
         "    have hle : r ≤ y := by linarith\n"
         "    nlinarith [mul_nonneg hr (sub_nonneg.mpr h2)]\n"
         "  · nlinarith [mul_nonneg (sub_nonneg.mpr h2) (add_nonneg hr (by norm_num : (0:ℝ) ≤ 2))]\n"
         "\n"
         "theorem bareClock (beta b : ℝ) (hbeta : 0 < beta) (hb : 0 < b) :\n"
         "    b^2 * (2/(beta*b)) * (beta/b) = 2 := by field_simp; ring\n"
         "\n"
         "theorem scaledCone (n : ℕ) {x : ℕ → ℝ} (hx : Tendsto x atTop atTop) :\n"
         "    Tendsto (fun j => x j ^ n * Real.exp (-x j)) atTop (𝓝 0) :=\n"
         "  (Real.tendsto_pow_mul_exp_neg_atTop_nhds_zero n).comp hx\n"
         "\n"
         "private def twiceIntegrated (n : ℕ) : ℕ := (2*n+1).factorial\n"
         "theorem separatedDenominators :\n"
         "    (twiceIntegrated 1, twiceIntegrated 2, twiceIntegrated 3) = (");
    number(factorial(3));
    emit(",");
    number(factorial(5));
    emit(",");
    number(factorial(7));
    emit(") := by decide\n"
         "\n"
         "#print axioms wordStep\n"
         "#print axioms conjugateForce\n"
         "#print axioms inverseCommutator\n"
         "#print axioms midpointCounts\n"
         "#print axioms tiltedWalks\n"
         "#print axioms noShortPaths\n"
         "#print axioms twoStepReturn\n"
         "#print axioms evenMajorant\n"
         "#print axioms integrateTerm\n"
         "#print axioms twoIntegrations\n"
         "#print axioms phaseInterpolation\n"
         "#print axioms bareClock\n"
         "#print axioms scaledCone\n"
         "#print axioms separatedDenominators\n"
         "end YangMills.Locality\n"
         "LEAN-END\n");
}

__attribute__((used,noreturn)) static void run(void) {
    static unsigned char input[4];
    long fd = syscall3(2, (long)"task.bin", 0, 0);
    if (fd < 0 || syscall3(0, fd, (long)input, sizeof input) != 3 ||
        syscall3(0, fd, (long)(input+3), 1) != 0 || syscall3(3, fd, 0, 0) != 0) stop(2);
    if (!input[0] && !input[1] && !input[2]) parent();
    else if (input[0] == 1) child(input[1],input[2]);
    else if (input[0] == 2) grandchild(input[1],input[2]);
    else stop(2);
    stop(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
