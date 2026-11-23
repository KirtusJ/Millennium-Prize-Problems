# How many exact transfer moments can hide the midpoint ratio?

Director C4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)  
Research program directed by Kirtus Justus

In G4’s class of positive buffered transfer measures, even **exact** early-time covariances can admit opposite conclusions at the mass-gap clock. For every fixed $0<\kappa<1/4$, there are two families with the same gap and identical moments through degree $\lfloor\kappa J\beta^{-1/128}\rfloor$. Their midpoint ratios tend to $\sqrt e$ and infinity. Both approximate the free 24-plaquette clover reference to $O(\beta^{-1/8})$ uniformly over all moment indices and satisfy the stated clock floor. G4 gives an upper bound of order $J\beta^{-1/128}$ on the sufficient degree for this class with exact inputs. The power of $\beta$ in that bound is therefore sharp in the worst case. The construction concerns information in time moments and leaves open which sequences can arise from the Wilson action. [G4’s sufficient estimate](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/c5877ed6160686605f690a2ebf23cd89717f4ee2/yang-mills/g4/site-clock/certificate.md) · [G4’s original common-clock construction](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/c5877ed6160686605f690a2ebf23cd89717f4ee2/yang-mills/g4/site-clock/precision-limit.md)

## Extrapolation by a signed measure

Let $0<c<b<1$ and $d\ge1$. Evaluation of any polynomial of degree at most $d$ at $b$ can be represented by integration over $[0,c]$. At the nodes $x_i=c(1+\cos(i\pi/d))/2$, $0\le i\le d$, use the signed measure $\sigma=\sum_i L_i(b)\delta_{x_i}$, where $L_i$ are the cardinal polynomials of Lagrange interpolation. The nodes decrease and $b$ is above all of them, so $\operatorname{sign}L_i(b)=(-1)^i$. Since $T_d(2x_i/c-1)=(-1)^i$, applying interpolation to that Chebyshev polynomial gives the **exact** total variation norm
$$
 \|\sigma\|_{\rm TV}=\sum_i |L_i(b)|=T_d(2b/c-1).
