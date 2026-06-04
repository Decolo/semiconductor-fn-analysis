# PEG/PSG: Worked Examples

> Data in examples is from mid-2026. Prices, multiples, and fundamentals change. The *method* is what matters — apply the framework to current data, not these numbers.

## Example 1: Optical Module Leader — 中际旭创 (300308)

The textbook PEG case. Profitable, high-growth, asset-light, margins expanding.

### Raw Data (FY2025)

| Metric | 2025 | 2024 | YoY |
|--------|------|------|-----|
| Revenue | 382.4 亿 | 238.6 亿 | +60% |
| Net Profit | 108.0 亿 | 51.7 亿 | +109% |
| EPS | 9.80 元 | 4.72 元 | +108% |
| Gross Margin | 42.0% | 33.8% | +8.2ppt |
| Net Margin | ~28% | ~22% | +6ppt |
| ROE | 43.8% | 31.2% | +12.6ppt |
| Overseas Revenue | 91% | — | — |

### PEG Analysis

```
Stock Price: ~¥700
Market Cap: ~¥7,700 亿
PE (static, FY2025): 700 ÷ 9.80 ≈ 71×
Net Profit Growth: 109%
Static PEG: 71 ÷ 109 = 0.65

Forward (2026E):
  Consensus net profit: ¥204-246 亿 (growth 89-128%)
  Forward PE: 7,700 ÷ 225 ≈ 34× (midpoint)
  Forward PEG: 34 ÷ 108 ≈ 0.31
```

### Growth Quality Check

| Dimension | Data | Signal |
|-----------|------|--------|
| **PEG** | Static 0.65, Forward 0.31 | 🟢 Undervalued by PEG |
| **Margin Trajectory** | GM 34% → 42%, still rising (Q4: 44.5%) | 🟢 Strong upward |
| **Growth Durability** | 800G #1 globally, 1.6T ramping; AI capex multi-year | 🟢 3-5 year visibility |
| **Growth Efficiency** | R&D + S&M ~8% of revenue, growth 60% → efficiency 7.5 | 🟢 Highly efficient |

### Verdict

**PEG framework fit: Strong.** Static PEG 0.65 and forward PEG 0.31 are both well below 1.0 — deeply undervalued on this metric. Growth quality is excellent: margins are expanding (not buying growth), 800G leadership is durable, and 1.6T provides the next leg.

### Why Is PEG So Low?

The market is pricing in three fears that PEG doesn't capture:
1. **Customer concentration**: 91% overseas revenue. Geopolitical risk (tariffs, export controls).
2. **Cycle risk**: If AI capex slows, 1.6T orders could disappoint.
3. **Competition**: 新易盛, 天孚, Coherent are all chasing the same 1.6T market.

PEG says "cheap." Your job is to decide whether these fears are overblown or legitimate. **PEG quantifies the opportunity; it doesn't replace judgment on the risks.**

---

## Example 2: AI Power IC — 杰华特 (688141)

The PSG case. High growth, still burning cash. Framework is PSG with graduation watch.

### Raw Data (FY2025)

| Metric | Value |
|--------|-------|
| Revenue | 26.55 亿 (+58%) |
| DC-DC Revenue | 14.15 亿 (+56%) |
| Net Profit | **-7.17 亿** (loss widened) |
| Gross Margin | 26.4% (declining, -1ppt YoY) |
| R&D % of Revenue | 36% |
| Market Cap | ~¥440 亿 |

### PSG Analysis

```
PS = 440 ÷ 26.55 = 16.6×
Revenue Growth = 58%
PSG = 16.6 ÷ 58 = 0.29

→ PSG < 0.5 suggests undervaluation
```

### Growth Quality Check

