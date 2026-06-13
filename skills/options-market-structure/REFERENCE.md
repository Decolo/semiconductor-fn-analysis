# Options Market Structure: Reference

## What This Framework Is Really For

The goal is not to predict every market move from option chains. The goal is narrower:

> Use option-market structure to judge whether price trend is being confirmed, challenged, or made unstable.

Trend traders do not need a perfect options model. They need a disciplined way to recognize when the options market is:

- helping a move continue
- quietly warning that a move is fragile
- setting up a squeeze
- suppressing follow-through
- amplifying stress

---

## The Signal Layer

### 1. Put/Call Ratio by Moneyness

**What it measures:** relative demand for downside protection versus upside speculation.

**How to read it for trend context:**
- **Near-ATM directional zone:** For next-expiry direction, start with the strikes close enough to spot to matter for the next move. `ATM +/- 10%` is a useful default band, but tighten or widen it for the name's realized volatility, event calendar, and strike spacing.
- **Full-chain aggregate:** Treat total `put/call` as a diagnostic flag, not a direction signal. A high full-chain ratio only says "find where the puts are."
- **Deep OTM wing inventory:** Puts far below spot often represent crash insurance, collar inventory, or stale institutional hedges. They should feed the fragility and tail-risk read before they feed the short-term direction read.

**Decision rule:** If near-ATM `P/C` is call-heavy while full-chain `P/C` is put-heavy because deep OTM puts dominate the chain, the short-term read is not bearish by default. The cleaner interpretation is often **near-term bullish, but hedged**.

**When wing puts become directional:** Do not dismiss far OTM puts mechanically. They become more relevant to downside direction when spot is falling toward them, IV is rising with price weakness, downside skew is steepening, or put volume is moving from the wings into nearer strikes.

### 2. Implied Volatility

**What it measures:** how much future movement the options market is pricing.

**Trend interpretation:**
- Price up + IV stable/down = cleaner continuation backdrop
- Price down + IV up = more dangerous downside backdrop
- Price up + IV sharply up = often squeeze, stress, or event premium

### 3. Skew

**What it measures:** how much richer downside protection is than upside exposure.

**Trend interpretation:**
- High skew means the market still pays for disaster insurance
- A rally with persistently rich downside skew is often less comfortable than price alone suggests
- Collapsing skew can support risk-on continuation

### 4. Term Structure

**What it measures:** how implied volatility is distributed across expiries.

**Trend interpretation:**
- Calm upward-sloping term structure usually supports orderly conditions
- Front-end stress with a calmer back end often signals near-term fear, event risk, or forced hedging
- Weird kinks often deserve lower-confidence interpretation unless you know the event calendar

### 5. Gamma Environment

**What it measures:** whether dealer hedging is more likely to absorb moves or amplify them.

**Trend interpretation:**
- More positive gamma often means a higher chance of chop and lower chance of smooth breakout follow-through
- More negative gamma often means a higher chance of acceleration, overshoot, and ugly reversals

Do not pretend to know exact dealer positioning from weak data. Use this as an environment estimate, not as false precision.

### 6. Open Interest and Strike Crowding

**What it measures:** where positioning is concentrated.

**Trend interpretation:**
- Crowded strikes can pin price
- Breaks away from crowded strikes can trigger faster movement
- This is most useful as a map of structural levels, not as a stand-alone directional indicator

---

## The Regime Layer

The framework becomes useful only when signals are translated into a small set of market states.

### Regime 1: Trend Confirmation

**Typical shape**
- Price trend is already established
- IV is stable or supportive
- Skew is not flashing deep discomfort
- Gamma backdrop is not heavily suppressing follow-through

**What it means**
- Best environment for staying with the move
- Breakouts are more likely to carry

### Regime 2: Fragile Melt-Up

**Typical shape**
- Price is rising
- Near-ATM positioning is supportive, but tail protection stays elevated
- Skew is still rich
- IV is not behaving as calmly as the chart suggests

**What it means**
- The rally may continue, but it is less healthy than it looks
- Chasing extensions is riskier

### Regime 3: Squeeze Risk

**Typical shape**
- Upside positioning is forcing buy-side hedging
- Gamma backdrop is more likely to amplify
- Price can accelerate beyond what spot-only traders expect

**What it means**
- Strong upside can persist longer than a pure valuation or sentiment read would imply
- Entries become harder, but shorts become more dangerous

### Regime 4: Panic Hedge

**Typical shape**
- Downside protection demand surges near spot or rolls closer to spot
- IV jumps
- Skew steepens
- Gamma backdrop is hostile

**What it means**
- Downside moves can feed on themselves
- Trend shorts become easier to validate, but oversold bounces also become violent

### Regime 5: Range Compression

**Typical shape**
- Vol structure is calm
- Gamma backdrop is more damping than amplifying
- Crowded strikes pin price

**What it means**
- Trend traders should be suspicious of weak breakouts
- Mean reversion and failed follow-through are more common

### Regime 6: Mixed / Conflicted

**Typical shape**
- Signals point in different directions
- Some say continuation, others say caution

**What it means**
- Reduce confidence
- Avoid forcing a strong read just because one metric is loud

---

## Data-Confidence Ladder

Not every options claim deserves the same confidence.

### Level 1: Safe with basic public data

- approximate `put/call` balance
- rough IV level
- visible OI concentration by strike
- broad expiry map

**Usable for:** slower context reads, swing-trading support, general regime classification. Do not use aggregate `put/call` alone for short-term direction.

### Level 2: Usable with decent platform data

- strike-level OI bucketed by moneyness
- rough skew comparisons
- cleaner term-structure judgments
- broad gamma-environment framing

**Usable for:** stronger regime classification, better caveat control, and moneyness-aware directional reads

### Level 3: Requires stronger specialized data

- precise intraday flow interpretation
- exact dealer-positioning claims
- confident intraday gamma-flip calls
- "market makers must buy X billions" style statements

**Usable for:** only if the source quality actually supports it

Rule:

> If the data only supports Level 1, do not speak with Level 3 confidence.

---

## Semiconductor Lens

This repo is semiconductor-focused, so the framework should include one specific habit:

### Read the stack in order

1. **Broad market (`SPY`)**
2. **Growth / tech (`QQQ`)**
3. **Semiconductor sector (`SOXX`)**
4. **Dominant single names (`NVDA`, `AMD`, `TSM`)**

### Why this matters

- Sometimes semis are just following macro growth positioning
- Sometimes `NVDA` options activity distorts perception of the whole group
- Sometimes `SOXX` confirms the move better than `QQQ`

### Practical read

- `QQQ` supportive + `SOXX` supportive + `NVDA` not wildly distorted = best semi trend backdrop
- `NVDA` euphoric but `SOXX` weak = narrower and more fragile setup
- `SPY` calm but `QQQ` stressed = growth-specific caution even if the broad market looks fine

---

## Common Mistakes

1. Treating high full-chain `put/call` as an automatic bearish or contrarian signal
2. Using options data without first checking the spot trend
3. Speaking too confidently from weak or delayed chain data
4. Reading single-name options mania as sector-wide confirmation
5. Confusing "bullish" with "healthy"
6. Ignoring whether put OI is near spot or buried in deep OTM crash-protection strikes
7. Forcing a clean regime when the better answer is mixed

---

## Bottom Line

This framework is successful when it helps answer:

- Is the options market helping this trend continue?
- Is the move more fragile than price alone suggests?
- Is this a squeeze-prone tape, a panic tape, or a chop tape?

If it answers those questions better, more clearly, and with cleaner caveats, it is doing its job.
