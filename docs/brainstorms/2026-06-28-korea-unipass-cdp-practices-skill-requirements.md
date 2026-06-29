---
date: 2026-06-28
topic: korea-unipass-cdp-practices-skill
title: Korea UNIPASS CDP Practices Skill Requirements
---

# Korea UNIPASS CDP Practices Skill Requirements

## Summary

Create a practices skill for operating Korea UNIPASS customs trade pages through CDP and extracting table data reliably. The skill covers browser automation workflows, page-state recovery, common query cases, extraction contracts, and known pitfalls. Trade analysis, supply-chain interpretation, and investment conclusions stay outside this skill.

---

## Problem Frame

The Korea UNIPASS customs portal is usable without login, but the trade statistics page is JavaScript-heavy and does not expose the useful query form through the initial URL alone. A stable agent workflow needs to know how to load the real form, choose the right statistics view before searching, avoid controls whose state does not persist through CDP, and extract result rows without mixing headers, pagination chrome, or hidden table text into the dataset.

The immediate use case is repeated agent access to Korean import/export data by HS code and country. The durable value is not a one-off query result; it is an operating playbook that lets future agents perform the same platform interaction with less trial and error.

---

## Key Decisions

- **Operation first, analysis later.** The skill should stop at producing trustworthy structured trade rows and platform caveats; Codex or a separate research skill handles interpretation.
- **Prefer verified views over fragile filters.** The primary country-level workflow uses the `품목별+국가별` statistics view instead of the country checkbox popup.
- **Treat CDP page state as part of the workflow.** The skill must include readiness checks, mode-switch side effects, pagination settings, and recovery steps because direct navigation alone is insufficient.
- **Document failure paths as first-class guidance.** Known dead ends, especially the legacy country popup and restricted API access, should be marked clearly so agents do not retry them as if they were unresolved opportunities.

---

## Requirements

**Core CDP Workflow**

- R1. The skill must explain how to open the UNIPASS trade statistics shell and load the real query form before interacting with controls.
- R2. The skill must define readiness checks that confirm the form is present before selecting HS codes, periods, or statistics views.
- R3. The skill must cover monthly-period queries and note when the date controls change shape after switching period mode.
- R4. The skill must describe how to execute a query and recognize that the result table has loaded.

**Common Query Cases**

- R5. The skill must include an aggregate HS-code query case for `품목별`.
- R6. The skill must include an HS-code-by-country query case for `품목별+국가별`.
- R7. The skill must include a country-only or broad-country query case only if it can be described as a stable platform workflow.
- R8. The skill must explain that switching the statistics item can clear prior form state, so HS selections may need to be re-added after changing modes.

**Extraction Contract**

- R9. The skill must define the expected table columns for aggregate HS-code results.
- R10. The skill must define the expected table columns for HS-code-by-country results.
- R11. The skill must require extraction into structured rows with period, optional country, HS code, item name, export weight, export value, import weight, import value, and trade balance.
- R12. The skill must include a row-filtering rule that excludes headers, pagination controls, and non-data rows.
- R13. The skill must require units to be captured with the result set because Korea reports weight and value units differently from some comparison countries.

**Reliability and Recovery**

- R14. The skill must include page-size expansion before extraction when country-level results may exceed the default visible row count.
- R15. The skill must describe how to recover from an empty shell, stale tab, cleared form, or missing result table.
- R16. The skill must prefer reusing an already-open relevant browser tab before opening a new one.
- R17. The skill must separate verified workflows from hypotheses or manual-only paths.

**Pitfalls and Limits**

- R18. The skill must mark the country checkbox popup as CDP-hard because checked state can fail to persist after the popup closes.
- R19. The skill must mark data.go.kr API access as limited by Korean phone or i-PIN registration unless a valid service key is already available.
- R20. The skill must warn that Korea's available HS granularity may be a catch-all category for some materials, so extraction can be reliable even when product isolation is not.
- R21. The skill must avoid presenting a single commodity research example as the only valid use case for the platform.

---

## Key Flows

- F1. Aggregate HS-code query
  - **Trigger:** The user asks for Korea import/export data for one HS code without country breakdown.
  - **Steps:** Load the real form, select `품목별`, add the HS code, choose period mode and date range, run the query, extract aggregate rows.
  - **Outcome:** Structured rows keyed by period and HS code.
  - **Covered by:** R1, R2, R3, R4, R5, R9, R11, R12, R13.

- F2. HS-code-by-country query
  - **Trigger:** The user asks for imports or exports by source or destination country for a specific HS code.
  - **Steps:** Load the real form, switch statistics item to `품목별+국가별`, re-add the HS code if the switch cleared the form, choose period mode and date range, expand page size, run the query, extract country rows.
  - **Outcome:** Structured rows keyed by period, country, and HS code.
  - **Covered by:** R1, R2, R3, R4, R6, R8, R10, R11, R12, R14.

- F3. Recovery after fragile page state
  - **Trigger:** The result table is missing, the form is absent, or selected values disappeared after a mode switch.
  - **Steps:** Check whether the shell or real form is loaded, reload the form if needed, re-select the statistics view, re-add HS selections, rerun the query, and only then extract.
  - **Outcome:** The agent either reaches a known good table state or reports the precise blocked state.
  - **Covered by:** R2, R8, R15, R16, R17.

---

## Acceptance Examples

- AE1. **Covers R1, R2.** Given the initial UNIPASS URL has loaded only the menu shell, when the agent starts a query, then it loads the trade statistics form before clicking query controls.
- AE2. **Covers R6, R8, R18.** Given the user asks for HS-code data by country, when the agent chooses the workflow, then it uses `품목별+국가별` and does not attempt the legacy country checkbox popup.
- AE3. **Covers R10, R11, R12.** Given a country-level result table is visible, when the agent extracts rows, then each data row includes period, country, HS code, item name, export metrics, import metrics, and trade balance.
- AE4. **Covers R14.** Given the country-level query has more rows than the default page size, when extraction begins, then the agent expands the page size before collecting rows.
- AE5. **Covers R19, R20.** Given API access or commodity-level isolation is unavailable, when the agent reports results, then it distinguishes platform extraction limits from analysis conclusions.

---

## Success Criteria

- A future agent can perform aggregate and country-level Korea customs queries without rediscovering the real form-loading step.
- A future agent defaults to `품목별+국가별` for HS-code-by-country data and avoids the known checkbox popup trap.
- Extracted output has a predictable row schema and preserves units.
- Blocked states are reported as platform or access constraints instead of silent failures.

---

## Scope Boundaries

- Supply-chain analysis, investment interpretation, and anomaly detection are outside this skill.
- Cross-country comparison workflows are outside this skill except for unit and granularity caveats needed to avoid misleading extracted data.
- API automation through data.go.kr is not a primary path unless valid credentials are already available.
- Full product isolation within catch-all HS categories is not promised by this skill.

---

## Dependencies / Assumptions

- The agent has access to a CDP-controllable browser session.
- UNIPASS remains accessible without login for the relevant web workflow.
- The platform's selectors and Korean labels may drift, so the skill should include semantic checks in addition to selector references.
- The skill may use recent verified observations from the Korea customs workflow handoff and existing customs skill notes as source material.

---

## Sources / Research

- Existing Korea customs workflow handoff from 2026-06-27.
- Existing Korea customs trade data skill notes covering UNIPASS, data.go.kr, `품목별+국가별`, and known pitfalls.
