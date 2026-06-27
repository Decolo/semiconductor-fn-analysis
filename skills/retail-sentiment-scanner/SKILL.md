---
name: retail-sentiment-scanner
description: Cross-platform retail investor sentiment audit for stock positions — scan Twitter/X, Reddit, and Substack for narrative intensity, controversy depth, and consensus risk before acting on investment decisions. Use when the user wants to gauge retail sentiment, check if a position has become a crowded trade, find what retail/community investors are saying about specific tickers, or do a pre-trade sentiment check.
---

# Retail Sentiment Scanner

A **sentiment audit** — the structured cross-platform scan you run before adjusting a position, to answer one question: _is this trade crowded, controversial, or undiscovered?_

Not a valuation framework. Not a buy/sell signal on its own. It surfaces what the crowd thinks so you can measure that against your own thesis.

## Scope Gate

### Use this skill when

- You hold or are considering a position and want to measure retail/community sentiment
- You suspect a position has become a crowded trade and need evidence
- You want to cross-reference institutional consensus with retail narrative
- You're timing an entry and want to know if the crowd is already in
- A stock has moved 10x+ and you need to judge whether FOMO is priced in

### Do not use this skill when

- You need fundamental valuation — use `pb-semiconductor` or `peg-semiconductor`
- You're auditing a viral narrative claim-chain — use `speculative-narrative-audit`
- You're stress-testing a full investment thesis — use `fn-adversarial-review`
- You're reading options market structure — use `options-market-structure`
- The stock is illiquid and has no community discussion; state that absence instead of fabricating signal

## Sentiment Audit Contract

The audit produces four deliverables per ticker:

1. **Narrative consensus** — the dominant story the crowd believes, in one sentence
2. **Sentiment ratio** — rough bullish/bearish split with source counts
3. **Heat level** — Reddit post frequency + upvote intensity + meme/ETF presence
4. **Controversy depth** — whether the bull and bear cases are both substantive, or one side is absent

Do not average these into a "score." A stock can score high on heat _and_ low on controversy (consensus → crowded) or low on heat _and_ high on controversy (undiscovered → opportunity).

## Scan Workflow

Run three parallel scans, then cross-reference. Each platform answers a different question.

### Layer 1: Twitter/X — Narrative & Influencer Scan

**What it answers:** _What story is forming, and who is shaping it?_

Search for `$TICKER` or company name. Collect 10-20 recent posts (last 2 weeks). For each ticker extract:

- Dominant narrative (one sentence)
- Bullish post count vs bearish post count
- Notable voices (accounts with >100 likes or verified status)
- Red flags: CEO/insider selling mentions, "RSI overbought" warnings, "top is in" sentiment
- Hashtag or cashtag frequency (e.g. `$SNDK` velocity)

**Tool-agnostic commands:**
```
Search Twitter for: "$TICKER stock" OR "TICKER_NAME" (last 2 weeks)
Search Twitter for: "$TICKER bearish" OR "short TICKER" (last 2 weeks)
```

**Output:** Per-ticker narrative summary + rough bull/bear ratio + 3 most shared posts.

### Layer 2: Reddit — Retail Heat & FOMO Scan

**What it answers:** _How excited are retail investors, and is FOMO peaking?_

Search across r/wallstreetbets, r/stocks, r/investing, r/<ticker>_stock. Sort by relevance, limit to last 30 days.

For each ticker collect:
- Post count and average upvote score
- Most upvoted post title (this is the meme-level summary of crowd sentiment)
- Presence of "yolo," "all in," "mortgage," or "should I sell X to buy Y" language → FOMO signal
- Presence of leveraged ETF tracking the stock (e.g. $SNXX for SNDK) → retail frenzy signal
- Presence of "this time is different" phrasing → consensus risk signal
- Controversy: are there substantive bear posts with high engagement, or is dissent downvoted to zero?

**Tool-agnostic commands:**
```
Search Reddit: "TICKER" (r/wallstreetbets, r/stocks, r/investing, r/TICKER_Stock; 30 days)
Search Reddit: "TICKER bear" OR "short TICKER" (30 days)
```

