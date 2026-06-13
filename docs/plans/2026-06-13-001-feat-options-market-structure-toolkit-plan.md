---
date: 2026-06-13
origin: docs/brainstorms/2026-06-13-options-market-structure-toolkit-requirements.md
---

# feat: Add options market structure toolkit

## Summary

Add a document-first options market structure toolkit to `semiconductor-fn-analysis`. The implementation will create one new skill family under `skills/options-market-structure/`, update the root README for discovery, and keep the release aligned with the repo's current low-maintenance framework style.

---

## Problem Frame

The requirements document defines a gap between valuation frameworks and market-context interpretation. The repo already teaches how to value semiconductor archetypes, but it does not teach how to use options-market structure to judge trend conditions. This plan adds that capability without introducing software infrastructure, APIs, or execution tooling.

---

## Requirements

| ID | Requirement | Notes |
|---|---|---|
| R1 | Add a flagship skill | New `skills/options-market-structure/SKILL.md` |
| R2 | Add a regime translation layer | Included in reference material and surfaced in skill output |
| R3 | Add a data-confidence layer | Included in reference material |
| R4 | Add worked examples | Included in examples material |
| R5 | Keep the repo coherent | Update `README.md` skill table and structure section |
| R6 | Preserve low carrying cost | No runtime code or external API dependencies in first release |

---

## Key Technical Decisions

### K1. Implement as a document-first skill set

The repo's established pattern is `SKILL.md` plus companion markdown files. Reusing that pattern keeps the new toolkit legible, low-maintenance, and consistent with existing skills.

### K2. Put the regime model in reference content, not in a separate skill

The "state translation" layer is essential, but it does not need a separate top-level skill in v1. Keeping it inside the same folder reduces sprawl and makes the flagship skill self-contained.

### K3. Use examples as worked scenario cards

Examples should not be generic explanations. Each one should present a market setup, the relevant options observations, the resulting regime classification, and what that means for trend traders.

### K4. Keep semiconductor context inside the first release

A full sector-specific companion skill is deferred, but the first release should still include semiconductor-specific guidance in the reference and example layers so the repo remains on-brand.

---

## Output Structure

```text
docs/
  brainstorms/
    2026-06-13-options-market-structure-toolkit-requirements.md
  plans/
    2026-06-13-001-feat-options-market-structure-toolkit-plan.md
skills/
  options-market-structure/
    SKILL.md
    REFERENCE.md
    EXAMPLES.md
README.md
```

---

## Implementation Units

### U1. Add the flagship options-market-structure skill
**Goal:** Create the primary skill entrypoint that defines scope, usage criteria, workflow, signal checklist, regime output, and when not to use the framework.  
**Requirements:** R1, R2, R6  
**Dependencies:** None  
**Files:** `skills/options-market-structure/SKILL.md`  
**Approach:** Mirror the style of existing skill files: scope gate, core framework, output template, and preferred data-source order. The skill must explain that the toolkit is for interpreting options market structure in service of trend trading, not for trading options contracts directly.  
**Patterns to follow:** `skills/pb-semiconductor/SKILL.md`, `skills/peg-semiconductor/SKILL.md`  
**Test scenarios:**  
- Happy path: a user asks whether options structure confirms an uptrend and the skill's framing clearly routes them into a trend-context workflow rather than options trade selection.  
- Happy path: a user asks about `put/call`, `IV`, `skew`, and `gamma`, and the skill shows those as part of one integrated process rather than isolated glossary entries.  
- Edge case: a user is really asking about buying calls or puts; the skill should redirect away from contract speculation and back to structure interpretation.  
- Error path: a user wants precise intraday dealer-position conclusions from weak data; the skill should downgrade confidence and warn about data quality.  
- Integration scenario: the skill output template should visibly connect raw signal inputs to a named regime and an actionable trend-reading conclusion.  
**Verification:** The new `SKILL.md` reads like a direct sibling of the existing two skills and fully explains the flagship workflow on its own.

### U2. Add the reference layer for signals, regimes, and data-confidence rules
**Goal:** Create the durable methodology reference that explains individual signals, their interactions, regime mapping, and confidence limits.  
**Requirements:** R2, R3, R6  
**Dependencies:** U1  
**Files:** `skills/options-market-structure/REFERENCE.md`  
**Approach:** Organize the reference into four sections: signal primitives, regime definitions, data-confidence ladder, and semiconductor-specific interpretation notes. The regime definitions should be compact and memorable.  
**Patterns to follow:** `skills/pb-semiconductor/REFERENCE.md`  
**Test scenarios:**  
- Happy path: the reference defines each core signal with interpretation relevant to trend context, not option pricing education.  
- Happy path: the regime section maps combinations of signals to named states with clear "what this means" language.  
- Edge case: overlapping signals that point in different directions should produce caveated interpretations instead of false certainty.  
- Error path: unsupported claims such as precise intraday dealer positioning from delayed data should be explicitly demoted.  
- Integration scenario: semiconductor-specific notes should connect `SPY` / `QQQ` / `SOXX` / `NVDA` relationships without overwhelming the core framework.  
**Verification:** A reader can move from raw signals to a regime judgment using the reference alone, and the data-confidence warnings are explicit.

### U3. Add worked examples and update repo discovery
**Goal:** Make the framework operational through examples and ensure the repo advertises the new skill correctly.  
**Requirements:** R4, R5  
**Dependencies:** U1, U2  
**Files:** `skills/options-market-structure/EXAMPLES.md`, `README.md`  
**Approach:** Write 3-5 worked scenarios covering trend confirmation, fragile rally, panic hedge, squeeze risk, and semiconductor-specific context. Update the root README's skill table, selector text, and structure map so the new skill is easy to find and correctly categorized.  
**Patterns to follow:** `skills/pb-semiconductor/EXAMPLES.md`, `skills/peg-semiconductor/EXAMPLES.md`, `README.md`  
**Test scenarios:**  
- Happy path: each example states the setup, options observations, regime conclusion, and trend implication.  
- Edge case: at least one example should show conflicting signals and explain why the answer is mixed rather than clean.  
- Integration scenario: the README should let a reader distinguish valuation skills from market-structure skills quickly.  
- Test expectation: none -- documentation-only unit with behavior validated through content review rather than automated tests.  
**Verification:** The examples feel usable as templates, and the README makes the new toolkit discoverable without confusing the repo's purpose.

---

## Scope Boundaries

### Deferred to Follow-Up Work

- Optional worksheet or checklist file for repeated use
- Automation helpers or notebooks
- A separate semiconductor-only companion skill if the core skill grows too broad

### Outside This Product's Identity

- Real-time dashboarding
- Broker integration
- Paid-data execution analytics

---

## Risks & Dependencies

- The framework could drift into generic options education if the prose stops anchoring on trend judgment.
- Regime naming could become too clever and too vague unless each regime is tied to observable signal combinations.
- Semiconductor context could either be too thin to matter or too large and distort the core skill; keep it secondary but present.

---

## Sources & Research

- `docs/brainstorms/2026-06-13-options-market-structure-toolkit-requirements.md`
- `skills/pb-semiconductor/SKILL.md`
- `skills/pb-semiconductor/REFERENCE.md`
- `skills/pb-semiconductor/EXAMPLES.md`
- `skills/peg-semiconductor/SKILL.md`
- `skills/peg-semiconductor/EXAMPLES.md`
- `docs/ideation/2026-06-13-options-market-structure-ideation.html`
