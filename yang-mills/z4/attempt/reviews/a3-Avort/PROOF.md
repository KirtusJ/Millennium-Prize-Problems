# PROOF.md — claim (A) for SU(2), d = 4, by center vortices (builder a3-Avort)

**This is NOT a proof.** The chain below has one CLAIMED step (S5a) and two MISSING steps (S5b, S6). Each is named, with a testable form. The conclusion (A), m(β) > 0 at every β, does not follow from what is written here.

Notation. SU(2) Wilson action S = β Σ_P ½ tr U_P, weight e^{+S}. Λ_L = periodic torus (Z/LZ)^4. V = a coclosed stack of L² plaquettes in the (1,2) plane at fixed (x1,x2), winding in directions 3,4. O[V] flips the sign of the coupling on V. Z^- = Z·⟨O[V]⟩. The vortex free energy is F_L(β) := −ln(Z^-/Z). The electric free energy is e^{−F^el_L} := ⟨½(1 − O[V])⟩ = ½(1 − e^{−F_L}).

Order of limits, fixed once: β is fixed first. L → ∞ is taken along L = 2^k L₀ (k → ∞) at fixed β. Lattice spacing is never sent to zero here; claim (A) is a lattice statement at fixed β. Uniformity in L is used in S4, S5b and S6 and is marked there.

## The chain

**S0 (CITED; partly an assumption of A1 §4.5).** For every β, the periodic states ⟨·⟩_{Λ_L} have weak limit points as L → ∞ (by compactness of SU(2)^E; this is elementary). Uniqueness of the infinite-volume state is *not* known at large β. A1 §4.5 assumes it. Everything below holds for every limit point along L = 2^k L₀.

**S1 (CITED).** Reflection positivity of the Wilson action in planes through sites and in planes between sites, for every β: Osterwalder–Seiler 1978 (LIT_RIGOROUS R2, read at abstract level only). G4's Lean result on finite slabs and periodic tori (INDEX_EXTRACT (a)1) is not reread by me. Hypotheses: Wilson action, periodic torus, even side length for the between-sites reflection. Our L = 2^k L₀ with L₀ even meets them.

**S2 (PROVED, given S1).** 0 ≤ ⟨½(1 − O[V])⟩ ≤ 1, i.e. 0 < Z^- ≤ Z and F_L ≥ 0.
*Proof.* Z^- > 0 because its integrand is positive. P := ½(1 − O[V]) satisfies P² = P pointwise, since O[V] = ±1 after the change of variables (Kovacs–Tomboulis eq. (4), (7)). Strictly, O[V] is a ratio of Boltzmann weights. Its expectation equals ⟨½(1−O[V])·½(1−O[V'])⟩ for any homologous V' (KT (7)). Take V' = r(V), the mirror image of V in a plane π between sites that does not meet V. Then ½(1−O[V']) = θ(½(1−O[V])), and RP gives ⟨θ(X) X⟩ ≥ 0. ∎
Weak point: the step "O[r(V)] = θ O[V]" needs the twist to be the reflected one. That holds by construction because O is real.

**S3 (CITED).** For a rectangular Wilson loop C (R × T) in the (1,2) plane,
  ⟨W[C]⟩_{Λ_L} ≤ 2 · (e^{−F^el_L})^{|A_C| / (L₁L₂)}.
Source: Kovacs–Tomboulis, Phys. Rev. D65 (2002) 074501, arXiv:hep-lat/0108017, eq. (11). I read eqs. (2)–(11) in full text myself. KT attribute it to Tomboulis–Yaffe, CMP 100 (1985) 313, which I did NOT read. Tomboulis arXiv:0707.2179 eq. (6.4) restates it without the factor 2.
Hypotheses against my use: (h1) SU(2), Wilson action, periodic in all directions. Met. (h2) Repeated reflections in planes containing a leg of the loop, until "all trU factors are eliminated by the lattice periodicity". This needs L₁/R and L₂/T to be powers of 2, and the reflection planes to pass through sites. I meet it by taking R, T dividing L₀ with L₀/R and L₀/T powers of 2. (h3) The planes must not bisect the vortex (hole 9, I-S Thm 2.2). KT place V at the "filled square" and move it by the change of variables, so this is consistent. I did not check their figure.
Note: the two sources differ by the factor 2 (KT (11) vs Tomboulis (6.4)). The KT form is the safe one: at β = ∞ the form without the 2 would give W ≤ 2^{−S/A} < 1, which is false.

