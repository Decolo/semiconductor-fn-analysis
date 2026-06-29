# Korea UNIPASS CDP Smoke Checklist

Use this checklist when validating that the live UNIPASS portal still matches the skill. This is a manual/CDP smoke test, not an automated test suite. Selector details live in `unipass-cdp-notes.md`; this file records pass/fail assertions.

## Fixture

- Last verified from source observations: 2026-06-27.
- Entry URL: `https://unipass.customs.go.kr/ets/etsItemSrch.do?menuId=ETS_MNU_00000103`.
- Redirect URL may be `https://tradedata.go.kr/cts/index.do?menuId=ETS_MNU_00000103`.
- Fixture HS code: use a known valid HS/HSK code such as `282619`.
- Fixture date range: use a pinned known-good recent range when available. Last documented fixture candidate: `2026.05` to `2026.05`; if the portal data window has moved, record the replacement month in this checklist before treating a no-data result as portal drift.
- Tested surfaces to record: Codex skill symlink, Hermes skill symlink, `.agents/skills` symlink, and live CDP browser.

## Setup

- Use a CDP-controllable Chrome session.
- Prefer an existing UNIPASS or `tradedata.go.kr/cts/` tab if one is open.
- If the tab state is unclear, record the URL and whether the real form readiness checks pass.

## Form Load

- Run the guarded loader from `unipass-cdp-notes.md`.
- Pass only if HS controls, statistics mode controls, period controls, and `조회` are all usable.
- Fail visibly if the loader function is undefined after timeout or the form controls never appear.

## Aggregate Query Check

- Select `통계항목 = 품목별` and verify the selected mode label/value.
- Add the fixture HS code and verify selected HS state, preferably through `#ETS0100019Q_checkdHsSgn`.
- Select `월별` with the helper in `unipass-cdp-notes.md`, verify the month fields exist, set the fixture date range, and run `조회`.
- Pass only if result headers map to:

```text
period, hs_code, item_name, export_weight, export_value, import_weight, import_value, trade_balance
```

- Pass only if `metadata.units` is present, commonly `톤(TON), 천 달러`.
- Pass only if the result is non-empty or the portal clearly reports a no-data state.

## HS Code by Country Check

- Select `통계항목 = 품목별+국가별` and verify the selected mode label/value.
- Confirm whether the mode switch cleared selected HS state; re-add and re-verify the fixture HS code if needed.
- Run `조회` if needed to render result controls.
- Set page size to the largest available option and verify the selected value.
- Pass only if result headers map to:

```text
period, country, hs_code, item_name, export_weight, export_value, import_weight, import_value, trade_balance
```

- Pass only if `국가` appears as a table column without using the country popup.
- Pass only if pagination state is checked. If more than one page exists and pagination was not collected, mark extraction as truncated rather than complete.

## Row Filtering Check

- Extract table rows through the helper in `unipass-cdp-notes.md` or equivalent visible table-cell mapping.
- Pass only if extracted rows are schema-shaped objects, not raw cell arrays.
- Exclude:
  - headers
  - pagination controls
  - hidden menu text
  - search-form labels
  - totals unless explicitly requested
  - leading selection/control cells such as `선택`

## Recovery Check

For each failure state, verify the skill gives a deterministic next action:

- Shell but no form: rerun the guarded loader.
- Stale tab: reload URL and form call, then re-check selectors.
- Cleared state: re-add HS code after changing `통계항목` and verify selected HS state.
- Missing table: confirm required form state, rerun `조회`.
- Wrong columns: re-check `통계항목`.
- Too few country rows: expand page size and rerun query.

## Known Pitfall Check

- Confirm the workflow does not depend on the country checkbox popup.
- Confirm data.go.kr is documented as credential-gated.
- Confirm commodity granularity limits are described as extraction caveats, not analysis conclusions.
- Confirm agent skill directories resolve to the repo-owned source, not a private copy.
