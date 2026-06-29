# China Customs Trade Data Smoke Checklist

Use this checklist after editing the skill or when checking portal drift.

## Fixture

- Entry URL: `http://stats.customs.gov.cn/queryData/queryDataByWhere`
- Results URL base: `http://stats.customs.gov.cn/queryData/queryDataList`
- Fixture HS: `28261930` WF6.
- Fixture direction: export (`iEType=0`).
- Fixture breakdown: province (`outerField2=TRADE_CO_PORT`, empty `outerValue2`).
- Fixture period: use the most recent available single month or a known recent month such as 2026-05 when reproducing the prior WF6 workflow.

## URL Builder Check

Run from repo root:

```bash
python3 skills/china-customs-trade-data/scripts/china_customs_url.py \
  --hs 28261930 \
  --direction export \
  --year 2026 \
  --start-month 5 \
  --end-month 5 \
  --breakdown province
```

Pass only if output includes:

- The default URL starts with `http://stats.customs.gov.cn/queryData/queryDataByWhere`.
- `outerField1=CODE_TS`
- `outerValue1=28261930`
- `outerField2=TRADE_CO_PORT`
- no non-empty `outerValue2`
- `iEType=0`
- `codeLength=8`
- no `currentStartTime`, `currentEndTime`, `currentRecentTime`, or `currentDateBySource` unless explicitly provided from a live page

Also run:

```bash
python3 skills/china-customs-trade-data/scripts/china_customs_url.py \
  --hs 28261930 \
  --direction export \
  --year 2026 \
  --start-month 5 \
  --end-month 5 \
  --breakdown country \
  --country "South Korea"
```

Pass only if this resolves to `outerValue2=133`.

Run an invalid country check:

```bash
python3 skills/china-customs-trade-data/scripts/china_customs_url.py \
  --hs 28261930 \
  --direction export \
  --year 2026 \
  --start-month 5 \
  --end-month 5 \
  --breakdown country \
  --country Atlantis
```

Pass only if the helper rejects the unknown nonnumeric country before printing a URL.

## CDP Check

- Reuse an existing customs tab if present.
- Confirm query page or results page loads.
- Confirm CAPTCHA behavior is documented and not bypassed.
- If CAPTCHA appears, pass only if the agent asks the user to solve it manually.
- If result table loads, extract visible rows and keep a raw snapshot.
- If the site returns service busy, pass only if the agent reports that state and retries conservatively.

## Skill Behavior Check

- The answer identifies official vs fallback sources.
- The answer uses China country codes (`116` Japan, `133` Korea), not Japan/Korea platform mappings.
- The answer does not confuse WF6 with NF3.
- The answer separates extraction from thesis analysis.
