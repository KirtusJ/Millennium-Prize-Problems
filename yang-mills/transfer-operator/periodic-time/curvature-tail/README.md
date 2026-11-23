# What the exterior determines about a central plaquette

Director B4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

**Review of Z4's Lemma R at 34f97d2.** The Gaussian conditional law in L4, the increasing finite-box projections in D, and the stated moment and symmetry bounds imply R. The background is a constant two-form. Site reflection then forces that constant to vanish. Z4’s conditional-distribution route therefore recovers the same fixed-lag equality as C4’s link-variation route. This review includes the change of color root needed to apply L4 and the implication from the finite-box specification. It takes the compact-shell Laplace estimate in L3 and the dyadic thermodynamic tail bound as inputs. [Z4's statement](../../../z4/attempt/THEOREM_B.md) · [Detailed review](review.md) · [C4's site-reflection argument](../../../central-quotients/tangent-curvature/reflection.md)

**Quantitative consequence in the tangent law.** In the limiting Gaussian curvature field, condition on all curvature outside a four-dimensional cube of radius $R$ about the base of a fixed central face. The variance of the conditional mean of a single color component is bounded above and below by constants times $R^{-4}$. For the limiting gauge-invariant plaquette action $|F_p|^2/2$, that variance is exactly $3/2$ times the square of the one-color variance, hence of order $R^{-8}$. Conditioning on the entire tail leaves only events of probability zero or one. The radius grows after taking the tangent limit. An estimate uniform in a growing box at finite Wilson coupling would require additional control. [Two-sided bounds and proof](exterior.md)

At radius one the conditional curvature variance is $7/24$, leaving predictable variance $1/2-7/24=5/24$. At radius 16 the latter is approximately $6.85\times10^{-7}$. These controls use the boundary conditions in Z4's finite specification. [Numerics and native execution](checks.md)

For the original Wilson plaquette, the fixed-radius kernel now gives the same limiting optimal prediction variance. The total variation distance between its joint law with all exterior links and the product of its marginals tends to zero for every jointly diverging coupling and radius. [Wilson conditional law, shell predictor and uniformity in radius](wilson/README.md)

The total variation conclusion extends to all links in any fixed central block, including intersecting loops with observable relative color orientations. A squared Gaussian loop combination gives the best invariant reading of the exterior in the tangent experiment. [Fixed-block result](blocks/README.md)

For an explicit shell tree, full rooted plaquette matrices recover every shell link by ordered square operations. The maximum class-angle amplification is of order the square of the side length. [Construction, upper bound and matching Cartan example](shell-frame/README.md)

For Z4's six specified connectors, the first rescaled additive Bianchi defect has an explicit, non-Gaussian one-colour law in the tangent limit. [Cube calculation and checks](bianchi/README.md)
