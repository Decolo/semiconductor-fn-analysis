# PEG/PSG: Reference

## Why PEG/PSG Exists

### The PB Blind Spot

`pb-semiconductor` covers heavy-asset cyclicals. A wafer fab is worth something even when it's losing money — you can touch the machines, estimate replacement cost, and anchor on book value.

An optical module designer has none of that. Their assets are:
- Engineers who design high-speed transceivers
- Customer relationships (design wins at NVIDIA, Google, Meta)
- Proprietary DSP algorithms and packaging know-how

None of these appear on the balance sheet. Book value is meaningless. PB is irrelevant.

### The PEG Insight

Peter Lynch popularized PEG: "A stock is fairly valued when PE equals its growth rate."

The logic: a company growing profits at 30% per year will double profits in ~2.5 years. Paying 30× PE for that is reasonable — you're buying future earnings at a discount to today's multiple. Paying 60× PE for 30% growth (PEG = 2) means you need the growth to persist much longer to break even.

### The PSG Necessity

When a company isn't profitable, PE doesn't exist. But you still need to answer: "Is this price insane, or does the growth justify it?"

PSG substitutes revenue growth for profit growth. It's a weaker signal — revenue doesn't equal value creation — but it's the best available when profits are negative or microscopic.

---

## The PEG Trap: When "Cheap PEG" Lies

### Trap 1: Cyclical Peak Earnings

```
Memory maker at cycle peak:
  PE = 8×, Profit Growth = 150% YoY
  PEG = 0.05 → "Screaming buy!"

6 months later:
  Oversupply → price crash → profit vanishes
  PE = ∞, PEG = undefined
```

The "150% growth" wasn't structural — it was the cycle. **PEG only works when growth is secular, not cyclical.**

### Trap 2: One-Time Gains

```
Company sells a building, books $500M gain.
  Net profit +200% YoY
  PEG = 0.5 → "Cheap!"

Core business actually grew 5%.
```

Always strip out non-recurring items. Use operating profit growth, not reported net profit.

### Trap 3: Margin Mean-Reversion

```
Company at 40% net margin (unsustainable peak):
  PE = 20×, Profit Growth = 30%
  PEG = 0.67 → "Undervalued!"

Margins normalize to 15%:
  PE becomes 53×, growth drops to 5%
```

Check whether current margins are sustainable or peaking. Use through-cycle margin estimates.

### Trap 4: The PSG "Revenue Mirage"

```
Company grows revenue 80% by selling $1.00 products for $0.70.
  PSG = 0.5 → "Great value!"

Gross margin = -30%.
Every dollar of "growth" destroys $0.30 of value.
```

**PSG must always be paired with gross margin analysis.** Revenue growth with declining margins is worse than no growth.

---

## Growth Quality Dimensions

### Dimension 1: Margin Trajectory

| Gross Margin Trend | Implication | PEG/PSG Adjustment |
|--------------------|-------------|-------------------|
| Rising (↑) | Pricing power, scale benefits kicking in | Premium justified |
| Flat (→) | Stable competitive position | Neutral |
| Declining (↓) | Competition, commoditization, price war | **Danger — cheap PEG is a trap** |

**Key question:** "If this company doubled revenue, would gross margin go up, stay flat, or go down?"

- Goes up → operating leverage (good)
- Stays flat → stable moat (acceptable)
- Goes down → they're buying growth (bad)

### Dimension 2: Growth Durability

Growth doesn't last forever. Estimate how many years the current growth rate can persist:

| Growth Driver | Typical Duration | Example |
|---------------|-----------------|---------|
| Technology monopoly | 5-10+ years | ASML EUV |
| Platform lock-in | 3-7 years | NVIDIA CUDA, MPS in GPU reference designs |
| Capacity catch-up | 2-4 years | New fab ramping to meet demand |
| Product cycle | 1-3 years | Single GPU generation |
| Price-driven share gain | 0-2 years | Undercutting competitors (reversible) |

Durability determines what PEG is reasonable:
- Growth durable for 5+ years → PEG up to 2.5× is acceptable
- Growth durable for 2-3 years → PEG should be ≤ 1.5×
- Growth dependent on single cycle → PEG must be < 1×

### Dimension 3: Growth Efficiency

Not all growth costs the same. Compare revenue growth to the spend required to generate it:

```
Growth Efficiency = Revenue Growth Rate ÷ (R&D% of Revenue + S&M% of Revenue)

> 1.5 : Efficient — growth is pulling its weight
1.0-1.5 : Moderate — growth covers its costs
0.8-1.0 : Expensive — spending heavily for growth
< 0.8 : Unsustainable — spending more than growth returns
```

Example: 杰华特
- Revenue growth: 58%
- R&D % of revenue: 36%
- S&M % of revenue: ~5%
- Growth Efficiency = 58 ÷ (36 + 5) = 1.41 → Moderate, slightly below efficient

Example: MPS
- Revenue growth: 26%
- R&D % of revenue: ~15%
- S&M % of revenue: ~5%
- Growth Efficiency = 26 ÷ (15 + 5) = 1.30 → Moderate, but high margin makes each unit of growth more valuable