**Output:** Post count, top upvote, FOMO indicators, controversy presence/absence.

### Layer 3: Substack — Deep Analysis & Opposing Views

**What it answers:** _What are the serious independent analysts saying, and what's the strongest counter-thesis?_

Search Substack for `TICKER` or company name. Collect 3-5 most recent posts (last 30 days).

For each ticker extract:
- Core thesis of the most substantive post
- DCF/valuation target if provided (compare to current price)
- The strongest bear argument found across all posts
- The most surprising data point or structural insight
- Whether the author is long-biased, short-biased, or neutral

**Tool-agnostic commands:**
```
Search Substack: "TICKER stock" OR "TICKER analysis" (30 days)
Search Substack: "TICKER bear" OR "TICKER short" OR "TICKER overvalued" (30 days)
```

**Output:** Strongest bull thesis, strongest bear thesis, valuation gap (if any), most surprising finding.

### Layer 4: Cross-Reference Matrix

Combine the three layers into a single view per ticker:

| Ticker | X Sentiment | Reddit Heat | Substack Depth | Consensus Risk | Action Signal |
|--------|:-----------:|:-----------:|:--------------:|:--------------:|---------------|
| SNDK  | 6:4 Bullish | 🔴 Extreme | DCF $423 vs $2,180 | Crowded | Reduce |
| MU    | 7:3 Bullish | 🟡 High | SCA contract thesis | Moderate | Hold/trim |
| TER   | 9:1 Bullish | 🟢 Low | ATE oligopoly | High (one-sided) | Cautious add |
| LRCX  | 7:3 Bullish | 🟢 Low | Etch monopoly | Low | Accumulate |

**Heat level key:**
- 🔴 Extreme: r/WSB front page, meme ETF exists, "yolo" posts, >500 upvotes
- 🟡 High: active subreddit, regular posts, >100 upvotes, split opinions
- 🟢 Low: sparse discussion, institutional coverage dominant, <50 upvotes

**Consensus risk key:**
- **Crowded:** 9:1+ consensus, zero bear arguments found, "this time is different" dominant
- **Moderate:** 7:3 split, bear arguments exist but weak, some dissent visible
- **Low:** 6:4 to 5:5, substantive bull and bear arguments both present

## Output Template

After completing all four layers, produce this output structure:

```markdown
# Retail Sentiment Audit — [Date]

## Per-Ticker Summary

### TICKER — [One-line verdict]

| Layer | Finding |
|-------|---------|
| X/Twitter | [Narrative, ratio, key voice] |
| Reddit | [Heat, top post, FOMO flags] |
| Substack | [Deep thesis, valuation gap, surprise] |

**Conclusion:** [Action implication — reduce/hold/add/wait]

## Heatmap

[Cross-reference matrix table]

## Key Contrarian Signals

- [Most important bear argument found across all platforms]
- [Most important structural risk identified]
```

## Pitfalls

- **Recency bias:** Twitter sentiment in the last 48 hours can invert after earnings. Always note the earnings date proximity.
- **Loud minority:** One account with 50 posts can dominate a search. Count unique authors, not total posts.
- **Echo chamber:** r/TICKER_Stock is self-selected bulls. Always cross-check with general subreddits.
- **Paid content:** Substack authors may hold positions they write about. Check for disclosure; if absent, downgrade the post's weight.
- **Absence is signal:** If a stock has zero Reddit discussion, that's data — it means the trade is not yet crowded.
- **Overfitting to consensus:** A 9:1 bullish ratio doesn't mean the stock will drop. It means the _marginal buyer is already in_, and any bad news has no cushion of skeptical capital waiting to buy the dip.

## Platform Abstraction

This skill does not mandate specific CLI tools. Any agent with internet access can run the scans using:

- **Twitter/X:** native API, opencli, browser automation, or Nitter
- **Reddit:** native API, opencli, Pushshift, or browser automation
- **Substack:** native search, opencli, or browser automation

The output format and cross-reference logic remain identical regardless of the access method.
