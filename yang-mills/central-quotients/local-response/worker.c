/* The parent conditions four lateral signs, the child evaluates a signed
   two-state channel, and the grandchild computes two center moments.
   Each process returns its part of the Lean source on serial. */
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


static unsigned gcd(unsigned a, unsigned b) {
    while (b) {
        unsigned r = a % b;
        a = b;
        b = r;
    }
    return a;
}

static void parity(void) {
    unsigned sums[2] = {0,0};
    for (unsigned mask = 0; mask < 16; ++mask) {
        unsigned minus = 0, weight = 1;
        for (unsigned i = 0; i < 4; ++i) {
            if ((mask >> i) & 1) ++minus;
            else weight *= 4;
        }
        sums[minus % 2] += weight;
    }
    emit("LEAN-BEGIN\n"
         "import Mathlib.Analysis.Calculus.Deriv.Mul\n"
         "import Mathlib.Analysis.Calculus.Deriv.Add\n"
         "import Mathlib.Analysis.InnerProductSpace.Basic\n"
         "import Mathlib.Tactic.LinearCombination\n"
         "import Mathlib.Tactic.FieldSimp\n"
         "import Mathlib.Tactic.Linarith\n"
         "import Mathlib.Tactic.NoncommRing\n"
         "import Mathlib.Tactic.NormNum\n"
         "import Mathlib.Tactic.Ring\n"
         "\n"
         "namespace YangMills.CentralQuotient.LocalResponse\n"
         "\n"
         "def lateralWeight (odd : Bool) : ℕ :=\n"
         "  ((List.range 16).map fun mask =>\n"
         "    let k := ((List.range 4).filter mask.testBit).length\n"
         "    if (k % 2 == 1) == odd then 4^(4-k) else 0).sum\n"
         "\n"
         "theorem lateralCensus : lateralWeight false = ");
    number(sums[0]);
    emit(" ∧ lateralWeight true = ");
    number(sums[1]);
    emit(" := by decide +kernel\n"
         "\n"
         "/-- Uniform average over a single unbiased center sign. -/\n"
         "noncomputable def signAverage (f : ℝ → ℝ) : ℝ := (f 1 + f (-1)) / 2\n"
         "\n"
         "/-- Conditional face parity fixes the fourth lateral sign from the other three. -/\n"
         "theorem cubeParityAverage (p a b c d : ℝ) :\n"
         "    signAverage (fun x => signAverage (fun y => signAverage (fun z =>\n"
         "      (1+a*x)*(1+b*y)*(1+c*z)*(1+d*p*x*y*z)))) = 1 + p*a*b*c*d := by\n"
         "  unfold signAverage\n"
         "  ring\n"
         "\n"
         "/-- Mean of the next sign conditioned on the preceding sign. Here j is its\n"
         "signed bond, including the preceding sign, and m is the effective suffix bias. -/\n"
         "noncomputable def nextMean (m j : ℝ) : ℝ := (m+j)/(1+m*j)\n"
         "\n"
         "noncomputable def transmission (m j : ℝ) : ℝ := j*(1-m^2)/(1-(m*j)^2)\n"
         "\n"
         "private theorem mul_abs_lt_one {m j : ℝ} (hm : |m| ≤ 1) (hj : |j| < 1) :\n"
         "    |m*j| < 1 := by\n"
         "  rw [abs_mul]\n"
         "  calc |m| * |j| ≤ 1 * |j| := mul_le_mul_of_nonneg_right hm (abs_nonneg j)\n"
         "       _ < 1 := by simpa using hj\n"
         "\n"
         "theorem conditionalSlope {m j : ℝ} (hm : |m| ≤ 1) (hj : |j| < 1) :\n"
         "    (nextMean m j - nextMean m (-j))/2 = transmission m j := by\n"
         "  obtain ⟨lo,hi⟩ := abs_lt.mp (mul_abs_lt_one hm hj)\n"
         "  have hp : 1+m*j ≠ 0 := by linarith\n"
         "  have hn : 1-m*j ≠ 0 := by linarith\n"
         "  have hprod : 1-(m*j)^2 ≠ 0 := by\n"
         "    rw [show 1-(m*j)^2 = (1-m*j)*(1+m*j) by ring]\n"
         "    exact mul_ne_zero hn hp\n"
         "  simp only [nextMean, transmission, mul_neg, ← sub_eq_add_neg]\n"
         "  field_simp [hp, hn, hprod]\n"
         "  ring\n"
         "\n"
         "LEAN-END\n");
    request(1,2,4);
}

