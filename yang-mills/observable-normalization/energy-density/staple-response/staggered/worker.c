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
    emit("A4 LEAN import Mathlib.Analysis.SpecialFunctions.Integrals\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN open scoped BigOperators\n");
    emit("A4 LEAN namespace YangMills.Staggered\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Move a nearest-neighbor pair of faces from a link sum onto the test\n");
    emit("A4 LEAN function. The permutation can be a shift on any finite periodic lattice. -/\n");
    emit("A4 LEAN theorem moveShift {α : Type*} [Fintype α] (e : α ≃ α) (w f : α → ℝ) :\n");
    emit("A4 LEAN     (∑ x, w x*(f x+f (e.symm x))) = ∑ x, (w x+w (e x))*f x := by\n");
    emit("A4 LEAN   simp_rw [mul_add, add_mul]\n");
    emit("A4 LEAN   rw [Finset.sum_add_distrib, Finset.sum_add_distrib]\n");
    emit("A4 LEAN   congr 1\n");
    emit("A4 LEAN   simpa using (Equiv.sum_comp e.symm (fun y => w (e y)*f y))\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem alternatingFace {α : Type*} [Fintype α] (e : α ≃ α) (χ ψ f : α → ℝ)\n");
    emit("A4 LEAN     (flip : ∀ x, χ (e x) = -χ x) :\n");
    emit("A4 LEAN     (∑ x, χ x*ψ x*(f x+f (e.symm x))) = ∑ x, χ x*(ψ x-ψ (e x))*f x := by\n");
    emit("A4 LEAN   rw [moveShift e (fun x => χ x*ψ x) f]\n");
    emit("A4 LEAN   apply Finset.sum_congr rfl\n");
    emit("A4 LEAN   intro x _\n");
    emit("A4 LEAN   rw [flip]\n");
    emit("A4 LEAN   ring\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem uniformZero {α : Type*} [Fintype α] (e : α ≃ α) (χ f : α → ℝ)\n");
    emit("A4 LEAN     (flip : ∀ x, χ (e x) = -χ x) : (∑ x, χ x*(f x+f (e.symm x)))=0 := by\n");
    emit("A4 LEAN   simpa using alternatingFace e χ (fun _ => 1) f flip\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem secondStencil (x j k : ℝ) :\n");
    emit("A4 LEAN     x^2-(x+j)^2-(x-k)^2+(x+j-k)^2=-2*j*k := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem mixedStencil (x y j k l m : ℝ) :\n");
    emit("A4 LEAN     x*y-(x+j)*(y+l)-(x-k)*(y-m)+(x+j-k)*(y+l-m)=-(j*m+k*l) := by ring\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem coefficient (v : ℝ) : (-1/2:ℝ)*((-2)*v/1536)=v/1536 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem compensateReciprocal {β S : ℝ} (hβ : β ≠ 0) (h : 6*β-S ≠ 0) :\n");
    emit("A4 LEAN     β^3*(-3/(4*(6*β-S))+1/(8*β)+S/(48*β^2))+S^2/288 =\n");
    emit("A4 LEAN     -S^3/(288*(6*β-S)) := by field_simp; ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.Staggered\n");
    emit("A4 LEAN #print axioms YangMills.Staggered.moveShift\n");
    emit("A4 LEAN #print axioms YangMills.Staggered.alternatingFace\n");
    emit("A4 LEAN #print axioms YangMills.Staggered.uniformZero\n");
    emit("A4 LEAN #print axioms YangMills.Staggered.secondStencil\n");
    emit("A4 LEAN #print axioms YangMills.Staggered.mixedStencil\n");
    emit("A4 LEAN #print axioms YangMills.Staggered.coefficient\n");
    emit("A4 LEAN #print axioms YangMills.Staggered.compensateReciprocal\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
