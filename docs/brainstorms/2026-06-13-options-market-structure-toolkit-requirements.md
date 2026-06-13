---
date: 2026-06-13
topic: options-market-structure-toolkit
---

# Brainstorm: Options Market Structure Toolkit

## Summary

Add a new market-structure skill family to `semiconductor-fn-analysis`, anchored by a flagship skill that helps a trend trader read options-market signals without turning the repo into an options-trading or execution product.

The first release should be document-first, matching the repo's current style: one primary skill, one reference layer that translates signals into regimes, and one examples layer that shows how to use the framework on real market setups.

---

## Problem Frame

The repo currently helps with valuation framework selection for semiconductor investing, but it has no framework for reading broad market conditions. The user wants an options-market lens not to trade `call`/`put` contracts directly, but to answer a more useful question for trend trading:

> Is options positioning currently confirming trend, warning of fragility, or implying a higher chance of chop, squeeze, or panic?

Most open-source options tooling stops at raw metrics like `put/call`, `IV`, `skew`, or `gamma exposure`. That is useful for specialists but weak for discretionary traders. The gap this toolkit should fill is interpretation.

---

## Users

### Primary user

- A discretionary trader or investor who already understands trend and price action
- Wants to use options market structure as context, not as the primary trading instrument
- Needs a concise workflow that turns options signals into market-state judgment

### Secondary user

- A semiconductor-focused investor who wants to connect index options context back to `QQQ`, `SOXX`, `NVDA`, and semi names

---

## Goals

1. Give the user a reusable way to read options-market structure for trend context.
2. Translate raw options signals into plain-English market regimes.
3. Show how the framework behaves on real examples so it is usable, not just educational.
4. Preserve the repo's current identity as a curated framework library rather than a trading dashboard or code-heavy analytics product.

---

## Non-Goals

- Teaching the mechanics of buying or selling options contracts
- Recommending specific options trades or strikes
- Building a real-time scanner, dashboard, or execution system in the first release
- Depending on premium data feeds to make the first version usable

---

## Key Decisions

### 1. Document-first, not software-first

The first release should follow the existing pattern in this repo: `SKILL.md` + reference material + examples. It should not begin with a Python package, CLI, or web app.

### 2. Interpretation over raw analytics

The flagship skill should answer "what does this imply for trend conditions?" rather than "what are today's option chain metrics?"

### 3. Regime language is required

The toolkit should not stop at metric explanation. It must define a small set of regime states such as:

- trend confirmation
- squeeze risk
- panic hedge
- range compression
- fragile melt-up

### 4. Examples are part of the product, not optional garnish

Without worked cases, the framework will read as market lore. Example scenarios should be present in the first release.

### 5. Semiconductor relevance should be present but not dominate the core

The core framework should work on broad equity index context first. Semiconductor-specific interpretation should be included as a companion angle, not as the only use case.

---

## Requirements

### R1. Add a flagship skill

Create a new skill that explains when to use options-market structure in trend trading, what signals to check, and how to convert those signals into a judgment.

### R2. Add a regime translation layer

Define a compact state model that maps combinations of options signals into named market regimes.

### R3. Add a data-confidence layer

Document which inferences are safe with free or delayed sources and which claims require higher-quality data.

### R4. Add worked examples

Provide multiple case templates showing how the framework behaves in different market conditions.

### R5. Keep the repo coherent

Update the root README so the new skill is discoverable and clearly distinguished from valuation frameworks.

### R6. Preserve low carrying cost

The first release should add value without requiring ongoing software maintenance, API credentials, or execution infrastructure.

---

## Acceptance Examples

### AE1. Broad market trend check

A user asks whether current options structure is supporting an ongoing equity uptrend. The skill walks through `put/call`, `IV`, `skew`, `gamma`, and strike concentration, then outputs a regime-style conclusion such as "trend confirmation with squeeze risk" plus caveats.

### AE2. Fragile rally interpretation

A user sees price rising but also sees elevated skew and nervous hedging. The skill explains why this can still be a fragile melt-up instead of a clean trend confirmation.

### AE3. Semiconductor lens

A user wants to understand whether bullish activity in `NVDA` options is confirming the whole semiconductor tape or distorting it. The toolkit explains how to separate broad index context from single-name options effects.

### AE4. Data-source caution

A user wants to infer intraday dealer positioning from a weak or delayed feed. The toolkit explicitly warns that the inference quality is low and downgrades the confidence of any conclusion.

---

## Scope Boundaries

### In Scope

- New skill folder under `skills/`
- Primary `SKILL.md`
- Reference material for signals, regimes, and data-confidence rules
- Examples material with real-use templates
- Root README update for discovery

### Deferred for Later

- Scripts or notebooks that calculate metrics automatically
- A structured checklist artifact or worksheet format
- A separate semiconductor-only companion skill

### Outside This Product's Identity

- Broker integration
- Real-time alerting or scanners
- Paid-data-heavy analytics product
- Options trade recommendation engine

---

## Success Criteria

- A new user can understand what the skill is for in under two minutes.
- A trend trader can use the framework without needing to trade options directly.
- The regime layer is small enough to remember and specific enough to use.
- The examples make the framework feel operational rather than theoretical.
- The new skill feels like a natural extension of the existing repo rather than a different product jammed into it.

---

## Outstanding Questions

- Should semiconductor-specific context stay inside the core reference file or split into a later companion file?
- Should future automation live inside this repo or remain external and feed into the document-first skills?
