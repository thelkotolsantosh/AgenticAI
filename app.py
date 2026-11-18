import argparse
import csv
from collections import Counter
from decimal import Decimal, InvalidOperation


def review(path):
    with open(path, encoding="utf-8-sig", newline="") as stream:
        rows = csv.DictReader(stream)
        required = {"vendor", "invoice", "amount"}
        if not required <= set(rows.fieldnames or []):
            raise ValueError("CSV needs vendor, invoice and amount columns.")
        records = list(rows)
    keys = [tuple((row[field] or "").strip().casefold() for field in ("vendor", "invoice"))
            for row in records]
    counts = Counter(keys)
    for line, (row, key) in enumerate(zip(records, keys), start=2):
        flags = []
        if not all(key):
            flags.append("missing vendor or invoice")
        elif counts[key] > 1:
            flags.append("duplicate vendor and invoice")
        try:
            amount = Decimal(row["amount"] or "")
            if not amount.is_finite() or amount <= 0:
                flags.append("check amount")
        except InvalidOperation:
            flags.append("check amount")
        if flags:
            yield line, flags


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Route invoice exceptions to a human reviewer using local rules.")
    parser.add_argument("invoices")
    args = parser.parse_args()
    try:
        issues = list(review(args.invoices))
    except (OSError, ValueError, csv.Error) as error:
        parser.error(str(error))
    for line, flags in issues:
        print(f"Record {line-1}: {', '.join(flags)}")
    print(f"Records for review: {len(issues)}")
