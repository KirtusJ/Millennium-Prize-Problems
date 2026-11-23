# What three positive lag moments can resolve

Let $\nu$ be a finite positive measure on $x\ge0$ with $m_j=\int x^j\,d\nu$ and $|m_j-W|\le\epsilon$ for $j=1,2,3$. Write $I=[1-\eta,1+\eta]$, $0<\eta\le1/2$. The polynomial $q(x)=2x-x^2$ equals one and has zero slope at the band center, and vanishes at zero. The loss $D=m_3-2m_2+m_1=\int x(x-1)^2d\nu$ lies between zero and $4\epsilon$. On $I$ one has $|1-q(x)|=(x-1)^2\le x(x-1)^2/(1-\eta)$. Outside $I$, use $|2-x|\le1+|x-1|$ to obtain $|q(x)|\le(\eta^{-2}+\eta^{-1})x(x-1)^2$. Integration gives
$$
 |\nu(I)-W|\le 3\epsilon+
  4\epsilon\max\{(1-\eta)^{-1},\eta^{-2}+\eta^{-1}\}.
$$
It even allows arbitrarily much mass at zero. This gives the fixed-cylinder rate proposed in the [G4 review](https://github.com/KirtusJ/Millennium-Prize-Problems/pull/2#issuecomment-7098437858) of order $\epsilon/\eta^2$ using the same hypotheses. The all-lag Wilson proof uses additional transfer structure.

This order is necessary for general positive spectra, even if the three moments and total mass are provided exactly. Choose $0<\eta<1/2$, $0<a\le1$. Let $\mu$ have mass $1-a$ at one and mass $a/2$ at each of $1\pm\eta/2$. Let $\nu$ have mass $1-a/16$ at one and mass $a/32$ at each of $1\pm2\eta$. The laws have identical moments of orders zero through three: total mass one, mean one, second moment $1+a\eta^2/4$, third moment $1+3a\eta^2/4$. Their closed-band masses differ by $a/16$. Taking $\epsilon=3a\eta^2/4$ makes the ambiguity $\epsilon/(12\eta^2)$. Scaling $x$ by a common small transfer ratio permits a positive contracting diagonal transfer realizing both examples alongside a separate vacuum. They are moment controls, not Wilson models.
