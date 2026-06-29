#!/usr/bin/env python3
"""Fetch Japan Trade Statistics rows from e-Stat CSV files."""

from __future__ import annotations

import argparse
import csv
import io
import json
import re
import sys
from dataclasses import asdict, dataclass
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


BASE_FILES_URL = "https://www.e-stat.go.jp/en/stat-search/files"
BASE_DOWNLOAD_URL = "https://www.e-stat.go.jp/stat-search/file-download"
TOUKEI = "00350300"
TSTAT = "000001013141"

MONTHS = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]

COUNTRIES = {
    "103": "Republic of Korea",
    "105": "People's Republic of China",
    "106": "Taiwan",
    "110": "Viet Nam",
    "113": "Malaysia",
    "118": "Indonesia",
    "123": "India",
    "204": "Denmark",
    "205": "United Kingdom",
    "206": "Ireland",
    "302": "Canada",
    "304": "United States of America",
    "305": "Mexico",
}

# Known e-Stat tclass pairs for tstat=000001013141. These are deliberately
# verified by CSV contents after discovery because UI labels can be ambiguous.
EXPORT_PAIRS = [
    ("000001013186", "000001013187"),
    ("000001013180", "000001013181"),
    ("000001013183", "000001013184"),
    ("000001013189", "000001013190"),
    ("000001013192", "000001013193"),
    ("000001013195", "000001013196"),
    ("000001013198", "000001013199"),
    ("000001013201", "000001013202"),
]

IMPORT_PAIRS = [
    ("000001013186", "000001013188"),
    ("000001013180", "000001013182"),
    ("000001013183", "000001013185"),
    ("000001013189", "000001013191"),
    ("000001013192", "000001013194"),
    ("000001013195", "000001013197"),
    ("000001013198", "000001013200"),
    ("000001013201", "000001013203"),
]


@dataclass
class MonthlyRow:
    month: str
    quantity2: int
    value_thousand_yen: int
    implied_yen_per_quantity2: float | None


@dataclass
class TradeRow:
    exp_or_imp: str
    year: str
    hs: str
    country_code: str
    country: str
    quantity_unit: str
    quantity2_year: int
    value_thousand_yen_year: int
    monthly: list[MonthlyRow]


@dataclass
class Result:
    source: str
    stat_inf_id: str
    direction: str
    requested_hs: str
    hs_match_mode: str
    requested_country: str | None
    value_unit: str
    commodity_confidence: str
    rows: list[TradeRow]


def fetch_text(url: str) -> str:
    req = Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://www.e-stat.go.jp/",
        },
    )
    with urlopen(req, timeout=30) as response:
        body = response.read()
        charset = response.headers.get_content_charset() or "utf-8"
        return body.decode(charset, errors="replace")


def iter_stat_ids(direction: str) -> Iterable[str]:
    pairs = IMPORT_PAIRS if direction == "import" else EXPORT_PAIRS
    seen: set[str] = set()

    for tclass1, tclass2 in pairs:
        url = (
            f"{BASE_FILES_URL}?page=1&layout=dataset&toukei={TOUKEI}"
            f"&tstat={TSTAT}&tclass1={tclass1}&tclass2={tclass2}"
            "&cycle_facet=cycle&data=1&metadata=1"
        )
        try:
            html = fetch_text(url)
        except (HTTPError, URLError, TimeoutError) as exc:
            print(f"warning: failed to discover candidates for {tclass1}/{tclass2}: {exc}", file=sys.stderr)
            continue
        for stat_id in re.findall(r"statInfId=(\d+)&fileKind=1", html):
            if stat_id not in seen:
                seen.add(stat_id)
                yield stat_id


def download_csv(stat_id: str) -> list[dict[str, str]]:
    url = f"{BASE_DOWNLOAD_URL}?statInfId={stat_id}&fileKind=1"
    text = fetch_text(url)
    if "Exp or Imp,Year,HS,Country" not in text[:200]:
        return []
    return list(csv.DictReader(io.StringIO(text)))


