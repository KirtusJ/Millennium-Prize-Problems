# Formal scope and reproduction

Three recursive PCP OS workers generated the Lean source. The parent boot computed the cube and relative-star Gaussian triangles, Wilson first coefficients and locally matched Abelian first coefficients on the short open/relative pair. It did the gauge-fixed source expansion modulo 101. The child boot used twisted Fourier projectors modulo 193 for both placements on the periodic box. It computed the leading pair and triangle readings and the local circle response independently of the tree-gauge Hessian. The grandchild boot assembled the analytic declarations and the measured checks. The three outputs were respectively the bytes 24, 77, 84, 18, 70, 37, two modular lists (90, 90, 123, 70, 97 and 192, 192, 175, 18, 188), and the 8,956-byte module. A separate replay reproduced it and all nine predecessor modes. The native microVM skipped its asynchronous keyboard tests. [Serial captures, verified register and check output](evidence/) · [Kernel identity and baseline](../execution.md)

| SHA-256 | Artifact |
|---|---|
| e21e0b5837c5dcdd5a108e1ed2bd1cd89c0447db31c2b5374f61ee3b682fe06d | Compiled guest ELF |
| 0565c917e76598e286c07daa80b4652eafcf8e442d273e0cc4068828e56a79a2 | Generated Lean source |

Lean 4.19.0 and Mathlib c44e0c8ee63ca166450922a373c7409c5d26b00b checked 22 declarations. These include the block determinant and complementary kernel identities under their matrix hypotheses, odd-cycle parity, the local action algebra, distance normalization algebra, uniqueness of a bounded integer in a residue class, the four signed Wilson certificates, the two normalized coefficient bounds for the supplied readings, and agreement with native residues. The three measured list checks are axiom-free. The remaining dependency reports contain subsets of propext, Classical.choice and Quot.sound. Twelve deliberate changes failed at the intended declarations. The gauge reduction, Laplace expansion, graph and Fourier identifications, numerator majorants and bulk estimates are derived in the mathematical notes. Connecting the complete integral to the formal rational inputs still uses those derivations and the host and guest programs. [Lean declarations](DualScalar.lean) · [Adverse tests](check_mutations.py)

The exact finite-torus evaluator reconstructed each Wilson reading twice from eight modular inversions and an absolute integer bound. A separate gauge frame and prime checked the readings. Two smaller tori admitted exact rational frame-to-frame comparisons. A two-dimensional character identity and a direct compact quadrature tested the twisted measure. A nonconstant reciprocal source checked the open/relative determinant and full curvature covariance. Two trees agreed on all four open/relative placements. A direct marked-face identity checked the Abelian and squared-deficit action changes. Bulk numerical checks used two quadrature orders. The predecessor finite scalar calculations were re-run after extracting their shared word evaluator. [Recorded checks](evidence/checks.txt) · [Finite compact model](twisted-wilson.md) · [Bulk action comparison](bulk-action.md)

Use the kernel, PCP OS source and environment identified in the baseline. LANE is the absolute spectral-support directory. MATHLIB points to the pinned Mathlib checkout with the matching toolchain on PATH. Host computations use Python, NumPy, SciPy and SymPy. The certificate runs below compare the entire regenerated JSON to the stored fixture.

~~~sh
export OPENBLAS_NUM_THREADS=1
python -I "$LANE/positive-time/replay.py" --dual-scalar --kernel "$KERNEL" --pcp-source "$PCP_SRC"
(cd "$MATHLIB" && lake env lean "$LANE/dual-scalar/DualScalar.lean")
for orientation in cube star; do
  python -I "$LANE/dual-scalar/certify_twist.py" "$orientation"
  python -I "$LANE/dual-scalar/certify_twist.py" "$orientation" --skew
done
for check in boxes twist bulk action; do
  python -I "$LANE/dual-scalar/check_$check.py"
done
python -I "$LANE/dual-scalar/check_mutations.py" --mathlib "$MATHLIB"
~~~
