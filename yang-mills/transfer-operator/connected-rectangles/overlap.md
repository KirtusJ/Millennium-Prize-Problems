# The propagating unit tube is a coherent sum of measured plaquettes

The long-time contribution has a concrete vector in the Wilson transfer Hilbert space. For a cell $c$ inside the spatial rectangle $Q$, write $f_c=\chi(U_{\partial c})-\langle\chi(U_{\partial c})\rangle$ and $f_Q=W_Q-w$. Use the same unnormalized trace throughout. In a fixed time slice, write the vectors as $f\Omega$. At integer lag $k$ propagate them halfway:
$$
 u=S^{k/2} f_Q\Omega,\qquad v_c=S^{k/2} f_c\Omega,\qquad v=\sum_{c\subset Q}v_c.
$$
Fractional powers use the positive transfer. Their Gram matrix uses only ordinary integer-lag correlations.

The mixed connected reading of the rectangle and a single chosen cell has unique first term $z^{A-1+4k}$. The projected horizontal path starts at $Q$ and ends at $\{c\}$, hence costs at least $A-1$. A nontrivial cut still costs at least four faces per slab. To attain both lower bounds, the path must retain $c$ in every intermediate section or it would pay twice for dropping and restoring it. Each four-face cut must then be the unit wall at $c$. There is one cap $Q\setminus\{c\}$ and one unit tube. The parity and lift arguments from the [two-rectangle case](surfaces.md) apply. Projecting the support to the loop plane misses $c$, so no subset can fill either boundary alone. Peeling the cap and integrating the walls gives coefficient one in units of $z^{A-1+4k}$. This includes a cell at a corner. Two identical elementary plaquettes have the unique wall term $z^{4k}$ by the same argument. Two **different** coplanar cells require at least two horizontal faces and four temporal occurrences per slab. Their connected series starts no earlier than degree $4k+2$.

Under the growing-loop assumptions of the [analytic bound](analyticity.md), all of these estimates hold uniformly over the cells. In particular, the off-diagonal entries divided by $z^{4k}$ are bounded by $8e^8(4/\rho)^{4k}(\beta/\rho)^2$ using Schwarz's lemma. This remains smaller than any inverse power of $A$ after summing over all $A^2$ pairs. Set $H=z^{Pk}$ and $J=A z^{2(A-1)+4k}$. For each fixed $N$ the errors below can be bounded by $o(A^{-N})$ relative to the displayed positive main terms:
$$
 \|v\|^2\sim A z^{4k},\qquad \langle u,v\rangle\sim A z^{A-1+4k},
 \qquad \|u\|^2\sim H+J.
$$
In the last relation, when the two integer powers differ, their ratio after removing their coefficients is at most $z$ for the smaller term. This explains why the sum is a valid relative approximation even though the two coefficients are separately identified only where their respective surfaces minimize.

The squared normalized overlap with **one explicit plaquette sum** is consequently asymptotic to $J/(H+J)$. In the late regime $J/H\to\infty$,
$$
             \frac{\|u-z^{A-1}v\|}{\|u\|}\longrightarrow0 .
$$
The matrix elements determine its sign as well as its normalization. In the early regime $J/H\to0$ the overlap vanishes. At exact connected equality, subtracting $z^{A-1}v$ from the rectangle leaves squared norm $z^{Pk}(1+o(1))$, while the rectangle's total squared norm is $(A+1)z^{Pk}(1+o(1))$. The errors are small enough to resolve the residual even as $A$ grows. This identifies which localized gauge-invariant observables account for the $A$-fold coefficient without assigning an eigenstate to each cell or asserting any degeneracy.