| Dimension | Data | Signal |
|-----------|------|--------|
| **PSG** | 0.29 | 🟢 Cheap on PSG |
| **Margin Trajectory** | GM 26%, declining | 🔴 Danger signal |
| **Growth Durability** | Huawei ecosystem, DrMOS国产替代 | 🟡 2-3 years, policy-dependent |
| **Growth Efficiency** | 58 ÷ (36+5) = 1.41 | 🟡 Moderate |
| **R&D Burden** | 36% of revenue — 9.57亿 burn | 🔴 Heavy |

### Graduation Watch

| Signal | Status |
|--------|--------|
| Gross Margin ≥ 35% | ❌ 26%, declining |
| Operating Margin positive | ❌ Deeply negative |
| Net Margin positive | ❌ -27% |
| Revenue Growth ≥ 30% | ✅ 58% |

**Score: 1/4.** Nowhere near graduation. Stay on PSG.

### Verdict

**PSG framework fit: Strong, but with caution flags.** PSG 0.29 says cheap. But declining gross margin and 36% R&D burn rate mean this "cheapness" could be a value trap if the company can't convert revenue growth to profit.

The bull case: if revenue hits ¥50亿 and R&D stays flat at ¥10亿, R&D ratio drops to 20% — suddenly the P&L works. That's the operating leverage bet embedded in the PSG 0.29.

---

## Example 3: Mixed Business — 晶丰明源 (688368)

PSG with segment split. A low-growth legacy business hides a high-growth AI power chip business.

### Raw Data (FY2025)

| Segment | Revenue | Growth | Gross Margin |
|---------|---------|--------|-------------|
| LED 驱动 | 7.78 亿 | -10% | 34% |
| AC-DC 电源 | 2.96 亿 | +8% | 41% |
| 电机控制 | 4.00 亿 | +26% | 47% |
| **HPC 电源** | **0.96 亿** | **+122%** | 37% |
| **Total** | **15.70 亿** | **+4%** | **39%** |

```
Market Cap: ~¥310 亿
Net Profit: ¥0.36 亿 (PE ~861× — meaningless)
```

### Naive PSG (Wrong)

```
PS = 310 ÷ 15.70 = 19.7×
Total Revenue Growth = 4%
PSG = 19.7 ÷ 4 = 4.9 → Absurdly expensive
```

This doesn't make sense because the 4% total growth hides the HPC business growing at 122%.

### Segment-Split PSG (Correct)

```
Legacy segments valuation:
  LED 驱动 (declining): 2× PS → ¥15.6 亿
  AC-DC (low growth): 4× PS → ¥11.8 亿
  电机控制 (mid growth): 6× PS → ¥24.0 亿
  Total legacy: ~¥51 亿

HPC Growth Segment:
  Residual value: ¥310 − ¥51 = ¥259 亿
  HPC PS = 259 ÷ 0.96 = 270×
  HPC PSG = 270 ÷ 122 = 2.2

→ Premium, but justifiable for 122% growth
```

### Graduation Watch

| Signal | Status |
|--------|--------|
| Gross Margin ≥ 35% | ✅ 37% (HPC), 39% (overall) |
| Operating Margin positive | ✅ Barely positive |
| Net Margin positive | ✅ ¥0.36亿, thin but positive |
| Revenue Growth ≥ 30% | ❌ 4% overall, but ✅ 122% for HPC |

**Score: 3/4 (using HPC segment).** Close to PEG transition for the growth segment.

### Verdict

**PSG framework fit: Strong with segment split required.** The key insight: 94% of revenue is low-growth, but the market is pricing the 6% that's growing 122%. Segment-split PSG of 2.2 is expensive but within range for a company with NVIDIA OpenVReg certification and a complete VPD product portfolio.

The risk: if HPC growth decelerates before reaching meaningful scale (¥5亿+), the premium multiple collapses. The reward: if HPC revenue hits ¥10亿 at 122% CAGR, PSG compresses rapidly to reasonable levels.

---

## Example 4: The Benchmark — MPS / MPWR (NASDAQ)

This is what 杰华特 and 晶丰明源 aspire to become. Use MPS as the PEG benchmark to calibrate expectations.

### Raw Data (FY2025)

