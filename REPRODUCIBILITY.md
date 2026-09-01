# Reproducibility statement

## Included

This repository contains the outputs supplied with the SILO manuscript:

- nominal best solutions and full optimizer populations;
- detailed PVT data and extracted extrema;
- 1,000-sample Monte Carlo exports;
- oscillator transient waveforms;
- rectifier amplitude sweeps and S11 sweeps;
- optimizer/testbench setup files; and
- circuit-level and cross-optimizer PDF reports.

These materials enable numerical inspection, independent plotting, checking
of tabulated values, and secondary statistical analysis.

## Simulation conditions recorded in the package

| Item | LC oscillator | RF–DC rectifier |
|---|---|---|
| CMOS technology | 180 nm | 180 nm |
| Nominal frequency | 5 GHz | 920 MHz |
| Nominal temperature | 27 °C | 27 °C |
| Process corners | TT, SS, FF, SF, FS | TT, SS, FF, SF, FS |
| Temperature points | -40, 0, 27, 70, 85 °C | -40, 0, 27, 70, 85 °C |
| Supply points | 1.62, 1.80, 1.98 V | 0 V external DC supply |
| Monte Carlo samples | 1,000 | 1,000 |

Optimizer-specific population sizes, generation budgets, search bounds,
targets, and penalties are recorded in each `setup.txt` file.

## Required for a complete simulation rerun

A complete regeneration of the transistor-level results additionally requires:

1. Cadence Spectre and the corresponding simulation environment;
2. the licensed 180-nm CMOS PDK and statistical device models;
3. circuit schematics or netlists and verification testbenches; and
4. the SILO optimization implementation and its simulator interface.

These files were not present in the supplied supplementary archive and are not
reconstructed in this repository. Consequently, the current release should be
described as a **supplementary data and reports repository**, not a fully
executable artifact.

## Recommended verification workflow

1. Run `python scripts/validate_repository.py`.
2. Run `python scripts/summarize_best_solutions.py` and compare the output with
   `SILO_Overall_Performance_Summary.pdf`.
3. Use the optimizer-specific PDF report for primary interpretation.
4. Use the raw CSV data to regenerate plots or perform additional analysis.
5. Record the repository commit identifier in any derived work.

The raw research files are preserved without numerical rewriting. The only
directory normalization made for repository consistency is the use of `HYB`
for the Hybrid optimizer in both case studies.
