---
name: japan-customs-trade-data
description: Use when extracting Japan customs import/export data from e-Stat by HS/statistical code, country, month, or when checking Japan commodity-code granularity.
---

# Japan Customs Trade Data

Use this skill to extract Japan trade statistics from e-Stat and return structured rows with explicit commodity-granularity caveats.

Japan's trade statistics are published by the Ministry of Finance, but bulk file access is through e-Stat. Treat `customs.go.jp` as the codebook/source-reference site and `e-stat.go.jp` as the data-download site.

## Scope Gate

Use this skill when the user needs:

- Japan import/export rows for an HS or 9-digit statistical code
- Japan trade data by country and month
- e-Stat file-download guidance for Trade Statistics of Japan
- Japan customs code granularity checks for a commodity such as WF6
- CDP diagnosis when the e-Stat browse UI or customs code pages need live inspection

Do not use this skill as the investment-analysis layer. Stop after extracting data, stating limitations, and giving basic trend math unless the user explicitly asks for supply-chain or equity interpretation.

## References

- For deterministic CSV extraction and e-Stat page behavior, read [references/e-stat-csv-contract.md](references/e-stat-csv-contract.md).
- For WF6-specific code mapping and caveats, read [references/wf6-code-granularity.md](references/wf6-code-granularity.md).
- For country-code decoding, read [references/country-codes.md](references/country-codes.md).
- For live browser/CDP diagnosis, read [references/e-stat-cdp-notes.md](references/e-stat-cdp-notes.md).
- For validation after edits or portal drift, read [references/smoke-checklist.md](references/smoke-checklist.md).

## Preferred Extraction Path

Use the bundled CLI before manual browsing:

```bash
python3 skills/japan-customs-trade-data/scripts/japan_trade.py \
  --direction export \
  --hs 282619900 \
  --country 103 \
  --monthly
```

Default output is a human-readable table. Use `--format json` for downstream analysis and `--format csv` for spreadsheet work.

## Workflow

1. Identify whether the requested commodity has a direct Japan statistical code.
   - Japan uses 9-digit statistical codes: 6-digit HS plus 3 domestic digits.
   - Export and import domestic suffixes can differ.
   - If the product is not separately coded, label the result as a proxy bucket.
2. Choose direction:
   - `export` for Japan shipments to destination countries.
   - `import` for Japan purchases from origin countries.
3. Choose code precision:
   - Use a 9-digit code for exact Japan statistical rows.
   - Use a 6-digit HS prefix only when the user asks for the broader HS family or when exploring code availability.
4. Choose country if needed:
   - Korea is `103`, China `105`, Taiwan `106`, United States `304`.
   - Decode other countries from `references/country-codes.md` or the customs code page.
5. Run the CLI and record source metadata:
   - `statInfId`
   - `survey_date` if discoverable from the e-Stat page
   - `direction`
   - `hs_match_mode`
   - `commodity_confidence`
   - units
6. Return rows and caveats. Do not silently convert `千円`; if converting to million yen, say so.

## Output Rules

Every answer based on extracted data must state:

- Source: e-Stat Trade Statistics of Japan CSV endpoint.
- Code: HS/statistical code used.
- Direction and country code, when applicable.
- Units: quantity unit and value in `千円` unless converted.
- Product confidence:
  - `direct_code` when the code directly identifies the requested product.
  - `proxy_bucket` when the product is only part of a broader code bucket.

For monthly trend tables, include quantity, value, and implied unit price when quantity is non-zero.

## Pitfalls

- Do not treat e-Stat `layout=datalist` as a reliable extraction surface. Use `layout=dataset` or the direct `file-download` endpoint.
- Do not parse CSV with naive `split(',')`; use a CSV parser.
- Do not assume export and import use the same 7-9 digit suffix.
- Do not treat Japan proxy buckets as pure product data. WF6 is not separately identifiable in Japan customs data.
- Do not rely on a single e-Stat UI row label without verifying the downloaded CSV contains the requested `HS` and `Country`.
- Do not use CDP as the primary extraction path unless the direct CSV workflow fails or the user specifically asks to inspect the website.