static void channel(unsigned signs, unsigned faces) {
    if (signs != 2 || faces != 4) stop(5);
    /* Prior weights 4,1 and parallel/antiparallel bond weights 3,1.
       Positive-next probabilities are 12/13 and 4/7 respectively. */
    unsigned up_total = 4*3+1, down_total = 4+3;
    unsigned den = up_total * down_total;
    unsigned num = 4*3*down_total - 4*up_total;
    unsigned common = gcd(num,den);
    emit("LEAN-BEGIN\n"
         "\n"
         "theorem signedChannelExample : (nextMean (3/5) (1/2) - nextMean (3/5) (-(1/2)))/2 =\n"
         "    (");
    number(num/common);
    emit("/");
    number(den/common);
    emit(" : ℝ) := by norm_num [nextMean]\n"
         "/-- Uniform over every suffix field. Equality holds when m = 0. -/\n"
         "theorem transmissionBound {m j : ℝ} (hm : |m| ≤ 1) (hj : |j| < 1) :\n"
         "    |transmission m j| ≤ |j| := by\n"
         "  obtain ⟨mlo,mhi⟩ := abs_le.mp hm\n"
         "  obtain ⟨jlo,jhi⟩ := abs_lt.mp hj\n"
         "  obtain ⟨lo,hi⟩ := abs_lt.mp (mul_abs_lt_one hm hj)\n"
         "  have hm2 : 0 ≤ 1-m^2 := by nlinarith [mul_nonneg (by linarith : 0 ≤ 1-m) (by linarith : 0 ≤ 1+m)]\n"
         "  have hj2 : 0 ≤ 1-j^2 := by nlinarith [mul_nonneg (by linarith : 0 ≤ 1-j) (by linarith : 0 ≤ 1+j)]\n"
         "  have hd : 0 < 1-(m*j)^2 := by\n"
         "    nlinarith [mul_pos (by linarith : 0 < 1-m*j) (by linarith : 0 < 1+m*j)]\n"
         "  have hsmall : 1-m^2 ≤ 1-(m*j)^2 := by nlinarith [mul_nonneg (sq_nonneg m) hj2]\n"
         "  rw [transmission, abs_div, abs_mul, abs_of_nonneg hm2, abs_of_pos hd, div_le_iff₀ hd]\n"
         "  exact mul_le_mul_of_nonneg_left hsmall (abs_nonneg j)\n"
         "\n"
         "theorem zeroFieldSharp (j : ℝ) : transmission 0 j = j := by simp [transmission]\n"
         "\n"
         "theorem stripPropagation (v m j B : ℕ → ℝ)\n"
         "    (bias : ∀ n, |m n| ≤ 1) (bond : ∀ n, |j n| < 1)\n"
         "    (majorant : ∀ n, |j n| ≤ B n)\n"
         "    (step : ∀ n, v (n+1) = transmission (m n) (j n) * v n) (d : ℕ) :\n"
         "    |v d| ≤ |v 0| * ∏ i ∈ Finset.range d, B i := by\n"
         "  induction d with\n"
         "  | zero => simp\n"
         "  | succ n ih =>\n"
         "    rw [step, abs_mul, Finset.prod_range_succ]\n"
         "    calc\n"
         "      _ ≤ B n * |v n| :=\n"
         "        mul_le_mul_of_nonneg_right ((transmissionBound (bias n) (bond n)).trans (majorant n)) (abs_nonneg _)\n"
         "      _ ≤ B n * (|v 0| * ∏ i ∈ Finset.range n, B i) :=\n"
         "        mul_le_mul_of_nonneg_left ih ((abs_nonneg _).trans (majorant n))\n"
         "      _ = _ := by ring\n"
         "\n"
         "/-- Both endpoints have bare bias m and the interior has effective bond k. -/\n"
         "theorem endpointCovariance (m k : ℝ) (h : 1+k*m^2 ≠ 0) :\n"
         "    (m^2+k)/(1+k*m^2) - (m*(1+k)/(1+k*m^2))^2 =\n"
         "      k*(1-m^2)^2/(1+k*m^2)^2 := by\n"
         "  field_simp\n"
         "  ring\n"
         "\n"
         "LEAN-END\n");
    request(2,signs,faces);
}

