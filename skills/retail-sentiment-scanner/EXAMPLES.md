# Retail Sentiment Scanner — Examples

## Example 1: Storage Manufacturer Position Review (June 2026)

### Context
An investor holding SNDK ($85K), MU ($31K), and DRAM ETF ($83K) wanted to gauge whether storage manufacturers had become a crowded trade before rotating into storage equipment stocks (LRCX, TER).

### Scan Execution

**Twitter/X (opencli)**
- Searched `$SNDK` → 6:4 bullish/bearish split; Barchart warning "RSI 99.22 = most overbought stock in history"
- Searched `$MU` → 7:3 bullish; SCA strategic customer agreement narrative dominant; CEO sold 80K shares in May-June
- Searched `$TER` → 9:1 bullish; NVIDIA new customer catalyst; zero bear posts found
- Searched `$LRCX` → 7:3 bullish; low engagement, few retail posts

**Reddit (opencli)**
- Searched `SNDK` on r/wallstreetbets → "If you invested $50K 15 months ago = $3.76M" (942 upvotes); r/tradewithcongress post "Rep. Ro Khanna +5,039%" (1,552 upvotes); $SNDK $1000 ITM call post (503 upvotes)
- Searched `MU` on r/MU_Stock → "Should I sell my Lululemon stock to buy MU?" (FOMO detected); UBS target $535→$1,625 (853 upvotes)
- Searched `TER` → near-zero independent posts; only mentioned in NASDAQ-100 addition thread
- Searched `LRCX` → "In the AI Gold Rush, what are the shovels?" (586 upvotes); BofA target $330→$480 (low engagement)

**Substack**
- SNDK: "Growth Miracle or Valuation Trap?" — DCF $423-690 vs $2,180 market price. Requires 40% FCF CAGR for 5 years to justify.
- TER: "The $67B Chip-Testing Gorilla Hiding in Plain Sight" — stock 22% above analyst consensus, yet zero sell ratings.
- MU/HBM: "The More Anthropic Buys Micron HBM, the Faster Optical Memory Pooling Arrives" — HBM consumes 3x wafer per bit vs DDR5. Structural supply shortage, but optical disaggregation is the long-term risk.

### Cross-Reference Matrix

| Ticker | X Sentiment | Reddit Heat | Substack Depth | Consensus Risk | Action |
|--------|:-----------:|:-----------:|:--------------:|:--------------:|--------|
| SNDK  | 6:4 Bullish | 🔴 Extreme | DCF $423 vs $2,180 | Crowded | Reduce |
| MU    | 7:3 Bullish | 🟡 High | SCA contract thesis | Moderate | Hold/trim |
| TER   | 9:1 Bullish | 🟢 Low | ATE oligopoly | High (one-sided) | Cautious add |
| LRCX  | 7:3 Bullish | 🟢 Low | Etch monopoly | Low | Accumulate |

### Key Contrarian Signals

1. **SNDK RSI 99.22** is the highest monthly RSI reading ever recorded on Barchart — technically unprecedented
2. **SNDK tokenized on Solana** — retail access expanding to on-chain, a late-cycle signal
3. **TER has zero sell ratings** despite being 22% above consensus — when everyone is long, there's no marginal buyer left
4. **HBM consumes 3x wafer area per bit vs DDR5** — the more HBM is built, the tighter all DRAM supply becomes (endogenous shortage)

### Investment Decision

Reduced SNDK and DRAM ETF positions. Began building LRCX (deterministic etch leader) and TER (HBM ATE expectation gap). MU held but not added, given CEO selling and consensus crowding.

---

## Example 2: Pre-Earnings Sentiment Check (Template)

### Context
A position in a semiconductor stock is 50% above cost basis. Earnings are in 3 days. The question: hold through earnings, or trim before?

### Scan Execution

**Twitter/X (earnings week)**
- Search `$TICKER earnings` → collect sentiment, target price changes, estimate revisions
- Flag any "priced in" language — if bulls already claim "everyone knows earnings will be great," the bar for a positive surprise is higher
- Note analyst upgrades/downgrades in the last 5 days

**Reddit (earnings thread)**
- Search `TICKER earnings` on r/wallstreetbets → count "yolo into earnings" posts vs "sell the news" posts
- Check r/TICKER_Stock for position screenshots — large unrealized gains → selling pressure after earnings

**Substack (deep dive)**
- Search for the most recent earnings preview post
- Extract: whisper number vs consensus, key metric to watch, bear case trigger

### Output
```
Pre-earnings sentiment: 8:2 bullish on X, moderate FOMO on Reddit, Substack focused on gross margin risk.
Decision: trim 30% before earnings, hold remainder. The bar for a positive surprise is high.
```

---

## Anti-Patterns (What NOT to Do)

### ❌ Treating sentiment as a trade signal
Sentiment audit tells you _what the crowd thinks_, not what the stock will do. A 9:1 bullish consensus can persist for months before reversing. Use sentiment to size your position and time your entries, not to call tops.

### ❌ Scanning only the fan subreddit
r/MU_Stock is self-selected bulls. If you only scan there, you'll think sentiment is 10:0 bullish. Always cross-check with general forums (r/wallstreetbets, r/stocks, r/investing).

### ❌ Averaging platforms into one number
"Overall sentiment: 7.3/10" is useless. The value is in the _differences_ between platforms: Twitter might be bearish while Reddit is euphoric, or Substack might have a DCF that's 80% below market price while Reddit is celebrating.

### ❌ Running the scan once and forgetting
Sentiment shifts fast. Run the scan weekly for active positions, monthly for long-term holds. Track changes: is the controversy deepening or resolving? Is FOMO accelerating or cooling?
