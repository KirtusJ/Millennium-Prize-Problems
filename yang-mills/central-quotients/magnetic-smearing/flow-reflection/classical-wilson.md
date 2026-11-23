# Fixed physical flow carries magnetic data across the plane in compact SU(2)

There is a deterministic obstruction complementary to the measure-dependent reflected forms. At fixed positive physical flow time, even the bounded scalar reading $\min(1,a^{-4}(1-\operatorname{Re}U_{12}))$ at a fixed positive time cannot be approximated uniformly over compact Wilson configurations by any function of the original positive half. The following construction uses the nonlinear lattice flow itself.

Use periodic boxes of physical period $2\pi$ in every direction and $a=2\pi/N$ with $N$ divisible by eight. Put $U_1(t,x)=\exp(\mathbf i\,\theta(t,x_2))$ in a fixed circle subgroup of $SU(2)$ and take every other link equal to the identity. The phases are independent of $x_1,x_3$. The full Wilson flow preserves this ansatz. Each time or direction-2 link sees opposite contributions from its two direction-1 neighbors, by translation invariance in $x_1$. All other faces incident to an unoccupied direction have identity holonomy or cancel in the same way. Velocities are entirely in the circle algebra. The exact remaining equation in lattice flow units is
$$
 \partial_\tau \theta(z)=
 \sum_{j=\pm e_0,\pm e_2}\sin(\theta(z+j)-\theta(z)).
$$
The convention is the unit round metric and the sum of $1-\operatorname{Re}U_p$ with one face per square. Varying the reduced cosine action or taking its individual link derivatives gives the same equation. [Wilson flow definition](https://arxiv.org/pdf/1006.4518)

Initialize one configuration at identity and the other by $\theta=a f(t)\sin x_2$ on the physical grid, where $f$ is smooth, periodic, nonnegative, nonzero and supported strictly inside the negative half. They agree on *every* original link in the closed positive half. With $\tau=s/a^2$, write $A_a=\theta/a$. Its physical-time equation is $a^{-3}\sum_j\sin(a[A_a(z+aj)-A_a(z)])$. It converges uniformly on compact flow-time intervals to the sampled heat solution
$$
 A(s,t,x_2)=e^{-s}(P_s f)(t)\sin x_2 ,
$$
where $P_s$ is the periodic one-dimensional heat semigroup.

For the convergence estimate, the sampled smooth solution has uniformly bounded derivatives through order four. Taylor expansion of the symmetric difference gives a residual of order $a^2$ in the heat equation; the sine correction contributes $O(a^3)$ since its arguments are $O(a^2)$. The exact phase variables stay in $[-a\|f\|_\infty,a\|f\|_\infty]$ by the extremum principle for sufficiently small $a$. The sampled continuum field stays in the same rescaled range. Subtract the equations. The error evolves by a weighted nearest-neighbor difference with nonnegative weights (the intermediate cosines divided by $a^2$), plus the residual. The maximum principle gives $\sup_{0\le s\le S}\|A_a-A\|_\infty\le C_S a^2$ from equal initial data. This estimate suffices even after taking one spatial difference quotient.

The spatial plaquette at $x_2=0$ has phase $\theta(t,0)-\theta(t,a)$. Dividing by $a^2$ gives a limit $-e^{-s}(P_s f)(t)$. It is nonzero at every physical time when $s>0$ by positivity of the periodic heat kernel. At $t=\pi/4$ the normalized plaquette deficit tends to $\tfrac12 e^{-2s}(P_s f)(\pi/4)^2>0$, whereas the trivial configuration gives zero. Clipping at one preserves strict separation and bounds the reading on the entire configuration space. Any original-half function has the same value on these two inputs. At least one of its two errors is therefore at least half the observed difference. Rescaling the physical box gives such examples at any prescribed finite distance from the plane.

This excludes a configuration-uniform vanishing half-space error at fixed physical $s$ for the bounded reading just specified. Each test configuration can have negligible Wilson probability, so it leaves open the corresponding $L^2$ approximation on a prescribed interacting trajectory. Spatial-only flow preserves the time slices exactly. The [separate shrinking-time bound](wilson-locality.md) is also consistent with this obstruction.

### Finite-spacing check

The companion calculation evolves the exact sine lattice equations by fourth-order Runge–Kutta. It uses $s=1/2$ and a smooth bump strictly within the negative half. An independent Fourier sum computes the continuum target. The proof above controls the spatial approximation analytically; the computed table is a deterministic consistency check. The seed has nonzero magnetic curvature already in its negative-time support. [Code](check_classical.py) · [Recorded outputs](execution.md)