static void transfer(unsigned signs, unsigned faces) {
    if (signs != 2 || faces != 4) stop(5);
    const int twice_cos_2[2] = {2,-2}, twice_cos_3[3] = {2,-1,-1};
    unsigned order_two = 0, order_three = 0;
    for (unsigned k = 0; k < 2; ++k) order_two += twice_cos_2[k]*twice_cos_2[k];
    for (unsigned k = 0; k < 3; ++k) order_three += twice_cos_3[k]*twice_cos_3[k];
    emit("LEAN-BEGIN\n"
         "/-- The missing two-step return through the orthogonal complement.\n"
         "The algebraic identity needs only idempotence. -/\n"
         "theorem twoStepDifference {A : Type*} [Ring A] (P T : A) (hP : P*P = P) :\n"
         "    P*T^2*P - (P*T*P)^2 = P*T*(1-P)*T*P := by\n"
         "  have cancel : (P*T*P)^2 = P*T*P*T*P := by\n"
         "    calc (P*T*P)^2 = P*T*(P*P)*T*P := by noncomm_ring\n"
         "         _ = _ := by rw [hP]\n"
         "  rw [cancel]\n"
         "  noncomm_ring\n"
         "\n"
         "open scoped ComplexInnerProductSpace\n"
         "\n"
         "/-- Quadratic-form version for a complex Hilbert-space test fixed by P.\n"
         "The symmetry premises are sufficient for this identity. -/\n"
         "theorem twoStepEnergy {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H]\n"
         "    (P T : H → H) (p2 : ∀ x, P (P x) = P x)\n"
         "    (ps : ∀ x y, ⟪P x,y⟫ = ⟪x,P y⟫) (ts : ∀ x y, ⟪T x,y⟫ = ⟪x,T y⟫)\n"
         "    (f : H) (fixed : P f = f) :\n"
         "    (⟪f,P (T (T f))⟫).re - (⟪f,P (T (P (T f)))⟫).re =\n"
         "      ‖T f-P (T f)‖^2 := by\n"
         "  have first : ⟪f,P (T (T f))⟫ = ⟪T f,T f⟫ := by\n"
         "    calc _ = ⟪P f,T (T f)⟫ := (ps _ _).symm\n"
         "         _ = ⟪f,T (T f)⟫ := by rw [fixed]\n"
         "         _ = _ := (ts _ _).symm\n"
         "  have second : ⟪f,P (T (P (T f)))⟫ = ⟪T f,P (T f)⟫ := by\n"
         "    calc _ = ⟪P f,T (P (T f))⟫ := (ps _ _).symm\n"
         "         _ = ⟪f,T (P (T f))⟫ := by rw [fixed]\n"
         "         _ = _ := (ts _ _).symm\n"
         "  rw [first, second]\n"
         "  have cross : ⟪T f,P (T f)⟫ = ⟪P (T f),P (T f)⟫ := by rw [ps (T f), p2]\n"
         "  rw [norm_sub_sq (𝕜 := ℂ), cross]\n"
         "  change (RCLike.re ⟪T f,T f⟫) - (RCLike.re ⟪P (T f),P (T f)⟫) =\n"
         "    ‖T f‖^2 - 2*(RCLike.re ⟪P (T f),P (T f)⟫) + ‖P (T f)‖^2\n"
         "  simp only [inner_self_eq_norm_sq]\n"
         "  ring\n"
         "\n"
         "/-- The lists give twice the real parts of the second and third roots of unity. -/\n"
         "theorem centerSquareSums :\n"
         "    (([2, -2] : List ℤ).map (fun x => x^2)).sum = ");
    number(order_two);
    emit(" := by decide +kernel\n"
         "\n"
         "theorem cubicCenterSquareSum :\n"
         "    (([2, -1, -1] : List ℤ).map (fun x => x^2)).sum = ");
    number(order_three);
    emit(" := by decide +kernel\n"
         "\n"
         "/-- Differentiate the weighted Wronskian using the two radial equations. -/\n"
         "theorem fluxDerivative (u v p : ℝ → ℝ) (r du dv au av w E l κ : ℝ)\n"
         "    (hu : HasDerivAt u du r) (hv : HasDerivAt v dv r)\n"
         "    (hpu : HasDerivAt (fun x => p x * deriv u x) au r)\n"
         "    (hpv : HasDerivAt (fun x => p x * deriv v x) av r)\n"
         "    (su : κ*au = -(E+l*r)*w*u r) (sv : κ*av = -(E-l*r)*w*v r) :\n"
         "    HasDerivAt (fun x => κ * (p x * deriv u x * v x - p x * deriv v x * u x))\n"
         "      (-2*l*r*w*u r*v r) r := by\n"
         "  have h := ((hpu.mul hv).sub (hpv.mul hu)).const_mul κ\n"
         "  convert h using 1\n"
         "  rw [hu.deriv, hv.deriv]\n"
         "  linear_combination -(v r)*su + (u r)*sv\n"
         "\n"
         "/-- Fibrewise density reduces to two independent real rows. -/\n"
         "theorem fibreSeparation {K : Type*} [Field K] (u v a b x y : K)\n"
         "    (det : u*b-v*a ≠ 0) (h : u*x+v*y = 0) (k : a*x+b*y = 0) : x=0 ∧ y=0 := by\n"
         "  have hx : (u*b-v*a)*x = 0 := by linear_combination b*h - v*k\n"
         "  have hy : (u*b-v*a)*y = 0 := by linear_combination u*k - a*h\n"
         "  exact ⟨(mul_eq_zero.mp hx).resolve_left det, (mul_eq_zero.mp hy).resolve_left det⟩\n"
         "\n"
         "end YangMills.CentralQuotient.LocalResponse\n"
         "\n"
         "open YangMills.CentralQuotient.LocalResponse\n"
         "#print axioms lateralCensus\n"
         "#print axioms cubeParityAverage\n"
         "#print axioms conditionalSlope\n"
         "#print axioms transmissionBound\n"
         "#print axioms signedChannelExample\n"
         "#print axioms centerSquareSums\n"
         "#print axioms cubicCenterSquareSum\n"
         "#print axioms zeroFieldSharp\n"
         "#print axioms stripPropagation\n"
         "#print axioms endpointCovariance\n"
         "#print axioms twoStepDifference\n"
         "#print axioms twoStepEnergy\n"
         "#print axioms fluxDerivative\n"
         "#print axioms fibreSeparation\n"
         "LEAN-END\n");
}

__attribute__((used,noreturn)) static void run(void) {
    static unsigned char input[4];
    long fd = syscall3(2, (long)"task.bin", 0, 0);
    if (fd < 0 || syscall3(0, fd, (long)input, sizeof input) != 3 ||
        syscall3(0, fd, (long)(input+3), 1) != 0 || syscall3(3, fd, 0, 0) != 0) stop(2);
    if (!input[0] && !input[1] && !input[2]) parity();
    else if (input[0] == 1) channel(input[1],input[2]);
    else if (input[0] == 2) transfer(input[1],input[2]);
    else stop(2);
    stop(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
