---
name: pb-semiconductor
description: PB-first analysis framework for heavy-asset cyclical semiconductor companies (MLCC, foundries, memory, specialty chemicals). Use when analyzing semiconductor manufacturing stocks, comparing valuations in cyclical sectors, or when user mentions PB analysis, 市净率, 重资产周期品, MLCC valuation, or foundry investment.
---

# PB-First Semiconductor Analysis

Analyze heavy-asset cyclical semiconductor manufacturing companies through a PB-priority lens. PE distorts during cycles; PB provides a more stable anchor for asset-heavy, commoditized manufacturing.

## Scope Gate: Does PB Apply?

### ✅ PB is the right anchor
- MLCC / passive component manufacturing
- Wafer foundries (mature and advanced nodes)
- Memory / storage (DRAM, NAND)
- Specialty chemicals with manufacturing moats (WF₆, electronic gases)

Why: heavy fixed assets, cyclical pricing, commoditized output. PE at cycle peak = value trap.

### ❌ PB is the wrong anchor
- Upstream materials with tech moats (dielectric powders, nickel powder, carrier tape) — value is in IP/certifications, not fixed assets
- Fabless chip design — differentiated products, PE works fine
- Optical modules / ASICs — product iteration drives margin expansion, PE works
- Equipment makers — order book matters more than book value

## Core Framework: Four-Dimensional Screen

For each candidate, score across four dimensions:

### 1. PB (Asset Cheapness)
- Current PB vs. 52-week range vs. peer average
- Key insight: **PB repair trajectory > absolute PB level**. A stock at PB 5× rising from 1.3× may have more room than one at PB 11× that already ran from 4.7×.

### 2. Gross Margin (Asset Quality)
- Same PB, different gross margin = completely different assets
- **PB ÷ Gross Margin** = effective price per unit of quality capacity
  - Example: 风华 PB 5.1 ÷ 16.8% = 30.4 vs. 三环 PB 10.75 ÷ 43.5% = 24.7 → 三环 is actually cheaper on quality-adjusted basis
- Low gross margin + low PB can be a value trap, not a bargain

### 3. Capex Readiness (Capacity Online)
- Fixed Assets / Net Assets ratio — is the book value "real"?
- Construction-in-progress / Fixed Assets — how much capacity is still not producing?
- Only count capacity that is **already online and producing**

### 4. Price Increase Sustainability (Optionality Quality)
- Supply-side: competitor shutdowns, export controls, capacity retirement
- Demand-side: AI/server/auto capex trajectory, 3D NAND layer count acceleration
- Duration: how many quarters can tight supply last?
- Policy risk: can the supply constraint be reversed by political decisions?

## Downside Protection

For every candidate, answer: **"If prices don't rise, how much do I lose?"**

- Low gross margin companies (e.g., 风华 17%) are more vulnerable — no margin buffer
- High gross margin companies (e.g., 三环 43%) have a cushion
- Policy-driven scarcity (export controls) is more fragile than technology-driven scarcity

## Analysis Output Template

```markdown
## [Company Name] ([Ticker])

| Dimension | Data | Signal |
|-----------|------|--------|
| PB | [value] × (52w range: [low]–[high]) | 🟢/🟡/🔴 |
| Gross Margin | [value] % | 🟢/🟡/🔴 |
| PB ÷ GM (quality-adjusted) | [value] | 🟢/🟡/🔴 |
| Fixed Assets / Net Assets | [value] % | 🟢/🟡/🔴 |
| Capex Online Ratio | [value] % | 🟢/🟡/🔴 |
| Supply Constraint Durability | [quarters / risk level] | 🟢/🟡/🔴 |

### Verdict
[Fit to PB framework: Strong / Moderate / Weak]
[Key catalyst]
[Downside risk if thesis breaks]

### Peer Ranking
[Comparison table with quality-adjusted PB and ranking]
```

## Three-Indicator Quick Sieve

When scanning many names, use this preliminary filter. It catches obviously unsuitable candidates — not a hard gate. Human override is expected.

```
PB < 12× + Gross Margin > 15% + Fixed Assets / Net Assets > 40%
```

Failing one dimension is a **flag, not a rejection**. A company that fails on GM (like 风华 17%) can still be a valid PB play — just with higher downside risk. A company that fails on PB (like 三环 10.75×) may be the quality compounder you want instead. The sieve surfaces which dimension to scrutinize, not a binary pass/fail.

## Cross-Industry Analogy Check

Borrow from mature cyclical industries:
- **Shipping**: PB + fleet age + orderbook/ fleet ratio → map to PB + node/line generation + construction-in-progress/capacity ratio
- **Oil & Gas**: PB + reserve replacement ratio → map to PB + capacity addition / demand growth ratio

See [REFERENCE.md](REFERENCE.md) for detailed methodology and [EXAMPLES.md](EXAMPLES.md) for worked cases.

## Data Sources

Preferred lookup order for agents:

1. **PB, market cap, 52-week range** — Yahoo Finance, Eastmoney (东方财富), TradingView
2. **Gross margin, FA/NA, capex status** — Company annual/interim reports (资产负债表 + 利润表)
3. **Supply constraint signals** — Industry news (price hike announcements, competitor shutdowns), customs data (export volumes)
4. **Peer comparison** — Same-sector listed companies, cross-check PB ranges
