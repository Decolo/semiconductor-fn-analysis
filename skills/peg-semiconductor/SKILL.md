---
name: peg-semiconductor
description: PEG/PSG growth-valuation framework for asset-light high-growth semiconductor companies (optical modules, fabless chip design, AI power ICs). Companion to pb-semiconductor. Use when analyzing growth semiconductor stocks, comparing PEG/PSG valuations, or when user mentions PEG, PSG, 成长股估值, 光模块, or growth stock valuation.
---

# PEG/PSG Growth-Valuation Framework

Valuation framework for asset-light, high-growth companies where PB is irrelevant. Two variants depending on profitability stage: **PEG** for profitable growth, **PSG** for unprofitable growth.

## Scope Gate: PEG, PSG, or Neither?

### ✅ PEG applies (profitable growth)

- Optical modules / transceivers (中际旭创, 新易盛, 天孚通信)
- Fabless chip design with differentiated products (AI ASICs, GPUs)
- High-margin analog/mixed-signal IC in steady growth (MPS)
- SaaS / recurring revenue with visible margin expansion

Why: differentiated products, pricing power, high and stable/improving gross margins. Growth is real and drops to the bottom line.

### ✅ PSG applies (unprofitable growth)

- Fabless design in R&D burn phase (杰华特)
- Early-stage high-growth where profit is thin or negative (晶丰明源 HPC)
- Companies transitioning from heavy R&D investment to monetization
- Revenue doubling year-over-year but margins haven't caught up yet

Why: the company isn't profitable, so PEG is mathematically meaningless. But revenue is growing rapidly and there's a path to profitability.

### ❌ Neither applies

- Heavy-asset cyclical manufacturing → use **PB framework** (pb-semiconductor)
- Commodity manufacturers with no pricing power → use PB or PE-cycle-adjusted
- Deep value / no growth → use traditional PE/PB hybrid
- Financials / real estate → use PB/ROE, not PEG

### The Decision Tree

```
Is the company asset-light (Fabless/SaaS/IP-driven)?
  │
  ├── NO → Use PB framework (pb-semiconductor)
  │
  └── YES → Is it profitable with stable/improving margins?
        │
        ├── YES → Use PEG
        │
        └── NO → Use PSG, track graduation to PEG
```

---

## Framework A: PEG (Profitable Growth)

### Formula

```
PEG = PE ÷ Net Profit Growth Rate (%)

  PE = Market Cap ÷ Net Profit (TTM or forward)
  Growth Rate = YoY net profit growth % (use forward estimate when available)

PEG < 1   → Undervalued
PEG = 1   → Fair value
PEG 1-2   → Premium, but acceptable for high-quality growth
PEG > 2   → Expensive — needs very strong conviction
```

### Growth Quality Adjustment

Raw PEG can be misleading. Not all growth is equal. Apply two quality checks:

**1. Margin Trajectory (↑ → premium justified, ↓ → cheap PEG is a trap)**
- Gross margin stable or improving → growth is high-quality
- Gross margin declining → "growth" may be bought with price cuts

**2. Growth Durability (how many years can this sustain?)**
- Visible growth pipeline ≥ 3 years → premium justified
- Growth dependent on single product cycle → discount
- Ask: "What kills this growth? When?"

For advanced quality metrics including growth efficiency analysis, see [REFERENCE.md](REFERENCE.md).

### Quick PEG Sieve

```
PEG < 1.5 + Gross Margin > 35% + Net Margin > 10%
```

Candidates that pass all three are high-quality growth at a reasonable price.

---

## Framework B: PSG (Unprofitable Growth)

### Formula

```
PSG = PS ÷ Revenue Growth Rate (%)

  PS = Market Cap ÷ Revenue (TTM)
  Growth Rate = YoY revenue growth %

PSG < 0.5 → Potentially undervalued (rare)
PSG 0.5-1.0 → Reasonable
PSG 1.0-2.0 → Premium
PSG > 2.0 → Expensive — needs extraordinary growth to justify
```

### Why PSG Exists

