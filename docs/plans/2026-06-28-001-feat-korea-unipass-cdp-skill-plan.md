---
title: "feat: Add Korea UNIPASS CDP practices skill"
type: feat
date: 2026-06-28
origin: docs/brainstorms/2026-06-28-korea-unipass-cdp-practices-skill-requirements.md
---

# feat: Add Korea UNIPASS CDP practices skill

## Summary

Add a repo-owned Korea UNIPASS customs CDP practices skill under `skills/` and expose it to local agents through the existing symlink-based skill distribution pattern. The skill will turn the verified UNIPASS workflow into an operation-first playbook for browser setup, query execution, table extraction, page-state recovery, and known platform pitfalls.

---

## Problem Frame

The current verified Korea customs workflow lives outside this repo in personal Hermes skill material and session handoff notes. That makes it useful as research memory, but weaker as a reusable source skill for Codex, Hermes, and Claude Code.

The implementation should establish `semiconductor-fn-analysis` as the source of truth for this customs operation skill, matching the repo's existing pattern for semiconductor-related skills that are linked into agent-specific skill directories.

---

## Requirements

**Source Skill Placement**

- R1. The Korea UNIPASS skill source lives in `skills/korea-customs-trade-data/`.
- R2. Agent-specific skill directories consume the repo-owned source through symlinks or equivalent link registration.
- R3. The existing Hermes Korea customs material is treated as migration input, not as the long-term source of truth.

**Operation Workflow Coverage**

- R4. The skill documents how to open the UNIPASS shell and load the real query form before interacting with controls.
- R5. The skill documents aggregate HS-code queries through `품목별`.
- R6. The skill documents HS-code-by-country queries through `품목별+국가별`.
- R7. The skill captures mode-switch side effects, especially form state clearing after changing the statistics item.
- R8. The skill includes result-table readiness checks and page-size expansion before country-level extraction.

**Extraction and Recovery**

- R9. The skill defines aggregate and country-level result schemas.
- R10. The skill tells agents how to filter data rows from table chrome, headers, and non-data rows.
- R11. The skill preserves units with extracted rows.
- R12. The skill includes recovery guidance for empty shell pages, stale tabs, cleared form state, and missing result tables.

**Pitfall Boundaries**

- R13. The country checkbox popup is marked as CDP-hard and not the default country workflow.
- R14. data.go.kr API access is documented as secondary and credential-gated.
- R15. Commodity granularity limits are documented as extraction caveats, not analysis conclusions.
- R16. Supply-chain interpretation, investment analysis, and cross-country analytical conclusions stay out of this skill.

---

## Key Technical Decisions

- **Repo-owned source skill:** Put the durable skill under `skills/korea-customs-trade-data/` so the repo, not an agent-private directory, owns the canonical content.
- **Update-by-migration, not blank rewrite:** Use the existing Hermes skill and UNIPASS notes as source material, but reshape them into a practices-first document rather than preserving the old research-note order.
- **Main skill for stable workflow, reference file for raw CDP notes:** Keep `SKILL.md` concise and operational; move selector catalogs, raw page architecture, and lower-confidence observations into `references/`.
- **Smoke checklist over automated tests:** Validate this as a skill document for a live JS portal with review and CDP smoke scenarios, not unit tests.

---

## Output Structure

```text
skills/
  korea-customs-trade-data/
    SKILL.md
    references/
      unipass-cdp-notes.md
      smoke-checklist.md
```

External agent skill directories should link to `skills/korea-customs-trade-data/` using the same pattern already used for the repo's existing linked skills.

---

## Implementation Units

### U1. Establish Repo-Owned Skill Source

- **Goal:** Create `skills/korea-customs-trade-data/` as the canonical source skill location.
- **Requirements:** R1, R2, R3.
- **Dependencies:** None.
- **Files:** `skills/korea-customs-trade-data/SKILL.md`, `skills/korea-customs-trade-data/references/unipass-cdp-notes.md`.
- **Approach:** Start from the existing Korea customs skill and UNIPASS CDP notes, then normalize the directory to match the repo's current skill layout.
- **Patterns to follow:** Existing `skills/pb-semiconductor/SKILL.md` and `skills/peg-semiconductor/SKILL.md` single-skill directory convention.
- **Test scenarios:**
  - Confirm the skill has valid frontmatter with a distinct `name` and operation-focused `description`.
  - Confirm the source directory contains no agent-private path assumptions.
  - Confirm migrated reference notes preserve the verified form-loading and `품목별+국가별` facts.
- **Verification:** The repo contains a readable Korea customs skill source under `skills/` and the old Hermes material is no longer the only source.

### U2. Reshape SKILL.md Into an Operation Playbook