$$
This norm is minimal over all representing signed measures on that interval. The same polynomial is bounded by one there and attains the displayed value at $b$. In particular a positive measure on $[0,c]$ alone cannot in general implement this extrapolation. Splitting $\sigma=\sigma^+-\sigma^-$ lets us construct two positive measures instead. [Bos, Maʻu and Waldron, §2, Proposition 2.1](https://www.math.auckland.ac.nz/~waldron/Preprints/Extremal-growth/BosMauWaldron1.pdf) · [NIST DLMF, eq. 18.5.1](https://dlmf.nist.gov/18.5.E1)

## A pair on the same physical clock

Use G4’s notation $m=\beta^{-1/7}$, $a=\beta^{-1/64}$, $A=a^8$, $c=e^{-a}$, $b=e^{-2m}$, $J=\lfloor1/(2m)\rfloor-1$ and $h=\lfloor(J-1)/2\rfloor$. The two-step moment index $j$ corresponds to time separation $2+2j$. We have $aJ/\log\beta\to\infty$, $2mJ\to1$, and $h=J/2+O(1)$.

The buffered free clover measure $\nu_*$ on $[0,1]$ has finite positive mass and moments $M_k^*\le C(1+k)^{-8}$. With $k=\lfloor1/a\rfloor$, $\nu_*([c,1])\le e^{ak} M_k^*=O(A)$. Replace this tail by $A\delta_c$ and call the resulting measure $\lambda$. Then $\|\lambda-\nu_*\|_{\rm TV}=O(A)$. Its moments $Q_i$ satisfy $A c^i\le Q_i\le Bc^i$ with a fixed $B$, and $Q_h\ge c^{h-J}Q_J$. These properties use only the stated upper estimate on the actual free clover moments. [Free-reference input](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/c5877ed6160686605f690a2ebf23cd89717f4ee2/yang-mills/g4/site-clock/README.md)

Take $d=\lfloor\kappa J\sqrt a\rfloor$ and fix $2\kappa<\theta<1/2$. Let $w=A e^{-\theta aJ}$, $v=A e^{-2aJ}$ and $\Delta=w-v$. For large $\beta$ the interpolation nodes and weights above exist with $b>c$. Set
$$
 \nu_{\rm bounded}=\lambda+w\delta_b+\Delta\sigma^-,
 \qquad
 \nu_{\rm divergent}=\lambda+v\delta_b+\Delta\sigma^+.
$$
Their signed difference is $\Delta(\delta_b-\sigma)$. Their first $d+1$ moments, **including the mass**, are identical. The common values need only approximate the corresponding free moments. They are not assumed to equal them. Both measures have strictly positive mass at $b$ and all their remaining support lies in $[0,c]$. Thus $1\oplus\sqrt u$ on $\mathbb C\Omega\oplus L^2(\nu)$ has the same gap $m$ above its vacuum for both, and $0\oplus1$ has the stated $T^2$ spectral measure.

The price of compensation is small:
$$
 \operatorname{arcosh}(2b/c-1)
 =\operatorname{arcosh}(2e^{a-2m}-1)
 =(2+o(1))\sqrt a .
$$
This follows from $m=o(a)$ and the expansion of $\cosh$ at zero. Thus $\Delta\|\sigma\|_{\rm TV}\le A\exp[-(\theta-2\kappa+o(1))aJ]=o(A)$. In particular both full measures are within $O(A)$ of $\nu_*$ in variation. If exact agreement with the **reference** mass at index zero is required, multiply both by the same scalar $\|\nu_*\|/\|\nu_{\rm bounded}\|=1+O(A)$. This preserves all ratios and equalities. For either measure the denominator $M_J$ lies between $A e^{-aJ}$ and $O(A)$ before that optional common scaling, which gives the clover clock bounds with suitable constants.

For the bounded family the part supported below or at $c$ contributes at most $(B+o(A))c^i$ at index $i$. This is $o(w)$ at both $h$ and $J$, since $\theta<1/2$ and $|\log A|=o(aJ)$. The atom at $b$ therefore determines the ratio, which tends to $b^{h-J}\to\sqrt e$. For the divergent family let $D_i$ be the moment of its part on $[0,c]$. Then $D_h\ge c^{h-J}D_J$, $D_J\ge A c^J$, and $v b^J/D_J\le e^{-aJ}$. Consequently $M_h/M_J\ge e^{a(J-h)}/(1+e^{-aJ})\to\infty$.

No decision rule using only these shared exact inputs, the common clock and the stated bounds can distinguish the two families. This includes adaptive queries restricted to indices at most $d$. G4’s upper bound also assumes a positive measure, a uniform total-mass bound and a quantitative floor on $M_J$. Both families satisfy those inputs. The comparison determines the order of the necessary worst-case time extent. It does not determine the best constant, the precision needed above this degree, or the information contained in additional Wilson identities. Related work on instability of full density recovery from Hausdorff moments uses a different observation model and target. [Gerth et al., *The Hausdorff moment problem in the light of ill-posedness of type I*](https://arxiv.org/abs/2104.06029)

## Checks

The host checker verifies degree-three interpolation and the exact variation $148/27$ with rational arithmetic. A separate positive reference with $-\log u$ distributed as Gamma$(8,1)$ has moments $(1+i)^{-8}$ and an explicit truncated tail. Four finite clocks compare both positive measures at 135 decimal digits. This numerical reference exercises the construction; the argument above uses G4’s free clover measure. At $J=1024$ the pair matched all indices through 42 to absolute discrepancy below $10^{-80}$, with midpoint ratio $1.64932442$ in the bounded family and log ratio $222.783336$ in the divergent family.

Two three-generation PCP OS runs checked a separate integer-scaled degree-two pair for all moments through degree three. Three of those moments agree and the degree-three difference is 120. The Lean read-back includes the identity for arbitrary quadratic coefficients. Three altered declarations and an invalid guest request were rejected in each deployment. The asymptotic lower bound is a written proof. [Python check](check.py) · [Native worker](worker.c) · [Lean identities](ExactClock.lean) · [Replay script](verify.py) · [Verification records](receipts.zip)
