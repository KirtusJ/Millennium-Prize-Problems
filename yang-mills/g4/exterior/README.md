# Which Wilson links can be integrated out without changing physical states?

Director G4 · November 23, 2026. For the site reflection at time zero, **retain the spatial links on the reflection slice**. Integrating A4's remaining selected links then preserves every reflected inner product of bounded gauge-invariant closed-half cylinder observables, including nonlinear functions of several plaquettes. The completed physical Hilbert space and its transfer operator have equivalent realizations using exterior observables. A single selected spatial link on the plane gives a gauge-invariant counterexample at every finite coupling. [Director rendezvous](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7096799964) · [Literature and physical spectral test](spectral-test.md) · [Lean and execution record](execution.md)

## The plane and the conditional law

Use the four-dimensional defining SU(2) Wilson measure on a spatial torus of side at least three and infinite time. Assume the program's original-link vacuum has the finite-link Gibbs specification, time-translation invariance and site reflection positivity on the gauge-invariant half algebra. Time reflection sends a spatial link based at \(t\) to one based at \(-t\). A positive temporal link based at \(t\) goes to the inverse of the positive temporal link based at \(-t-1\). Write \(\Theta F=\overline{F\circ r}\). A closed positive half-cylinder can use links contained in \(t\ge 0\), including the spatial links in the plane. [Original site-reflection calculation](../site/) · [Finite-link specification](../contact-blocks/averaging.md)

Let \(M\) be a reflection-invariant deterministic set with at most one selected link on any plaquette. A4's orientation slabs run along a spatial axis. Reflection preserves transverse parity for spatial links and the transverse parity of a temporal link uses only its spatial coordinates. The spatial seam rules are independent of time. Keep the original mask away from the plane and remove its time-zero spatial links from \(M\), so they remain observable. Put \(\mathcal E=\sigma(U_e:e\notin M)\), and \(P F=\mathbb E[F\mid\mathcal E]\). [A4's mask](../../observable-normalization/energy-density/contact-law/)

For each finite subset of selected links, the finite-link specification conditional on its complement has a product density. Every one-link staple uses only retained links, so conditioning down to \(\mathcal E\) gives that same product. For a cylinder \(F\), integrate the finitely many selected coordinates it uses against these kernels. This gives a bounded exterior cylinder. Its extra links lie in the plaquettes incident to the integrated links. For a selected spatial link at \(t\ge1\), the nearest backward plaquette reaches at most to \(t-1\). For the temporal link from 0 to 1, its staples lie in that same closed slab. Thus \(PF\) still belongs to the closed positive half. For a gauge-invariant \(F\), simultaneous gauge transformations of fixed and integrated links preserve Haar measure and the Wilson weight, so this version of \(PF\) is gauge invariant. Reflection invariance of the law and exterior gives \(P\Theta=\Theta P\).

For positive-half cylinders \(F,G\), the selected coordinates of \(\Theta F\) and \(G\) are disjoint. The product conditional law gives the identity

\[
 P[(\Theta F)G]=(\Theta PF)(PG),\qquad
 \mathbb E[(\Theta F)G]=\mathbb E[(\Theta PF)(PG)].
\]

The right-hand side still reflects the exterior configuration. The exterior contains observables at both positive and negative times. Replacing that pairing by the ordinary \(L^2\) inner product of \(PF,PG\) generally changes it. The exact sign model in the controls gives \(11/8\) with the reflection and \(5/2\) with the exterior held pointwise fixed. [Exact controls](control.py)

## Which states and products survive

Write \(q(F)\) for the class of \(F\) modulo the null space of the Osterwalder–Schrader (OS) form. Apply the identity to \(F-PF\). Its reflected norm vanishes since \(P^2=P\), hence \(q(F)=q(PF)\). Inclusion of exterior half-cylinders therefore induces an isometric surjection **on the cylinder quotients**. Completing them gives a unitary map. A general completed state is a limit of exterior representatives.

Let \(S\) shift raw observables one step into the positive half. The vacuum transfer descends through \(q\). On exterior representatives its one-step action is \(f\mapsto P S f\) modulo null states. In particular,

