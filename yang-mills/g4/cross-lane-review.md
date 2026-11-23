# G4 cross-lane review

November 22, 2026. These checks are scoped to the pinned contributions. They do not assert a four-dimensional construction or mass gap.

## C4: quotient measure and flat lifts

I read C4's [finite quotient result at fa3b65d](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/fa3b65d022743b1e11dc4863c19a735585b88804/yang-mills/central-quotients). The independent [Python check](crosscheck_quotient.py) constructs a cube from its eight geometric vertices and twelve edges, enumerates all 4,096 edge-sign assignments, and sums the Boltzmann weights as rational numbers. It does not call C4's face-incidence implementation. It finds 32 even face-sign patterns, each with multiplicity 128. At identity and beta = log 2, the mean weight is 8177/2048, exceeding the independent-face value 15625/4096 by 729/4096.

I separately enumerate Hamilton quaternion products for all 256 ordered four-tuples and all sixteen sign choices per tuple. Exactly 46 tuples admit commuting lifts; the 35 nonzero six-bit commutator patterns each occur six times. This supports the stated finite classification. The obstruction concerns simultaneous flat periodic lifts, not individual group-element lifts or a continuum construction on R4. This is an independent arithmetic execution and source review, not a G4 replay of C4's Lean development.

The reflection-positivity implication is precise. Let q map the cover configuration space to the quotient, let mu be a reflection-positive measure upstairs, and set nu = q_* mu. Require q to commute with the specified reflections and pullback by q to preserve the chosen positive-time test class. For any admissible complex test F whose reflected product is integrable,

\[
\int \overline{F(\bar\theta y)}F(y)\,d\nu(y)
=\int \overline{(F\circ q)(\theta x)}(F\circ q)(x)\,d\mu(x)\ \ge 0.
\]

Thus reflection positivity passes to this exact pushforward. For the Wilson measure, C4's shared-edge average is the relevant density. An independently chosen quotient action must establish its own identity or comparison. Replacing the shared-edge average by the product of face averages is not justified by this argument. This measure-theoretic identity is an analytic argument here; it is not one of G4's real-kernel Lean theorems. It establishes neither nontriviality nor a uniform gap.

## D4: spectral support and order of limits

I read [D4's a06ad946 source and argument](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/a06ad94657f44323afbe75ce387b8924e9c3aeb6/yang-mills/spectral-support), including the hypotheses of `noTransferMassAbove`, `denseProjectionOfMomentBounds` and `decayAtRoundedTime`. For a positive spectral variable x, the lower bound on a tail at s > r is s^t mu([s,infinity)); dividing the moment bound gives M(r/s)^t. The cutoff limit is taken at each fixed time before the unbounded time sequence. A common convergence rate across the test family is unnecessary for that order. A diagonal array alone does not provide these fixed-time premises.

The final tail is open at r; an atom at r is allowed. The density must cover the entire vacuum complement, and the supplied identity between the measure and the squared projection norm is essential. The physical-clock inequality is time <= N*a, so a ceiling provides the upper envelope when a > 0. Convergence along rounded physical times remains a separate input. These are mathematical/source checks; G4 has not replayed D4's Lean file or independently recomputed the six-reading inverse matrix in this review. B4's independently reported executions remain attributed to B4.

G4's limit lemma can preserve the nonnegative test forms used in reconstruction once a common limit exists. It does not produce D4's uniform decay estimate, spectral identity, or density. A4's nonzero-observable estimates must concern the same regulator, observables, time units and limit.
