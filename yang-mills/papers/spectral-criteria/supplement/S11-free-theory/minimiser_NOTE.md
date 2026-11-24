# Note on `minimiser_result.txt`

Predicate Z1 FAILED as written and is kept. It asked that no other symmetry class be within 1e-12 of the rate at q = (1,0,0). The class (127,0,0) has the same rate: the rate is invariant under k → π − k in each component (the reflection q → N/2 − q), which the predicate did not take into account; the same pairs appear in `matrixbridge_result.txt` (for instance (0,0,31) at side 64). Up to that reflection and the permutations, the smallest rate at side 256 is at the lowest axial momentum, and the next class, (1,1,0), is 4.0e-3 above it.

What the run adds: at side 2²⁰ the rate at (1,1,0) exceeds the rate at (1,0,0) by 1.0e-6, and the excess of (1,0,0) over the limit 0.674941363 is 2.4e-6; the two excesses are in the ratio 1.41. So at small momentum the rate depends on the momentum through its length to this accuracy, and the lowest axial momentum is the minimiser because it is the shortest. This is an observation at the momenta computed, not a proof.
