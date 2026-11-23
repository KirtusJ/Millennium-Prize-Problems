# A scalar insertion with two exact null conditions

Take disjoint endpoint four-cubes $f,g$ and three candidate profiles $h_j$. Each profile is a sum of complete middle four-cubes. Define three rows of length three. The entries of $a$ are the Gaussian triangles $T^0(f,g,h_j)$, the entries of $b$ are the matched Abelian first coefficients, and those of $d$ are the Wilson first coefficients. Choose $c$ proportional to $a\times b$ with positive third component. This choice uses only $a,b$. All three triangles are linear in the third source. Therefore the single insertion $h=\sum_jc_j h_j$ satisfies exactly
$$
 T^0(f,g,h)=0,\qquad T^1_{\rm matched}(f,g,h)=0,\qquad
 T^1_{\rm Wilson}(f,g,h)=c\cdot d .
$$
The unmodified three-circle coefficient is the negative of the matched coefficient for every source, so it also vanishes. The last dot product is strictly negative in both boxes below. Positive rescaling of $h$ cancels from the reported normalizations. The written calculation takes the primitive integer vector; moderate decimal weights are shown only to describe the sources. Using the rounded weights in place of the exact ones leaves a Gaussian residual.

On the $5\times3\times1\times1$ box use end cells at $(0,0,0,0)$ and $(4,0,0,0)$. The candidate middle cells start at $(2,j,0,0)$ for $j=0,1,2$. Their common faces are counted with their respective linear weights. The end probes and the middle insertion have pairwise disjoint link supports. On the $9\times1^3$ box take endpoints 0 and 8. The three intermediate profiles sum cells at times $\{2,6\}$, $\{3,5\}$ and $\{4\}$ respectively. Reflection through the middle exchanges the endpoints and fixes each profile.

| Geometry | $c/\max_j\lvert c_j\rvert$ | Leading endpoint covariance | First coefficient of $\kappa/\sqrt{V_{ff}V_{gg}V_{hh}}$ | First coefficient of $\kappa/(V_{fg}\sqrt{V_{hh}})$ |
|---|---|---:|---:|---:|
| Transverse | $(-0.00281043,-1,0.78679640)$ | $1.08728173\times10^{-4}$ | $-1.96389993\times10^{-7}$ | $-0.03944515743$ |
| Temporal | $(0.16477115,-0.66479700,1)$ | $6.39996620\times10^{-11}$ | $-8.30157844\times10^{-16}$ | $-0.00030655655$ |

Here $V_{ij}$ is the covariance in the actual measure. The two leading denominators are strictly positive by exact evaluation. Since the Gaussian numerator is zero, their own first corrections drop out. The raw Wilson coefficient for $\max|c_j|=1$ is about $-2.05610160\times10^{-5}$ in the transverse case and $-9.82851201\times10^{-14}$ in the temporal case. The latter is especially sensitive to cancellation in floating arithmetic. The data include the full rational input columns, signed integer weights, exact combined triangle and exact squares of the normalized responses. [Exact records](evidence/null.json)

A second spanning tree yields the identical exact combined coefficients. An independent implementation on PCP OS performs elimination directly in $\mathbb F_{101}[s_1,s_2,s_3]/(s_1^2,s_2^2,s_3^2)$, computes the three input profiles per box, and solves the two equations there. With $c_3=1$ (one-based indexing), the temporal output $(c_1,c_2,T^0,T^1_{\rm matched},T^1_{\rm Wilson})$ reduces to $(17,28,0,0,28)$; the transverse output is $(64,95,0,0,32)$. Both agree with the rational data. Exact rational cancellations and the negative signs are separately checked in Lean. A single nonzero residue can detect a nonzero rational with invertible denominator; the rational proof is needed for its sign. [Native evaluator](box_mod.h) · [Lean module](ScalarResponse.lean)

These filters intentionally depend on the geometry and the two reference responses. They give finite, separated interaction diagnostics. They do not implement a spherical projection of the close pair in the continuum. In particular the largest tabulated fractional sensitivity uses a small endpoint covariance, and the temporal filter has very little absolute signal. Extending either result to a fixed physical window requires estimates uniform in the changing geometry and coupling.
