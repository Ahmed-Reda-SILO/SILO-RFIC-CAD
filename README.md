<div align="center">

# ⚡ SILO

### Spectre-in-the-Loop variability-aware CAD for RFIC design

[![Research Artifact](https://img.shields.io/badge/research-artifact-1261A0?style=for-the-badge)](#-overview)
[![CMOS Technology](https://img.shields.io/badge/CMOS-180%20nm-18794E?style=for-the-badge)](#-study-at-a-glance)
[![Cadence Spectre](https://img.shields.io/badge/simulator-Cadence%20Spectre-B64B2A?style=for-the-badge)](#-simulation-and-verification-space)
[![Optimizers](https://img.shields.io/badge/optimizers-DE%20%7C%20GA%20%7C%20Hybrid-6F42C1?style=for-the-badge)](#-optimization-strategies)
[![Monte Carlo](https://img.shields.io/badge/Monte%20Carlo-1000%20samples-8A4B08?style=for-the-badge)](#-variation-aware-data)
[![Data License](https://img.shields.io/badge/data-CC%20BY%204.0-2F7D32?style=for-the-badge)](LICENSE-DATA.md)

**[📊 Open the Overall Performance Summary](SILO_Overall_Performance_Summary.pdf)**

[Data dictionary](DATA_DICTIONARY.md) · [Reproducibility statement](REPRODUCIBILITY.md) · [Citation metadata](CITATION.cff)

</div>

---

## 🔬 Overview

**SILO** is a Spectre-in-the-Loop CAD framework developed for variability-aware RFIC design optimization. This repository provides the supplementary research artifact supporting the paper:

> **“SILO: A Spectre-in-the-Loop CAD Framework for Variability-Aware RFIC Design”**

The release brings together the optimization and verification evidence for two transistor-level RFIC case studies: a **5-GHz LC oscillator** and a **920-MHz RF–DC rectifier**. Differential Evolution (DE), a Genetic Algorithm (GA), and a Hybrid GA–DE strategy are evaluated under consistent Cadence Spectre conditions.

The repository includes selected solutions, complete optimization populations, 1,000-sample Monte Carlo exports, PVT results, transient or S-parameter datasets, simulation setup files, and technical reports.

> [!IMPORTANT]
> This is the paper's **supplementary data and reports repository**. It supports inspection, independent plotting, statistical analysis, and verification of reported values. A complete transistor-level rerun additionally requires the proprietary 180-nm PDK, Cadence Spectre environment, circuit netlists/testbenches, and the SILO implementation, which are not distributed in this release.

## ✨ Why this repository matters

- 🔁 **Consistent comparison:** DE, GA, and Hybrid optimization use aligned design objectives and simulation conditions.
- 🧬 **Variation-aware evidence:** every selected solution is evaluated using PVT sweeps and 1,000 Monte Carlo samples.
- 📡 **Two RFIC design classes:** the release covers both an active RF oscillator and a passive RF energy-harvesting rectifier.
- 📂 **Traceable raw data:** optimization populations and verification outputs are available for independent analysis.
- 📈 **Publication-ready reports:** consolidated and optimizer-specific PDF reports summarize the primary findings.
- 🧪 **Reproducibility support:** setup files, a data dictionary, validation scripts, and citation metadata are included.

## 🧭 Study at a glance

| Case study | Target operation | Main objectives | Variation-aware verification | Additional evidence |
|---|---:|---|---|---|
| LC oscillator | 5 GHz | Frequency, power, output swing, phase noise, FoM | Five process corners, three supply voltages, five temperatures, 1,000 MC samples | One-cycle and extended transient waveforms |
| RF–DC rectifier | 920 MHz | PCE, output voltage, input power, ripple, area | Five process corners, five temperatures, 1,000 MC samples | RF-amplitude sweeps and S11 with/without IMN |

## 🧠 Optimization strategies

| Strategy | Role in the study |
|---|---|
| **DE** | Continuous global search using mutation, crossover, and selection |
| **GA** | Population-based exploration using crossover and mutation |
| **Hybrid GA–DE** | GA exploration followed by DE refinement within the defined optimization budget |

Optimizer-specific bounds, targets, penalties, population sizes, and generation budgets are recorded in each `setup.txt` file.

## 🏆 Headline nominal results

### 5-GHz LC oscillator

| Optimizer | Frequency (GHz) | Power (mW) | Peak output (V) | PN @ 1 MHz (dBc/Hz) | FoM (dBc/Hz) |
|---|---:|---:|---:|---:|---:|
| DE | 5.080616 | 9.336126 | 1.394506 | **−119.5082** | −183.9249 |
| GA | 4.995913 | 9.147608 | 1.443161 | −119.0940 | −183.4532 |
| **Hybrid** | **5.060124** | **3.809193** | **1.485755** | −116.2680 | **−184.5429** |

> [!NOTE]
> The Hybrid solution achieves approximately **58–59% lower nominal power** than the DE and GA solutions while providing the best nominal FoM among the three reported solutions.

### 920-MHz RF–DC rectifier

| Optimizer | PCE (%) | Output voltage (V) | Input power (dBm) | Area (µm²) | Dynamic range (dB) | Sensitivity (dBm) |
|---|---:|---:|---:|---:|---:|---:|
| DE | 92.7231 | 0.503295 | −28.8589 | 641 | 22.1099 | −16.97 |
| GA | 90.6913 | 0.500417 | −28.7609 | 841 | 22.4218 | −16.05 |
| **Hybrid** | **94.9870** | **0.522454** | **−28.9783** | **634** | **23.0500** | **−18.58** |

> [!NOTE]
> The Hybrid solution provides the highest nominal PCE, the smallest estimated area, the widest dynamic range, and the best sensitivity among the three reported solutions.

All values are transcribed from [`SILO_Overall_Performance_Summary.pdf`](SILO_Overall_Performance_Summary.pdf). Use the raw datasets for numerical processing and the optimizer-specific reports for detailed interpretation.

## 🧬 Variation-aware data

Each optimizer directory provides:

| Data product | Purpose |
|---|---|
| Best solution | Records the selected design variables, nominal metrics, and optimizer cost |
| Population history | Preserves evaluated candidate designs across generations |
| PVT metrics | Reports performance across the defined process, voltage, and temperature space |
| PVT extrema | Identifies minimum and maximum metric values and their operating corners |
| Monte Carlo data | Contains the original 1,000-sample statistical export |
| Technical report | Summarizes nominal, Monte Carlo, PVT, yield, and runtime results |

Circuit-specific exports additionally provide oscillator transient waveforms and rectifier amplitude/S11 sweeps. See the [`DATA_DICTIONARY.md`](DATA_DICTIONARY.md) for field definitions and file-pattern guidance.

## 🌡️ Simulation and verification space

| Parameter | LC oscillator | RF–DC rectifier |
|---|---|---|
| CMOS technology | 180 nm | 180 nm |
| Simulator | Cadence Spectre | Cadence Spectre |
| Nominal operating frequency | 5 GHz | 920 MHz |
| Nominal temperature | 27 °C | 27 °C |
| Process corners | TT, SS, FF, SF, FS | TT, SS, FF, SF, FS |
| Temperature points | −40, 0, 27, 70, 85 °C | −40, 0, 27, 70, 85 °C |
| Supply points | 1.62, 1.80, 1.98 V | 0-V external DC supply |
| Monte Carlo samples | 1,000 per optimizer | 1,000 per optimizer |


## 📁 Repository structure

```text
SILO-RFIC-CAD/
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
├── LICENSE-CODE.md
├── LICENSE-DATA.md
├── README.md
├── README.pdf
├── REPRODUCIBILITY.md
└── SILO_Overall_Performance_Summary.pdf
```

Each `DE`, `GA`, or `HYB` directory contains an optimizer-specific PDF report, `setup.txt`, and a `raw_data/` directory.

## 🔐 Reproducibility and responsible reuse

- Original research datasets are retained without numerical rewriting.
- The validation script checks the expected structure, CSV row consistency, and Monte Carlo sample counts.
- The directory name `HYB` is used consistently for the Hybrid optimizer.
- Derived figures or tables should identify the source files and record the repository commit used.
- Proprietary foundry files, PDK models, simulator installation data, and credentials must not be redistributed.
- The interpretation boundary and rerun requirements are detailed in [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md).

## 📚 How to cite

If you use the SILO datasets, reports, or helper scripts in academic work, please cite the accompanying paper and this research artifact.

### IEEE reference format

> A. R. Mohamed, “SILO: Spectre-in-the-Loop RFIC Design Data,” GitHub repository, Sep. 2026. [Online]. Available: https://github.com/Ahmed-Reda-SILO/SILO-RFIC-CAD. Accessed: Sep. 1, 2026.

### IEEEtran LaTeX format

```latex
\bibitem{SILOData}
A. R. Mohamed, ``SILO: Spectre-in-the-Loop RFIC Design Data,''
GitHub repository, Sep. 2026. [Online]. Available:
\url{https://github.com/Ahmed-Reda-SILO/SILO-RFIC-CAD}.
Accessed: Sep. 1, 2026.
```

### BibTeX format

```bibtex
@misc{Mohamed2026SILOData,
  author       = {Ahmed Reda Mohamed},
  title        = {{SILO: Spectre-in-the-Loop RFIC Design Data}},
  year         = {2026},
  month        = sep,
  note         = {GitHub repository, accessed Sep. 1, 2026},
  howpublished = {GitHub repository},
  url          = {https://github.com/Ahmed-Reda-SILO/SILO-RFIC-CAD}
}
```

Machine-readable citation metadata are provided in [`CITATION.cff`](CITATION.cff).

## 👨‍🔬 Author

**Dr. Ahmed Reda Mohamed, Member, IEEE**<br>
Postdoctoral Fellow, Interdisciplinary Research Center for Communication Systems and Sensing (IRC-CSS)<br>
King Fahd University of Petroleum and Minerals (KFUPM), Dhahran, Saudi Arabia

Project profile: [Ahmed-Reda-SILO](https://github.com/Ahmed-Reda-SILO)

## 📄 License

- Research data, reports, and documentation: [CC BY 4.0](LICENSE-DATA.md)
- Python helper scripts: [MIT License](LICENSE-CODE.md)

---

<div align="center">

Developed for transparent, variability-aware RFIC design optimization and reproducible research. ⚡📡

</div>