| Metric | Value |
|--------|-------|
| Revenue | $27.9 亿 (+26%) |
| Net Profit (GAAP) | ~$6.2 亿 |
| Gross Margin | 55.2% |
| Net Margin | ~22% |
| ROIC | 25% |
| Cash / Debt | $14.6亿 / ~$0 (zero debt) |
| Market Cap | ~$420 亿 |

### PEG Analysis

```
PE (TTM): ~68×
Net Profit Growth: ~25-30% (estimated)
PEG: 68 ÷ 27 = 2.5×

→ PEG > 2 suggests overvaluation by the simple formula
```

### Why PEG 2.5× is acceptable for MPS

| Quality Factor | MPS Score | Why It Justifies Premium |
|----------------|-----------|--------------------------|
| Gross Margin | 55% | Moat-level margins — each dollar of growth is 2× more valuable than average |
| Margin Durability | 10+ years | Proprietary BCD process + NVIDIA reference design lock-in |
| ROIC | 25% | Growth creates value, not destroys it |
| Balance Sheet | Net cash | Zero financial risk |
| Growth Visibility | 3-5 years | Rubin, Kyber, 1MW rack — growth pipeline is secured |

The "fair" PEG for MPS is not 1.0 — it's closer to 2.0 given the quality. At 2.5×, it's slightly above fair value. **The market is pricing MPS like a compounder, not a cyclical.** This is the right treatment.

### Comparison: MPS vs. Chinese Challengers

| | MPS (MPWR) | 杰华特 | 晶丰明源 (HPC) |
|------|------|------|------|
| Gross Margin | 55% | 26% | 37% |
| Net Margin | 22% | -27% | ~2% |
| ROIC | 25% | Negative | ~2% |
| PEG / PSG | PEG 2.5 | PSG 0.29 | PSG 2.2 |
| Framework | PEG (mature) | PSG (burn) | PSG (transition) |
| Growth Rate | 26% (stable) | 58% (revenue) | 122% (HPC rev) |

The gap between MPS and its Chinese challengers is enormous — but so is the growth rate gap. The question isn't "are they as good as MPS?" It's "can they close the gap fast enough to justify the PSG?"

---

## Example 5: PEG/PSG Misfire — Wolfspeed (WOLF)

Wolfspeed in 2025-2026 looked like a growth story: SiC for EVs and AI data centers. But neither PEG nor PSG would have saved you — because the margins were never real.

### The Trap

```
Wolfspeed FY2025:
  Revenue: ~$800M (declining, not growing)
  Gross Margin: -27% (selling below cost)
  Net Loss: widening
  
  PSG? PS ~3.7×, Revenue Growth negative → meaningless
  PEG? PE is negative → can't calculate
  
  Yet the stock rallied 250% YTD in 2026 on "AI data center SiC" narrative.
```

### Why Both Frameworks Failed

| Framework | What It Would Say | Reality |
|-----------|-------------------|---------|
| PSG | Can't apply (revenue declining) | "Growth" was a narrative, not in the numbers |
| PEG | Can't apply (negative profit) | Price was driven by short-squeeze + AI hype |
| PB | PB was distorted post-bankruptcy | Assets impaired, 200mm yields unproven |

**The fix**: when a company has negative gross margins and declining revenue, no growth framework applies. You're not buying growth — you're buying a narrative. The scope gate should reject it: "If gross margin is negative and revenue is declining, stop. This is a turnaround/special-situation bet, not a growth investment."

### The Scope Gate in Action

```
中际旭创 → 42% GM, expanding, 109% profit growth → PEG framework ✅
杰华特 → 26% GM, declining, 58% revenue growth → PSG framework ✅ (with caution)
Wolfspeed → -27% GM, declining revenue → Neither ❌ → Narrative/special-situation
```

The framework you choose determines the answer you get. **Choosing the wrong framework is the single biggest valuation mistake in semiconductor investing.** Sometimes the right answer is: "None of the above — this isn't an investment, it's a bet."
