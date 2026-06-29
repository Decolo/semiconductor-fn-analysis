---
name: china-customs-trade-data
description: Use when operating China's official customs statistics platform through CDP for HS-code import/export rows, country/province breakdowns, CAPTCHA-assisted queries, or WF6 customs checks.
---

# China Customs Trade Data

Use this skill to operate China's official customs statistics query platform and return structured customs rows with platform caveats.

The official site is interactive and rate-limited. Unlike Japan e-Stat, it is not a stable unauthenticated CSV endpoint. Treat CDP plus user-solved CAPTCHA as the primary workflow.

## Scope Gate

Use this skill when the user needs:

- China Customs `stats.customs.gov.cn` query operation
- HS code import/export rows from the official platform
- Country-level or province-level breakdowns
- CDP recovery guidance for CAPTCHA, service-busy states, or async result pages
- WF6 or tungsten upstream customs checks using China HS codes

Do not use this skill as the investment-analysis layer. Stop after extraction, caveats, fallback-source notes, and basic row math unless the user explicitly asks for thesis interpretation.

## References

- For live CDP operation, read [references/customs-cdp-notes.md](references/customs-cdp-notes.md).
- For query parameters and URL construction, read [references/query-parameters.md](references/query-parameters.md).
- For WF6 and tungsten-related HS codes, read [references/wf6-and-tungsten-codes.md](references/wf6-and-tungsten-codes.md).
- For fallback source handling, read [references/fallback-sources.md](references/fallback-sources.md).
- For validation after edits or portal drift, read [references/smoke-checklist.md](references/smoke-checklist.md).

## Preferred Workflow

1. Build a form URL with the bundled helper:

```bash
python3 skills/china-customs-trade-data/scripts/china_customs_url.py \
  --hs 28261930 \
  --direction export \
  --year 2026 \
  --start-month 5 \
  --end-month 5 \
  --breakdown province
```

2. Use a CDP-controllable Chrome tab to open the form page.
3. Fill or verify form fields.
4. Click `查询`.
5. Ask the user to solve CAPTCHA in the browser when it appears. Do not attempt to bypass it.
6. After redirect to `queryDataList`, wait for async rows and extract visible table text/HTML.
7. Return structured rows and platform state.

## Query Types

### HS by Country

Use this for destination/source country analysis.

```text
outerField1=CODE_TS
outerValue1=<HS_CODE>
outerField2=ORIGIN_COUNTRY
outerValue2=<COUNTRY_CODE optional>
```

Known country codes:

- Japan: `116`
- Korea: `133`

### HS by Province

Use this for exporter/importer registered-location breakdowns.

```text
outerField1=CODE_TS
outerValue1=<HS_CODE>
outerField2=TRADE_CO_PORT
outerValue2=
```

`TRADE_CO_PORT` means `收发货人注册地`. Leave `outerValue2` empty to show all provinces.

## Extraction Rules

- Preserve the exact units shown by the platform.
- Preserve currency setting, usually `usd`.
- Distinguish flow direction: `iEType=0` export, `iEType=1` import.
- Keep the raw table text or row snapshot when the platform is unstable.
- Report whether data came from official customs, direct `queryDataList`, CAPTCHA-assisted form flow, or fallback sources.

## Recovery Guide

- CAPTCHA iframe appears: tell the user to solve it manually, then continue after redirect.
- `当前服务请求较多，请稍后重试`: wait 30-60 seconds, then retry from a fresh tab.
- 429/rate limit: slow down. Avoid repeated CDP eval bursts; space actions by 10+ seconds.
- Runtime/eval timeouts: site may be down. If CDP itself is stale and no other active browser task depends on it, stop the CDP daemon, then retry once.
- Direct `queryDataList` fails: use the form page and CAPTCHA flow.
- Old platform `http://43.248.49.97/`: treat as dead; do not use it.

When blocked, report the exact URL, visible page state, whether CAPTCHA is open, whether results table exists, and any visible service message.

## Pitfalls

- Do not promise CAPTCHA-free official extraction.
- Do not use `curl` as the primary path; the site commonly returns HTTP 412/504 or service-busy responses outside the browser.
- Do not confuse WF6 `28261930` / `2826193000` with NF3 `28129011`.
- Do not confuse country codes: Japan is `116`, Korea is `133`.
- Do not use `ORIGIN_COUNTRY` when the user asked for province/exporter-region breakdown; use `TRADE_CO_PORT`.
- Do not treat fallback sources as official unless cross-validated against customs.
