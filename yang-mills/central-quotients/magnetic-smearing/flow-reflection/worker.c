/* Recursive PCP work on a reflected magnetic covariance. */
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

static void parent(void) {
    int weights[3] = {3,-64,25};
    int group[5] = {0};
    for (unsigned i=0; i<3; ++i)
        for (unsigned j=0; j<3; ++j) group[i+j] += weights[i]*weights[j];
    emit("LEAN-BEGIN\n"
         "import Mathlib.Data.Complex.ExponentialBounds\n"
         "import Mathlib.Tactic.Linarith\n"
         "import Mathlib.Tactic.NormNum\n"
         "import Mathlib.Tactic.Positivity\n"
         "import Mathlib.Tactic.Ring\n"
         "\n"
         "namespace YangMills.FlowReflection\n"
         "\n"
         "theorem shiftedDistance (u v R : ℝ) : u - (-2*R-v) = u+v+2*R := by ring\n"
         "\n"
         "theorem fixedExponential (w R u v : ℝ) :\n"
         "    Real.exp (-w*(u+v+2*R)) =\n"
         "      Real.exp (-2*w*R)*Real.exp (-w*u)*Real.exp (-w*v) := by\n"
         "  rw [← Real.exp_add, ← Real.exp_add]\n"
         "  congr 1\n"
         "  ring\n"
         "\n"
         "theorem rankOnePositive {ι : Type*} (I : Finset ι) (c g : ι → ℝ) (d : ℝ) (hd : 0 ≤ d) :\n"
         "    0 ≤ ∑ i ∈ I, ∑ j ∈ I, c i * c j * (d*g i*g j) := by\n"
         "  have he : (∑ i ∈ I, ∑ j ∈ I, c i * c j * (d*g i*g j)) =\n"
         "      d*((∑ i ∈ I, c i*g i)*(∑ j ∈ I, c j*g j)) := by\n"
         "    simp only [Finset.sum_mul, Finset.mul_sum]\n"
         "    apply Finset.sum_congr rfl\n"
         "    intro i _\n"
         "    apply Finset.sum_congr rfl\n"
         "    intro j _\n"
         "    ring\n"
         "  rw [he]\n"
         "  exact mul_nonneg hd (mul_self_nonneg _)\n"
         "\n"
         "theorem heatDeficit {v : ℝ} (h0 : 0 ≤ v) (h1 : v ≤ 1) :\n"
         "    0 ≤ 1 - (1-v)^2 ∧ 1 - (1-v)^2 ≤ 2*v := by\n"
         "  constructor\n"
         "  · nlinarith [mul_nonneg h0 (sub_nonneg.mpr h1)]\n"
         "  · nlinarith [sq_nonneg v]\n"
         "\n"
         "/-- The connected OS form for coefficients (3,-64,25). -/\n"
         "def three (m : ℕ → ℝ) : ℝ :=\n"
         "  3*(3*m 1-64*m 2+25*m 3)-64*(3*m 2-64*m 3+25*m 4)+25*(3*m 3-64*m 4+25*m 5)\n"
         "\n"
         "theorem collected (m : ℕ → ℝ) : three m =\n"
         "    9*m 1-384*m 2+");
    number((unsigned)group[2]);
    emit("*m 3-3200*m 4+625*m 5 := by unfold three; ring\n"
         "\n"
         "theorem gridDrop (v : ℕ → ℝ) (hp : ∀ j, 0 ≤ v j-2*v (j+1)+v (j+2)) (n : ℕ) :\n"
         "    v 0-v n ≤ n*(v 0-v 1) := by\n"
         "  have hstep : ∀ j : ℕ, v j-v (j+1) ≤ v 0-v 1 := by\n"
         "    intro j\n"
         "    induction j with\n"
         "    | zero => exact le_rfl\n"
         "    | succ j ih => linarith [hp j]\n"
         "  induction n with\n"
         "  | zero => simp\n"
         "  | succ n ih =>\n"
         "    rw [Nat.cast_succ, add_mul, one_mul]\n"
         "    linarith [hstep n]\n"
         "\n"
         "/-- A quadratic increment bound and all reflected second differences force zero drop. -/\n"
         "theorem cuspRigidity (C : ℝ → ℝ) (K t : ℝ) (ht : 0 < t)\n"
         "    (hp : ∀ (h : ℝ), 0 < h → ∀ j : ℕ,\n"
         "      0 ≤ C (j*h)-2*C ((j+1:ℕ)*h)+C ((j+2:ℕ)*h))\n"
         "    (hs : ∀ h : ℝ, 0 < h → C 0-C h ≤ K*h^2) : C 0 ≤ C t := by\n"
         "  by_contra! hd\n"
         "  obtain ⟨n, hn⟩ := exists_nat_gt (max 0 (K*t^2/(C 0-C t)))\n"
         "  have hn0 : (0:ℝ) < n := lt_of_le_of_lt (le_max_left _ _) hn\n"
         "  have hn1 : K*t^2/(C 0-C t) < n := lt_of_le_of_lt (le_max_right _ _) hn\n"
         "  have hh := div_pos ht hn0\n"
         "  have h := gridDrop (fun j : ℕ => C ((j:ℝ)*(t/n))) (hp _ hh) n\n"
         "  simp only [Nat.cast_zero, zero_mul, Nat.cast_one, one_mul] at h\n"
         "  rw [show (n:ℝ)*(t/n)=t by field_simp] at h\n"
         "  have h' := h.trans (mul_le_mul_of_nonneg_left (hs _ hh) hn0.le)\n"
         "  have h'' : (C 0-C t)*n ≤ K*t^2 := by\n"
         "    calc\n"
         "      _ ≤ ((n:ℝ)*(K*(t/n)^2))*n := mul_le_mul_of_nonneg_right h' hn0.le\n"
         "      _ = _ := by field_simp\n"
         "                  ring\n"
         "  exact (not_lt_of_ge h'') (by nlinarith [(div_lt_iff₀ (sub_pos.mpr hd)).mp hn1])\n"
         "\n"
         "LEAN-END\n");

    request(1,4,2);
}
static void child(unsigned dim, unsigned pair) {
    if (dim!=4 || pair!=2) stop(5);
    /* Outward endpoints for 10000/e, using the more precise Mathlib bounds. */
    unsigned long scale = 100000000000000UL;
    unsigned lo = (unsigned)(scale/27182818286UL);
    unsigned hi = (unsigned)((scale+27182818283UL-1)/27182818283UL);
    /* Widen the upper bound to reproduce the stated interval. */
    ++hi;
    if (hi != 3680) stop(6);
    emit("LEAN-BEGIN\n"
         "/-- s = 1/8, T = h = 1; the common positive factor B is divided out. -/\n"
         "noncomputable def moment (k : ℕ) : ℝ :=\n"
         "  (1-(1+(k:ℝ)^2)*Real.exp (-((k:ℝ)^2)))^2 / (k:ℝ)^8\n"
         "\n"
         "theorem baseInterval : ");
    number(lo);
    emit("/10000 ≤ Real.exp (-1) ∧ Real.exp (-1) ≤ ");
    number(hi);
    emit("/10000 := by\n"
         "  rw [Real.exp_neg, inv_eq_one_div]\n"
         "  constructor\n"
         "  · apply (le_div_iff₀ (Real.exp_pos _)).2\n"
         "    linarith [Real.exp_one_lt_d9]\n"
         "  · apply (div_le_iff₀ (Real.exp_pos _)).2\n"
         "    linarith [Real.exp_one_gt_d9]\n"
         "\n"
         "theorem exponentialPower (k : ℕ) :\n"
         "    Real.exp (-((k:ℝ)^2)) = Real.exp (-1)^ (k^2) := by\n"
         "  rw [← Real.exp_nat_mul]\n"
         "  push_cast\n"
         "  ring_nf\n"
         "\n"
         "def side (k : ℕ) (q : ℝ) : ℝ := 1-(1+(k:ℝ)^2)*q^(k^2)\n"
         "\n"
         "theorem sides (k : ℕ) : side k (3680/10000) ≤ side k (Real.exp (-1)) ∧\n"
         "    side k (Real.exp (-1)) ≤ side k (3678/10000) := by\n"
         "  have hl := pow_le_pow_left₀ (show 0 ≤ (3678/10000:ℝ) by norm_num) baseInterval.1 (k^2)\n"
         "  have hu := pow_le_pow_left₀ (Real.exp_pos (-1)).le baseInterval.2 (k^2)\n"
         "  have hc : 0 ≤ 1+(k:ℝ)^2 := by positivity\n"
         "  exact ⟨sub_le_sub_left (mul_le_mul_of_nonneg_left hu hc) 1,\n"
         "         sub_le_sub_left (mul_le_mul_of_nonneg_left hl hc) 1⟩\n"
         "\n"
         "theorem enclose (k : ℕ) (lo hi : ℝ) (h0 : 0 ≤ side k (3680/10000))\n"
         "    (hl : lo ≤ (side k (3680/10000))^2 / (k:ℝ)^8)\n"
         "    (hu : (side k (3678/10000))^2 / (k:ℝ)^8 ≤ hi) : lo ≤ moment k ∧ moment k ≤ hi := by\n"
         "  rw [moment, exponentialPower]\n"
         "  change lo ≤ (side k (Real.exp (-1)))^2 / (k:ℝ)^8 ∧ _ ≤ hi\n"
         "  have H := sides k\n"
         "  exact ⟨hl.trans (div_le_div_of_nonneg_right (pow_le_pow_left₀ h0 H.1 2) (by positivity)),\n"
         "    (div_le_div_of_nonneg_right (pow_le_pow_left₀ (h0.trans H.1) H.2 2) (by positivity)).trans hu⟩\n"
         "LEAN-END\n");

    request(2,dim,pair);
}
static void grandchild(unsigned dim, unsigned pair) {
    if (dim!=4 || pair!=2) stop(5);
    long coeff[5] = {9,-384,4246,-3200,625};
    long endpoints[5] = {699073600,32227030,1520406,152587,25600};
    long upper = 0;
    for (unsigned n=0; n<5; ++n) upper += coeff[n]*endpoints[n];
    if (upper>=0 || -upper>2147483647L) stop(6);
    emit("LEAN-BEGIN\n"
         "theorem explicitNegative : three moment ≤ -");
    number((unsigned)(-upper));
    emit("/10000000000 := by\n"
         "  have h1 := enclose 1 (696960000/10000000000) (699073600/10000000000) (by norm_num [side]) (by norm_num [side]) (by norm_num [side])\n"
         "  have h2 := enclose 2 (32227030/10000000000) (32241167/10000000000) (by norm_num [side]) (by norm_num [side]) (by norm_num [side])\n"
         "  have h3 := enclose 3 (1520387/10000000000) (1520406/10000000000) (by norm_num [side]) (by norm_num [side]) (by norm_num [side])\n"
         "  have h4 := enclose 4 (152587/10000000000) (152588/10000000000) (by norm_num [side]) (by norm_num [side]) (by norm_num [side])\n"
         "  have h5 := enclose 5 (25599/10000000000) (25600/10000000000) (by norm_num [side]) (by norm_num [side]) (by norm_num [side])\n"
         "  rw [collected]\n"
         "  linarith [h1.2,h2.1,h3.2,h4.1,h5.2]\n"
         "\n"
         "theorem signedTest : three moment < 0 := lt_of_le_of_lt explicitNegative (by norm_num)\n"
         "\n"
         "theorem samePlaneError {Q A e : ℝ} (bound : -(2*A*e+e^2) ≤ Q) (h : Q < 0) :\n"
         "    -Q ≤ 2*A*e+e^2 ∧ 0 < 2*A*e+e^2 := by constructor <;> linarith\n"
         "\n"
         "end YangMills.FlowReflection\n"
         "open YangMills.FlowReflection\n"
         "#print axioms shiftedDistance\n"
         "#print axioms fixedExponential\n"
         "#print axioms rankOnePositive\n"
         "#print axioms heatDeficit\n"
         "#print axioms collected\n"
         "#print axioms baseInterval\n"
         "#print axioms exponentialPower\n"
         "#print axioms sides\n"
         "#print axioms enclose\n"
         "#print axioms explicitNegative\n"
         "#print axioms signedTest\n"
         "#print axioms samePlaneError\n"
         "#print axioms gridDrop\n"
         "#print axioms cuspRigidity\n"
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
