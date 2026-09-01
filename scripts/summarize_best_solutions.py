#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Print selected nominal metrics from the six best-solution CSV files."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_one(relative_path: str) -> dict[str, str]:
    with (ROOT / relative_path).open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 1:
        raise ValueError(f"Expected one data row in {relative_path}, found {len(rows)}")
    return rows[0]


def format_table(headers: list[str], rows: list[list[str]]) -> str:
    widths = [len(item) for item in headers]
    for row in rows:
        widths = [max(width, len(item)) for width, item in zip(widths, row)]
    line = "  ".join(item.ljust(width) for item, width in zip(headers, widths))
    rule = "  ".join("-" * width for width in widths)
    body = ["  ".join(item.ljust(width) for item, width in zip(row, widths)) for row in rows]
    return "\n".join([line, rule, *body])


def main() -> None:
    oscillator_rows: list[list[str]] = []
    rectifier_rows: list[list[str]] = []

    for optimizer, prefix in (("DE", "de"), ("GA", "ga"), ("Hybrid", "hyb")):
        osc = read_one(
            f"LC_Oscillator/{'HYB' if optimizer == 'Hybrid' else optimizer}/raw_data/"
            f"{prefix}_lcoscillator_best_solution.csv"
        )
        oscillator_rows.append(
            [
                optimizer,
                f"{float(osc['Fosc_Hz']) / 1e9:.6f}",
                f"{float(osc['PD_W']) * 1e3:.6f}",
                f"{float(osc['PN_1M_dBc']):.4f}",
                f"{float(osc['FOM_1M']):.4f}",
            ]
        )

        rec = read_one(
            f"RF_Rectifier/{'HYB' if optimizer == 'Hybrid' else optimizer}/raw_data/"
            f"{prefix}_rfrectifier_best_solution.csv"
        )
        rectifier_rows.append(
            [
                optimizer,
                f"{float(rec['PCE']):.4f}",
                f"{float(rec['VOUTMAX']):.6f}",
                f"{float(rec['PIDBM']):.4f}",
                f"{float(rec['Area']) * 1e12:.3f}",
            ]
        )

    print("LC oscillator")
    print(format_table(["Optimizer", "Fosc_GHz", "PD_mW", "PN_1M", "FOM_1M"], oscillator_rows))
    print("\nRF-DC rectifier")
    print(format_table(["Optimizer", "PCE_pct", "VOUT_V", "PIN_dBm", "Area_um2"], rectifier_rows))


if __name__ == "__main__":
    main()
