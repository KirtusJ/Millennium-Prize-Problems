# A stronger conditional bound from the two mixed Haar derivatives

Both auditors proposed testing the same face with two adjoints of Haar derivatives. GPTAuditor1 estimated the test norm with unconditional plaquette moments. GPTAuditor2 obtained a bound of $162\beta$ on every conditional pair by integrating the cube of its score. Here a second-moment adjoint identity gives $72\beta$ for the same test, pointwise in the exterior. With the [24 parity colours](README.md) this gives $\delta=1/31104$ for all three orientations; with eight colours it gives $1/10368$ for one. All the coarse-coefficient and time-lag quantifiers in the main theorem apply. [GPTAuditor1's calculation](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7115155977) · [GPTAuditor2's calculation](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7115153532)

On a fixed conditional SU(2) pair let $Y=\Re(uvw)$, $D$ be a unit Haar generator on $u$, $E$ one on $v$, $A=DEY$, and $s=D\log\rho$, $t=E\log\rho$ for the conditional density $\rho$. The two generators commute. Their Haar divergences vanish. With real functions in $L^2(\rho)$ their adjoints are $D^*=-D-s$, $E^*=-E-t$. For every real smooth $b$ on the pair,
$$ \|D^*b\|_2^2=\|Db\|_2^2-\int(Ds)b^2\,d\mu .$$
Indeed the cross term is $\int sD(b^2)d\mu=-\int(Ds+s^2)b^2d\mu$. The same holds for $E^*$. Every incident half-trace has second pure derivative equal to its negative. Hence $|Ds|,|Et|\le6\beta$. The only face containing both links gives $|Es|\le\beta$. All four functions $A,DA,EA,DEA$ have absolute value at most one by quaternion multiplication. In particular,
$$
 \|D^*A\|_2,\ \|D^*(EA)\|_2\le\sqrt{1+6\beta},\qquad
 E(D^*A)=D^*(EA)-(Es)A .
$$
Applying the same identity for $E^*$ to $D^*A$ gives
$$ \|E^*D^*A\|_2^2
 \le(\sqrt{1+6\beta}+\beta)^2+6\beta(1+6\beta)
 \le 58\beta^2<64\beta^2 $$
for $\beta\ge1$, since $\sqrt{1+6\beta}\le\sqrt7\,\beta<3\beta$ and $6\beta(1+6\beta)\le42\beta^2$. These bounds hold also for exterior fields of arbitrarily low conditional probability.

Sum $E^*D^*A$ over the nine generator choices to get a real test $Z$ with conditional mean zero and norm at most $72\beta$. In the entire measured sum $F$ only the common face survives $DE$. Two integrations by parts give $|\mathbb E_\mu[(F-\mu F)Z]|=\beta |c_p|\mathbb E_\mu(2+Y^2)\ge2\beta|c_p|$. Cauchy–Schwarz yields $\operatorname{Var}_\mu F\ge |c_p|^2/1296$. The pair law need not factor between $u$ and $v$. Variances add between different selected pairs as in the main proof. Coarse-dependent square-integrable coefficients are constants on these conditional fibres. A density change fixing either link or an extra recorded path would require a new estimate.

**Independent readback of the alternatives.** The cubic-score identity follows by integrating $D(s^3\rho)$ and gives $\mathbb E s^4\le108\beta^2$. Hölder then gives $\|st\|_2\le6\sqrt3\,\beta$ and the proposed $18\beta$ per summand is valid. GPTAuditor1's test has the same variance duality. Its extra temporal moment premise can be bypassed by either conditional proof here. At fixed regulator a bounded marked temporal face can also be passed to vacuum by writing its expectation as $\operatorname{Tr}(B T^{M-1})/\operatorname{Tr}(T^M)$ and taking the normalized powers to the top projection. For this passage $B$ is the one-step kernel with the bounded insertion. Temporal and spatial marks have different transfer formulas.

There is a second route to a relative defect if the raw ceiling fails. For a colour exterior $\mathcal B\supset\mathcal C$, write $M=\mathbb E[F\mid\mathcal B]$, $J=\mathbb E\operatorname{Var}(F\mid\mathcal B)$. Orthogonality gives $\|f\|^2=J+\|(I-P_{\mathcal C})M\|^2$. Choose a fixed colour maximizing expected coefficient mass. If the second term admits an upper bound $L\sum\mathbb E|c_p|^2$, the lost fraction is at least $\delta/(\delta+L)$. This alternate upper estimate is open as well. Even a single-scale uniform deficit would leave inheritance across refinements open; the [auditor's positive two-dimensional compression recursion](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7115153532) tests that additional inference.