def clean(value: str | None) -> str:
    return (value or "").strip().strip("'").strip('"')


def parse_int(value: str | None) -> int:
    value = clean(value).replace(",", "")
    if not value:
        return 0
    return int(value)


def hs_matches(row_hs: str, requested_hs: str, match_mode: str) -> bool:
    if match_mode == "exact":
        return row_hs == requested_hs
    return row_hs.startswith(requested_hs)


def commodity_confidence(direction: str, requested_hs: str) -> str:
    if direction == "export" and requested_hs in {"282619", "282619900"}:
        return "proxy_bucket"
    if direction == "import" and requested_hs in {"282619", "282619090"}:
        return "proxy_bucket"
    return "direct_code"


def build_trade_row(raw: dict[str, str], include_empty_months: bool) -> TradeRow:
    monthly: list[MonthlyRow] = []
    for month in MONTHS:
        quantity = parse_int(raw.get(f"Quantity2-{month}"))
        value = parse_int(raw.get(f"Value-{month}"))
        if not include_empty_months and quantity == 0 and value == 0:
            continue
        implied = (value * 1000 / quantity) if quantity else None
        monthly.append(
            MonthlyRow(
                month=month,
                quantity2=quantity,
                value_thousand_yen=value,
                implied_yen_per_quantity2=implied,
            )
        )

    country_code = clean(raw.get("Country"))
    return TradeRow(
        exp_or_imp=clean(raw.get("Exp or Imp")),
        year=clean(raw.get("Year")),
        hs=clean(raw.get("HS")),
        country_code=country_code,
        country=COUNTRIES.get(country_code, f"Code_{country_code}" if country_code else ""),
        quantity_unit=clean(raw.get("Unit2")),
        quantity2_year=parse_int(raw.get("Quantity2-Year")),
        value_thousand_yen_year=parse_int(raw.get("Value-Year")),
        monthly=monthly,
    )


def find_rows(
    *,
    direction: str,
    requested_hs: str,
    match_mode: str,
    country: str | None,
    stat_inf_id: str | None,
    include_empty_months: bool,
) -> Result:
    candidates = [stat_inf_id] if stat_inf_id else iter_stat_ids(direction)
    attempted = 0

    for candidate in candidates:
        if not candidate:
            continue
        attempted += 1
        try:
            raw_rows = download_csv(candidate)
        except (HTTPError, URLError, TimeoutError) as exc:
            print(f"warning: failed to download {candidate}: {exc}", file=sys.stderr)
            continue

        rows: list[TradeRow] = []
        for raw in raw_rows:
            row_hs = clean(raw.get("HS"))
            row_country = clean(raw.get("Country"))
            if not hs_matches(row_hs, requested_hs, match_mode):
                continue
            if country and row_country != country:
                continue
            rows.append(build_trade_row(raw, include_empty_months))

        if rows:
            return Result(
                source="e-Stat Trade Statistics of Japan CSV",
                stat_inf_id=candidate,
                direction=direction,
                requested_hs=requested_hs,
                hs_match_mode=match_mode,
                requested_country=country,
                value_unit="thousand_yen",
                commodity_confidence=commodity_confidence(direction, requested_hs),
                rows=rows,
            )

    if attempted == 0:
        raise RuntimeError("No candidate statInfId values found from e-Stat.")

    country_clause = f" and country {country}" if country else ""
    raise RuntimeError(f"No rows found for HS {requested_hs}{country_clause}.")


def result_to_dict(result: Result) -> dict[str, object]:
    data = asdict(result)
    return data


