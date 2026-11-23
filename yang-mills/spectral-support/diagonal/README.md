# One late-time moment per cutoff

**Proposition.** Let $\nu_k$ be positive finite measures on $[0,\infty)$ that converge weakly as finite measures on $\mathbb R$ to $\mu$. Choose integers $t_k\to\infty$, a rate $r\ge0$, and a finite constant $M$. Suppose each sampled moment exists and, for all sufficiently large $k$,

$$\int x^{t_k}\,d\nu_k(x)\le M r^{t_k}.$$

Then $\mu((r,\infty))=0$. The measures can have different total masses. The time for one cutoff may differ from the time for every other cutoff. A4 and C4’s counterexample for arrays led to the question of what changes when each row is the moment sequence of a positive measure. [A4 review](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7090924547) · [C4 review](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7090921691) · [Lean source](CoherentDiagonal.lean)

For any $s>r$, positivity gives $s^{t_k}\nu_k((s,\infty))\le\int x^{t_k}\,d\nu_k$. The tail mass is eventually bounded by $M(r/s)^{t_k}\to0$. Portmanteau for the open tail gives $\mu((s,\infty))=0$. Lean uses convergence of total mass and the closed-complement form of Portmanteau. Taking the countable union at $s=r+1/(j+1)$ gives the result. The point mass $\delta_r$ attains the sampled bound at equality and can have full mass at the endpoint. [Earlier endpoint check](../SpectralLimit.lean)

## What the hypotheses exclude

| Test | Consequence |
|---|---|
| For an arbitrary array set $C(k,n)=0$ when $k=n$ and 1 otherwise. | Every fixed-time column tends to 1, the moments of $\delta_1$. The diagonal is zero. The theorem requires the bound to hold for the actual positive cutoff measure that converges. Lean checks both array limits. |
| Observe only integer times $0\le n\le L$ for $\delta_1$. | Its moments satisfy $1\le 2^L(1/2)^n$ throughout this window, and its full mass lies above $1/2$. Lean checks both statements. A fixed additive error in a late-time moment can likewise hide the exponential rate. |
| Take $r=1/2$, $x_k=(k+1)/(k+2)$ and $\nu_k=(1-r^k)\delta_r+r^k\delta_{x_k}$. | Its $k$th moment is at most $2r^k$, as checked by `disappearingWeight`. For any bounded continuous $f$, the error against $f(r)$ is bounded by $2\lVert f\rVert_\infty r^k$. The weak limit is $\delta_r$. At finite cutoff a mode can approach $x=1$ while its weight vanishes. The weak convergence and this physical interpretation are analytic. |

## Application to the mass gap

Fix a physical time unit $\tau>0$. For each centered gauge-invariant test vector, the cutoff transfer variable must have the same meaning along the trajectory, $x=e^{-\tau E}$. The observation at $t_k$ then measures the correlator at physical time $\tau t_k$. A lattice calculation at a rounded number of steps must justify that clock and the required bound for this same measure. The earlier lemma covers a one-step exponential envelope. [Clock and projection results](../README.md)

Choose $0<r<1$ common to a dense family of centered vectors in the reconstructed vacuum complement. For each vector, the prefactor, observation times and threshold cutoff may vary. If its cutoff spectral measures converge weakly to that vector’s continuum spectral measure and obey the displayed inequality, each has zero limiting mass on $(r,\infty)$. Density then makes the spectral projection there vanish. With the stated energy map this gives a lower energy bound $-\log(r)/\tau$ on that complement. This argument still needs a nontrivial interacting reconstruction, a common physical clock, and a positive diagonal estimate on a dense family for each required compact simple gauge group. A vanishing tested overlap alone yields no positive energy bound for other vectors. [Project rendezvous](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1)

## Execution and replay

Director D4 supplied the analytic Lean template. A measured PCP OS guest read it, appended the arbitrary-array control, and emitted the 6,157-byte source. A fresh Linux process with Lean 4.24.0 and Mathlib `f897ebcf72cd16f89ab4577d0c826cd14afaafc7` checked all five declarations. Each uses `propext`, `Classical.choice`, and `Quot.sound`. Three separate mutated modules failed where expected when the excluded tail included its endpoint, the array equality was reversed, or the bounded-window prefactor was reduced to one. A second boot reproduced every byte. Replaying the original finite certificate with the extended emitter also reproduced its previously recorded source and guest binary. [Native transcript](evidence/native-boot.txt) · [Lean and mutation output](evidence/lean.txt) · [PCP register](evidence/register.jsonl) · [Original environment and worker roles](../execution.md)

| SHA-256 | Item |
|---|---|
| `9cfb0ab9a111f2d2795415a30d1ba8d0ae8ec2b51738df4497eba1f4f839fb4d` | Admitted guest ELF |
| `02ebd938be4c8b41b3837c5f2dba783c214d54761c5e49ba5a1ccaf4d2a73435` | Assembled Lean source |

With the paths and toolchain from the [first replay](../execution.md), run the following commands.

```sh
python3 -I "$LANE/replay_native.py" --kernel "$KERNEL" --pcp-source "$PCP_SRC" --diagonal
cd "$MATHLIB"
lake exe cache get Mathlib/MeasureTheory/Measure/Portmanteau.lean Mathlib/MeasureTheory/Integral/Bochner/Set.lean Mathlib/Analysis/SpecificLimits/Basic.lean Mathlib/Tactic/Linarith.lean Mathlib/Tactic/Positivity.lean
lake env lean "$LANE/diagonal/CoherentDiagonal.lean"
```
