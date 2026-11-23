# The tree-gauge determinant

Let $d_0$ and $d_1$ be the forward lattice difference on vertices and the oriented curl on positive links of the periodic $L^4$ cubical complex, with the ordinary unweighted Euclidean inner product. In one color let $B$ be the matrix of $d_0$ with the root vertex column deleted, let $W$ contain the four wrap indicator one-cochains, and let $E$ contain the standard basis vectors on the $n=3(V-1)$ links left after deleting the tree and four anchor links. Thus $D_1=d_1E$ in the [compact integral](proof.md).

The square matrix $[B,W,E]$ is unimodular. Given an integer link cochain, first subtract the unique integer vertex gradient which reproduces its entries on the oriented tree, taking the root potential zero. Subtract the four integer multiples of the wrap indicators that reproduce its remaining anchor values. The cochain left over has only the $E$ coordinates. Each subtraction is unique and integral. Both the $B$ and $W$ columns have zero curl.

For Fourier mode $k$ let $\delta_i=e^{2\pi i k_i/L}-1$ and $\lambda_k=\sum_i|\delta_i|^2$. On that mode the curl is exterior multiplication by $\delta$. For $k\ne0$ its squared singular values on the orthogonal complement of its kernel are $\lambda_k$ with multiplicity three. At $k=0$ the whole four-dimensional block has zero curl. Complexification preserves the real squared singular spectrum, counting conjugate modes with their multiplicities. Consequently the kernel dimension is $V+3$ and it is exactly the span of $K=[B,W]$. The $D_1$ columns form a basis of the exact two-cochains. Put $P=\prod_{k\ne0}\lambda_k$, with the empty product one.

The matrix-tree theorem gives $\det(B^TB)=\tau_L=P/V$ for the positive-link multigraph. It also follows from Cauchy–Binet because every square full-rank tree incidence minor is $\pm1$ and the other minors vanish. The product of nonzero eigenvalues of $d_0^Td_0$ equals the sum of its $V$ principal cofactors, giving the second equality. For each $i$, the wrap cochain differs from the constant $1/L$ in direction $i$ by the gradient of $H_i(x)=-x_i/L$. The four indicators projected orthogonally off vertex gradients therefore have orthogonal columns, each with squared norm $V/L^2$. The kernel Gram determinant is
$$
 \det(K^TK)=\tau_L(V/L^2)^4=\tau_L V^2 .
$$

Project $E$ orthogonally off $K$, writing $E_\perp$ for the result. Taking the Schur complement in the unit Gram determinant of $[K,E]$ gives $\det(E_\perp^TE_\perp)=1/(\tau_LV^2)$. The curl on this complement multiplies squared volumes by $P^3$. Hence
$$
 \det(D_1^TD_1)=\frac{(V\tau_L)^3}{\tau_LV^2}
               =V\tau_L^2.
$$
At $L=1$ the incidence and residual Gaussian determinants are empty and equal one. At $L=2$ the two bonds in each periodic coordinate connect the same pair of vertices and both enter the Laplacian. [Exact finite-lattice controls](check.py) · [An independent proof of the matrix-tree theorem](https://arxiv.org/abs/1404.3876)