- **Goal:** Rewrite the main skill body around stable CDP workflows instead of one-off research findings.
- **Requirements:** R4, R5, R6, R7, R8, R13, R16.
- **Dependencies:** U1.
- **Files:** `skills/korea-customs-trade-data/SKILL.md`.
- **Approach:** Organize the main document by scope gate, prerequisites, tab selection, form loading, query cases, extraction, recovery, and pitfall boundaries.
- **Patterns to follow:** Existing skill scope gates and "do not use when" boundaries in `skills/speculative-narrative-audit/SKILL.md`.
- **Test scenarios:**
  - Given a user asks for Korea HS-code-by-country data, the skill routes the agent to `품목별+국가별`.
  - Given a user asks for aggregate HS-code data, the skill keeps `품목별` as the aggregate workflow.
  - Given a user asks for analysis meaning, the skill stops at extraction and points analysis outside this skill.
  - Given the agent sees only the UNIPASS shell, the skill instructs loading the real form before interacting with query controls.
- **Verification:** A reader can follow the main skill from tab selection to query execution without reading raw notes first.

### U3. Define Extraction Contract and Recovery Checklist

- **Goal:** Make table extraction and blocked-state reporting predictable.
- **Requirements:** R8, R9, R10, R11, R12, R15.
- **Dependencies:** U2.
- **Files:** `skills/korea-customs-trade-data/SKILL.md`, `skills/korea-customs-trade-data/references/smoke-checklist.md`.
- **Approach:** Add explicit aggregate and country-level column contracts, row filtering rules, unit preservation, page-size guidance, and recovery branches.
- **Technical design:** Directional extraction contract:

```text
aggregate row = period + hs_code + item_name + export_weight + export_value + import_weight + import_value + trade_balance + units
country row = period + country + hs_code + item_name + export_weight + export_value + import_weight + import_value + trade_balance + units
```

- **Patterns to follow:** Existing Korea customs notes for table columns and CDP page-state pitfalls.
- **Test scenarios:**
  - Covers aggregate extraction. Given aggregate results, the expected row schema has no `country` field.
  - Covers country extraction. Given `품목별+국가별` results, the expected row schema includes `country`.
  - Given the table contains header or pagination text, the checklist requires excluding non-data rows.
  - Given the table reports tons and thousand USD, the checklist requires preserving those units.
- **Verification:** The skill can be reviewed against the acceptance examples from the origin requirements without inventing extraction fields.

### U4. Link and Compatibility Pass

- **Goal:** Make the repo-owned source available to the user's agent environments through the existing link pattern.
- **Requirements:** R2, R3.
- **Dependencies:** U1, U2, U3.
- **Files:** `skills/korea-customs-trade-data/SKILL.md`, `skills/korea-customs-trade-data/references/smoke-checklist.md`.
- **Approach:** Document and verify the symlink targets for Codex, Hermes, and Claude Code using the user's current link conventions. Replace any duplicate private copy only after confirming it is not the canonical source.
- **Patterns to follow:** Existing linked skills such as the repo's PB and PEG semiconductor skills.
- **Test scenarios:**
  - Confirm Codex can discover the linked skill in a new session or through the configured skill list.
  - Confirm Hermes sees the linked skill without retaining a divergent private copy.
  - Confirm any Claude Code exposure uses the same source directory rather than copying content.
  - Confirm broken or missing links fail visibly rather than leaving two different skill versions.
- **Verification:** Each intended agent surface resolves to the repo-owned skill source or has a documented reason for not being linked.

---

## Scope Boundaries

- The plan does not include building a standalone scraper, API client, or test harness.
- The plan does not solve data.go.kr account registration.
- The plan does not encode WF6-specific analysis as the default workflow.
- Historical Hermes content can remain as archival input during implementation, but the repo-owned skill should become canonical.

---

## Risks & Dependencies

- **Symlink drift:** Agent directories can silently retain old physical copies. The implementation must check whether a target is a symlink or a real directory before changing it.
- **Portal drift:** UNIPASS selectors and labels can change. The skill should include semantic readiness checks, not only brittle selector lists.
- **Scope creep:** Cross-country comparison and investment analysis are adjacent, but including them would weaken the operation-only practices skill.
- **Agent-discovery differences:** Codex, Hermes, and Claude Code may load skill directories differently, so verification must check each intended surface.

---

## Documentation / Operational Notes

- Keep `SKILL.md` as the entry point that an agent can read quickly.
- Put raw selector details, page architecture notes, and lower-confidence experiments in `references/unipass-cdp-notes.md`.
- Put verification steps in `references/smoke-checklist.md` so future portal drift can be checked without bloating the main skill.
- If the implementation replaces an existing private Hermes directory with a symlink, preserve useful content first.

---

## Sources / Research

- `docs/brainstorms/2026-06-28-korea-unipass-cdp-practices-skill-requirements.md`
- Existing repo skill examples under `skills/`.
- Existing Korea customs skill and UNIPASS notes from the user's local skill library.
- Current linked-skill pattern observed for the repo's semiconductor skills.
