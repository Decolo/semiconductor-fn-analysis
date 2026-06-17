# Fundamental Adversarial Review Examples

## Example 1: Agent Thesis After PB Analysis

### Input

> Company A is a buy because PB is only 2.1x, lower than peers at 4-6x. Gross margin recovered last quarter, so the market should re-rate it to 4x PB as the cycle turns.

### Good Review Shape

```markdown
## Adversarial Review: Company A PB Re-Rating Thesis

### Verdict
Survives with conditions.

### Load-Bearing Claims
| Claim | Data status | Logic status | Impact |
|-------|-------------|--------------|--------|
| PB is 2.1x | Confirmed, but uses latest market cap with prior-period book value | Valid with timing caveat | Minor |
| Peers trade at 4-6x PB | Unsupported because peer set mixes high-margin materials with commodity capacity | Weak | Major |
| Gross margin recovery means re-rating to 4x PB | Confirmed one-quarter recovery, but cycle duration unproven | Weak | Major |

### Highest-Impact Problems
- **Major confidence reducer - peer mismatch:** The peer set compares a commodity manufacturer with higher-margin specialty materials names. That can overstate fair PB.
- **Major confidence reducer - one-quarter extrapolation:** One margin recovery quarter does not prove a cycle turn unless pricing, utilization, and backlog also confirm.

### Strongest Bear Case
The stock is cheap because the assets are lower quality, not because the market missed the cycle. PB re-rating needs sustained gross-margin repair, not only low PB.

### What Would Change the Verdict
Two more quarters of margin improvement, utilization evidence, and a peer set limited to comparable asset quality.

### Bottom Line
The thesis is not broken, but the 4x PB target is under-supported. Keep the setup as a watchlist candidate, not a high-conviction buy.
```

## Example 2: Data Authenticity Challenge

### Input

> This supplier's AI packaging revenue doubled and now accounts for 30% of sales, so PEG is below 1.

### Good Review Shape

```markdown
### Highest-Impact Problems
- **Thesis-breaking - segment data not found:** The cited "30% of sales" claim is not present in segment disclosure, earnings slides, or investor Q&A. If this revenue is material, its absence is negative evidence.
- **Major confidence reducer - PEG denominator risk:** The growth rate uses the promoted AI segment, but the PE numerator uses full-company market cap. That mixes a high-growth segment with slower legacy revenue.

### Strongest Bear Case
The company may have AI exposure, but the thesis turns a small or undisclosed product line into a full-company growth valuation. The right frame may be mixed optionality, not simple PEG.
```

## Example 3: Internal Contradiction

### Input

> The stock is safe because downside is protected by low PB, but upside comes from a new asset-light chip design business that deserves a SaaS-like multiple.

### Good Finding

```markdown
- **Major confidence reducer - framework conflict:** The downside case relies on asset value, while the upside case relies on an asset-light optionality multiple. Those can coexist only if the thesis values the legacy assets and new business separately. A single blended multiple hides the risk.
```

## Reusable Review Prompts

- If this one claim is false, does the thesis collapse?
- Is the company-specific bridge proven, or only the industry background?
- Are the numerator and denominator from the same business segment and time period?
- Does the chosen valuation framework match the business archetype?
- What would a skeptical analyst say is already priced?
- Which next filing, exchange reply, customer proof, or margin trend would change the verdict?
