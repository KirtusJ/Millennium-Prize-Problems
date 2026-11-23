# A gap above all zero-energy states

A spectral gap $m>0$ above the vacuum sector means $P_H((0,m))=0$ for the nonnegative Hamiltonian $H$ in the specified reconstructed representation. That sector may contain several zero-energy states. Subtracting the expectation in one vacuum removes its component alone. Z4’s product-group scaling control brought this distinction to the director review. [Z4’s correction](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7091266599)

Fix a physical time difference $s>0$. For a state with scalar positive spectral measure $\mu$, set $C(t)=\int e^{-tE}\,d\mu(E)$. The vector $(I-e^{-sH})v$ has measure

$$d\nu_s(E)=(1-e^{-sE})^2\,d\mu(E).$$

For every set $A$, Lean proves $\nu_s(A)=0$ if and only if $\mu(A\setminus\{0\})=0$. Its positive-time observable is the three-reading combination

$$D_s C(t)=C(t)-2C(t+s)+C(t+2s)=\int e^{-tE}\,d\nu_s(E).$$

Lean also derives integrability of the right-hand side from integrability at the three raw measurement times. These statements hold even if the raw measure has infinite total mass. If $T_k\to\infty$ and $D_s C(T_k)\le M e^{-mT_k}$ eventually, the checked spectral theorem now yields $\mu((0,m))=0$. Neither endpoint is excluded. For cutoff-dependent spectra, apply the [positive-time transfer](../README.md) to the *filtered* measures first: the earlier and later fixed-time difference limits and the late difference must come from the same cutoff row. The directly checked theorem `positiveGapAboveKernel` assumes the displayed envelope on the reconstructed measure. [Lean declarations](GapAboveVacuum.lean)

If this holds at the same $m$ for a dense family of vectors in the chosen reconstructed space, the continuous projection $P_H((0,m))$ vanishes throughout. For a smaller family, the conclusion is confined to the subspace it generates under the stated spectral tests. Vacuum uniqueness, a nonzero excitation, reconstruction of the field theory, and the uniform interacting envelope are separate inputs. The quadratic weight only determines whether positive-energy sets have *zero* mass. It does not give a uniform lower bound on the fraction of spectral weight retained as $E\downarrow0$.

## Controls and measurement requirements

* **Two vacuum states.** Let $H=\operatorname{diag}(0,0,1)$, choose the first basis vector as vacuum, and test the vector $e_2+e_3$. It is already orthogonal to that vacuum and has $C(t)=1+e^{-t}$. At $s=\log2$, its second difference is $e^{-t}/4$. The original measure has both a zero-energy atom and an atom at the exact threshold 1. The gap statement is correct despite both atoms. This finite-dimensional example is analytic.
* **A shrinking filter can counterfeit a higher gap.** Take $\mu=\delta_1$ and $s_k=e^{-T_k}$. Since $1-e^{-s_k}\le s_k$, the unnormalized difference at $T_k$ is at most $e^{-3T_k}$ although the physical energy is one. At every fixed positive time, the filtered correlation tends to zero. Lean checks the inequality. The conclusion requires the limiting test to retain positive weight at each positive energy, as a fixed physical $s>0$ does. A clock step that shrinks with the lattice spacing cannot automatically serve as that test.
* **Raw error propagation.** If the three readings have certified absolute errors $e_0,e_1,e_2$, the absolute error of their second difference is at most $e_0+2e_1+e_2$. Exact cancellation of constant vacuum correlations does not ensure the same cancellation for measurement errors. To use the subrate version at late $T_k$, the resulting error times $e^{bT_k}$ must vanish for every $b<m$, or a tighter certified joint bound must replace it.

## Execution

The three-stage PCP OS path used the reciprocal root 1. The assembled 5,873-byte Lean source has SHA-256 `2002c660d00ff94e5714aa7e3f3c69fa8946181174dc518fbee21e13845ad6d8`. The guest ELF has SHA-256 `81ee0657560726917fcae43810d3faac7e2827c2a3250bcff4a481369552d198`. The parent emitted the factor $1-q$, its child computed the coefficients $1,-2,1$, and the grandchild assembled the source and the zero-set control. Each stage booted its own measured kernel under a nested registered host process. The analytic template was written by D4. Lean ran on the host with the checked [PositiveTime dependency](../PositiveTime.lean), version 4.24.0 and Mathlib `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`. The five resulting declarations used only `propext`, `Classical.choice`, and `Quot.sound`. Four false mutations exercised inclusion of the vacuum, a zero filter time, the wrong polynomial sign and an overstrong rate. [Check output](evidence/checks.txt) · [Factor boot](evidence/factor.serial.txt) · [Square boot](evidence/square.serial.txt) · [Assembly boot](evidence/assemble.serial.txt) · [Register](evidence/register.jsonl)

Use the [same kernel, compiler and Mathlib pins as the positive-time calculation](../execution.md). In a shell with Lean 4.24.0 on the executable path, the final two invocations compile the dependency and check the difference result. Both native modes replay independently.

```sh
python3 -I "$LANE/positive-time/replay.py" --kernel "$KERNEL" --pcp-source "$PCP_SRC" --difference
cd "$MATHLIB"
lake exe cache get Mathlib/MeasureTheory/Integral/Bochner/ContinuousLinearMap.lean
D4_OLEAN=$(mktemp -d)
lake env lean --root="$LANE/positive-time" -o "$D4_OLEAN/PositiveTime.olean" "$LANE/positive-time/PositiveTime.lean"
lake env sh -c 'export LEAN_PATH="$1:$LEAN_PATH"; exec lean "$2"' sh "$D4_OLEAN" "$LANE/positive-time/vacuum/GapAboveVacuum.lean"
```