---

## The PSG→PEG Graduation Criteria

When a company transitions from loss-making to profitable, its valuation framework shifts. Track these four signals:

### Signal 1: Gross Margin ≥ 35%
Without at least 35% gross margin, the path to meaningful net profit is too narrow. Below this threshold, PSG is the permanent framework — the company may never graduate.

### Signal 2: Operating Margin Turning Positive
The first sign that scale is converting to profit. Watch for:
- Two consecutive quarters of positive operating margin
- Operating leverage: revenue growth rate > opex growth rate

### Signal 3: Net Margin Turning Positive
The graduation trigger. When net profit turns positive:
- Forward PE becomes calculable → PEG can replace PSG
- First quarter of profitability may be noisy (one-time items). Wait for confirmation.

### Signal 4: Revenue Growth ≥ 30% at Crossover
If growth has already slowed below 30% by the time profitability arrives, the best part of the growth story is over. PEG may look reasonable but upside is limited.

### The Graduation Scorecard

```
Signals triggered:
  [ ] Gross Margin ≥ 35%
  [ ] Operating Margin positive (2 quarters)
  [ ] Net Margin positive
  [ ] Revenue Growth ≥ 30%

0-1 signals: Stay on PSG
2-3 signals: Transition watch — prepare PEG analysis
4 signals:  Switch to PEG
```

---

## Segment Split for Mixed Businesses

When only part of the business is high-growth, forcing PSG on total revenue produces nonsense.

### Method

1. Value the legacy segment at a reasonable mature-company multiple
   - Low-growth LED driver: 2-3× PS
   - Low-growth AC-DC: 3-5× PS

2. Subtract from market cap:
   ```
   Growth Segment Value = Market Cap − Legacy Segment Value
   ```

3. Apply PSG to the growth segment alone:
   ```
   Segment PS = Growth Segment Value ÷ Growth Segment Revenue
   Segment PSG = Segment PS ÷ Growth Segment Growth Rate
   ```

### Example: 晶丰明源

```
Market Cap: ¥310亿

Legacy segments:
  LED驱动 (¥7.78亿, -10% growth) → 2× PS = ¥15.6亿
  AC-DC (¥2.96亿, +8% growth) → 4× PS = ¥11.8亿
  电机控制 (¥4.00亿, +26% growth) → 6× PS = ¥24.0亿
  Total legacy value: ~¥51亿

HPC Growth Segment:
  Residual value: ¥310亿 − ¥51亿 = ¥259亿
  HPC Revenue: ¥0.96亿
  Segment PS: 259 ÷ 0.96 = 270×
  HPC Growth Rate: 122%
  Segment PSG: 270 ÷ 122 = 2.2

→ Premium, but explainable for a segment with 122% growth.
```

Without the split, raw PSG would be: 20 ÷ 4 = 5.0 (absurdly expensive). The split reveals that what you're really paying for — the HPC business — has a PSG of 2.2, which is premium but consistent with the growth rate.

---

## Cross-Framework Mapping

### When to use which framework

```
                    ┌──────────────────────────────┐
                    │ Is the company asset-heavy?   │
                    │ (Factories, equipment, mines) │
                    └──────────────┬───────────────┘
                           YES     │     NO
                    ┌──────────────┴──────────────┐
                    │   pb-semiconductor (PB)      │
                    │   Quality-adjusted PB         │
                    │   Capex readiness             │
                    │   Supply constraint durability│
                    └──────────────────────────────┘

                    ┌──────────────────────────────┐
                    │ Is the company profitable      │
                    │ with stable/rising margins?   │
                    └──────────────┬───────────────┘
                           YES     │     NO
                    ┌──────────────┴──────────────┐
                    │   PEG framework               │
                    │   PE ÷ Profit Growth           │
                    │   + Margin trajectory          │
                    │   + Growth durability          │
                    └──────────────────────────────┘

                    ┌──────────────┴──────────────┐
                    │   PSG framework               │
                    │   PS ÷ Revenue Growth          │
                    │   + Graduation tracking         │
                    │   + Segment split if needed    │
                    └──────────────────────────────┘
```

### Transition Between Frameworks

A single company can move through all three frameworks over its lifecycle:

```
Startup         → PSG (burning cash, revenue growing)
Scale-up        → PSG→PEG transition (approaching profitability)
Profitable growth → PEG (profits growing, margins expanding)
Mature/cyclical  → PE + ROIC (stable, dividend-paying)
```

The framework should match the company's current stage, not where you hope it will be in 3 years. **Using a later-stage framework too early is the most common valuation error in growth investing.**

---

## Sources and Attribution

This framework synthesizes:
- **Peter Lynch**: PEG ratio concept from "One Up on Wall Street" (1989)
- **labubu_trader / ShanghaoJin**: PB vs. PE scope gate for semiconductors; the insight that optical modules and fabless design need different frameworks
- **SaaS valuation practice**: PSG as the standard framework for unprofitable SaaS (Bessemer, a16z)
- **Michael Mauboussin**: ROIC and growth durability as quality adjustments to simple multiples