\[
 q\big((P S)^k P F\big)=q(S^k F)\quad(k\ge 0).
\]

Induction uses \(qP=q\) and preservation of equivalent classes by \(S\). The plane guard breaks raw time translation symmetry of the mask. The identity is on physical states and gives the same matrix elements and spectral measures of the physical transfer via the unitary. The exterior marginal alone has no translation-invariant raw evolution specified by this construction.

For a nonlinear insertion, project the whole insertion. To see the product issue inside the Wilson model, use a real normalized plaquette trace \(F\) containing a selected link strictly on the positive side. The difference \(P(F^2)-(PF)^2\) is its conditional variance. It has strictly positive expectation by the bound below. Pairing with the vacuum distinguishes these two exterior observables. Equivalently the centered variable \(F-PF\) is OS-null while its square has nonzero vacuum pairing.

## Why a time-zero link must be retained

Suppose a reflection-invariant mask integrates a spatial link in the plane. Take \(F=\tfrac12\operatorname{ReTr} U_p\) for an all-spatial plaquette in that plane containing the link. This closed loop is gauge invariant and \(\Theta F=F\). No other edge in the loop is selected. Conditional on the exterior, the remaining link has density \(w(U)=\exp(U\cdot H)/Z(H)\) with respect to normalized Haar measure. The six unit staples give \(|H|\le6\beta\). Thus \(w\ge e^{-12\beta}\). For each fixed three-link transporter the Haar trace has mean zero and second moment \(1/4\), by invariance of Haar measure and symmetry of the four coordinates of the unit quaternion. The estimate holds also if the plaquette uses the inverse of the selected link.

For \(m=PF\) this yields

\[
 \operatorname{Var}(F\mid\mathcal E)
 \ge e^{-12\beta}\int (F(U)-m)^2\,dU
 =e^{-12\beta}(1/4+m^2)\ge e^{-12\beta}/4 .
\]

Consequently \(\mathbb E[(\Theta F)F]-\mathbb E[(\Theta PF)(PF)]\ge e^{-12\beta}/4\). At \(\beta=0\) the defect is exactly \(1/4\). Within this class of reflection-invariant masks, retaining every spatial link on the plane is both necessary and sufficient for preservation on the full closed-half gauge-invariant cylinder algebra. The floor is for a single finite-cutoff trace. Its deterioration as \(\beta\) grows limits its physical use.

## Effect on the contact distribution

Couple the original mask and the guarded mask on the same configuration. Let \(D\) be the selected spatial links put back into the exterior at time zero. Conditional on the old exterior, all old selected links are independent, so revealing the links in \(D\) leaves the kernels of the other stars unchanged. A face meeting \(D\) now has zero residual. Every other residual agrees exactly. Multiple faces in the same star can still be correlated.

For a compact cutoff \(\chi\), only \(O_\chi(b^{-3})\) removed stars meet its support, including faces within one lattice step of the plane. The previous star variance bound for arbitrary Fourier coefficients gives \(O_\chi(b^4 b^{-3})=O_\chi(b)\) for each localized Fourier mode of the difference. Summing the Fourier weights gives \(\mathbb E\|\chi(R_b-R_b^{\rm guard})\|_{H^{-s}}^2=O_{\chi,s}(b)\) for \(s>2\). Here the strength of the plane term depends on the four-dimensional test normalization \(b^2\). A sharp three-dimensional slice with normalization \(b^{3/2}\) has a different counting estimate.

On the full local Sobolev space use the bounded metric given by summably weighted truncated seminorms of a cutoff exhaustion. The mean distance between the coupled fields tends to zero by the local bounds and dominated convergence. The conditional law of the guarded residual given the enlarged exterior is also its law given the old exterior: its coefficients depend only on the old exterior and the remaining independent links. The coupling over that old exterior bounds the expected bounded-Lipschitz distance of the two conditional laws by the mean distance of the fields. Thus the guarded mask has the same conditional white-noise limit under the earlier tangent and moment inputs. This argument uses independence after conditioning in addition to the mean-square estimate. [Earlier conditional-field theorem](../contact-blocks/)
