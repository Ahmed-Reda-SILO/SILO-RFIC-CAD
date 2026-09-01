#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate expected SILO files and structural consistency of CSV datasets."""

from __future__ import annotations

import csv
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OPTIMIZERS = ("DE", "GA", "HYB")
PREFIXES = {"DE": "de", "GA": "ga", "HYB": "hyb"}
REPORTS = {"DE": "DE_Report.pdf", "GA": "GA_Report.pdf", "HYB": "Hybrid_Report.pdf"}


def expected_files() -> list[Path]:
    files = [ROOT / "README.pdf", ROOT / "SILO_Overall_Performance_Summary.pdf"]
    for case, stem in (("LC_Oscillator", "lcoscillator"), ("RF_Rectifier", "rfrectifier")):
        for optimizer in OPTIMIZERS:
            prefix = PREFIXES[optimizer]
            base = ROOT / case / optimizer
            raw = base / "raw_data"
            files.extend(
                [
                    base / REPORTS[optimizer],
                    base / "setup.txt",
                    raw / f"{prefix}_{stem}_best_solution.csv",
                    raw / f"{prefix}_{stem}_population.csv",
                    raw / f"{prefix}_{stem}_pvt_metrics.csv",
                    raw / f"{prefix}_{stem}_pvt_minmax_report.csv",
                    raw / f"{prefix}_mcdata",
                ]
            )
            if case == "LC_Oscillator":
                files.extend(
                    [
                        raw / f"{prefix}_{stem}_transient_one_cycle.csv",
                        raw / f"{prefix}_{stem}_xray_trans_waveforms.csv",
                    ]
                )
            else:
                files.extend(
                    [
                        raw / f"{prefix}_{stem}_param_sweep_metrics.csv",
                        raw / f"{prefix}_{stem}_xray_s11_vs_freq_With_IMN.csv",
                        raw / f"{prefix}_{stem}_xray_s11_vs_freq_Without_IMN.csv",
                    ]
                )
    return files


def validate_csv(path: Path) -> list[str]:
    problems: list[str] = []
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.reader(handle)
        try:
            header = next(reader)
        except StopIteration:
            return [f"empty CSV: {path.relative_to(ROOT)}"]
        if not header or any(not field.strip() for field in header):
            problems.append(f"invalid header: {path.relative_to(ROOT)}")
        width = len(header)
        row_count = 0
        for line_number, row in enumerate(reader, start=2):
            row_count += 1
            if len(row) != width:
                problems.append(
                    f"row-width mismatch: {path.relative_to(ROOT)}:{line_number} "
                    f"({len(row)} fields; expected {width})"
                )
        if row_count == 0:
            problems.append(f"no data rows: {path.relative_to(ROOT)}")
    return problems


def validate_mcdata(path: Path) -> list[str]:
    rows = [line for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if len(rows) != 1000:
        return [f"Monte Carlo row count: {path.relative_to(ROOT)} has {len(rows)}; expected 1000"]
    widths = {len(line.split()) for line in rows}
    if len(widths) != 1:
        return [f"inconsistent Monte Carlo row widths: {path.relative_to(ROOT)}"]
    return []


def main() -> int:
    problems: list[str] = []
    required = expected_files()
    for path in required:
        if not path.is_file():
            problems.append(f"missing required file: {path.relative_to(ROOT)}")

    for path in sorted(ROOT.glob("**/*.csv")):
        problems.extend(validate_csv(path))
    for path in sorted(ROOT.glob("**/*_mcdata")):
        problems.extend(validate_mcdata(path))

    if problems:
        print("Repository validation FAILED")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print(
        "Repository validation PASSED: "
        f"{len(required)} required research files, "
        f"{len(list(ROOT.glob('**/*.csv')))} CSV files, and "
        f"{len(list(ROOT.glob('**/*_mcdata')))} Monte Carlo files checked."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