When a company is losing money, PE and PEG are meaningless. PSG is the fallback: "I can't measure your profit yet, so let's at least see if your revenue growth justifies your price."

PSG is **inferior** to PEG. It's what you use when you have no choice. The entire PSG framework is a temporary bridge — you're betting the company crosses to profitability before growth slows.

### The PSG→PEG Graduation

Track these signals for the transition:

| Signal | Threshold |
|--------|-----------|
| Gross margin | ≥ 35% and stable/rising |
| Operating margin | Turning positive (within 2 quarters) |
| Net margin | Turning positive (within 4 quarters) |
| Revenue growth | Still ≥ 30% at profitability crossover |

When 3 of 4 signals trigger: **switch from PSG to PEG.**

### Segment Split for Mixed Businesses

When a company has both growth and legacy segments (e.g., 晶丰明源):

1. Value the legacy business separately (low PS or PE multiple)
2. Subtract legacy value from market cap → residual value
3. Apply PSG to the growth segment alone using residual value
4. This gives a truer picture than applying PSG to total revenue

---

## Cross-Framework Map

```
Company Lifecycle:

  Heavy Asset             Asset-Light Growth
  ───────────             ──────────────────

  Building factory        R&D investment phase
       │                       │
       ▼                       ▼
  PB framework            PSG framework
  (pb-semiconductor)      (this skill)
       │                       │
       ▼                       ▼
  Capacity online,        Profit inflection
  cycle recovery               │
       │                       ▼
       ▼                  PEG framework
  PE-cycle-adjusted       (this skill)
                               │
                               ▼
                          Mature, stable
                          PE + ROIC
```

---

## Output Template

```markdown
## [Company Name] ([Ticker])

### Stage: PEG / PSG / Graduation Watch

| Dimension | Data | Signal |
|-----------|------|--------|
| PE / PS | [value] × | |
| Growth Rate (NP / Rev) | [value] % | |
| Raw PEG / PSG | [value] | 🟢/🟡/🔴 |
| Gross Margin | [value] % | 🟢/🟡/🔴 |
| Margin Trajectory | ↑/→/↓ | 🟢/🟡/🔴 |
| Growth Efficiency | [value] | 🟢/🟡/🔴 |

### Quality-Adjusted PEG/PSG: [value]

### Verdict
[Framework fit: Strong / Moderate / Weak]
[Key catalyst for re-rating]
[Risk: what kills the growth story?]

### Graduation Watch (PSG only)
[Which signals have triggered? Which are pending?]
```

---

## Common Pitfalls

1. **Using PEG for cyclicals** — a memory maker at cycle peak has low PE and high profit growth → low PEG. This is a trap. The "growth" is cyclical, not structural.
2. **Confusing revenue growth with value creation** — PSG doesn't care about margins. A company can grow revenue 100% with -50% gross margins. PSG says "cheap." Your wallet says otherwise.
3. **Ignoring share dilution** — growth funded by massive SBC/share issuance is lower quality than organic growth. Check shares outstanding trend.
4. **Single-year snapshots** — PEG uses one year's growth. Look at 2-3 year forward CAGR for durability.
5. **Using PSG when PEG works** — if a company is profitable, use PEG. PSG is the fallback, not the first choice.

See [REFERENCE.md](REFERENCE.md) for detailed methodology and [EXAMPLES.md](EXAMPLES.md) for worked cases.

For hybrid names with legacy revenue plus a high-expectation new technology platform, see [MIXED-OPTIONALITY.md](MIXED-OPTIONALITY.md). Use that when a company is being re-rated by a new packaging/substrate/process story that is still too small for normal PEG/PSG to explain on a full-company basis.

## Data Sources

Preferred lookup order for agents:

1. **PE, PS, market cap** — Yahoo Finance, Eastmoney (东方财富), TradingView
2. **Revenue/net profit growth, gross margin, segment breakdown** — Company annual/interim reports, earnings presentations
3. **Growth durability signals** — Product roadmaps, customer announcements, industry capex trends, analyst day transcripts
4. **Graduation tracking** — Quarterly reports for margin trajectory, operating leverage, R&D spend ratio
