# Speculative Narrative Audit Examples

## Example: Real Supply Shock Grafted Onto Weak Product Mapping

### Setup

A viral post claims a listed manganese-materials company is a hidden beneficiary of "electronic-grade manganese bromide" used as an MLCC liquid precursor. The post cites a real overseas manganese supply disruption, then claims domestic uniqueness, high prices, capacity expansion, profit uplift, and a large market-cap target.

### Claim Chain

| Layer | Claim | What to Check | Read |
|-------|-------|---------------|------|
| Industry event | Overseas manganese mine disruption tightened supply | Miner press releases, industry price data | Can be true |
| Company mapping | Listed company produces the obscure high-value product | Annual report, segment disclosure, subsidiary scope, exchange Q&A | Kill-switch |
| Product/application | Product is a key MLCC precursor | MLCC makers, materials suppliers, technical docs | Often the weak link |
| Capacity/price | Exact tonnage and price jump | Company disclosure, price databases, customs data | Needs hard source |
| Profit bridge | Price jump adds major profit | Capacity, utilization, gross margin, pass-through | Should appear in guidance/filings if material |
| Valuation target | Market cap can multiply | Only meaningful if prior layers survive | Lowest evidentiary weight |

### Audit Logic

Do not stop at "manganese supply disruption is real." That only validates the background. The thesis lives or dies on whether the company actually has the promoted product line and whether that product is a real bottleneck in the downstream process.

Strong negative signal:

```text
The alleged business is material enough to change earnings,
but it is absent from annual/interim reports, product breakdowns,
subsidiary descriptions, ratings reports, and investor communication.
```

### Classification

If the industry event is real but the company-specific product mapping is unsupported, classify as:

```text
Likely concept essay / unverified trading narrative
```

Use "likely concept essay" when the product chemistry or downstream application conflicts with primary technical sources. Use "unverified trading narrative" when the mapping is plausible but not yet evidenced.

## Example: AI Server Material Claim With Unproven Supplier Mapping

### Setup

A post claims a small materials company is a hidden supplier of an advanced thermal-management material for AI servers. The post cites real AI server power-density growth, then claims the company is entering the supply chain of a major accelerator vendor through an unnamed module maker.

### Claim Chain

| Layer | Claim | What to Check | Read |
|-------|-------|---------------|------|
| Industry event | AI server power density is rising | OEM roadmaps, cooling vendors, hyperscaler capex | Can be true |
| Company mapping | The company supplies the named material into AI servers | Annual report, customer concentration, product certifications, investor Q&A | Kill-switch |
| Product/application | The material is actually used in that cooling architecture | OEM technical docs, module teardown, materials specs | Technical gate |
| Capacity/price | Capacity and ASP imply meaningful revenue | Capex disclosure, shipment data, price checks | Needs hard source |
| Profit bridge | New material changes margin profile | Segment revenue, gross margin, utilization | Filing test |
| Valuation target | Re-rate to AI materials multiple | Only valid if mapping and profit bridge survive | Lowest weight |

### Audit Logic

This case should not be rejected just because the industry event is promotional. The right question is whether the specific company has verified product qualification or shipments. If official cooling-stack materials contradict the post's material claim, classify as **False mapping**. If the material is plausible but company supply-chain evidence is missing, classify as **Unverified trading narrative**.

## Reusable Questions

- What is the exact product name in filings?
- Which subsidiary produces it?
- Is revenue, capacity, or capex disclosed for it?
- Who are the customers and what certifications are required?
- Does the downstream industry officially use this material?
- Are the quoted prices from a real price database or copied across social posts?
- If the claimed profit uplift is large, why is it absent from filings or guidance?
- Has the stock already repriced the story?
- What announcement or filing would kill the thesis?

## Reusable Verdict Language

### High confidence

```text
The thesis is supported by primary-source product disclosure, capacity evidence, and a plausible profit bridge. The remaining question is valuation, not existence.
```

### Medium confidence trading setup

```text
The background event is real and the market is trading the mapping, but the company-specific bridge is not yet proven. Treat it as a trading narrative until product, capacity, or customer evidence appears.
```

### Low confidence / concept essay

```text
The narrative uses a real industry event as an anchor, but the key company mapping is weak or absent in primary sources. If the promoted business were large enough to reshape earnings, its absence from filings is a material warning sign.
```

### False mapping

```text
The story depends on a product/application link that contradicts primary technical sources. Price action may continue, but the fundamental thesis should be treated as unsupported.
```
