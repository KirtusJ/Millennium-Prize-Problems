Report of a review sub-agent (same model family as the director; not independent review), as handed back; saved by the director.

**`report.md` was not written.** The Write call to `/home/user/z4-workers/mod-sci/report.md` was refused by the harness ("Subagents should return findings as text, not write report files"), and I did not route around it through the shell. The full report is therefore below, which is why this exceeds the 900 words you asked for. If you want the file, save sections A to E as they stand.

What does exist on disk:
- `/home/user/z4-workers/mod-sci/recompute.py` (standard library only; predicates in the docstring before the first run), sha256 7ef48bbf…e90b53
- `/home/user/z4-workers/mod-sci/results.txt` (opened with mode `x`), sha256 e96e667c…99ab0a
- Command, run from `/home/user/z4-workers/mod-sci`: `python3 -I recompute.py /home/user/Millennium-Prize-Problems/yang-mills/z4/attempt/reviews results.txt`
- The first run exited 1 (my bug: a line filter also caught the "PREDICATE S" lines; no output file was written). The second run exited 0 with 30 predicates met and 0 failed.

I share the director's model family, so my agreement is not independent review. Nothing under `/home/user/Millennium-Prize-Problems` was edited. What I recomputed is arithmetic on the deposited summaries: I regenerated no ensemble and recomputed no jackknife from per-stream data. I did not read the Rust samplers or `main.pdf`, and I reviewed no theorem.

Every manuscript number I checked matches the records in value. The problems are in what is omitted and in four places where the wording says more than the design supports.

# A. Findings, each with replacement LaTeX

Severity: H = the manuscript says more than the record supports, or omits something a reader needs to weigh the number; M = material omission of design; L = wording.

## F1 (H) s:time, last paragraph: "It does show …" is not supported by the design

Sentence: "It does show that slowness under the local updates and slowness in time are different properties, which is the reason for separating Hypothesis h:mix from the auxiliary statement."