**S4 (PROVED, given S0, S3).** Suppose there are σ > 0, K < ∞ and L₀ such that F_L(β) ≤ K L² e^{−σ L²} for all L = 2^k L₀ (uniform in L). Then every limit point satisfies ⟨W_{R×T}⟩ ≤ 2 e^{−σ RT}, an area law.
*Proof.* e^{−F^el} = ½(1−e^{−F}) ≤ F/2 (F ≥ 0 by S2). So ln⟨W⟩_{Λ_L} ≤ ln 2 + (RT/L²)(ln(K L²/2) − σL²). As L → ∞ this tends to ln 2 − σRT. W is a local function, so the bound passes to the weak limit. ∎
Weaker sufficient input: liminf_L (−ln F_L)/L² ≥ σ > 0.

**S5 — the vortex condition: F_L(β) → 0 with rate e^{−σ(β) L²}, for every β.** I split it in two.

**S5a (CLAIMED).** Monotonicity: for SU(2), d = 4, every β > 0 and L | L', F_{L'}(β) ≤ F_L(β).
The argument as I would defend it:
- At strong coupling (β small) the cluster expansion gives F_L ≈ L² e^{−σL²} (Tomboulis 0707.2179 §6.1 says it is "explicitly realized within the strong coupling expansion"; not reread in the original, Münster 1981). This is decreasing in L.
- At weak coupling the classical action of a twist on an L⁴ box is scale invariant in d = 4 (it is the minimal-action flux configuration, of order β·π²·(L3L4)/(L1L2) = O(β) for cubic boxes). Hence F_L ≈ c·β_eff(L), with β_eff the coupling at scale L.
- Blocking L → 2L lowers β_eff for a non-abelian group (asymptotic freedom), so F decreases in L in both regimes.
- At intermediate β, the claim is that F interpolates monotonically, because the twist's free energy is a "surface" quantity that a block-spin step can only spread.
Weakest point: the last two bullets are the renormalization-group comparison F_{2L}(β) ≤ F_L(β') with β' ≤ β. No inequality of that form is proved; it is exactly the Tomboulis/Migdal–Kadanoff comparison that Ito–Seiler object to (holes 3–5). I do not close it.

**S5b (MISSING).** Strict decay: liminf_{L→∞} (−ln F_L(β))/L² ≥ σ(β) > 0, for every β, uniformly along L = 2^k L₀.
S5a alone gives only lim F_L = F_∞ ≥ 0. Neither F_∞ = 0 nor the rate follows. Testable form: Monte Carlo of F_L at fixed β for L = 4, 6, 8, …, checking that ln F_L is linear in L² with negative slope. Kovacs–Tomboulis 2000 report this numerically for SU(2) up to β ≈ 2.5 (abstract only; measured, not proved).

**S6 (MISSING).** Area law ⇒ gap. Needed statement: if every infinite-volume limit point at β satisfies ⟨W_{R×T}⟩ ≤ C e^{−σRT}, then the transfer matrix H_β on the gauge-invariant (zero electric flux) part of Ω^⊥ has inf spec ≥ m(β) > 0.
- No theorem gives it. Chatterjee 2021 Thm 2.4 (LIT_RIGOROUS R5(e), fact 9) goes the *other* way: strong mass gap (Def 2.3) ⇒ area law.
- As an abstract implication it is false. Example: SU(2) LGT tensored with a decoupled free massless scalar has an area law and no gap. So S6 needs the pure-gauge dynamics.
- Route (b) does not repair it. The electric flux free energy controls the lowest energy in the *nonzero* electric-flux sectors (≈ σL, the winding flux string). It says nothing about the zero-flux (glueball) sector. That is INDEX_EXTRACT (c)1, "gap in each of two sectors ⇒ gap".
Testable form: for a family of transfer matrices with area-law Wilson loops (e.g. 3D U(1), Villain), compare the zero-flux gap with σ. This is a consistency check only, not a proof.

## (i) Discriminator table

| Model | S1–S4 | S5a (monotone) | S5b (rate) | S6 | Conclusion (A) true? | First failing step, and why |
|---|---|---|---|---|---|---|
| U(1), d = 4, weak coupling (Coulomb) | hold (a Z₂ ⊂ U(1) twist, π flux; KT's derivation uses only RP and O = ±1) | plausibly holds: F_L → const ~ β·π²/2 (scale-invariant classical flux, no running) | **fails**: F_∞ > 0, Wilson loop has a perimeter law (Guth; Fröhlich–Spencer) | — | **false** | **S5b.** A marginal (non-running) coupling keeps the twist cost O(β) at every L. |
| Z₂, d = 4, β > β_c ≈ 0.44 | hold (twist = flip of the coupling sign) | **fails**: child measured F = 3.2, 8.2, 15.8 for L = 2, 3, 4 at β = 0.6 (≈ 1.0·L²) | fails | — | **true** (gap via Adhikari–Cao-type finite-group decay) | **S5a.** Deconfined: the vortex sheet has a surface tension, so the chain cannot give the gap. The right reason: the gap here does not come from confinement. |
| Z₂, d = 4, β = 0.3 (confined) | hold | consistent (child: 0.077 → 0.004 → 0.006 ± 0.005) | consistent | MISSING | true | none fails visibly; S6 still MISSING |
| U(1), d = 3 (Villain) | hold, with a line twist in d = 3 | expected to hold (Göpfert–Mack area law at all β) | expected to hold | MISSING (the gap m_D > 0 is known independently) | true | none; the chain would need S6 |
| d = 2, SU(2) or U(1) | hold | PROVED by explicit character formula: Z^-/Z = Σ_j (−1)^{2j} a_j^N / Σ_j a_j^N → 1 monotonically in N | PROVED (rate e^{−N ln(a_0/a_{1/2})}) | gap known by explicit formula | true | none; but 2D does not discriminate abelian from non-abelian |

## (ii) Where non-abelian structure enters

Only at S5a/S5b, through asymptotic freedom (β_eff(2L) < β_eff(L)). That step is CLAIMED and MISSING. **No proved or cited step of this chain uses non-abelian structure.** S1–S4 hold verbatim for U(1) and for Z₂.

## (iii) The test

The first CLAIMED step is S5a. It was tested by:
- my `vortex_su2.py`: SU(2), L = 2, 3, 4, β = 1.8 and 2.4, exact identity F = 2β∫⟨Σ_V ½trU_P⟩_s ds plus Monte Carlo;
- the child's `child/vortex.c` on Z₂ (the discriminator).
Results are in report.md.
- Z₂ at β = 0.6: S5a is false, as it must be (deconfined). This does not refute S5a for SU(2), but it shows S5a is not a general property of center-symmetric gauge theories. Any proof of it must use SU(2) specifics.
- SU(2), L = 2, 3, 4:
  - β = 1.8: F = 0.69 ± 0.24, −0.26 ± 0.28, 0.49 ± 0.40.
  - β = 2.4: F = 3.06 ± 0.42, 1.55 ± 0.45, 2.81 ± 0.95.
  - Monotonicity at 3σ was met in 4/4 cases. But the errors are as large as the differences. At β = 2.4, F(4) > F(3) at the 1.2σ level, so the data do not support strict decrease from L = 3 to L = 4.
  - S5a is **not refuted and not supported** on these boxes. The test is too weak to bear weight.

## Weakest link

S5 (the vortex condition at all β, uniformly in L) is the whole content of confinement. This chain only *relocates* (A) onto it. Beyond it, S6 (area law ⇒ gap in the zero-flux sector) is a separate MISSING implication. It would remain open even if S5 were proved.

## What a challenger should attack first

1. **S6**: show that no argument from Wilson-loop/vortex bounds alone reaches the zero-flux gap. The decoupled-massless-scalar example already kills the abstract version.
2. **S5a**: produce a β for SU(2) where F_{2L} > F_L beyond errors (small L at large β is where lattice artefacts may give it).
3. **S3's hypotheses**: the factor-2 discrepancy between KT (11) and Tomboulis (6.4); the power-of-2 tiling; the position of V relative to the reflection planes (hole 9).
4. **S0**: the infinite-volume limit is along periodic tori only. The other boundary conditions that Chatterjee's Def 2.3 needs are not covered.
