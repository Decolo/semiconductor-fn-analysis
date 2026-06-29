#!/usr/bin/env python3
"""Build China Customs Statistics query URLs."""

from __future__ import annotations

import argparse
import json
import sys
from urllib.parse import urlencode


RESULT_BASE = "http://stats.customs.gov.cn/queryData/queryDataList"
FORM_BASE = "http://stats.customs.gov.cn/queryData/queryDataByWhere"

COUNTRY_CODES = {
    "japan": "116",
    "jp": "116",
    "116": "116",
    "korea": "133",
    "south-korea": "133",
    "south korea": "133",
    "kr": "133",
    "133": "133",
}


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build official China Customs query URLs for CDP-assisted use."
    )
    parser.add_argument("--hs", required=True, help="HS/customs code, e.g. 28261930.")
    parser.add_argument("--direction", choices=["export", "import"], required=True)
    parser.add_argument("--year", type=int, required=True)
    parser.add_argument("--start-month", type=int, required=True)
    parser.add_argument("--end-month", type=int, required=True)
    parser.add_argument(
        "--breakdown",
        choices=["country", "province"],
        default="country",
        help="country uses ORIGIN_COUNTRY; province uses TRADE_CO_PORT.",
    )
    parser.add_argument(
        "--country",
        help="Country name/code for country breakdown, e.g. japan, korea, 116, 133. Omit to list all.",
    )
    parser.add_argument("--currency", default="usd")
    parser.add_argument("--page", type=int, default=1)
    parser.add_argument(
        "--current-start-time",
        help="Optional platform active-window YYYYMM value. Omit unless copied from the live form/page.",
    )
    parser.add_argument(
        "--current-end-time",
        help="Optional platform active-window YYYYMM value. Omit unless copied from the live form/page.",
    )
    parser.add_argument(
        "--current-recent-time",
        help="Optional platform active-window YYYYMM value. Omit unless copied from the live form/page.",
    )
    parser.add_argument(
        "--current-date-by-source",
        help="Optional platform active-window YYYYMM value. Omit unless copied from the live form/page.",
    )
    parser.add_argument(
        "--output",
        choices=["url", "json"],
        default="url",
        help="Print a URL or JSON with form/result URLs and parameters.",
    )
    parser.add_argument(
        "--url-kind",
        choices=["form", "result"],
        default="form",
        help="Default is form because reliable use requires the CAPTCHA-assisted form workflow.",
    )
    return parser.parse_args(argv)


def validate(args: argparse.Namespace) -> None:
    if not (1 <= args.start_month <= 12 and 1 <= args.end_month <= 12):
        raise ValueError("start-month and end-month must be 1-12.")
    if args.start_month > args.end_month:
        raise ValueError("start-month must be <= end-month.")
    if not args.hs.isdigit():
        raise ValueError("hs must contain digits only.")
    if args.breakdown == "province" and args.country:
        raise ValueError("province breakdown leaves country empty; do not pass --country.")


def normalize_country(country: str | None) -> str:
    if not country:
        return ""
    key = country.strip().lower()
    if key in COUNTRY_CODES:
        return COUNTRY_CODES[key]
    raw = country.strip()
    if raw.isdigit():
        return raw
    raise ValueError(
        "unknown country alias. Use a numeric China customs code or one of: "
        "japan, jp, 116, korea, south-korea, south korea, kr, 133."
    )


def build_params(args: argparse.Namespace) -> dict[str, str]:
    direction = "0" if args.direction == "export" else "1"
    outer_field2 = "TRADE_CO_PORT" if args.breakdown == "province" else "ORIGIN_COUNTRY"
    outer_value2 = "" if args.breakdown == "province" else normalize_country(args.country)

    params = {
        "pageNum": str(args.page),
        "codeLength": str(len(args.hs)),
        "selectTableState": "1",
        "orderType": "CODE ASC DEFAULT",
        "iEType": direction,
        "currencyType": args.currency,
        "year": str(args.year),
        "startMonth": str(args.start_month),
        "endMonth": str(args.end_month),
        "monthFlag": "1",
        "outerField1": "CODE_TS",
        "outerValue1": args.hs,
        "outerField2": outer_field2,
        "outerValue2": outer_value2,
    }
    optional_current = {
        "currentStartTime": args.current_start_time,
        "currentEndTime": args.current_end_time,
        "currentRecentTime": args.current_recent_time,
        "currentDateBySource": args.current_date_by_source,
    }
    for key, value in optional_current.items():
        if value:
            params[key] = value
    return params


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    try:
        validate(args)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    try:
        params = build_params(args)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    result_url = f"{RESULT_BASE}?{urlencode(params)}"
    form_url = f"{FORM_BASE}?{urlencode(params)}"

    if args.output == "json":
        print(
            json.dumps(
                {
                    "form_url": form_url,
                    "result_url": result_url,
                    "params": params,
                    "captcha_required_for_reliable_use": True,
                    "default_url_kind": args.url_kind,
                    "current_window_params_included": any(
                        key in params
                        for key in (
                            "currentStartTime",
                            "currentEndTime",
                            "currentRecentTime",
                            "currentDateBySource",
                        )
                    ),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        print(form_url if args.url_kind == "form" else result_url)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
