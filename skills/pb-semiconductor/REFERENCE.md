# PB-Semiconductor: Reference

## Why PB > PE for Heavy-Asset Cyclicals

### The PE Trap

A memory maker at the cycle peak:
- Revenue surges → Net profit explodes → PE looks cheap (e.g., 8×)
- Analyst buys because "8× PE is cheap for a semiconductor company"
- 6 months later: oversupply → price crash → profit vanishes → PE becomes infinite
- The "cheap PE" was an illusion — it was cheap only at the peak

PE measures **current profitability**, which is the most misleading signal in a cycle.

### The PB Anchor

The same memory maker:
- Fab costs $20B to build, $15B on the balance sheet
- Market cap $30B → PB = 2×
- Memory price crash → profit gone, but the fab is still worth at least replacement cost
- PB provides a floor based on **what it would cost to recreate the capacity**

PB measures **productive capacity**, which doesn't evaporate when prices fall.

### When PE DOES Work

PE is valid when the product is differentiated and margins are stable/improving:
- Fabless chip design (NVIDIA, AMD, 海光信息)
- Optical modules (产品有迭代, 毛利率提升)
- EDA tools / IP licensing

The test: **if the product is a commodity where the lowest-cost producer wins, use PB. If the product has pricing power from differentiation, PE is acceptable.**

---

## The Four Dimensions in Detail

### Dimension 1: PB (Asset Cheapness)

**What to look at:**
- Current PB vs. 52-week low and high
- PB vs. industry peer group
- PB repair distance: how far has it already moved from the cycle low?

**Interpretation:**
- PB near 52w low + catalyst for re-rating = highest upside
- PB near 52w high + catalyst fully priced = limited upside regardless of thesis quality
- PB driven entirely by market sentiment, not asset changes = fragile

**Watch out for:**
- PB that's low because assets are impaired (stranded capacity, obsolete nodes)
- PB that's low because of excessive dilution / share issuance
- Cross-border PB comparisons without accounting adjustment (depreciation methods differ)

### Dimension 2: Gross Margin (Asset Quality)

**The core insight:** Two companies with identical PB can have completely different asset quality. A factory making 43% gross margin products is worth more than one making 17% — but PB treats them the same.

**Quality-Adjusted PB = PB ÷ Gross Margin**

This tells you: "How much am I paying for each unit of *quality* capacity?"

Lower is better. A company at PB 10× with 50% GM (adjusted = 20) is cheaper than one at PB 5× with 15% GM (adjusted = 33).

**Limitations:**
- Gross margin can also be cyclical (input costs, utilization rates)
- Not all low GM is bad — early-stage capacity ramping depresses GM temporarily
- The adjustment should use normalized/through-cycle GM, not peak/trough

### Dimension 3: Capex Readiness

**The test: "Is the oven already baking bread?"**

Three checks:
1. **Fixed Assets / Net Assets** — confirms the assets are "real" (manufacturing), not financial or intangible
2. **Construction-in-Progress / Fixed Assets** — lower is better; high CiP means capacity isn't online yet
3. **Depreciation / Fixed Assets** — aging equipment may have low book value but also low productivity

**Capex Readiness Spectrum:**
```
Fully Online          Ramping           Building          Planning
    ✅                  ⚠️                 ❌                 ❌
(风华 post-定增)    (炬火成都基地)    (三环MLCC延至27)  (Kaz Resources)
```

### Dimension 4: Supply Constraint Durability

**Types of supply constraints (most durable to most fragile):**

1. **Technology monopoly** (most durable) — Only you can make it (博迁 80nm nickel)
   - Hardest to break, longest duration
   
2. **Capacity lead time** — Takes 3-5 years to build new capacity (TSMC 2nm, WF₆ plants)
   - Competitors can eventually enter, but slowly
   
3. **Competitor exit / structural decline** — Competitor shuts down (关东电化 WF₆)
   - Can reverse if economics improve, but unlikely in short term
   
4. **Policy / export control** (most fragile) — Government restricts supply (China RE export controls)
   - Can reverse overnight with a political decision
   - Requires constant monitoring of policy signals

**Duration estimate:**
- Tech monopoly: 5-10+ years
- Capacity lead time: 2-4 years
- Competitor exit: 1-3 years
- Policy-driven: days to months

---

## The Downside Protection Rule

**Always answer: "If my thesis is wrong, what's the maximum loss?"**

Framework:
1. Estimate PB at cycle trough (look at historical lows or peer trough multiples)
2. PB drawdown = Current PB − Trough PB
3. Drawdown % = PB drawdown ÷ Current PB
4. Margin buffer = Gross Margin — the higher, the more cushion before losses

**Example:**
- 风华: PB 5.1×, trough PB ~1.3×, drawdown risk = 75%, margin buffer = 17% (thin)
- 三环: PB 10.75×, trough PB ~3.1×, drawdown risk = 71%, margin buffer = 43% (thick)

风华 has slightly more PB downside AND much thinner margin protection → higher risk despite lower PB.

---

## Sources and Attribution

This framework synthesizes:
- **labubu_trader** (@labubu_trader): Low PB + already-invested capex framework for MLCC manufacturers
- **ShanghaoJin / Herman Jin** (@ShanghaoJin): PB over PE for semiconductor cyclicals; Intel 1× PB case study; "unit capacity market cap" method for foundries
- **Shipping industry**: PB + fleet age + orderbook ratio (mature cyclical industry methodology)
- **Oil & Gas industry**: PB + reserve replacement ratio (100-year track record of cyclical asset valuation)

---

## Common Pitfalls

1. **Applying PB to companies where value isn't in fixed assets** — upstream materials, fabless design, IP companies
2. **Ignoring asset quality** — same PB, different gross margin = completely different value
3. **Confusing low PB with undervaluation** — some companies deserve low PB (structural low ROE)
4. **Ignoring PB repair trajectory** — a PB that's already run from 1× to 10× has less room than one at 3× → 5×
5. **Ignoring policy risk** — export-control-driven scarcity can reverse overnight
6. **Single-dimension analysis** — using only PB without GM, capex, and durability checks
