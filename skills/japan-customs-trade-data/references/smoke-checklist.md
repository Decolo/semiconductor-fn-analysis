# Japan Customs Trade Data Smoke Checklist

Use this checklist after editing the skill, updating scripts, or detecting e-Stat portal drift.

## Fixture

- Source: e-Stat Trade Statistics of Japan CSV endpoint.
- Dataset: `toukei=00350300`, `tstat=000001013141`.
- Fixture direction: export.
- Fixture HS: `282619900`.
- Fixture country: `103` Republic of Korea.
- Fixture survey date observed: `2026May`.
- Fixture `statInfId`: `000040466825`.
- Product caveat: proxy bucket for possible WF6 exports, not pure WF6.

## CLI Check

Run from repo root:

```bash
python3 skills/japan-customs-trade-data/scripts/japan_trade.py \
  --direction export \
  --hs 282619900 \
  --country 103 \
  --monthly \
  --format json
```

Pass only if output includes:

- `statInfId` or `stat_inf_id` equal to `000040466825` for the fixture path, or another official candidate with identical fixture row values.
- `commodity_confidence` equal to `proxy_bucket` for WF6 mode or clearly stated as not direct product data.
- `value_unit` equal to `thousand_yen`.
- `quantity_unit` equal to `KG`.

Expected 2026 monthly rows:

| Month | Quantity2 KG | Value 千円 |
|---|---:|---:|
| Jan | 52,724 | 534,751 |
| Feb | 57,499 | 649,651 |
| Mar | 59,415 | 680,178 |
| Apr | 28,515 | 372,788 |
| May | 22,930 | 435,659 |

## Parser Check

- Uses `csv.DictReader` or equivalent structured parser.
- Reads monthly fields by header names such as `Quantity2-May`, not hard-coded indexes.
- Keeps blank future months out of monthly trend output.
- Does not crash on missing countries; labels unknown codes as `Code_XXX`.
- Rejects invalid HS input such as `ABC` before making network requests.
- Rejects non-3-digit country input before making network requests.
- Country-code mapping matches the official customs code page for common codes:
  - `110` Viet Nam
  - `113` Malaysia
  - `123` India
  - `205` United Kingdom
  - `302` Canada
  - `305` Mexico
- Non-WF6 exact-code rows use documented `commodity_confidence=direct_code`.

## Skill Behavior Check

- The answer labels `282619900` as a proxy bucket, not pure WF6.
- The answer says values are in `千円` before any conversion.
- The answer separates extraction from investment interpretation.
- CDP notes are used only for live UI diagnosis, not as the default data path.
