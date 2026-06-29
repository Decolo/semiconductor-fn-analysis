---
name: korea-customs-trade-data
description: Use when extracting Korea UNIPASS/韩国海关 import/export rows by HS/HSK code, country, or month through CDP browser automation.
---

# Korea UNIPASS Customs Trade Data

Use this skill to operate the Korea UNIPASS trade statistics web UI through CDP and return structured rows plus platform caveats.

## Scope Gate

Use this skill when the user needs:

- Korea import/export rows for an HS code
- Korea import/export rows by HS code and country
- UNIPASS browser operation, recovery, or extraction guidance
- A reminder of known CDP traps in the Korea customs portal

Do not use this skill as the analysis layer. Stop before supply-chain interpretation, anomaly detection, investment conclusions, or commodity-specific theses.

## References

- For live CDP operation, read [references/unipass-cdp-notes.md](references/unipass-cdp-notes.md) first. It is the canonical source for selectors, snippets, waits, and extraction helpers.
- Read [references/smoke-checklist.md](references/smoke-checklist.md) only when validating portal drift or agent-surface exposure.

## Prerequisites

- A Chrome tab controllable through CDP.
- Prefer reusing an already-open UNIPASS or `tradedata.go.kr/cts/` tab before opening a new one.
- The web workflow is no-login for the supported queries. The data.go.kr API is secondary and requires a valid service key.

## Load the Real Query Form

Direct navigation can load the UNIPASS shell without the query form. Load and verify the real form before touching query controls.

1. Open:

```text
https://unipass.customs.go.kr/ets/etsItemSrch.do?menuId=ETS_MNU_00000103
```

2. If the query form is absent, run the guarded loader from `references/unipass-cdp-notes.md`.

3. Confirm readiness before operating controls:

- HS search controls exist.
- `통계항목` can be selected.
- `조회` can be clicked.
- Period controls exist after choosing the desired period mode.

If these checks fail, reload the entry URL, run the guarded loader once more, then report shell/form state if still blocked.

## Query Case A: Aggregate HS Code

Use this when the user asks for Korea data for one or more HS codes without country breakdown.

1. Ensure `통계항목` is `품목별`; verify the selected label before continuing.
2. Add the HS code through the primary HS-entry path in `references/unipass-cdp-notes.md`; verify selected HS state before searching.
3. Choose period mode. For monthly data, select `월별`; note that the date controls switch to `YYYY.MM` month selects.
4. Set start and end months.
5. Click `조회` (`.btnSearch.w50p`).
6. Wait for the success or failure signals in `references/unipass-cdp-notes.md`.
7. Extract aggregate rows with this schema:

```text
metadata.units
rows[]: period, hs_code, item_name, export_weight, export_value, import_weight, import_value, trade_balance
```

Do not include a `country` field for aggregate rows.

## Query Case B: HS Code by Country

Use this when the user asks for source-country, destination-country, or country-level import/export data for a specific HS code.

1. Switch `통계항목` to `품목별+국가별` before searching; verify the selected label before continuing.
2. Treat the mode switch as destructive: it can clear selected HS codes and other form state.
3. Re-add the HS code after switching modes if the selected-HS postcondition fails.
4. Choose period mode and date range.
5. Run `조회` once if needed to render result controls.
6. Set page size to the largest available option with the helper in `references/unipass-cdp-notes.md`; verify the selected value.
7. Rerun or wait for refreshed results.
8. Extract country-level rows with this schema:

```text
metadata.units
rows[]: period, country, hs_code, item_name, export_weight, export_value, import_weight, import_value, trade_balance
```

This is the default country workflow. It avoids the country checkbox popup and makes `국가` a result-table column.

## Table Extraction Rules

- Preserve the unit line as result-set metadata. Korea commonly reports weight as `톤(TON)` and value as `천 달러`.
- Filter to data rows only. Exclude table headers, pagination text, search controls, hidden menu text, totals unless explicitly requested, and non-row chrome.
- For CDP extraction, use the canonical result extraction helper in `references/unipass-cdp-notes.md` or map visible result-table cells by header order.
- If raw `tr` extraction includes a leading selection/control column such as `선택`, strip it before applying the schema.
- Keep numeric strings as displayed unless the user asked for normalized numbers. If normalizing, retain the original units in metadata.

## Recovery Guide

- **Empty shell:** Run the guarded loader and re-check form readiness.
- **Stale tab:** Reuse the tab only if the readiness checks pass. Otherwise reload the URL and real form call.
- **Mode switch cleared state:** Re-add HS selections after changing `통계항목`.
- **Missing result table:** Confirm the real form is loaded, required fields are selected, page size is set if needed, then rerun `조회`.
- **Wrong columns:** Re-check `통계항목`. Aggregate `품목별` has no `국가`; `품목별+국가별` should include `국가`.
- **Too few country rows:** Expand `#ETS0100019Q_showPagingLine` to `100`, rerun the query, then extract.

When still blocked, report the precise state: shell vs form, selected `통계항목`, HS selection presence, period range, whether the result table exists, and any visible portal error.

## Pitfalls

- Do not use the `품목별` country checkbox popup as the default country workflow. It is CDP-hard: checkbox state can appear checked but fail to persist in page state after the popup closes.
- Do not treat data.go.kr as the primary route unless a valid service key is already available. Registration can require Korean phone or i-PIN verification.
- Do not promise commodity isolation beyond the HS code the platform exposes. Some Korea HSK categories are catch-all buckets; that is an extraction caveat, not an analysis conclusion.
- Do not assume direct URL navigation means the form is ready. The shell and the query form are different page states.
