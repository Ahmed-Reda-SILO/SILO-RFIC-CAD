# SILO: Spectre-in-the-Loop RFIC Design Data

Supplementary data and reports for the paper:

> **SILO: A Spectre-in-the-Loop CAD Framework for Variability-Aware RFIC Design**

This repository documents two transistor-level RFIC design case studies—a
5-GHz LC oscillator and a 920-MHz RF–DC rectifier—optimized using Differential
Evolution (DE), a Genetic Algorithm (GA), and a Hybrid GA–DE strategy. It
contains the reported nominal solutions, complete optimization populations,
PVT and Monte Carlo results, circuit-specific waveform or S-parameter data,
simulation setup files, and summary reports.

## Highlights

- Cadence Spectre transistor-level results in a 180-nm CMOS technology
- Direct DE, GA, and Hybrid comparison under consistent simulation conditions
- Five process corners: TT, SS, FF, SF, and FS
- Temperature range from -40 °C to 85 °C
- Oscillator supply sweep from 1.62 V to 1.98 V
- 1,000-sample Monte Carlo analysis for each optimized design
- Raw CSV datasets for independent plotting and secondary analysis

## Selected nominal results

### 5-GHz LC oscillator

| Optimizer | Frequency (GHz) | Power (mW) | Peak output (V) | PN @ 1 MHz (dBc/Hz) | FoM (dBc/Hz) |
|---|---:|---:|---:|---:|---:|
| DE | 5.080616 | 9.336126 | 1.394506 | -119.5082 | -183.9249 |
| GA | 4.995913 | 9.147608 | 1.443161 | -119.0940 | -183.4532 |
| Hybrid | 5.060124 | 3.809193 | 1.485755 | -116.2680 | -184.5429 |

### 920-MHz RF–DC rectifier

| Optimizer | PCE (%) | Output voltage (V) | Input power (dBm) | Area (µm²) | Dynamic range (dB) | Sensitivity (dBm) |
|---|---:|---:|---:|---:|---:|---:|
| DE | 92.7231 | 0.503295 | -28.8589 | 641 | 22.1099 | -16.97 |
| GA | 90.6913 | 0.500417 | -28.7609 | 841 | 22.4218 | -16.05 |
| Hybrid | 94.9870 | 0.522454 | -28.9783 | 634 | 23.0500 | -18.58 |

Values above are transcribed from
[`SILO_Overall_Performance_Summary.pdf`](SILO_Overall_Performance_Summary.pdf).
Use the raw datasets for numerical processing.

## Repository structure

```text
.
├── LC_Oscillator/
│   ├── DE/
│   ├── GA/
│   └── HYB/
├── RF_Rectifier/
│   ├── DE/
│   ├── GA/
│   └── HYB/
├── scripts/
│   ├── summarize_best_solutions.py
│   └── validate_repository.py
├── CITATION.cff
├── DATA_DICTIONARY.md
├── REPRODUCIBILITY.md
├── README.pdf
└── SILO_Overall_Performance_Summary.pdf
```

Each optimizer directory contains:

- a PDF report with nominal, Monte Carlo, and PVT results;
- `setup.txt`, recording optimizer and Spectre testbench settings; and
- `raw_data/`, containing the underlying optimization and verification data.

See [`DATA_DICTIONARY.md`](DATA_DICTIONARY.md) for a file-by-file guide.

## Quick start

The helper scripts use only the Python standard library (Python 3.9 or later
is recommended).

Validate the expected repository structure and CSV row consistency:

```bash
python scripts/validate_repository.py
```

Print a compact table of the six nominal best solutions:

```bash
python scripts/summarize_best_solutions.py
```

The CSV files can also be opened directly in MATLAB, Python/pandas, R, or a
spreadsheet application.

## Reproducibility scope

This release supports inspection, independent replotting, and secondary
analysis of the reported results. Re-running the proprietary transistor-level
simulations additionally requires Cadence Spectre, the licensed 180-nm CMOS
PDK and device models, circuit netlists/testbenches, and the SILO optimization
implementation. Those proprietary or implementation files are not part of
the supplied supplementary package. See
[`REPRODUCIBILITY.md`](REPRODUCIBILITY.md) for details.

## Citation

Please cite the accompanying paper when using this material. GitHub and other
CFF-aware services can read the repository metadata from
[`CITATION.cff`](CITATION.cff).

## Contact

Ahmed Reda Mohamed  
Interdisciplinary Research Center for Communication Systems and Sensing  
King Fahd University of Petroleum and Minerals (KFUPM)  
[ahmed.mohamed@kfupm.edu.sa](mailto:ahmed.mohamed@kfupm.edu.sa)

## License

The research data, reports, and documentation are licensed under the
[Creative Commons Attribution 4.0 International License](LICENSE-DATA.md).
The helper scripts in `scripts/` are licensed under the
[MIT License](LICENSE-CODE.md).