Record (d2-time):
- One combination, one frozen slice, one coupling, linear predictors, lag one.
- The later slice is not frozen; its coarse background is free (slice-0 plaquette .76990, slice-1 .75181). The test asks whether a function selected for a −I background on slice 0 is predicted by marks on a slice whose background is generic.
- It is a conditional one-step correlation given the slice-0 coarse links, not ⟨f,A²f⟩ of the transfer operator.
- The held-out R² carries an offset of about −0.017, so a true R² up to about 0.03 is not excluded (the worker's own caveat).
- The local quotient is an average over 24 colours and one time step is a full transfer step, so the two "rates" are not on one scale.
- The separation of h:mix from the auxiliary statement is a logical distinction made in s:arch and needs no measurement.

Replace the paragraph by:

```latex
So, for this one combination on this one frozen slice, the linear predictors that were tried recover at most
a few per cent of its variance one slice later. The later slice is not frozen, so its coarse background is
not the one for which the combination was selected; the test is a correlation conditional on the coarse
links of one slice, not a matrix element of the transfer operator, and it is not a measurement of
Hypothesis~\ref{h:mix}. It does not bound the best prediction from the later slice, and it does not exclude
other combinations that propagate slowly. The local quotient (an average over the $24$ colours) and a
correlation over one time step are not on a common scale, so the two numbers are not compared here. The
distinction between Hypothesis~\ref{h:mix} and the auxiliary statement is the logical one of
Section~\ref{s:arch}; this measurement neither supports nor contradicts either.
```

## F2 (H) s:time, "Setup and result": omitted design, omitted values, one unlike comparison

1. The rule fixed before the runs had three outcomes. Its "does not persist" clause (R² < 0.02 with error < 0.01) was met in both forms, and the worker judged that clause uninformative because of the offset. The manuscript quotes only the 0.1 clause.
2. The errors (2) are a jackknife over the 16 held-out streams with the fitted coefficients held fixed. The variance of the fit is not included (stated in `antime.py`).
3. "About −0.017" is two numbers: −0.016(2) (later-slice form) and −0.019(2) (transported form). The null expectation −p/(N−p−1) with p = 308 and N = 16×1152 = 18432 is −0.0170, so describing it as an over-fitting offset is right. Adding it back gives roughly +0.004 and +0.015; this is a rough correction, not an estimator.
4. The 15-mark fit, 0.011(2), was not in the rule (measured only, chosen after the data). At lag −1, which estimates the same quantity by reflection, it is 0.005(2). The two differ by 2.4 standard errors (my computation), and the manuscript quotes the larger.
5. "0.083(6) against 0.032(5)" is like-for-like in construction: transported form, lag one, 32 streams each, each background with its own selected 308-mark combination. It is not the same function on both, because the sampled-background weights were refitted.
6. The plain four-mark average, not selected at all, gives 0.076(5) against 0.009(6). So the excess at −I is not a property of the selected combination.
7. The form that is a function of the later slice alone gives 0.022(4) against −0.003(6). The manuscript reports only the larger, transported, correlation.
8. These correlations use all 32 streams; the R² values use 16 + 16. The section header says only "jackknife over streams".
9. 48 table rows were computed (2 forms × 4 lags × 3 vectors × 2 backgrounds); six are quoted.
10. No result file of this run is deposited. `d2-time/` holds programs, weights, report and notes, but no `results/` and no archive, so the numbers rest on the worker's report alone.

Replace the "Setup and result" paragraph by:

```latex
\emph{Setup and result.} Same lattice, coupling and frozen slice; $32$ fresh streams, $16$ for fitting and
$16$ held out. The later slices are not frozen. The $308$-mark combination selected above was regressed on
the same $308$ marks one time slice later, in two gauge-invariant forms: with reference directions taken on
the later slice, and with the later marks transported back along time-like links to the frozen reference (a
mark of the second form is not a function of the later slice alone). The rule fixed before the runs had
three outcomes: persistence if the held-out coefficient of determination exceeds $0.1$ and exceeds that on
the sampled background by three standard errors; no persistence if it is below $0.02$ with error below
$0.01$; otherwise unresolved. The values are $-0.013(2)$ and $-0.002(2)$ (errors over the held-out streams
with the fitted coefficients fixed; the uncertainty of the fit is not included). With $308$ regressors and
$18432$ fitting measurements an uncorrelated target gives about $-0.017$, and the same fit at a lag of three
slices, where no correlation is seen, gives $-0.016(2)$ and $-0.019(2)$. The second clause of the rule is
therefore met formally but cannot exclude a coefficient of determination up to about $0.03$, and we draw no
verdict from it. The following were not part of the rule and were chosen after the data were seen. A fit on
$15$ marks in the transported form gives $0.011(2)$ at lag $+1$ and $0.005(2)$ at lag $-1$, which estimate the
same quantity. The correlation of the combination with its own copy one slice later (all $32$ streams) is
$0.083(6)$ in the transported form and $0.022(4)$ in the later-slice form, and $0.016(6)$ in the transported
form at two slices. On the sampled background the combination selected there gives $0.032(5)$ and $-0.003(6)$.
The unselected average of four plaquette marks gives $0.076(5)$ at $-I$ and $0.009(6)$ on the sampled
background in the transported form, so the larger correlation at $-I$ is not particular to the selected
combination. The result files of this run are not in the deposit; the numbers are those of the run's
report~\cite{RepoData}.
```

## F3 (H) s:local (ii): the rule fixed in advance said the opposite; the paired comparison was not the rule

Sentence: "The values decrease as the span grows, on both backgrounds, and a comparison paired on the same held-out streams resolves each decrease, including the last. … No lowest value is indicated on either."

Record (c2-grow, `an4.py` docstring, predicate G1): "stopped falling" := |difference| ≤ 2 combined standard errors, treating the two values as independent.

| step | −I: unpaired z, rule outcome | −I: paired z | sampled: unpaired z, rule outcome | sampled: paired z |
|---|---|---|---|---|
| 15 → 49 | −6.4, not stopped | −38.4 | −6.1, not stopped | −8.6 |
| 49 → 181 | −1.3, **stopped** | −15.2 | −3.6, not stopped | −5.8 |
| 181 → 308 | −0.8, **stopped** | −11.8 | −13.7, not stopped | −15.3 |

- "Resolves" is right for all six steps, as a statement about pairs of fixed selected combinations. All paired |z| exceed 2.95, the two-sided 1 % point of t with 15 degrees of freedom.
- The paired values were printed by the same program as "measured only"; they were not the registered rule. The registered rule was met at −I for the last two steps, and the manuscript does not say so.
- The spans are nested, so the smallest quotient of a span cannot increase. The measurement is of the size of the steps, not their sign.
- Percentages recomputed: 19.9, 4.9, 2.8 at −I; 9.5, 4.5, 15.9 on the sampled background.

Replace (ii) by:

```latex
(ii) The spans are nested, so the smallest quotient of a span cannot increase as it grows; the measurement
is of the size of the steps. The rule fixed before the run compared successive entries as if independent
and called the decrease stopped when they differ by less than two combined standard errors. By that rule
the decrease stopped after $49$ marks on the first background and did not stop on the second. The entries
of a row are computed on the same held-out streams, and the paired differences, which the rule did not
use, are $38$, $15$ and $12$ standard errors on the first background and $9$, $6$ and $15$ on the second. On
the first background the steps are $20$, $5$ and $3$ per cent; on the second $10$, $4$ and $16$ per cent,
the last being the largest. The data indicate no lowest value on either, and the ratio of the two rows
($2.8$) is for these spans only.
```

## F4 (H) s:local (iii): the conclusion rests on the single mark; one failed check and two further displacements are omitted

Sentence: "(iii) Displacing the frozen holonomy … Two displacements are not an interval, but the low quotient is not confined to the immediate neighbourhood of −I that Theorem t:ret controls usefully."

Record:
- **Registered run (e2-repair):** Q1 = 1.004(11), Q4 = 1.034(13) (recomputed 1.0037, 1.0334; Q4 is 2.6 standard errors above 1). The burn-in check failed for the four-mark average at −I (d = +2.11), all four half-differences are positive, and Q4 on first/second halves is 1.049(21)/1.018(19).
- **First run:** 1.016(11). Its hot/cold check had been reported as met through a reducer that split streams by file-name order; with the split repaired it fails (z = −2.68).
- **Other displacements (z1-mix6):** 0.5/β; 1/β (0.992(13)); and 4/β = 1.22 rad, where the single-mark ratio is 1.075(11) and the four-mark quotient rises from .0469(5) to .0577(7).
- **Which quotient is "low":** the low quotient of this section is the selected combination (.015 to .021), not the single mark (.061, against .071 to .081 on three sampled backgrounds).
- **Selected combination under displacement:** the record has one displacement only. In b2-matrix, same 15 marks at 1/β: .0207(2) against .0216(5), ratio .96(2), separate runs. Nothing was measured for it at 2/β.

Replace (iii) by:

```latex
(iii) Displaced backgrounds were measured for single marks at four displacements and for the selected
combination at one. With the frozen holonomy at round distance $1/\beta$ from $-I$, the $15$-mark
combination selected there has held-out quotient $.0207(2)$, against $.0216(5)$ at $-I$ in a separate run
of the same design. For the single plaquette mark the ratio of the quotient at distance $2/\beta$ to that
at $-I$ is $1.016(11)$ in a first run and $1.004(11)$ in a second, registered, run; at $4/\beta$ it is
$1.075(11)$. For the four-mark average the ratio at $2/\beta$ is $1.034(13)$. Two checks failed: the
hot-start against cold-start check of the first run at $2/\beta$ ($2.7$ standard errors; it had been
reported as passed because of an error in the reduction program, since repaired), and one of the four
burn-in checks of the second run, in which all four drifts have the same sign. These are a few points, not
an interval. They indicate that the quotients measured at $-I$ are also found at distances of order
$1/\beta$; they do not determine how far, and the neighbourhood that Theorem~\ref{t:ret} controls usefully
is smaller than the largest distance tried.
```

Check the last clause against Theorem t:ret before using it; I did not review the theorem.

## F5 (M) Section opening (s:evid): "can show", "raw data", and the replication unit

Sentences: "A trial can therefore show that a constant is at most some value; …" and "Programs, seeds, raw data, the pass rules fixed before each run and the rules that failed are in RepoData."

- A true trial value bounds a constant. An estimate of it with a statistical error does not, by the manuscript's own rule that nothing is a bound.
- The raw data are not all deposited. c2-grow deposits summaries only (`child/DATA_NOT_DEPOSITED.md`: the per-stream matrices and raw files are regenerated from seeds). d2-time deposits no result file.
- z1-mix6 and z1-mix8 record that a rebuilt binary does not replay the archived streams bit for bit, so "regenerated from the seeds" means statistically, not byte for byte.
- The number of streams behind an error differs by measurement (16, 32, 8 + 8, 16 + 16) and is not stated.
- Thermalisation and autocorrelation are not mentioned.

Replace the paragraph by:

```latex
This section reports Monte Carlo estimates for $\SU(2)$. A \emph{stream} is an independent run of the
sampler with its own seed, started hot or cold in alternation; the stream is the unit of replication.
Errors are delete-one-stream jackknife standard errors, a digit in parentheses is the standard error in the
last digit, and the number of streams behind each error is stated with it. Where a test function was
selected from a span, the selection used one set of streams and the reported value comes from other
streams; the error is then that of the selected function with its coefficients fixed, and does not include
the variability of the selection. Each measurement tries particular test functions in an inequality that
an open hypothesis, or the auxiliary statement, would need for all functions. The exact value for a trial
function limits a constant from one side. What is reported is an estimate of that value with a statistical
error, which is not a bound; no measurement can show that a hypothesis holds, and none is used in a proof.
Every measurement is at one coupling per lattice, on lattices of side $5$ to $10$ with periodic time, with
heat-bath sampling; thermalisation was checked only by comparing hot and cold starts and first and second
halves, and some of these checks failed (they are named where they bear on a number). Couplings were taken
from a calibration in~\cite{RepoData} and not recalibrated, so every statement at ``matched'' couplings
inherits it. Programs, seeds, the rules fixed before each run, the rules that failed and summary files are
in~\cite{RepoData}; per-stream data are deposited for Section~\ref{s:cross} and for the single-mark runs,
and are regenerated from the seeds for the others.
```

## F6 (M) s:cross items 1 to 3: sample sizes, multiplicity, "rejected", the range of 1 − R, an unreproduced external value

Recomputed from `f2-cross2/results_text/`:

| ensemble pair | chains | R_10 | R_5 | ratio | ratio + 2 SE | (1 − ratio)/SE |
|---|---|---|---|---|---|---|
| time extent 2 × side, held-out | 8 + 8 | 0.9318(40) | 0.9903(30) | 0.9409(49) | 0.9507 | 12.1 |
| time extent 4 × side, independent | 16 + 16 | 0.9317(25) | 0.9957(11) | 0.9357(27) | 0.9412 | 23.7 |

- **Threshold:** max(0.9507, 0.9412) = 0.951, as the manuscript says.
- **1 − R:** 1 − R_5 is 0.97 per cent (2 × side) and 0.43 per cent (4 × side); 1 − R_10 is 6.8 per cent at both. "About 1 per cent" holds for the first pair only.

**Multiplicity.**
- First span (e2-cross): the report counts 22 frozen tests at each of two time extents, in two forms (the table file has 24 rows). None was below one in the quotient form.
- The second study was designed after that outcome was known, with a new span (54 functions, five classes), new seeds and four times the measurements.
- In it 25 frozen tests were examined per pair, and the reported one is the minimum of ratio + 2 SE over the 25. The next smallest are 1.0004 and 1.0026, so selection among the 25 does not produce the effect.
- The same frozen test was then evaluated on ensembles that share no chain with either the selection or the first evaluation.

**Does the design protect the claim?**
- It protects "this test has ratio below one on this pair" against selection.
- It does not make 0.951 a confidence limit at a stated level. It is two standard errors from a jackknife over 8 + 8 chains (about 14 degrees of freedom, one-sided level near 96 to 97 per cent rather than 97.7), read as the larger of two limits.
- It inherits the coupling match, which was not rechecked.
- "Rejected" names a test outcome. The rule's own word was "defeated", and the object is an inequality for one function.

**Omitted results a reader needs.**
- In the 4 × side fine ensemble the first run was killed after 2 chains, and the rerun has 1000 measurements per chain, not 2000.
- On the same fine lattice at 2 × side, the other director's four-bin winding statistic (.00408(72), 4 streams × 128) is not reproduced: these ensembles give .00158(14), 3.4 combined standard errors away. The cause is not determined.
- Energy form: the E ratio 0.00407(5) equals the variance ratio 0.00336 times the quotient ratio 1.212. That test's quotient ratio is above one, which the manuscript does not say.

Replace items 1 to 3 by:

```latex
\item \emph{Unnormalised energies.} In a first span of $16$ slice-averaged functions ($16$ streams per
lattice, $500$ measurements each, half used for selection), the test selected to minimise the ratio of
energies has, on the $8+8$ held-out streams, two-time energy on side $10$ equal to $0.00407(5)$ times that
on side $5$. This is the ratio of its stationary variances, $0.0034$, times the ratio of its quotients,
$1.21(1)$: the function has a much smaller variance on the finer lattice and decays slightly faster there.
An inequality $\mathcal E_{10}(f)\ge c\,\mathcal E_5(f)$ with $c$ of order one therefore fails for this
function on this pair as a matter of normalisation, and a comparison of deficits must account for the
change of variance. In this span no test had a quotient ratio below one.
\item \emph{Normalised quotients.} A second study, designed after the first was seen, used new streams
($16$ per lattice, $2000$ measurements each), a span of $54$ functions, and five classes of test. Of the $25$
tests fixed on the selection streams, one, selected to minimise $\mathsf R_{10}/\mathsf R_5$ among
slice-averaged functions, has a ratio below one on the $8+8$ held-out streams: $\mathsf R_5=0.990(3)$,
$\mathsf R_{10}=0.932(4)$, ratio $0.941(5)$. The other $24$ have ratio plus two standard errors above one.
The same fixed test on ensembles of twice the time extent, which share no stream with the selection
($16+16$ streams; $1000$ measurements per stream on side $10$), gives $\mathsf R_5=0.996(1)$,
$\mathsf R_{10}=0.932(2)$, ratio $0.936(3)$. So this test retains about $7$ per cent of its correlation over
the lag on the finer lattice and between $0.4$ and $1$ per cent on the coarser. The rule fixed in advance
reads off the ratio plus two standard errors on both pairs, $0.951$ and $0.941$: for this test, on this
pair, at these couplings, the estimates do not support $\mathsf R_{10}\ge\alpha\,\mathsf R_5$ with
$\alpha>0.951$. The figure is two jackknife standard errors over few streams, not a confidence limit at a
stated level, and it inherits the coupling match. One related number is unexplained: for a different
statistic on the same finer lattice an earlier run by another program in~\cite{RepoData} gives $0.0041(7)$
where these ensembles give $0.0016(1)$.
\item \emph{What this does not show.} Hypothesis~\ref{h:coarse} compares the smallest deficits on the two
lattices, not the values of one test, and $\varepsilon_i$ is a difference of deficits. One test cannot
measure it, and this result is neither evidence for nor against the hypothesis. The lattices have periodic
time of finite extent and are not the vacuum; one pair of sides, one renormalised coupling and one lag were
used. The first span contained no such test, so the outcome depends on the span, and a larger span could
change it again.
```

## F7 (M) s:rem: "the backgrounds on which decay is slow" conflates the auxiliary quotient with h:mix

No decay in time was measured to be slow on any background. s:local is about local updates, and Table tab:status says "h:mix: open; not measured". Replace the clause by:

```latex
Hypothesis~\ref{h:mix}, with gates wide enough to contain whatever backgrounds turn out to have slow decay
in time (none has been identified: Section~\ref{s:local} concerns the local updates only, on two
backgrounds) and still within the budget of Hypothesis~\ref{h:budget};
```

## F8 (L) Introduction, after Theorem t:ret: "because that is where the measurements … find slow local relaxation"

One background with three plaquettes at −I was compared with one sampled background, and the quotient at displacement 1/β is not higher. Replace by:

```latex
The gate is centred at $-I$ because the smallest local quotients we measured are on a background with
three plaquettes at $-I$ (Section~\ref{s:local}: two backgrounds, one lattice, one coupling); this is a
choice suggested by those trials, not a result.
```

## F9 (L) s:not item 5: "one-sided by nature"

```latex
\item The measurements of Section~\ref{s:evid} are Monte Carlo estimates on lattices of side $5$ to $10$,
one coupling each, with statistical errors. The exact value of a trial function limits a constant from one
side; an estimate of it is not a bound. No measurement is evidence for or against a hypothesis, and none is
used in a proof.
```

## F10 (L) s:local (i): say which span and which convention

The 81 per cent is for the 308-mark span (recomputed .8116); the 15-mark span lies wholly on the three plaquettes. In the 308-mark span four exact linear dependencies among the marks were removed and the minimum-norm coefficients used, so the shares depend on that convention. Replace the first two sentences of (i) by:

```latex
(i) The selected combination is collective. In the $308$-mark span, $81$ per cent of the sum of its squared
coefficients, each scaled by the standard deviation of its mark, belongs to the three coarse plaquettes
with holonomy $-I$ ($9$ per cent to the adjacent plaquette that contains both altered links). Four exact
linear relations among these marks were removed and the coefficients of least norm taken, so the shares
depend on that convention; in the $15$-mark span the coefficients on one of the three plaquettes have the
sign opposite to those on the other two.
```

## F11 (M) s:local Setup: what was fixed, how the second background was chosen, stream design

Replace the last two sentences of the Setup paragraph ("For each span … slower relaxation.") by:

```latex
The four spans are nested and were fixed before the runs: the $15$ marks on the three $-I$ plaquettes; $49$
marks on the seven coarse plaquettes that contain an altered link; $181$ and $308$ marks that add the $33$
plaquettes sharing a coarse edge with those. Each background has one run of $32$ streams ($576$ sweeps
discarded, then $1152$ measurements six sweeps apart). For each span the linear combination with the
smallest quotient is selected on streams $0$ to $15$ and its quotient is reported, in
Table~\ref{tab:local}, on streams $16$ to $31$. The second background is one configuration: the first of
$60$ drawn from the unconditioned measure whose coarse plaquettes are all farther than $\pi/4$ from $-I$
($40$ qualified), a rule fixed in advance; on it the selected direction is less stable (for the $49$-mark
span the directions selected on the two halves have cosine $0.41$). Smaller means slower relaxation under
the local updates.
```

## F12 Table tab:local (task 4)

- The reader cannot tell n, what the parentheses mean, or that the caption's comparison values come from other runs.
- It is the four entries of a row (the columns) that share streams, not the two rows: the rows are independent runs (seeds 11100001 and 11300001).
- The caption's ".086" is from the earlier b2-matrix run; the table's own run gives .0893(9). ".062" is .0611(4) in the table's run.

```latex
\begin{table}[ht]
\centering\small
\begin{tabular}{@{}llcccc@{}}
\toprule
 & & \multicolumn{4}{c}{Number of marks in the span} \\
\cmidrule(l){3-6}
Background & & 15 & 49 & 181 & 308 \\
\midrule
A & held-out quotient  & .0208(5) & .0167(4) & .0159(4) & .0154(4) \\
  & quotient on selection streams & .0213 & .0172 & .0163 & .0157 \\
  & decrease from the span to its left &  & 20\% & 5\% & 3\% \\
\addlinespace
B & held-out quotient  & .0589(8) & .0533(5) & .0510(4) & .0428(4) \\
  & quotient on selection streams & .0587 & .0514 & .0482 & .0410 \\
  & decrease from the span to its left &  & 10\% & 4\% & 16\% \\
\bottomrule
\end{tabular}
\caption{Local quotient $\mathcal J/\mathcal V$ (dimensionless; smaller means slower relaxation under the
local updates) of the combination of marks selected on $16$ streams and evaluated on $16$ other streams of
the same run. Side $6$, $T=12$, $\beta=3.276133577$, one run of $32$ streams per background. A: frozen
background with three coarse plaquettes of holonomy $-I$. B: one frozen background drawn from the
unconditioned measure, every coarse plaquette at round distance greater than $1.1$ from $-I$. A digit in
parentheses is the jackknife standard error over the $16$ held-out streams, with the selected coefficients
fixed. The spans are nested and the four entries of a row are computed on the same streams, so they are
strongly correlated and their differences are far better determined than the errors shown suggest; the
two rows come from independent runs. All entries are estimates, not bounds. For comparison, in the same
runs and on all $32$ streams, the unselected average of the four plaquette marks of one coarse plaquette
gives $.0473(5)$ on A and $.0893(9)$ on B, and a single plaquette mark gives $.0611(4)$ on A.}
\label{tab:local}
\end{table}
```

The "selection streams" row is `train_lambda` in `an4.json`. On A the held-out value is below the selection value at every span. The swap of the two halves gives a positive symmetrised gap (+.00001 to +.00018), so the sign reflects the two halves and not a defect.

## F13 (L) Table tab:status rows

```latex
Auxiliary local mixing & open; estimates for trial functions on two frozen backgrounds, one lattice, one coupling (Table~\ref{tab:local}) \\
Hypothesis~\ref{h:coarse} & open; not measured; one trial function compared on one pair of lattices (Section~\ref{s:cross}) \\
```

## Checked and found consistent with the record

- All eight table entries and their rounding. They are standard errors from 16 held-out streams.
- The percentages 20, 5, 3 and 81 per cent.
- "About −0.017" as the size of the over-fitting offset.
- 0.941(5), 0.936(3) and 0.951; 0.00407(5) and 0.0034.
- s:set: "It measures relaxation under these artificial updates, not under the transfer operator."
- s:arch: the auxiliary statement is described as stronger than h:mix.
- The closing sentence of s:local ("estimates … not certified bounds").

# B. Negative results in the records: reported or omitted, and whether each matters

| record item | in manuscript | matters to a reader |
|---|---|---|
| Reducer split streams hot/cold by file-name order (e2-repair); one control changes MET → FAILED (z −2.68) | only "reduced part of the raw data again and corrected it" in s:disc | yes: the failed control is on the run behind 1.016(11). F4 |
| Burn-in check failed in the registered run (d = +2.11; all four drifts positive) | yes, in (iii) | yes; kept in F4 |
| Hot/cold check failed for the four-mark average in the table's run at −I (z 2.22 against 2); 2 of 18 failed in b2-matrix | no | minor: about the chance rate for a two-sigma check; covered by the F5 sentence |
| Pre-fixed "stopped falling" rule met at −I for the last two steps | no | yes. F3 |
| Sampled background: selected direction unstable (cosine .41 at 49 marks) | no | moderately. F11 |
| Gated measurement on the unconditioned measure not resolved (0 and 52 pairs against a rule of 200) | no | yes, as a limit: the gate fraction is 1.5e-4 at angle 1.2 and 6e-8 at 0.6. One sentence could be added to s:local |
| Thermalisation failed twice at β = 12 (a2-mixb), no number given; at β = 6 and 12 the four-mark ratio falls 13 to 29 per cent with displacement | no | bears on "one coupling": the flatness in (iii) is not seen at larger β. One clause |
| Side 8: variance hot/cold check failed for one sampled background (3.2σ) | no | no: no side-8 measurement is quoted |
| Other director's side-10 value not reproduced (3.4σ) | no | yes, one sentence. F6 |
| First 16-function span found no test below one | yes (item 3) | kept |
| First 4 × side fine run killed; rerun at half length | no | minor; n is now stated in F6 |
| Time test: local-reference carry-over "not resolved" | no | yes. F2 gives the number |
| d2-time results not deposited; c2-grow raw matrices not deposited | no ("raw data … are in") | yes. F5, F2 |
| Bitwise replay of archived streams fails across builds | no | minor |

# C. Design summaries

## C1. Local quotient (b2-matrix, c2-grow; single marks z1-mix6, e2-repair)

- **Question:** how small is J/V over a span of marks on a frozen coarse background. This concerns the auxiliary statement only.
- **Estimand:** J(F)/V(F) of the fixed combination F selected on the training streams, in the conditional law given the frozen slice. It is an upper trial value for the infimum over all F.
- **Unit:** stream. 32 per run (16 hot, 16 cold), 576 sweeps discarded, 1152 measurements 6 sweeps apart; train 0–15, held-out 16–31.
- **Fixed in advance:** lists L1–L4, estimators, split, predicates A1–A6, G1, G2; the clearance rule for the sampled background.
- **Chosen after data:** the emphasis on the paired comparison; extra lists (21 and 7 marks). The b2-matrix "extra" spans (31, 35, 43 marks) were added in sequence after seeing results, and c2-grow's L1 repeats the 15-mark set found there.
- **Selection:** generalised eigenproblem on the training half. Optimism gap held − train is −.0003 to −.0006 at −I and +.0002 to +.0028 on the sampled background; the symmetrised gap is positive.
- **Error model:** delete-one-held-stream jackknife with coefficients fixed; plug-in variance; streams assumed independent.
- **Multiplicity:** 4 nested spans × 2 backgrounds + 4 extra lists; 6 G1 tests; 6 hot/cold tests.
- **Controls:** gauge invariance 1.2e-15; byte identity with the previous sampler; L1 against the earlier run (z −1.1); child recomputation (same method).
- **Failed:** G1 ×4 as outcomes; hot/cold f4 at −I (z 2.22); the child's positive-definiteness check (4 exact null directions of the list).
- **Threats:** thermalisation tested only by hot/cold; one sampled background; span dependence (still falling); coupling on trust; one side; SU(2); local updates, not transfer dynamics.

## C2. Time test (d2-time)

- **Estimands:** ρ_w(t) = Corr(w·X(0), w·Y(t)) and held-out R² of w·X(0) on the 308 Y(t), in two forms, conditional on the frozen slice 0.
- **Unit:** stream. 32 per background with fresh seeds; ρ on all 32, R² fitted on 0–15 and evaluated on 16–31. The weights come from c2-grow's training half, so they are independent of these streams.
- **Fixed in advance:** the design and the three-outcome rule (`prodt.py` docstring); predicates M1, M2, A4, A7, S1.
- **Chosen after data:** the 15-regressor fit; the reading of the lag-3 value as an offset; the emphasis on ρ in the transported form.
- **Error model:** jackknife over held-out streams with β fixed (fit variance excluded).
- **Multiplicity:** 48 rows; 12 reflection tests per run at 3σ.
- **Controls:** 40 of 40 thermalisation and symmetry checks met (largest |z| 2.13); gauge invariance; byte identity; child recomputation with prescribed formulas.
- **Failed:** 3 instances of a test-design error (metadata prefix), rerun and met.
- **Threats:** offset −0.017 comparable to the signal; later slice unfrozen; linear predictors only; one lag resolved; no deposited results.

## C3. Cross-lattice (e2-cross, f2-cross2)

- **Estimand:** R_10(f)/R_5(f) for the frozen f at lag l/5; in e2-cross also E_10(f)/E_5(f).
- **Unit:** chain. 16 per ensemble (8 hot, 8 cold), burn 500 sweeps, 3 sweeps between measurements. Train i mod 4 ∈ {0,1}; held-out i mod 4 ∈ {2,3}, giving 8 + 8 held-out chains.
- **4 × side ensembles:** all 16 + 16 chains, none used in selection.
- **Measurements per chain:** 500 (e2-cross); 2000, and 1000 for the 4 × side fine ensemble (f2-cross2).
- **Fixed in advance:** predicates P1, P2, Q0, Q1, D, S and the "ratio + 2 SE at both extents" rule.
- **Chosen after the first study's data:** the second study's span, classes and statistics.
- **Error model:** delete-one-chain jackknife per lattice, combined in quadrature on the log ratio.
- **Multiplicity:** about 22 tests × 2 extents × 2 forms in the first study; 25 × 2 in the second, plus retraining at 4 × side (0.938(4)), two rotated copies and two period nulls.
- **Controls:** gauge and centre invariance with sensitivity controls; a coarse-against-coarse null (smallest bound 1.0004, so the selection procedure gives no spurious result); a fine period null.
- **Failed or adverse:** the worker's expectation "no test defeats α = 1"; the other director's side-10 2 × side value not reproduced; the first 4 × side fine run killed.
- **Threats:** coupling match on trust; finite periodic time; one pair, one lag; span dependence; winding τ_int of 8.6 to 14 measurements (24.6 against a limit of 25 in the first study's 4 × side fine ensemble).

# D. Module clauses

**Science, applied:**
- §2: question, what would count against it, and whether fixed before or after; independent units.
- §4.1: the Measurement, Statistical, Predictive and Computational rows.
- §4.2: plan timing against exposure; exploratory work remains exploratory.
- §5.2: shared dependencies; the child reruns share the method.
- §5.3: a value crossing a decision boundary (the lag-3 offset against the 0.02 clause).
- §5.4: estimate against bound.
- §6: non-significant is not "no effect"; reproduction against replication.
- §7.2: denominators and Monte Carlo uncertainty.
- §8.1: timing evidence.
- §8.3: null and adverse results.

**Science, not applied or not possible:**
- §1.1 Core records and dispositions: this was a task, not a commissioned Review.
- §3 protections: inapplicable.
- §5.1 source status: no published empirical source is relied on.
- §7.1 optional methods: not used.
- §10 `science.order`: I did not run the register instrument. "Rule before run" is taken from the workers' records and file times, which §8.1 says do not establish it.
- The one exception is `e2-repair/REGISTRATION.md`. I recomputed its digest (it matches `REGISTRATION.sha256`), and its stamp 01:45:40Z precedes the register's first production entry at 01:47:14Z.

**Statistics, applied:** §2.1–2.3 (the thresholds 0.1, 0.02, 2 SE and 3 SE are the briefs' and are attributed), §3.1, §3.2, §3.4, §4.1, §4.3, §4.5, §5.1–5.3, §5.5, §5.6, §6.1 (calibration carries no uncertainty in any record), §6.3, §7.1, §8.1, §8.5, §8.6, §8.8.

**Statistics, not applied:**
- §5.4, §5.7–5.8, §7.2–7.5: the target makes no such claim.
- §10.2–10.5: evaluation of the module itself.
- `statistics.grim` and `statistics.percent`: the reported quantities are not means or proportions of whole-number counts.
- §8.7: the host configuration of the workers' sessions is unknown to me.

a2-mixb was read only by search for failed predicates.

# E. Counts

- **Findings:** 13. H: F1–F4. M: F5, F6, F7, F11. L: F8, F9, F10, F13. Table: F12.
- **Replacement LaTeX blocks:** 13.
- **My predicates:** 30 met, 0 failed (table rounding 8, steps 3, share 1, paired 6, cross 9, energy 2, offset 1). One process failure of mine (first run, exit 1), kept.
- **Manuscript numbers against records:** 0 discrepancies in value.
- **Attribution:** 2 discrepancies. The caption's ".086" and ".062" come from earlier runs; the table's runs give .0893(9) and .0611(4).
- **One number where the record has two:** 2 ("about −0.017"; "about 1 per cent").
- **Omitted negative or failed items:** 12 listed in section B, of which 9 matter to a reader.
- **Tests examined before the reported cross-lattice test:** about 22 × 2 extents × 2 forms in the first span, then 25 × 2 extents in the second.