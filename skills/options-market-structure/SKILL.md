---
name: options-market-structure
description: Options market structure framework for trend traders. Use when analyzing whether options positioning is confirming trend, warning of fragility, signaling squeeze risk, or implying a higher chance of chop. Covers moneyness-aware put/call ratio, implied volatility, skew, term structure, gamma environment, and key open-interest strikes. Companion to the repo's semiconductor valuation skills.
---

# Options Market Structure for Trend Trading

Use this skill when the question is not "which option contract should I buy?" but:

> What is the options market implying about trend conditions right now?

This framework is for **trend context**, not options speculation. It helps translate option-market structure into a market-state judgment that can improve discretionary trading and investing.

## Scope Gate

### ✅ Use this skill when

- You trade or invest off price trends and want options-market confirmation
- You want to know whether current options positioning is supporting continuation, warning of fragility, or implying more chop
- You are comparing broad index context (`SPY`, `QQQ`, `SOXX`) with a key single name (`NVDA`, `TSLA`, etc.)
- You want to interpret `put/call`, `IV`, `skew`, `term structure`, `gamma`, or strike concentration as one picture

### ❌ Do not use this skill when

- You want a specific `call` or `put` trade idea
- You are asking about option pricing, theta decay, or contract selection
- You need precise intraday dealer-position estimates from low-quality or delayed data
- You are looking for a fully automated signal system

## Core Framework: Six Checks

### 1. Moneyness-Aware Put/Call Positioning

- First separate **near-ATM directional positioning** from **deep-wing tail protection**
- For next-expiry trend reads, start with an `ATM +/- 10%` band unless the name's volatility or strike spacing requires a different band
- Treat full-chain `put/call` as a warning flag to explain, not as a stand-alone direction signal
- If most put OI sits far below spot, read it primarily as crash insurance unless nearer strikes, IV, skew, and price action confirm downside pressure

### 2. Implied Volatility Level

- Rising IV usually means the market is paying up for uncertainty
- Falling or stable IV during an advance usually supports smoother trend continuation
- Price up + IV up can mean squeeze, stress, or event-risk, not always "healthy bullishness"

### 3. Skew

- Are downside `put`s priced much richer than upside `call`s?
- High skew often means large players are still paying for crash protection
- Skew matters most when price looks calm but protection demand remains expensive

### 4. Term Structure

- Compare near-dated vol with later expiries
- Front-end panic with a calmer back end often signals short-term stress
- A well-behaved curve is usually friendlier to steady trend conditions than an inverted or kinked curve

### 5. Gamma Environment

- In broad terms: is dealer hedging more likely to **dampen** moves or **amplify** them?
- Positive gamma often supports mean reversion and chop
- Negative gamma often supports acceleration, squeezes, and air pockets

### 6. Strike Concentration / Open Interest

- Which strikes are crowded with open interest or recent volume?
- These levels can pin price, attract price, or become acceleration points after a break
- Use them as structural reference levels, not as stand-alone signals

## Regime Translator

After the six checks, classify the market into one of these regimes:

1. **Trend Confirmation**  
   Price trend and options structure broadly agree. Best environment for clean continuation.

2. **Fragile Melt-Up**  
   Price is rising, but hedging demand or skew says the move is less comfortable than it looks.

3. **Squeeze Risk**  
   The tape is vulnerable to forced buying and sharp upside acceleration.

4. **Panic Hedge**  
   Protection demand and stress signals are dominating. Downside moves can reinforce themselves.

5. **Range Compression**  
   Dealer positioning and vol structure are more likely to suppress follow-through than fuel it.

6. **Mixed / Conflicted**  
   Signals disagree. Treat this as a lower-confidence environment rather than forcing a strong call.

See [REFERENCE.md](REFERENCE.md) for detailed definitions and [EXAMPLES.md](EXAMPLES.md) for worked cases.

## Practical Workflow

When answering a real question, move in this order:

1. Identify the trend backdrop in price first
2. Pick the relevant expiry window for the question
3. Split `put/call` into near-ATM directional positioning and deep-wing tail protection
4. Run the remaining options-structure checks
5. Name the regime
6. State what that regime implies for trend traders
7. State what could make the interpretation wrong
8. Downgrade confidence if the data source is weak

## Output Template

```markdown
## [Market / Ticker / Context]

### Price Backdrop
[Uptrend / downtrend / range / post-breakout / post-event]

| Check | Observation | Signal |
|------|-------------|--------|
| Directional P/C | [near-ATM band, expiry, put/call OI or volume] | 🟢/🟡/🔴 |
| Tail Hedge / Wing OI | [deep OTM put concentration and distance from spot] | 🟢/🟡/🔴 |
| Full-Chain P/C Caveat | [whether aggregate P/C is distorted by far OTM inventory] | 🟢/🟡/🔴 |
| IV | [description] | 🟢/🟡/🔴 |
| Skew | [description] | 🟢/🟡/🔴 |
| Term Structure | [description] | 🟢/🟡/🔴 |
| Gamma Environment | [description] | 🟢/🟡/🔴 |
| Strike Concentration | [description] | 🟢/🟡/🔴 |

### Regime
[Trend Confirmation / Fragile Melt-Up / Squeeze Risk / Panic Hedge / Range Compression / Mixed]

### Trend Implication
[What this means for a trend trader]

### Key Caveat
[What could invalidate the read]

### Confidence
[High / Medium / Low, based on both signal alignment and data quality]
```

## Semiconductor-Specific Use

This skill belongs in a semiconductor repo because broad options structure often explains when semi setups are likely to work cleanly and when they are being distorted by macro positioning.

Use this order:

1. Read broad index context (`SPY`, `QQQ`)
2. Check sector context (`SOXX`)
3. Check whether a single-name giant (`NVDA`) is confirming the sector or distorting it

Do not assume bullish `NVDA` options activity means the whole semiconductor tape has the same structure.

## Data Sources

Preferred order for research use:

1. **Options chain basics, expiries, OI, rough IV** — Yahoo Finance, TradingView
2. **Strike-level OI by moneyness** — required before using `put/call` for short-term direction
3. **Cleaner chain views and Greeks** — TradingView or higher-quality broker/platform feeds
4. **Precise intraday flow / dealer positioning claims** — only with stronger specialized sources

If the data is delayed, sparse, or partial, lower the confidence of the conclusion. See [REFERENCE.md](REFERENCE.md) for a data-confidence ladder.
