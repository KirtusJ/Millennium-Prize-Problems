/* A bounded proof-template worker for the PCP OS user ABI. ROLE selects a subgoal. */
#ifndef ROLE
#error ROLE required
#endif
__attribute__((used)) static volatile int worker_role = ROLE + 1;
static long sys(long n,long a,long b,long c) {
    long result;
    __asm__ volatile("syscall":"=a"(result):"a"(n),"D"(a),"S"(b),"d"(c):"rcx","r11","memory");
    return result;
}
static void emit(const char *s) {
    unsigned len=0;
    while(s[len]) ++len;
    while(len){
        long k=sys(1,1,(long)s,len);
        if(k<=0 || (unsigned long)k>len){sys(60,1,0,0);__builtin_unreachable();}
        len-=(unsigned)k;s+=k;
    }
}
__attribute__((used,noreturn)) static void run(void) {
#if ROLE == 0
    emit("A4 CHILD spectrum\n");
    emit("A4 LEAN import Mathlib.Data.Real.Basic\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN namespace YangMills.Plaquette\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- The second trace is that of P Q^{-1}, with the common edge forward in both loops. -/\n");
    emit("A4 LEAN theorem joinedTrace (a b x y z u v w : ℝ) :\n");
    emit("A4 LEAN     (2*(a*b + x*u + y*v + z*w))/2 - (2*a)*(2*b)/4 =\n");
    emit("A4 LEAN       x*u + y*v + z*w := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- With the same edge convention, the defect instead uses the trace of P Q. -/\n");
    emit("A4 LEAN theorem mismatch (a b x y z u v w : ℝ)\n");
    emit("A4 LEAN     (hp : a^2+x^2+y^2+z^2=1) (hq : b^2+u^2+v^2+w^2=1) :\n");
    emit("A4 LEAN     (x+u)^2+(y+v)^2+(z+w)^2 =\n");
    emit("A4 LEAN       2-2*(a*b-x*u-y*v-z*w)-(a-b)^2 := by\n");
    emit("A4 LEAN   linarith only [hp,hq]\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- For equal diagonal gradient moments A and cross moment B. -/\n");
    emit("A4 LEAN theorem edgeDecomposition (c d A B : ℝ) :\n");
    emit("A4 LEAN     A*c^2+2*B*c*d+A*d^2 = A*(c-d)^2+c*d*(2*A+2*B) := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- A uniform estimate for signed coefficients on a pair of neighboring plaquettes. -/\n");
    emit("A4 LEAN theorem edgeUpper (c d A B : ℝ) (hm : 0 ≤ A-B) (hp : 0 ≤ A+B) :\n");
    emit("A4 LEAN     A*c^2+2*B*c*d+A*d^2 ≤ 2*A*(c^2+d^2) := by\n");
    emit("A4 LEAN   have h := mul_nonneg hm (sq_nonneg (c+d))\n");
    emit("A4 LEAN   have g := mul_nonneg hp (sq_nonneg (c-d))\n");
    emit("A4 LEAN   linarith only [h,g]\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- A measured upper energy form and positive variance bound work for the same smearing. -/\n");
    emit("A4 LEAN theorem commonSmearing {energy variance R numerator denominator : ℝ}\n");
    emit("A4 LEAN     (hvar : 0 < variance) (hden : denominator ≤ variance)\n");
    emit("A4 LEAN     (hnum : energy ≤ numerator) (hcmp : numerator ≤ R*denominator) (hR : 0 ≤ R) :\n");
    emit("A4 LEAN     energy / variance ≤ R := by\n");
    emit("A4 LEAN   exact (div_le_iff₀ hvar).mpr (hnum.trans (hcmp.trans (mul_le_mul_of_nonneg_left hden hR)))\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.Plaquette\n");
    emit("A4 LEAN #print axioms YangMills.Plaquette.joinedTrace\n");
    emit("A4 LEAN #print axioms YangMills.Plaquette.mismatch\n");
    emit("A4 LEAN #print axioms YangMills.Plaquette.edgeDecomposition\n");
    emit("A4 LEAN #print axioms YangMills.Plaquette.edgeUpper\n");
    emit("A4 LEAN #print axioms YangMills.Plaquette.commonSmearing\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
