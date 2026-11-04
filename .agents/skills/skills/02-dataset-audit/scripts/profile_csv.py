#!/usr/bin/env python3
"""Read-only, dependency-free CSV/TSV structure and quality sample summary.

No raw values or rows are printed. Defaults to at most 100,000 data rows.
"""
from __future__ import annotations
import argparse
import csv
import json
import math
from collections import Counter
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Read-only CSV/TSV data quality snapshot")
    parser.add_argument("file", type=Path)
    parser.add_argument("--max-rows", type=int, default=100_000)
    parser.add_argument("--encoding", default="utf-8-sig")
    args = parser.parse_args()
    if args.max_rows < 1:
        parser.error("--max-rows must be positive")
    if not args.file.is_file():
        parser.error("file not found")

    with args.file.open("r", encoding=args.encoding, newline="") as f:
        preview = f.read(8192)
        f.seek(0)
        try:
            dialect = csv.Sniffer().sniff(preview, delimiters=",\t;|")
        except csv.Error:
            dialect = csv.excel_tab if args.file.suffix.lower() == ".tsv" else csv.excel
        reader = csv.reader(f, dialect)
        header = next(reader, [])
        if not header:
            print(json.dumps({"file": str(args.file), "error": "empty or headerless file"}, ensure_ascii=False))
            return 2
        missing = Counter()
        num_count = Counter()
        num_min = {}
        num_max = {}
        nonnum_count = Counter()
        distinct = [set() for _ in header]
        dup_rows = 0
        seen = set()
        malformed = 0
        read_rows = 0
        truncated = False
        for row in reader:
            if read_rows >= args.max_rows:
                truncated = True
                break
            read_rows += 1
            if len(row) != len(header):
                malformed += 1
            normalized = tuple((row[i].strip() if i < len(row) else "") for i in range(len(header)))
            if normalized in seen:
                dup_rows += 1
            else:
                seen.add(normalized)
            for i, value in enumerate(normalized):
                if len(distinct[i]) < 100_000:
                    distinct[i].add(value)
                if not value or value.lower() in ("nan", "null", "none", "na", "n/a"):
                    missing[i] += 1
                    continue
                try:
                    number = float(value)
                    if not math.isfinite(number):
                        raise ValueError("non-finite")
                    num_count[i] += 1
                    num_min[i] = min(num_min.get(i, number), number)
                    num_max[i] = max(num_max.get(i, number), number)
                except ValueError:
                    nonnum_count[i] += 1

    summary = {
        "file": str(args.file), "sampled_rows": read_rows, "sampling_note": "first N rows, not random",
        "truncated_at_max_rows": truncated, "columns": len(header),
        "duplicate_rows_in_sample": dup_rows, "malformed_row_lengths": malformed,
        "fields": [
            {"column_index": i, "name": name, "missing_count": missing[i],
             "missing_pct": round(100 * missing[i] / read_rows, 2) if read_rows else None,
             "unique_values_in_sample_at_most_100k": len(distinct[i]),
             "numeric_count": num_count[i], "nonnumeric_count": nonnum_count[i],
             "numeric_min": num_min.get(i), "numeric_max": num_max.get(i)}
            for i, name in enumerate(header)
        ],
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