def print_table(result: Result) -> None:
    print(f"source: {result.source}")
    print(f"stat_inf_id: {result.stat_inf_id}")
    print(f"direction: {result.direction}")
    print(f"requested_hs: {result.requested_hs} ({result.hs_match_mode})")
    if result.requested_country:
        country_name = COUNTRIES.get(result.requested_country, f"Code_{result.requested_country}")
        print(f"requested_country: {result.requested_country} {country_name}")
    print(f"value_unit: {result.value_unit}")
    print(f"commodity_confidence: {result.commodity_confidence}")
    print()

    for row in result.rows:
        print(
            f"{row.year} HS {row.hs} -> {row.country} ({row.country_code}) "
            f"annual {row.quantity2_year:,} {row.quantity_unit}, "
            f"{row.value_thousand_yen_year:,} thousand yen"
        )
        if not row.monthly:
            continue
        print("month,quantity2,value_thousand_yen,implied_yen_per_quantity2")
        for month in row.monthly:
            implied = (
                f"{month.implied_yen_per_quantity2:.2f}"
                if month.implied_yen_per_quantity2 is not None
                else ""
            )
            print(
                f"{month.month},{month.quantity2:,},"
                f"{month.value_thousand_yen:,},{implied}"
            )
        print()


def print_csv(result: Result) -> None:
    writer = csv.writer(sys.stdout)
    writer.writerow(
        [
            "stat_inf_id",
            "direction",
            "year",
            "hs",
            "country_code",
            "country",
            "month",
            "quantity_unit",
            "quantity2",
            "value_thousand_yen",
            "implied_yen_per_quantity2",
            "commodity_confidence",
        ]
    )
    for row in result.rows:
        for month in row.monthly:
            writer.writerow(
                [
                    result.stat_inf_id,
                    result.direction,
                    row.year,
                    row.hs,
                    row.country_code,
                    row.country,
                    month.month,
                    row.quantity_unit,
                    month.quantity2,
                    month.value_thousand_yen,
                    (
                        f"{month.implied_yen_per_quantity2:.6f}"
                        if month.implied_yen_per_quantity2 is not None
                        else ""
                    ),
                    result.commodity_confidence,
                ]
            )


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch Japan customs trade rows from e-Stat CSV files."
    )
    parser.add_argument("--direction", choices=["export", "import"], required=True)
    parser.add_argument("--hs", required=True, help="HS prefix or 9-digit Japan statistical code.")
    parser.add_argument("--country", help="Japan customs 3-digit country code, e.g. 103 for Korea.")
    parser.add_argument(
        "--match",
        choices=["auto", "exact", "prefix"],
        default="auto",
        help="Default auto uses exact for 9-digit codes and prefix otherwise.",
    )
    parser.add_argument("--stat-inf-id", help="Known e-Stat statInfId to bypass discovery.")
    parser.add_argument(
        "--include-empty-months",
        action="store_true",
        help="Keep months where quantity and value are both zero.",
    )
    parser.add_argument(
        "--monthly",
        action="store_true",
        help="Compatibility flag; monthly rows are always included when present.",
    )
    parser.add_argument("--format", choices=["table", "json", "csv"], default="table")
    return parser.parse_args(list(argv))


def validate_inputs(requested_hs: str, country: str | None) -> None:
    if not requested_hs.isdigit() or len(requested_hs) not in {2, 4, 6, 9}:
        raise ValueError("hs must be 2, 4, 6, or 9 digits for Japan customs queries.")
    if country and (not country.isdigit() or len(country) != 3):
        raise ValueError("country must be a 3-digit Japan customs country code.")


def main(argv: Iterable[str]) -> int:
    args = parse_args(argv)
    requested_hs = clean(args.hs)
    country = clean(args.country) if args.country else None
    try:
        validate_inputs(requested_hs, country)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    match_mode = args.match
    if match_mode == "auto":
        match_mode = "exact" if len(requested_hs) == 9 else "prefix"

    try:
        result = find_rows(
            direction=args.direction,
            requested_hs=requested_hs,
            match_mode=match_mode,
            country=country,
            stat_inf_id=args.stat_inf_id,
            include_empty_months=args.include_empty_months,
        )
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if args.format == "json":
        print(json.dumps(result_to_dict(result), ensure_ascii=False, indent=2))
    elif args.format == "csv":
        print_csv(result)
    else:
        print_table(result)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
