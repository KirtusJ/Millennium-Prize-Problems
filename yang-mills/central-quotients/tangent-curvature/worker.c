/* Three PCP guests enumerate cubical cells, reduce incidence and count Fourier polarizations. */
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




struct cell { unsigned mask, vertex; };
static unsigned bits(unsigned v) {
    unsigned total=0;
    for (; v; v>>=1) total+=v&1;
    return total;
}
static unsigned cells(unsigned degree, struct cell *list) {
    unsigned count=0;
    for (unsigned m=0;m<16;++m) if (bits(m)==degree)
        for (unsigned v=0;v<16;++v) if (!(m&v)) {
            list[count].mask=m;
            list[count++].vertex=v;
        }
    return count;
}
static unsigned rank(unsigned k) {
    struct cell low[32], high[32];
    unsigned cols=cells(k,low), rows=cells(k+1,high), pivots[32]={0}, total=0;
    for (unsigned i=0;i<rows;++i) {
        unsigned x=0;
        for (unsigned j=0;j<cols;++j) {
            unsigned bit=high[i].mask ^ low[j].mask;
            if (bits(bit)==1 && (high[i].mask&bit) &&
                (high[i].vertex==low[j].vertex || (high[i].vertex|bit)==low[j].vertex))
                x|=1u<<j;
        }
        for (unsigned j=0;j<cols && x;++j) if (x&(1u<<j)) {
            if (pivots[j]) x^=pivots[j];
            else { pivots[j]=x; ++total; break; }
        }
    }
    return total;
}
static void parent(void) {
    struct cell list[32];
    emit("LEAN-BEGIN\n"
         "import Mathlib.Analysis.SpecialFunctions.ExpDeriv\n"
         "import Mathlib.Analysis.Calculus.Deriv.Pow\n"
         "import Mathlib.Analysis.Calculus.MeanValue\n"
         "import Mathlib.Tactic.Linarith\n"
         "import Mathlib.Tactic.NormNum\n"
         "import Mathlib.Tactic.Ring\n"
         "\n"
         "import Mathlib.MeasureTheory.Integral.Bochner.Basic\n"
         "\n"
         "open MeasureTheory\n"
         "\n"
         "namespace YangMills.TangentCurvature\n"
         "\n"
         "/-- Each of the four coordinates of a cube cell is low, high or free. -/\n"
         "def cellCounts : ℕ → List ℕ\n"
         "  | 0 => [1]\n"
         "  | d+1 => let a := cellCounts d\n"
         "           (a.map (2*·) ++ [0]).zipWith (·+·) (0::a)\n"
         "\n"
         "theorem fourCubeCounts : cellCounts 4 = [");
    number(cells(0,list));
    emit(",");
    number(cells(1,list));
    emit(",");
    number(cells(2,list));
    emit(",");
    number(cells(3,list));
    emit(",");
    number(cells(4,list));
    emit("] := by decide\n"
         "\n"
         "/-- In each coordinate a missing bit is fixed at the lower or upper endpoint. -/\n"
         "def cells (k : ℕ) : List (Nat × Nat) :=\n"
         "  ((List.range 16).flatMap fun m => (List.range 16).map fun v => (m,v)).filter\n"
         "    fun (m,v) => (m &&& v) == 0 && ((List.range 4).filter fun i => m.testBit i).length == k\n"
         "\n"
         "def incident (high low : Nat × Nat) : Bool :=\n"
         "  (List.range 4).any fun i => high.1.testBit i &&\n"
         "    low.1 == high.1 - 2^i && (low.2 == high.2 || low.2 == high.2 + 2^i)\n"
         "\n"
         "def row (columns : List (Nat × Nat)) (high : Nat × Nat) : UInt32 :=\n"
         "  columns.zipIdx.foldl (fun bits entry =>\n"
         "    if incident high entry.1 then bits ||| ((1 : UInt32) <<< entry.2.toUInt32) else bits) 0\n"
         "\n"
         "/-- Eliminate pivot columns of a binary matrix from low to high. -/\n"
         "def binaryRank (rows : List UInt32) : ℕ :=\n"
         "  ((List.range 32).foldl (fun (state : ℕ × List UInt32) i =>\n"
         "    let mask := (1 : UInt32) <<< i.toUInt32\n"
         "    match state.2.find? (fun x => x &&& mask != 0) with\n"
         "    | none => state\n"
         "    | some pivot => (state.1+1, state.2.map (fun x => if x &&& mask != 0 then x ^^^ pivot else x)))\n"
         "    (0,rows)).1\n"
         "\n"
         "def incidenceRank (k : ℕ) : ℕ := binaryRank ((cells (k+1)).map (row (cells k)))\n"
         "\n"
         "LEAN-END\n");

    request(1,4,3);
}
static void child(unsigned dim,unsigned axes) {
    if (dim!=4 || axes!=3) stop(5);
    emit("LEAN-BEGIN\n"
         "set_option maxRecDepth 10000 in\n"
         "set_option maxHeartbeats 8000000 in\n"
         "theorem cubeRanks : (incidenceRank 1, incidenceRank 2) = (");
    number(rank(1));
    emit(",");
    number(rank(2));
    emit(") := by decide\n"
         "\n"
         "theorem exactFaceCount : 24-7 = (17 : ℕ) := by decide\n"
         "\n"
         "/-- The alternating face sum of a gradient vanishes. -/\n"
         "theorem squareGradient (a b c d : ℝ) : (b-a)+(c-b)-(c-d)-(d-a) = 0 := by ring\n"
         "\n"
         "/-- Unit quaternion scalar deficit and the magnitude of its imaginary part. -/\n"
         "theorem quaternionDeficit {w x y z : ℝ} (hs : w^2+x^2+y^2+z^2=1) :\n"
         "    2*(1-w) = x^2+y^2+z^2+(1-w)^2 := by nlinarith\n"
         "\n"
         "theorem temporalTilt {γ u logRatio cost : ℝ} (hγ : 0 < γ)\n"
         "    (ht : γ*u/2 ≤ logRatio+cost) : u ≤ 2*(logRatio+cost)/γ := by\n"
         "  apply (le_div_iff₀ hγ).2\n"
         "  linarith\n"
         "\n"
         "/-- The signed local incidence at an interior edge has squared norm six. -/\n"
         "theorem edgeVariance (x y z : ℝ) :\n"
         "    3*(x^2+y^2+z^2)+3*((-x)^2+(-y)^2+(-z)^2)=6*(x^2+y^2+z^2) := by ring\n"
         "\n"
         "/-- Integrating factor for either real component of the Ward characteristic ODE. -/\n"
         "theorem wardCharacteristic (a b : ℝ) (f : ℝ → ℝ)\n"
         "    (h : ∀ t, HasDerivAt f (-(a+b*t)*f t) t) (t : ℝ) :\n"
         "    f t = f 0 * Real.exp (-(a*t+b*t^2/2)) := by\n"
         "  let q := fun s : ℝ => a*s+b*s^2/2\n"
         "  have hq (s : ℝ) : HasDerivAt q (a+b*s) s := by\n"
         "    have h1 := ((hasDerivAt_id s).const_mul a).add\n"
         "      ((((hasDerivAt_id s).pow 2).const_mul b).div_const 2)\n"
         "    convert h1 using 1\n"
         "    simp [q]\n"
         "    ring\n"
         "  have hz (s : ℝ) : HasDerivAt (fun r => f r * Real.exp (q r)) 0 s := by\n"
         "    convert (h s).mul (hq s).exp using 1\n"
         "    ring\n"
         "  have hc := is_const_of_deriv_eq_zero (fun s => (hz s).differentiableAt)\n"
         "    (fun s => (hz s).deriv) t 0\n"
         "  change f t * Real.exp (q t) = f 0 * Real.exp (q 0) at hc\n"
         "  simp [q] at hc\n"
         "  rw [Real.exp_neg, ← hc]\n"
         "  field_simp\n"
         "\n"
         "LEAN-END\n");

    if (rank(0)!=15) stop(6);
    request(2,dim,axes);
}
static void grandchild(unsigned dim,unsigned axes) {
    if (dim!=4 || axes!=dim-1) stop(5);
    unsigned occupied=0;
    for (unsigned i=0;i<4;++i) for (unsigned j=i+1;j<4;++j)
        occupied+=(i==0 || j==0);
    emit("LEAN-BEGIN\n"
         "/-- Completing the square after removal of the Gaussian projection. -/\n"
         "theorem residualFactor (g u : ℝ) :\n"
         "    -g*(u-g)-(u-g)^2/2=g^2/2-u^2/2 := by ring\n"
         "\n"
         "theorem projectionDiagonal {a b c d : ℝ} (h : a+b+c+d ≠ 0) :\n"
         "    (a+b)/(a+b+c+d)+(c+d)/(a+b+c+d)=1 := by\n"
         "  field_simp\n"
         "  ring\n"
         "\n"
         "theorem traceOfProjection {a b c d : ℝ} (h : a+b+c+d ≠ 0) :\n"
         "    ((a+b)+(a+c)+(a+d)+(b+c)+(b+d)+(c+d))/(a+b+c+d)=");
    number(occupied);
    emit(" := by\n"
         "  field_simp\n"
         "  ring\n"
         "\n"
         "theorem colorFloor {D H loss : ℝ} (hh : 0 ≤ H) (hl : 0 ≤ loss)\n"
         "    (h : 3*(1/2:ℝ)+H+loss ≤ 2*D) : 3/4 ≤ D := by linarith\n"
         "\n"
         "theorem harmonicDifference {u v cross : ℝ} (hu : u=cross) (hv : v=cross) :\n"
         "    u+v-2*cross=0 := by linarith\n"
         "\n"
         "/-- A temporal Fourier coefficient solves the second-order Green recurrence. -/\n"
         "theorem greenInterior {r t : ℝ} (hr : r ≠ 0) (ht : t = r+r⁻¹) (n : ℕ) :\n"
         "    t*r^(n+1)-r^n-r^(n+2)=0 := by\n"
         "  rw [ht, pow_succ, pow_succ, pow_succ]\n"
         "  field_simp\n"
         "  ring\n"
         "\n"
         "theorem greenSource {r : ℝ} (h : r⁻¹-r ≠ 0) :\n"
         "    ((r+r⁻¹)-2*r)/(r⁻¹-r)=1 := by\n"
         "  apply (div_eq_one_iff_eq h).2\n"
         "  ring\n"
         "\n"
         "theorem radialCoefficient {p : ℝ} (hp : p ≠ 0) :\n"
         "    (120*(8*p/15))/(2*(2*p)^3)=4/p^2 := by\n"
         "  field_simp\n"
         "  ring\n"
         "\n"
         "theorem doubledThreshold : (Nat.choose 12 6)*Nat.factorial 6^2 = Nat.factorial 12 := by decide\n"
         "\n"
         "/-- Reflection gives a nonpositive expectation of a nonnegative square. -/\n"
         "theorem oddReflectionVanishes {α : Type*} [MeasurableSpace α] {μ : Measure α}\n"
         "    (f : α → ℝ) {c : ℝ} (hc : 0 < c) (hi : Integrable (fun x => (f x)^2) μ)\n"
         "    (hr : 0 ≤ -c * ∫ x, (f x)^2 ∂μ) : ∀ᵐ x ∂μ, f x = 0 := by\n"
         "  have hpos : 0 ≤ ∫ x, (f x)^2 ∂μ := integral_nonneg fun x => sq_nonneg (f x)\n"
         "  have hzero : (∫ x, (f x)^2 ∂μ) = 0 := by nlinarith\n"
         "  have he := (integral_eq_zero_iff_of_nonneg (fun x => sq_nonneg (f x)) hi).1 hzero\n"
         "  filter_upwards [he] with x hx\n"
         "  change (f x)^2 = 0 at hx\n"
         "  nlinarith\n"
         "\n"
         "theorem singleFaceCoefficient {p : ℝ} (hp : p ≠ 0) :\n"
         "    (6*(8*p/3))/(2*(2*p)^3)=1/p^2 := by\n"
         "  field_simp\n"
         "  ring\n"
         "\n"
         "theorem faceThreshold : (Nat.choose 8 4)*Nat.factorial 4^2 = Nat.factorial 8 := by decide\n"
         "\n"
         "/-- Iterating site-reflection Cauchy-Schwarz over successive doubled blocks. -/\n"
         "theorem iterateReflection (a : ℕ → ℝ) (hn : ∀ i, 0 ≤ a i)\n"
         "    (h : ∀ i, (a i)^2 ≤ a (i+1)) (n : ℕ) : (a 0)^(2^n) ≤ a n := by\n"
         "  induction n with\n"
         "  | zero => simp\n"
         "  | succ n ih =>\n"
         "    rw [pow_succ, pow_mul]\n"
         "    exact (pow_le_pow_left₀ (pow_nonneg (hn 0) _) ih 2).trans (h n)\n"
         "\n"
         "/-- The unbounded action is one half of the squared length of three colors. -/\n"
         "theorem actionMoments : ((3/4 : ℝ)^2+3/8=15/16) ∧ (3/2 : ℝ)*(1/2)^2=3/8 := by\n"
         "  norm_num\n"
         "\n"
         "end YangMills.TangentCurvature\n"
         "\n"
         "open YangMills.TangentCurvature\n"
         "#print axioms fourCubeCounts\n"
         "#print axioms cubeRanks\n"
         "#print axioms exactFaceCount\n"
         "#print axioms squareGradient\n"
         "#print axioms quaternionDeficit\n"
         "#print axioms temporalTilt\n"
         "#print axioms edgeVariance\n"
         "#print axioms wardCharacteristic\n"
         "#print axioms residualFactor\n"
         "#print axioms projectionDiagonal\n"
         "#print axioms traceOfProjection\n"
         "#print axioms colorFloor\n"
         "#print axioms harmonicDifference\n"
         "#print axioms greenInterior\n"
         "#print axioms greenSource\n"
         "#print axioms radialCoefficient\n"
         "#print axioms doubledThreshold\n"
         "#print axioms oddReflectionVanishes\n"
         "#print axioms singleFaceCoefficient\n"
         "#print axioms faceThreshold\n"
         "#print axioms iterateReflection\n"
         "#print axioms actionMoments\n"
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
