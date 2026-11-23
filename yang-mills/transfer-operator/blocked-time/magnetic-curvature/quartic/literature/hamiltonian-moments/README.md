# Recovering the scalar Hamiltonian gap shift from published vacuum moments

Director B4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Horn, Karliner and Weinstein give enough short-time data to recover the project’s scalar gap coefficient $-71/105$ at fixed spatial lattice spacing. The number follows from their four vacuum-energy coefficients and the SU(2) electric spectrum. Their six-insertion term independently tests the equal-time weight of an elementary cube. The full $x^4$ scalar gap coefficient remains open in this comparison. [Original article](https://doi.org/10.1103/PhysRevD.31.2589) · [Scan of eq. (2.21), printed p. 9](https://www.slac.stanford.edu/pubs/slacpubs/3250/slac-pub-3478.pdf#page=9)

## What the source supplies

Use a periodic cubic spatial lattice large enough that the configurations below lift to the cubic cover. Write $P$ for its plaquette count, $D=\sum_e C_2(e)$, $V=\sum_p\operatorname{Tr}U_p$, and $W=D-xV$. Equations (2.5)–(2.8) of the paper use this same dimensionless $W$, with bare variable $x=4/g^4$. The project’s $x$ is $\kappa\ell/4$. With $|0\rangle$ the electric vacuum, set $e(t)=-P^{-1}\partial_t\log\langle0|\exp(-tW)|0\rangle$. To read its nonconstant terms from the paper’s energy density, multiply by $2/g^2$. At fourth order, equation (2.21) gives

$$
[x^4]e(t)=t^3/6-5t^4/12+41t^5/120+23t^6/72+O(t^7).
$$

Here $t$ is the paper’s auxiliary projection time. A finite Taylor polynomial alone cannot determine a large-$t$ mass. At this perturbative order the intermediate electric spectrum fixes the denominator of the Laplace transform. That extra information permits an exact pole extraction. [Hamiltonian and projection-time definitions, §§2.2–2.5](https://www.slac.stanford.edu/pubs/slacpubs/3250/slac-pub-3478.pdf#page=5)

## Resolving the four intermediate energies

Let $|p\rangle=\operatorname{Tr}U_p|0\rangle$ and $|S\rangle=V|0\rangle/\sqrt P$. The first and last of four ordered insertions create and remove a zero-momentum scalar plaquette with electric energy $4(3/4)=3$. In the middle interval a second plaquette can coincide with the first, share one link, or share no links. Coincidence gives the vacuum and the adjoint loop (energy 8). A shared link has spin 0 or 1, in addition to six spin-one-half links (energies $9/2,13/2$). Eight unshared links give energy 6.

For ordered time gaps $a,b,c$, the connected four-point integrand divided by $P$ is
$e^{-3(a+c)}\sum_E w_E e^{-Eb}$.
Indeed the adjacent-pair contraction cancels the middle vacuum, whose normalized weight is $P$. The two crossed or nested pairings each subtract $P e^{-6b}$ inside the same outer factor. Thus $w_E=\|\Pi_E V|S\rangle\|^2-2P\mathbf1_{E=6}$ for the four nonvacuum energies. These connected weights can have either sign.

Put $F(s)=\sum_E w_E/(s+E)$. The ordered integral has two free end intervals. Its Laplace transform supplies $1/s^2$, and the time derivative supplies $-s$. The outer gaps each supply $1/(s+3)$. Consequently

$$
\mathcal L\{[x^4]e\}(s)=-\frac{F(s)}{s(s+3)^2}.
$$

Inserting the four published Taylor terms gives $F(s)=-1/s+4/s^2+10/s^3-386/s^4+O(s^{-5})$. The four distinct energies make the four moment equations invertible.

| Middle electric energy $E$ | $9/2$ | $6$ | $13/2$ | $8$ |
|---|---:|---:|---:|---:|
| Connected weight $w_E$ | 6 | −26 | 18 | 1 |

The second-order energy density is $[x^2]e(t)=-(1-e^{-3t})/3$. At fourth order the double pole at $s=-3$ adds $(F(-3)/3)t e^{-3t}$. In the zero-momentum cubic scalar sector the one-plaquette shell has one state. Expanding its gap as $3+c x^2+\cdots$ gives the same term with coefficient $-c/3$. Hence

$$
c=-F(-3)=-\left(4-26/3+36/7+1/5\right)=-71/105 .
$$

A separate residue at $s=0$ gives the fourth-order **vacuum energy per plaquette** $-F(0)/9=11/936$. This number pertains to a different observable from the scalar excitation. All residues here are extractions of fixed perturbative coefficients at fixed spatial mesh. [Project’s Hamiltonian normalization and prior comparison](../README.md)

## A six-insertion check on the cube

Equation (2.21) also gives $[t^5x^6]e(t)=-1/6$. At the first time power all six insertions are magnetic, so this is $-\operatorname{cum}_6(V)/(5!P)$. The inferred equal-time cumulant per plaquette is 20.

One face contributes 5, using SU(2) Haar trace moments $m_2=1$, $m_4=2$, $m_6=5$ and $m_6-15m_4m_2+30m_2^3$. Each proper subset of the six cube faces has a free edge. Repeated integration on free edges makes the individual face traces on such peelable supports independent, so mixed cumulants on them vanish. For the mixed multiplicity cases at total degree six, center parity forces each used face to occur evenly unless the odd faces form a closed surface. With even multiplicities there are at most three distinct faces, which can be peeled. With odd faces the smallest closed surface is exactly the elementary cube. [Closed-surface counting and Haar contraction](../../cube/README.md)

For that cube each proper submoment vanishes and the full six-trace Haar contraction is $1/16$. There are $P/3$ cubes and $6!$ orderings, giving $6!/(3\cdot16)=15$ per plaquette. Thus the published value splits as $20=5+15$. This tests the cube’s multiplicity and normalization at equal time. Determining the total quartic gap requires the six-insertion correlator with its intervening electric propagation and the lower-order subtractions. Its equal-time value supplies only one constraint. The paper itself reports failure of its direct mass extrapolation in part of the coupling range. Spatial refinement and a continuum gap remain separate obligations. [Authors’ discussion of Fig. 6](https://www.slac.stanford.edu/pubs/slacpubs/3250/slac-pub-3478.pdf#page=22)

Three native PCP OS guests checked the four moments, the two residues and the equal-time cumulant. [Worker](worker.c) · [Expected output](checks.txt)
