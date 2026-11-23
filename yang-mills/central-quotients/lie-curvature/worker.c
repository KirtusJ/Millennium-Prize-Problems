/* Native PCP clients enumerate a cube, contract its projectors, and count color channels. */
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




static unsigned circuits(void) {
    const unsigned path[6][3]={{1,2,3},{2,1,3},{2,3,1},{3,2,1},{3,1,2},{1,3,2}};
    unsigned total=0;
    for (unsigned i=0;i<6;++i) {
        const unsigned *a=path[i], *b=path[(i+1)%6];
        if ((a[0]==b[1] && a[1]==b[0] && a[2]==b[2]) ||
            (a[0]==b[0] && a[1]==b[2] && a[2]==b[1])) ++total;
    }
    return total;
}
static int order(unsigned a,unsigned b) { return (a<b)-(a>b); }
static int block(unsigned odd,unsigned a,unsigned b) {
    int same=3*(a==b), opposite=3*((a+3)%6==b);
    return odd ? same-opposite : same+opposite-1;
}
static unsigned contract(unsigned a,unsigned b) {
    int total=0;
    for (unsigned i=0;i<6;++i) for (unsigned j=0;j<6;++j)
        for (unsigned k=0;k<6;++k) for (unsigned l=0;l<6;++l)
            total+=order(i,j)*order(k,l)*block(a,i,k)*block(b,j,l);
    if (total<0) stop(5);
    return (unsigned)total;
}
static unsigned colors(unsigned n) {
    unsigned count=n-1;
    for (unsigned i=0;i<n;++i) for (unsigned j=i+1;j<n;++j) count+=2;
    return count;
}
static void parent(void) {
    emit("LEAN-BEGIN\n"
         "import Mathlib.MeasureTheory.Integral.Bochner.Basic\n"
         "import Mathlib.Tactic.Ring\n"
         "import Mathlib.Tactic.FieldSimp\n"
         "import Mathlib.Tactic.NoncommRing\n"
         "import Mathlib.Tactic.NormNum\n"
         "import Mathlib.Tactic.Linarith\n"
         "import Mathlib.Tactic.Positivity\n"
         "\n"
         "import Mathlib.Algebra.Star.Basic\n"
         "import Mathlib.Data.Real.Basic\n"
         "import Mathlib.Algebra.BigOperators.Ring.Finset\n"
         "\n"
         "open scoped BigOperators\n"
         "set_option maxRecDepth 10000\n"
         "open MeasureTheory\n"
         "\n"
         "namespace YangMills.LieCurvature\n"
         "\n"
         "/-- The six monotone paths around an elementary cube, changing one adjacent pair. -/\n"
         "def paths : List (List Nat) :=\n"
         "  [[1,2,3],[2,1,3],[2,3,1],[3,2,1],[3,1,2],[1,3,2]]\n"
         "\n"
         "def swaps (a b : List Nat) : Bool :=\n"
         "  (a == [b[1]!,b[0]!,b[2]!] || a == [b[0]!,b[2]!,b[1]!])\n"
         "\n"
         "theorem sixPaths : paths.length = ");
    number(circuits());
    emit(" ∧\n"
         "    (paths.zip (paths.drop 1 ++ paths.take 1)).all (fun p => swaps p.1 p.2) = true := by decide\n"
         "\n"
         "theorem cubeProduct {G : Type*} [Group G] (a b c d e f : G) :\n"
         "    (a*b⁻¹)*(b*c⁻¹)*(c*d⁻¹)*(d*e⁻¹)*(e*f⁻¹)*(f*a⁻¹) = 1 := by simp [mul_assoc]\n"
         "\n"
         "def jetMul {R : Type*} [Ring R] (a b : R × R) : R × R :=\n"
         "  (a.1+b.1, a.2+b.2+a.1*b.1)\n"
         "\n"
         "theorem jetAssociative {R : Type*} [Ring R] (a b c : R × R) :\n"
         "    jetMul (jetMul a b) c = jetMul a (jetMul b c) := by\n"
         "  apply Prod.ext\n"
         "  · exact add_assoc _ _ _\n"
         "  · simp only [jetMul]\n"
         "    noncomm_ring\n"
         "\n"
         "def bracket {R : Type*} [Ring R] (x y : R) := x*y-y*x\n"
         "\n"
         "theorem shiftedBracket {R : Type*} [Ring R] (u v : R) :\n"
         "    bracket (u-1) (v-1) = bracket u v := by unfold bracket; noncomm_ring\n"
         "\n"
         "theorem translatedCommutator {R : Type*} [Ring R] (u v ui vi : R)\n"
         "    (hu : u*ui=1) (hv : v*vi=1) :\n"
         "    u*v*ui*vi-1=(u*v-v*u)*ui*vi := by\n"
         "  have ht : v*u*ui*vi=1 := by rw [mul_assoc v u ui,hu,mul_one,hv]\n"
         "  rw [sub_mul,sub_mul,ht]\n"
         "\n"
         "LEAN-END\n");

    request(1,4,3);
}
static void child(unsigned dim,unsigned n) {
    if (dim!=4 || n!=3) stop(5);
    emit("LEAN-BEGIN\n"
         "/-- Quadratic terms in an inverse-odd coordinate give one half of the bracket. -/\n"
         "theorem skewProduct {R : Type*} [Ring R] [StarRing R] (a b : R)\n"
         "    (ha : star a = -a) (hb : star b = -b) :\n"
         "    a*b-star (a*b)=bracket a b := by simp [star_mul,ha,hb,bracket]\n"
         "\n"
         "theorem jacobiInsertion {R : Type*} [Ring R] (b c d : R) :\n"
         "    bracket b (bracket c d)-bracket d (bracket c b)=bracket c (bracket b d) := by\n"
         "  unfold bracket\n"
         "  noncomm_ring\n"
         "\n"
         "theorem tensorBianchi {R : Type*} [Ring R] (B : R → R →+ ℝ)\n"
         "    (hi : ∀ a b c, B (bracket a b) c=B a (bracket b c)) (a b c d : R) :\n"
         "    B (bracket a b) (bracket c d)-B (bracket a d) (bracket c b)\n"
         "      = B (bracket a c) (bracket b d) := by\n"
         "  rw [hi,hi,hi,← map_sub,jacobiInsertion]\n"
         "\n"
         "/-- Permuting tensor slots preserves the three norms in the Bianchi relation. -/\n"
         "theorem symTensorNorm (n cross : ℝ) (h : n+n-2*cross=n) :\n"
         "    (n+n+2*cross)/4=3*n/4 := by linarith\n"
         "\n"
         "def colorDimension (n : Nat) := n*n-1\n"
         "def adjointCasimir (n : Nat) := 2*n*n\n"
         "def bracketSum (n : Nat) := colorDimension n * adjointCasimir n\n"
         "\n"
         "theorem twoCharacterChecks : (bracketSum 2, bracketSum 3) = (24,144) := by decide\n"
         "\n"
         "theorem casimirExpansion {R : Type*} [Ring R] (t : Finset ℕ) (T : ℕ → R) (x : R) :\n"
         "    ∑ i ∈ t, bracket (T i) (bracket (T i) x) =\n"
         "    (∑ i ∈ t, T i*T i)*x + x*(∑ i ∈ t, T i*T i)\n"
         "    - ((∑ i ∈ t, T i*x*T i)+(∑ i ∈ t, T i*x*T i)) := by\n"
         "  rw [Finset.sum_mul, Finset.mul_sum, ← Finset.sum_add_distrib, ← Finset.sum_add_distrib,\n"
         "      ← Finset.sum_sub_distrib]\n"
         "  apply Finset.sum_congr rfl\n"
         "  intro i _\n"
         "  unfold bracket\n"
         "  noncomm_ring\n"
         "\n"
         "def orderSign (i j : ℕ) : ℤ := if i < j then 1 else if j < i then -1 else 0\n"
         "def cubeBlock (odd : Bool) (i j : ℕ) : ℤ :=\n"
         "  let same : ℤ := if i=j then 3 else 0\n"
         "  let opposite : ℤ := if (i+3)%6=j then 3 else 0\n"
         "  if odd then same-opposite else same+opposite-1\n"
         "\n"
         "def contraction (a b : Bool) : ℤ :=\n"
         "  ((List.range 6).map fun i => ((List.range 6).map fun j =>\n"
         "    ((List.range 6).map fun k => ((List.range 6).map fun l =>\n"
         "      orderSign i j*orderSign k l*cubeBlock a i k*cubeBlock b j l).sum).sum).sum).sum\n"
         "\n"
         "set_option maxHeartbeats 6000000 in\n"
         "theorem cubeContractions : (contraction true true, contraction true false, contraction false false)\n"
         "    = (");
    number(contract(1,1));
    emit(",");
    number(contract(1,0));
    emit(",");
    number(contract(0,0));
    emit(") := by decide\n"
         "\n"
         "/-- Pair and triple sums in the given ordering, without a choice of Lie basis. -/\n"
         "def pairs {R : Type*} [Ring R] : List R → R\n"
         "  | [] => 0\n"
         "  | a::xs => bracket a xs.sum + pairs xs\n"
         "\n"
         "def triples {R : Type*} [Ring R] (form : R →+ R →+ ℝ) : List R → ℝ\n"
         "  | [] => 0\n"
         "  | a::xs => form (pairs xs) a + triples form xs\n"
         "\n"
         "theorem orderedContraction {R : Type*} [Ring R] (form : R →+ R →+ ℝ)\n"
         "    (hl : ∀ a b, form (bracket a b) a=0) (hr : ∀ a b, form (bracket a b) b=0)\n"
         "    (xs : List R) : form (pairs xs) xs.sum = triples form xs := by\n"
         "  induction xs with\n"
         "  | nil => simp [pairs,triples]\n"
         "  | cons a xs ih =>\n"
         "    simp [pairs,triples,hl,hr,ih]\n"
         "\n"
         "LEAN-END\n");

    request(2,dim,n);
}
static void grandchild(unsigned dim,unsigned n) {
    if (dim!=4 || n!=3) stop(5);
    unsigned d=colors(n), casimir=2*n*n;
    emit("LEAN-BEGIN\n"
         "theorem gramTrace {a b : ℝ} (h : 3*a+2*b=3) : b=(3/2)*(1-a) := by linarith\n"
         "\n"
         "theorem orderedCubeRatio {a b : ℝ} (h : 3*a+2*b=3) :\n"
         "    6*a^2+2*b^2/3 = (15*a^2-6*a+3)/2 := by rw [gramTrace h]; ring\n"
         "\n"
         "theorem cubeRatioLower {a b : ℝ} (h : 3*a+2*b=3) (ha : 1/2 < a) :\n"
         "    15/8 < 6*a^2+2*b^2/3 := by\n"
         "  rw [orderedCubeRatio h]\n"
         "  nlinarith [sq_nonneg (a-1/2)]\n"
         "\n"
         "theorem cubicThreshold : 3*4=12 := by decide\n"
         "theorem quarticThreshold : 4*4=16 := by decide\n"
         "\n"
         "theorem wrongSubtraction (v c q : ℝ) : c*v-q=0 ↔ q=c*v := by constructor <;> intro h <;> linarith\n"
         "\n"
         "theorem gaussianRatio {v : ℝ} (hv : v ≠ 0) (d : ℝ) (hd : d ≠ 0) :\n"
         "    d*(d+2)*v^2/(d*v)^2=(d+2)/d := by\n"
         "  field_simp\n"
         "  ring\n"
         "\n"
         "theorem suThreeChannels : (bracketSum 3, 3*colorDimension 3*(adjointCasimir 3)^2)\n"
         "    = (");
    number(d*casimir);
    emit(",");
    number(3*d*casimir*casimir);
    emit(") := by decide\n"
         "\n"
         "theorem bracketDimensionRatio {d c : ℝ} (hd : d ≠ 0) (hc : c ≠ 0) :\n"
         "    (7*d*c^2/64)/(d*c/8)^2=7/d := by\n"
         "  field_simp\n"
         "  ring\n"
         "\n"
         "theorem excessSecondChannel (d c v t : ℝ) :\n"
         "    (2*d*t^2)*(c*v)^2+(2*d*t^2)*(c*v)^2=4*d*c^2*v^2*t^2 := by ring\n"
         "\n"
         "theorem singletDeterminant (d c v x : ℝ) :\n"
         "    (d*x^2)*(4*d*c^2*v^2*x^2+3*d*c^2*x^4)-(2*c*v*d*x^2)^2 =\n"
         "    3*(d*c*x^3)^2 := by ring\n"
         "\n"
         "theorem determinantShift (m n h k : ℝ) :\n"
         "    m*(h+2*k*n+k^2*m)-(n+k*m)^2=m*h-n^2 := by ring\n"
         "\n"
         "def symmetricNorm (n : ℕ) := 2*(n*n-1)*(n*n-4)\n"
         "\n"
         "theorem symmetricColorChecks : (symmetricNorm 2,symmetricNorm 3,symmetricNorm 4) =\n"
         "    (0,");
    number(2*d*(n*n-4));
    emit(",");
    number(2*colors(4)*(4*4-4));
    emit(") := by decide\n"
         "\n"
         "theorem oddSelection {α : Type*} [MeasurableSpace α] {μ : Measure α} (f : α → ℝ)\n"
         "    (s : α ≃ᵐ α) (hp : MeasurePreserving s μ μ) (hi : Integrable f μ)\n"
         "    (hneg : ∀ x, f (s x) = -f x) : Integrable f μ ∧ ∫ x, f x ∂μ = 0 := by\n"
         "  have h := hp.integral_comp' f\n"
         "  simp_rw [hneg] at h\n"
         "  rw [integral_neg] at h\n"
         "  exact ⟨hi, by linarith⟩\n"
         "\n"
         "theorem chargeRatio {n : ℝ} (hn : 1 < n) :\n"
         "    (2*(n^2-1)*(n^2-4))/(2*n^2*(n^2-1))=1-4/n^2 := by\n"
         "  have h1 : n^2-1 ≠ 0 := by nlinarith [sq_nonneg (n-1)]\n"
         "  have h2 : n ≠ 0 := by linarith\n"
         "  field_simp\n"
         "  ring\n"
         "\n"
         "theorem oddPlaquetteVariance : (6/12^2 : ℝ)*80*(1/2)^3=5/12 := by norm_num\n"
         "\n"
         "end YangMills.LieCurvature\n"
         "\n"
         "open YangMills.LieCurvature\n"
         "#print axioms sixPaths\n"
         "#print axioms cubeProduct\n"
         "#print axioms jetAssociative\n"
         "#print axioms shiftedBracket\n"
         "#print axioms translatedCommutator\n"
         "#print axioms skewProduct\n"
         "#print axioms jacobiInsertion\n"
         "#print axioms tensorBianchi\n"
         "#print axioms symTensorNorm\n"
         "#print axioms twoCharacterChecks\n"
         "#print axioms casimirExpansion\n"
         "#print axioms cubeContractions\n"
         "#print axioms gramTrace\n"
         "#print axioms orderedCubeRatio\n"
         "#print axioms cubeRatioLower\n"
         "#print axioms cubicThreshold\n"
         "#print axioms quarticThreshold\n"
         "#print axioms wrongSubtraction\n"
         "#print axioms gaussianRatio\n"
         "#print axioms suThreeChannels\n"
         "#print axioms bracketDimensionRatio\n"
         "#print axioms excessSecondChannel\n"
         "#print axioms orderedContraction\n"
         "#print axioms singletDeterminant\n"
         "#print axioms determinantShift\n"
         "#print axioms symmetricColorChecks\n"
         "#print axioms oddSelection\n"
         "#print axioms chargeRatio\n"
         "#print axioms oddPlaquetteVariance\n"
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
