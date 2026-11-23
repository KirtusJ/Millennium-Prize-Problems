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
    emit("A4 LEAN import Mathlib.MeasureTheory.Integral.Bochner.Set\n");
    emit("A4 LEAN import Mathlib.Analysis.SpecialFunctions.Pow.Real\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace NavierStokes.PressureAudit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN noncomputable def printed (R B : ℝ) : ℝ :=\n");
    emit("A4 LEAN   (B+1)*B^(1/2:ℝ)/R + R^(-(7/4:ℝ))*B^(3/4:ℝ)\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN noncomputable def formal (R A B : ℝ) : ℝ :=\n");
    emit("A4 LEAN   (B^(1/2:ℝ)+1)*(A/R+1/R^2) + R^(-(7/4:ℝ))*B^(3/4:ℝ)\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- At unit radius and unit localized L6 norm the paper gives a constant. -/\n");
    emit("A4 LEAN theorem printedUnit : printed 1 1 = 3 := by norm_num [printed]\n");
    emit("A4 LEAN \n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN /-- At the same inputs the comparison envelope grows with dissipation. -/\n");
    emit("A4 LEAN theorem formalUnit (A : ℝ) :\n");
    emit("A4 LEAN     formal 1 A 1 = 2*A+3 := by\n");
    emit("A4 LEAN   simp [formal]\n");
    emit("A4 LEAN   ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Even with B ≤ A+1, no constant multiple of the printed unit envelope\n");
    emit("A4 LEAN dominates the formal one for every possible nonnegative scalar A. -/\n");
    emit("A4 LEAN theorem noUniformComparison (C : ℝ) (hC : 0 ≤ C) :\n");
    emit("A4 LEAN     ∃ A : ℝ, 0 ≤ A ∧ 1 ≤ A+1 ∧ C * printed 1 1 < formal 1 A 1 := by\n");
    emit("A4 LEAN   simp only [printedUnit, formalUnit]\n");
    emit("A4 LEAN   exact ⟨2*C, by linarith, by linarith, by linarith⟩\n");
    emit("A4 LEAN \n");
#elif ROLE == 2
    emit("A4 LEAN /-- An absorption argument may still use the full dissipation in the energy balance. -/\n");
    emit("A4 LEAN theorem absorb {rate diss growth flux rem : ℝ}\n");
    emit("A4 LEAN     (budget : rate/2 + diss ≤ growth+flux)\n");
    emit("A4 LEAN     (control : flux ≤ diss/2+rem) (hd : 0 ≤ diss) :\n");
    emit("A4 LEAN     rate ≤ 2*growth+2*rem := by linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end NavierStokes.PressureAudit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN #print axioms NavierStokes.PressureAudit.printedUnit\n");
    emit("A4 LEAN #print axioms NavierStokes.PressureAudit.formalUnit\n");
    emit("A4 LEAN #print axioms NavierStokes.PressureAudit.noUniformComparison\n");
    emit("A4 LEAN #print axioms NavierStokes.PressureAudit.absorb\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
