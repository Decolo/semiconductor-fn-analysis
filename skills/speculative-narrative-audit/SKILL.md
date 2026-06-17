---
name: speculative-narrative-audit
description: Audit speculative semiconductor and materials stock narratives for false mappings, weak evidence, and concept-stock essay risk. Use when analyzing viral tweets, 小作文, 产业链传闻, 唯一/唯二, 隐形供应商, 预期差, 证伪节点, or unverified product/price/capacity claims; not for confirmed-business valuation or routine catalyst analysis.
---

# Speculative Narrative Audit

Use this skill to decide whether a market narrative is a real fundamental thesis, a plausible but unverified trading setup, or a likely false concept-stock essay.

## Scope Gate

- A viral post claims a company is the "only", "global top two", "hidden supplier", or "core beneficiary"
- The thesis jumps from an industry event to a specific listed-company profit explosion
- The story depends on obscure materials, price quotes, capacity numbers, or downstream mappings
- The user asks whether a rumor, 小作文, or concept-stock narrative has 预期差
- The stock has already moved and the question is whether the narrative is starting, spreading, or priced in

Do not use this skill for ordinary valuation of confirmed business lines, PB/PEG/PSG work after the thesis is established, or broad market-structure reads.

## Core Workflow

1. **Extract atomic claims**  
   Separate industry background, company mapping, product chemistry, capacity, price, profit bridge, and valuation target. One true background fact can hide a false company mapping.

2. **Find the kill-switch claim**  
   Ask: "If this one claim is false, does the whole thesis collapse?" Usually this is whether the company actually owns the promoted product, capacity, customer, or certification.

3. **Check evidence in priority order**
   - Company annual/interim reports and announcements
   - Exchange interaction records and abnormal-move announcements
   - Company website and subsidiary business descriptions
   - Upstream/downstream official technical materials
   - Industry price databases and customs/production data
   - Broker notes, social media, forums

   Primary filings and official technical sources control the verdict. Broker notes and social media can corroborate but cannot override them. Direct contradiction from primary technical sources should force **False mapping**, not **Unverified trading narrative**.

4. **Treat absence as evidence when materiality is high**  
   If a business line is supposed to add major profit, it should usually appear in reports, segment disclosures, subsidiary descriptions, ratings reports, or investor communication. Simultaneous absence across those sources is a negative signal, not neutral.

5. **Classify the narrative**
   - **Confirmed thesis**: key product/customer/capacity/profit bridge is supported by primary sources.
   - **Unverified trading narrative**: background is real, mapping is plausible but not yet evidenced, and the market is trading it.
   - **Likely concept essay**: real background is grafted onto a weak or mismatched company/product mapping.
   - **False mapping**: product chemistry, downstream application, or peer comparison contradicts primary technical sources.

6. **Map the trading stage**
   - **Discovery**: little price/volume reaction, few public posts.
   - **Diffusion**: volume rises, narrative spreads, price confirms attention.
   - **Crowded validation**: large volume, high volatility, investors hunt for proof.
   - **De-risk or de-rate**: clarification, exchange inquiry, or filings weaken the thesis.

7. **Name proof and disproof windows**  
   Near term: abnormal-move announcement, exchange inquiry, investor Q&A. Medium term: price databases, customer checks, broker verification. Hard filing window: next quarterly, interim, or annual report.

## Red Flags

- "Only supplier" or "global top two" with no primary source
- Clean number chain: price jump, capacity, profit, earnings, target market cap all line up too neatly
- Real industry event plus a weak company-specific bridge
- Obscure product name not present in company filings
- Downstream application uses different mainstream materials in official sources
- Peer comparison relies on a famous materials company but not the same product line
- Profit bridge implies materiality, but filings show no matching segment or subsidiary signal

## Output
Always return this shape:

```markdown
## Narrative Audit: [Company / Ticker]

### Verdict
[Confirmed thesis / Unverified trading narrative / Likely concept essay / False mapping]

| Layer | Claim | Best evidence | Support vs contradiction | Confidence |
|-------|-------|---------------|--------------------------|------------|
| Industry event | | | | |
| Company mapping | | | | |
| Product/application | | | | |
| Capacity/price | | | | |
| Profit bridge | | | | |
| Valuation target | | | | |

### Kill-Switch Claim
[The one claim that decides whether the thesis survives.]

### Trading Stage
[Discovery / Diffusion / Crowded validation / De-risk or de-rate]

### Proof Needed
[Specific evidence that would upgrade confidence.]

### Disproof Windows
[Specific dates/events where the thesis can be weakened or killed.]

### Bottom Line
[Investment thesis vs trading narrative, with confidence.]
```
See [EXAMPLES.md](EXAMPLES.md) for worked cases, reusable questions, and verdict language.
