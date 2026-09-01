# Data dictionary

## Common files

| Pattern | Description |
|---|---|
| `*_best_solution.csv` | Selected nominal optimum and its design variables, performance metrics, and cost |
| `*_population.csv` | Candidate population across optimizer generations |
| `*_pvt_metrics.csv` | Detailed process–voltage–temperature results for the selected design |
| `*_pvt_minmax_report.csv` | Minimum and maximum values extracted from the PVT sweep |
| `*_mcdata` | Headerless tab-separated Monte Carlo output retained in its original exported form |
| `setup.txt` | Design-variable bounds, targets, optimizer settings, PVT lists, Monte Carlo settings, and testbench parameters |
| `*_Report.pdf` | Human-readable nominal, Monte Carlo, and PVT summary |

The original Monte Carlo exports are deliberately left unchanged. Because the
`*_mcdata` files have no header row, use their accompanying PDF report and
`setup.txt` when interpreting columns.

## LC oscillator data

The oscillator best-solution and population tables contain device dimensions
and multiplicities followed by:

| Field | Meaning | Unit |
|---|---|---|
| `Fosc_Hz` | Oscillation frequency | Hz |
| `PD_W` | Power dissipation | W |
| `V1pk_V` | Fundamental differential peak voltage | V |
| `V1rms_V` | Fundamental differential RMS voltage | V |
| `PN_100k_dBc` | Phase noise at 100-kHz offset | dBc/Hz |
| `PN_1M_dBc` | Phase noise at 1-MHz offset | dBc/Hz |
| `FOM_100k` | Oscillator figure of merit at 100-kHz offset | dBc/Hz |
| `FOM_1M` | Oscillator figure of merit at 1-MHz offset | dBc/Hz |
| `cost` | Optimizer cost | dimensionless |

Additional oscillator exports:

| Pattern | Description |
|---|---|
| `*_transient_one_cycle.csv` | One steady-state oscillation cycle: time, X, Y, and differential voltage |
| `*_xray_trans_waveforms.csv` | Extended transient waveforms: time, X, Y, and differential voltage |

## RF–DC rectifier data

The rectifier best-solution and population tables contain device dimensions,
component multiplicities, load, and testbench settings followed by:

| Field | Meaning | Unit |
|---|---|---|
| `Area` | Estimated active area | m² |
| `VOUTMAX` | Maximum output voltage | V |
| `POUT_AVG` | Average output power | W |
| `PIN_AVG` | Average input power | W |
| `PCE` | Power-conversion efficiency | % |
| `PIDBM` | Input power | dBm |
| `DELTAVO` | Output ripple | V |
| `FOM1`–`FOM3` | Study-specific figures of merit | as defined in the paper/report |
| `cost` | Optimizer cost | dimensionless |

Additional rectifier exports:

| Pattern | Description |
|---|---|
| `*_param_sweep_metrics.csv` | RF-amplitude sweep and derived output/input/PCE/ripple metrics |
| `*_xray_s11_vs_freq_With_IMN.csv` | S11 versus frequency with the input matching network |
| `*_xray_s11_vs_freq_Without_IMN.csv` | S11 versus frequency without the input matching network |

## Naming convention

- `de_`: Differential Evolution
- `ga_`: Genetic Algorithm
- `hyb_`: Hybrid GA–DE optimization
- `mc`: Monte Carlo
- `pvt`: process–voltage–temperature
- `imn`: input matching network
