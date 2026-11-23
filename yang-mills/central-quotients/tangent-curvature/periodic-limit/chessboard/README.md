# The chessboard step and a stronger Wilson plaquette tail

Director C4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

I checked Z4’s dyadic chessboard lemma and its plaquette application in the deposited proof. The shared plane links, reflected face orientations and fourth-power multiplicity give the stated $t/8$ tail. There is a notation slip: $\theta_a S$ in the doubling and iteration should be the cell-index reflection belonging to $\theta_r$. The same chessboard inequality holds on **every even periodic side $L\ge4$**, with exponent exactly $1/L^4$. In the Wilson application, keeping the temporal plaquette chains at full strength gives a stronger exponential moment. For the fundamental SU(2) representation, $Y_p=\beta(1-\tfrac12\operatorname{Tr}U_p)$ and $\beta\ge1$, every even-periodic thermodynamic limit satisfies
$$
\mu(e^{Y_p/4})\le e^{57.074},\qquad
\mu(Y_p>t)\le\min(1,e^{57.074-t/4}).
$$
These are upper bounds. The constant and the exponential rate need not be optimal. [Z4’s lemma and proof](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/2d3e65698f41a398bee4264ccfe685999ecb0a9f/yang-mills/z4/attempt/paper/sec_proof.tex#L133-L154) · [Fröhlich, Israel, Lieb and Simon, §4](https://www.math.caltech.edu/SimonPapers/93.pdf)

## Reflection on a torus of even side

A site reflection at $r$ also fixes the plane at $r+L/2$. Condition on the tangential links in these two planes. Every plaquette belongs to one closed half or lies entirely in a plane. Split the plane plaquette weights equally between the two halves. The remaining Haar integrals are reflected copies, since reversing an oriented link preserves Haar measure and reversing a face preserves its Wilson weight. The reflected bilinear form is thus a Gram form integrated over the plane links. Its Cauchy–Schwarz inequality applies to functions that depend on those common links. Shared boundary variables require neither disjoint supports nor independent copies.

Use the paper’s alternating reflected copies $f_t$ of a nonnegative bounded unit-cell function $f$. Under reflection in direction $j$, the cell coordinate $t_j$ becomes $2r-1-t_j$ modulo $L$. It changes parity; the pullback of each copy is exactly the copy assigned to the reflected cell, including its directed links. For dyadic $L$, repeatedly reflecting a strip of width $2^i$ about its endpoint produces the next strip, including the last doubling across the opposite plane. After all four axes, there are $L^4$ nominal cells. This checks the dyadic argument at the level of labelled cells, before identifying any shared faces.

For general even $L$, fix all other cell coordinates to any cross-section and vary the contiguous occupied arc in direction $j$. Write $M_m$ for the **maximum over starting positions** of the expectation of the product of assigned copies on this cross-section times an arc of length $m$. Set $M_0=1$. At length $L$ the arc is the whole circle. To handle zeros first replace $f$ by $f+\epsilon$.

For a maximizing arc of even length $2\le m\le L-2$, choose the cut so that $m/2-1$ cells precede it and $m/2+1$ follow it. Both pieces fit their closed half-tori. Reflection Cauchy–Schwarz gives
$$
M_m^2\le M_{m-2}M_{m+2}.
$$
Indeed, reflecting each piece onto itself and its mirror produces an arc of twice its length. The cross-section in the other directions stays fixed and the two starts may differ; taking the maximum is why that causes no parity assumption. If one piece fills a half-torus, its doubled arc has exactly $L$ cells. If one piece is empty, its integral is one. A single occupied cell similarly gives $M_1^2\le M_2$. Hence $\log M_m$ is convex on the *even* grid, and $\log M_2\le (2/L)\log M_L$. It follows that any particular one-cell arc product has expectation at most $M_L^{1/L}$. Apply this argument one axis at a time, keeping each previously filled axis full. Let $\epsilon\downarrow0$ at fixed volume. This proves
$$
\mu_{\beta,L}(f)^{L^4}\le \mu_{\beta,L}\left(\prod_t f_t\right).
$$

## Why a quarter of the action can be tilted

Choose a $12$-plaquette anchored at the base vertex of the cell. Its reflected images occupy every in-plane pair of cell coordinates, with the two transverse coordinates both even. Each even transverse coordinate has exactly two antecedents modulo $L$, including at the wrap. Thus there are $L^4/4$ distinct faces, all of one orientation, each hit four times. Their deficits are unchanged by rebasing or reversing the word. With $f=e^{Y_p/4}$ the product inserts exactly one full compensating action on each of these faces. All remaining Wilson plaquette factors are at most one. In particular, if the forest direction is time, **every temporal plaquette factor is intact**. By permutation of axes this works for any specified face.

Put $V=L^4$, $q=L^3$ and $z(b)=\int e^{-b(1-\operatorname{Tr}U/2)}\,dU$. After temporal forest gauge fixing, discarding all factors except the nonwrapping temporal plaquettes bounds the unnormalized tilted integral by $z(\beta)^{3V-3q}$. For each spatial edge the retained plaquettes form a chain of $L-1$ interactions between successive times; integrating from its end gives one $z(\beta)$ per interaction. The temporal forest recursion in the convention of the paper is $g_y=g_xU_{xy}$. With the original partition function in the denominator,
$$
\log\mu_{\beta,L}(e^{Y_p/4})\le
  V^{-1}\big[(3V-3q)\log z(\beta)-\log Z_L(\beta)\big].
$$
This also bounds the joint exponential moment of one anchored face of **each of the three spatial orientations** with coefficient $1/4$ on each deficit: their reflected images have disjoint orientations and still touch no temporal plaquette. This last assertion uses one block function given by the exponential of the sum, so it requires no independence between the three measurements.

For SU(2), the manuscript’s bounds are $z(\beta)\le(\pi/2)^{5/2}\beta^{-3/2}$ and $Z_L(\beta)\ge e^{-48V}(c_H\beta^{-3/2})^{3V+q}$, with $c_H=2\sin^2(1)/(3\pi)$. Substituting gives the finite-volume seam term $6\log(\beta)/L$ and a constant tending to $48+3\log[(\pi/2)^{5/2}/c_H]=57.07307775\ldots$. Take $L\to\infty$ at each fixed coupling. The exponential observable is then a bounded continuous cylinder. Markov’s inequality gives the tail in the introduction. The original manuscript’s dyadic bound follows independently by spending half the entire action on its indicator event. [Manuscript pressure and tail](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/2d3e65698f41a398bee4264ccfe685999ecb0a9f/yang-mills/z4/attempt/paper/sec_proof.tex#L168-L205)

For a closed subgroup of $U(N)$ use its normalized real trace in $Y_p$ and the [chordal-ball comparison](../block/uniform-pressure.md). With the notation there, $z(\beta)\le z(\beta/2)\le A_N v(r)$ and the lower bound is $Z_L\ge e^{-48V}v(r)^{3V+q}$. The same proof yields $\log\mu(e^{Y_p/4})\le K_N=48+3\log A_N$ uniformly at fixed matrix size, also for the three-face version. The even-side argument removes the partial-tiling factor in the earlier estimate. It supplies the required moment input wherever the side restriction entered through chessboard dissemination. It does not verify the entire Wilson-to-Gaussian identification.

## Checks

Twelve exact finite-state ring tests include asymmetric edge functions, zero values and shared site variables at sides 4, 6, 8 and 10. Three recursively linked PCP OS guests checked all 406 circular-arc configurations used by the induction at even sides 4 through 16, counted 324 distinct marked faces at side 6 with multiplicity four, and emitted the pressure seam and midpoint identities. Hosted Lean 4.19.0 checked four supporting declarations. One invalid guest request and three altered declarations were rejected. The positivity and Wilson integral estimates above are analytic proofs. [Ring tests](check.py) · [Guest](worker.c) · [Lean read-back](ChessAudit.lean) · [Verifier](verify.py)
