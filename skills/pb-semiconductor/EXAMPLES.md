# PB-Semiconductor: Worked Examples

> Data in examples is from mid-2026. Prices, multiples, and fundamentals change. The *method* is what matters — apply the framework to current data, not these numbers.

## Example 1: MLCC Manufacturing — 风华高科 vs. 三环集团

### Raw Data (2026-06)

| | 风华高科 (000636) | 三环集团 (300408) |
|---|---|---|
| PB | 5.1 × | 10.75 × |
| 52w PB range | 1.3–5.6 × | 3.1–11.4 × |
| Gross Margin | 16.78% | 43.49% |
| Fixed Assets | 56.96 亿 | 60.04 亿 |
| Net Assets | ~120 亿 | ~224 亿 |
| FA / NA | ~47% | ~27% |
| Capex Status | ✅ 50亿定增已建成 | ⚠️ MLCC扩产延至2027 |
| PE (TTM) | — | — |

### Four-Dimensional Analysis

| Dimension | 风华高科 | Signal | 三环集团 | Signal |
|---|---|---|---|---|
| PB | 5.1× (52w低 1.3) | 🟢 low, rising | 10.75× (52w低 3.1) | 🔴 high, already ran |
| Gross Margin | 16.78% | 🔴 thin | 43.49% | 🟢 thick |
| **PB ÷ GM** | **30.4** | 🟡 | **24.7** | 🟢 |
| Capex Readiness | 50亿 done, producing | 🟢 | Delayed to 2027 | 🟡 |
| Supply Constraint | 5月暂停接单 | 🟢 | — | 🟡 |
| Downside Risk | Margin thin → fragile | 🔴 | Margin thick → resilient | 🟢 |

### Verdict

- **风华高科**: PB framework fit **Strong**. Lowest PB among major MLCC manufacturers, capex fully online, supply already tightening. Main risk: thin gross margin means no buffer if MLCC prices don't rise.
- **三环集团**: PB framework fit **Moderate**. Quality-adjusted PB is actually cheaper (24.7 vs. 30.4), but absolute PB has already expanded dramatically. Better quality, less upside remaining.

### Key Insight

Raw PB says 风华 is cheaper. Quality-adjusted PB says 三环 is cheaper. **Both can be right** depending on time horizon: 风华 has more PB repair upside, 三环 is the safer compounder.

---

## Example 2: PB Misfire — Why Upstream Materials Don't Fit

### 博迁新材 (605376)

| Metric | Value | Why PB Fails |
|---|---|---|
| PB | 26.6 × | Market isn't pricing the fixed assets |
| Fixed Assets | 11.46 亿 | Tiny relative to 460亿 market cap |
| FA / Net Assets | ~65% | Looks high, but... |
| Actual Value Driver | 80nm nickel powder monopoly | **Not on the balance sheet** |

The value is in the **technological monopoly** (only global supplier of 80nm nickel powder) and the **Samsung 4-year lock-in contract** (43-50亿). Neither appears in book value. Forcing a PB framework here produces the wrong answer (PB 26× looks "expensive" but the asset being priced isn't factories — it's the moat).

### Correct Anchor for Upstream Materials

| Company | Value Driver | Better Metric |
|---|---|---|
| 国瓷材料 | Dielectric powder #2 global, RE controls choking Japan | PE + certification pipeline progress |
| 博迁新材 | 80nm nickel monopoly, Samsung lock-in | Contract backlog / earnings visibility |
| 洁美科技 | Paper carrier tape >70% global, Samsung/Murata breakthrough | PE + market share trajectory |

---

## Example 3: Cross-Industry — Intel Foundry (per ShanghaoJin)

### The Trade

Intel at PB 1×. TSMC at PB 7×. Chinese DUV fabs (zero output) also at PB 1×.

### Framework Application

| Dimension | Intel |
|---|---|
| PB | 1× — absurdly low for a co with EUV + 2nm capability |
| Asset Quality | Only 2 companies globally can do 2nm (Intel + TSMC); Samsung at 30% yield doesn't count |
| Capex Readiness | EUV equipment already installed |
| Supply Constraint | 2nm capacity is structurally scarce |
| Downside | If 2nm fails, PB might go to 0.5× — but yield is a "one-sided function" (only improves) |

### Outcome Thesis

PB 1× → 6-7× over 3 years as 2nm yield improves. Yield improvement → asset re-rating → PB expansion. This is the purest form of the PB-first framework: bet on undervalued productive capacity that can only get better.

---

## Example 4: WF₆ / Specialty Chemicals — 中船特气 (688146)

### Context

Japan effectively halted tungsten exports to Japan (APT export 0 tons Jan-Apr 2026). 关东电化 likely curtailing WF₆ production. 中船特气 #1 globally at 2,000t capacity.

### Framework Application

| Dimension | 中船特气 |
|---|---|
| PB | ~? × (need current data) |
| Asset Quality | #1 global WF₆ capacity — scarce and hard to replicate |
| Capex Readiness | 2,000t already online |
| Supply Constraint | Japan export halt = structural, not cyclical |
| Policy Risk | **HIGH** — if China relaxes tungsten export controls, the monopoly window closes |

### Verdict

PB framework fit **Moderate with policy risk flag**. The supply constraint is real and verified (customs data), but it's policy-driven, not technology-driven. This is the most fragile type of scarcity.

---

## Quick Sieve Results (A-Share MLCC Ecosystem)

Applying `PB < 12× + GM > 15% + FA/NA > 40%` to known names:

| Company | PB | GM | FA/NA | Result |
|---|---|---|---|---|
| 风华高科 | 5.1× | 16.78% ✅ | ~47% ✅ | **Pass** (GM at edge — flag downside risk) |
| 三环集团 | 10.75× ✅ | 43.49% ✅ | ~27% ❌ | **Flag** (FA/NA low — more IP/tech than pure capacity) |

> The sieve doesn't reject these — it tells you what to scrutinize. 风华's thin margin means fragile thesis. 三环's low FA/NA means PB may understate the true asset base (goodwill, IP). Both are valid; the framework helps you know what you're betting on.
