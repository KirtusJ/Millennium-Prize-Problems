# Supplementary material

For the paper *Spectral criteria and conditional infrared estimates for four-dimensional lattice Yang–Mills theory* (Kirtus Justus, 24 November 2026), part of the research program [From Prephysical Hypotheses to Physical Models](https://github.com/KirtusJ/From-Prephysical-Hypotheses-to-Physical-Models).

- Reading copy: [`Spectral criteria and conditional infrared estimates for four-dimensional lattice Yang-Mills theory.pdf`](Spectral%20criteria%20and%20conditional%20infrared%20estimates%20for%20four-dimensional%20lattice%20Yang-Mills%20theory.pdf) (SHA-256 `b9f1d7c7b5df1bf8c9bd36a8866bb589cfac156e60b202ab82c25d0d8e4a5385`)
- Source: [`source/main.tex`](source/main.tex) (SHA-256 `f827ca65ff7caf8316811da80a4d5f806f7ee63a7b1bb88ad20b389d333af3db`) with [`source/preamble.tex`](source/preamble.tex); three passes of `pdflatex`.
- The paper does not prove a mass gap and has not been peer reviewed.

The paper cites the items below as "Supplement S*n*". Locations are relative to this folder. A digest is given for single files; folders carry their own records.

| Item | Content | Location | SHA-256 (single files) |
|---|---|---|---|
| S1 | Sampling programs (Rust), digests, seeds and commands | [`supplement/S1-sampling-programs/`](supplement/S1-sampling-programs/) |  |
| S2 | Local quotients on frozen backgrounds | [`supplement/S2-local-quotient/first-run/`](supplement/S2-local-quotient/first-run/)<br>[`supplement/S2-local-quotient/nested-spans/`](supplement/S2-local-quotient/nested-spans/) |  |
| S3 | Single-mark runs on displaced backgrounds and the second reduction | [`supplement/S3-displaced-backgrounds/side-6/`](supplement/S3-displaced-backgrounds/side-6/)<br>[`supplement/S3-displaced-backgrounds/side-8/`](supplement/S3-displaced-backgrounds/side-8/)<br>[`supplement/S3-displaced-backgrounds/other-couplings/`](supplement/S3-displaced-backgrounds/other-couplings/)<br>[`supplement/S3-displaced-backgrounds/second-reduction/`](supplement/S3-displaced-backgrounds/second-reduction/) |  |
| S4 | Time carry-over run (no result file was kept) | [`supplement/S4-time-carry-over/`](supplement/S4-time-carry-over/) |  |
| S5 | Cross-lattice runs, per-stream archive, coefficient vector of the reported test, reproduction recipe | [`supplement/S5-cross-lattice/first-study/`](supplement/S5-cross-lattice/first-study/)<br>[`supplement/S5-cross-lattice/second-study/`](supplement/S5-cross-lattice/second-study/)<br>[`supplement/S5-cross-lattice/second-study/results.tgz`](supplement/S5-cross-lattice/second-study/results.tgz)<br>[`supplement/S5-cross-lattice/second-study/frozen_vector_Z_ratio_opt.json`](supplement/S5-cross-lattice/second-study/frozen_vector_Z_ratio_opt.json)<br>[`supplement/S10-review-records/quality-review/f2/REPRODUCE.md`](supplement/S10-review-records/quality-review/f2/REPRODUCE.md)<br>[`supplement/S10-review-records/quality-review/scripts/reproduce_f2.py`](supplement/S10-review-records/quality-review/scripts/reproduce_f2.py) | `914fc35fa496bb433362b1378b972032c40ed1e67c4732c45e823d7d811b5795` results.tgz<br>`b542495cb7dc4c6a70c29b7ab41b257f12b867040da752fdc333264c7576bac2` frozen_vector_Z_ratio_opt.json<br>`1e47ae3a76f4fae21b2b027dc871c696e56883ddc8125e2e95bd4221d56c8ef7` REPRODUCE.md<br>`3a818c79400982d858a8b124042f22cef606be56eab23f83e2e4f0e4e3493b63` reproduce_f2.py |
| S6 | Calibration of the matched couplings (methods, programs and results; the raw sample archive is not copied here) | [`supplement/S6-coupling-calibration/`](supplement/S6-coupling-calibration/) |  |
| S7 | Lean files, statement and file digests | [`supplement/S7-lean/refinement-inequality/Inheritance.lean`](supplement/S7-lean/refinement-inequality/Inheritance.lean)<br>[`supplement/S7-lean/haar.lean`](supplement/S7-lean/haar.lean)<br>[`supplement/S7-lean/LEAN_PINS.md`](supplement/S7-lean/LEAN_PINS.md) | `74e9337dd18a9095754967635c18817780679eed46c3d1e8f8ea5634114ddf2b` Inheritance.lean<br>`47ff4a24b0fb9dae1d84b6592eb658113c9fd763ae4e7ce2a744586d3d0f2eec` haar.lean<br>`9de04f51ff9377a489ce8ee241ef3c4afe80e997a7d159b1f87f440cb92ae742` LEAN_PINS.md |
| S8 | Working notes: source derivations of Theorems 1.2 and 1.3, the bound of the transfer form by local losses, strong-coupling estimates | [`supplement/S8-source-derivations/inheritance.md`](supplement/S8-source-derivations/inheritance.md)<br>[`supplement/S8-source-derivations/return.md`](supplement/S8-source-derivations/return.md)<br>[`supplement/S8-source-derivations/bound-by-local-losses/`](supplement/S8-source-derivations/bound-by-local-losses/) | `462dfbe4f0cc706adf9d3d80d668124f43d53c2d246f607b131881d083070206` inheritance.md<br>`9e0161065ff426cbc3e626fa8fcf89054ca0ebf410df3d7177ca8a295cfa8579` return.md |
| S9 | Working notes: related hypotheses on the centre-neutral space | [`supplement/S9-related-hypotheses/`](supplement/S9-related-hypotheses/) |  |
| S10 | Records of the internal reviews of the paper and their test programs | [`supplement/S10-review-records/`](supplement/S10-review-records/) |  |

## Reading the records

The items are working records and are kept as they were written. Three things follow from that.

- **Names.** The records refer to the contributing AI systems by the project's working labels. Labels beginning with `Z` denote sessions of Claude (Anthropic); labels beginning with `G`, `A`, `B` or `C` followed by a digit denote sessions of OpenAI Codex; `GPTAuditor` labels denote sessions of OpenAI GPT models used as reviewers. The paper names the systems and not the labels.
- **Paths.** Some records quote the folder names and machine paths that were in use when they were written. The table above gives the present locations.
- **S6, S8 and S9** are copies, made on 24 November 2026, of working notes that are maintained elsewhere in this repository (`yang-mills/`); the copies are what the paper cites.

Not stored: the result files of the time carry-over run (S4), and the per-stream data behind Table 3 of the paper (S2), which are regenerated from the recorded seeds; across rebuilds of the sampler this reproduces them statistically, not byte for byte.
