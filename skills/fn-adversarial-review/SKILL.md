---
name: fn-adversarial-review
description: Adversarial review framework for semiconductor investment theses, data claims, and agent-generated conclusions. Use when the user asks to review an existing thesis, challenge an investment conclusion, verify data authenticity, test logical consistency, find contradictions, or stress-test a bull/bear case before acting on it.
---

# Fundamental Adversarial Review

Use this skill after a thesis or conclusion already exists. The job is not to produce a new stock pitch; it is to attack the existing one until the remaining conclusion is clearer, weaker, or explicitly conditional.

## Scope Gate

### Use this skill when

- A thesis, valuation, catalyst map, or agent conclusion needs an adversarial second pass
- The user asks whether the data is real, stale, cherry-picked, or internally inconsistent
- A PB/PEG/PSG conclusion needs stress testing before it becomes an investment view
- A company narrative conflicts with filings, segment data, peer economics, or price action
- The user wants the strongest opposing case, not another supportive summary

### Do not use this skill when

- The user has not formed a thesis yet; first use `pb-semiconductor`, `peg-semiconductor`, or `speculative-narrative-audit`
- The question is only about short-term options positioning; use `options-market-structure`
- The user wants a fresh valuation model rather than a review of an existing conclusion
- The review would require current market or filing data and no source access is available; state the limitation instead of pretending to verify

## Review Contract

The review must separate:

1. **Data truth** — whether the cited numbers, filings, sources, and dates support the claim
2. **Logic validity** — whether the causal chain, valuation bridge, and comparisons follow
3. **Internal consistency** — whether different parts of the thesis contradict each other
4. **Decision impact** — whether each problem changes the conclusion or only lowers confidence

Do not average problems into a vague confidence score. A single refuted load-bearing claim can kill a thesis even if many minor details are true.

## Subagent Workflow

When the platform supports subagents and the review is material, run parallel review agents. Pass each subagent the frozen thesis, the user's question, and any cited sources. Tell them not to rewrite the thesis.

### Agent A: Data Verifier

- Verify financial numbers against filings, company announcements, earnings materials, or reputable market data
- Check source dates, reporting periods, units, currency, share counts, segment definitions, and adjusted vs GAAP metrics
- Label each key data claim as **confirmed**, **refuted**, **unsupported**, **stale**, or **source-mismatch**
- Treat absence as negative evidence only when the claim should be material enough to appear in filings or official communication
- **Check for missing entities**: search for key players that should appear in the thesis but are absent (e.g. a company with significant market share omitted from a supply chain map; an important competitor unmentioned in a competitive analysis)
- **Verify stock codes**: confirm ticker symbols against exchange data (common errors: wrong ticker suffix, wrong exchange, stale codes after corporate actions)

### Agent B: Logic Adversary

- Find non sequiturs between industry facts and company-specific profit impact
- Check whether the valuation method fits the business archetype
- Look for double counting, denominator errors, wrong peer groups, cycle-peak extrapolation, and mixed-segment contamination
- Identify places where the thesis assumes the conclusion it tries to prove
- Flag cross-industry false analogies (e.g. "MLCC monopoly more concentrated than NVIDIA" — different barrier types: material process vs ecosystem lock-in)

### Agent C: Bear-Case Scout

- Name the cleanest way the thesis fails
- Find contradictory evidence, competing explanations, and base-rate objections
- Separate "this is false" from "this can be true but already priced"
- Identify the next proof or disproof window

If subagents are unavailable, run the same three passes sequentially and say that the review was not independently parallelized.

**Pitfall — subagent timeout on broad data verification**: When there are many data points to verify (e.g. 20+ claims in a supply chain map), the Data Verifier subagent can hit max_iterations and return truncated. Mitigations:
- Narrow Agent A's scope to the top 8-10 load-bearing claims only
- For diagram/visual data review, run an explicit "verify stock codes" pass first, then verify market share claims separately
- Accept partial results gracefully — Agent B (logic review) and agent-synthesized corrections often reveal the same errors

## Main-Agent Synthesis

The main agent owns the final judgment. Merge the subagent outputs, de-duplicate findings, resolve conflicts, and rank issues by conclusion impact:

1. **Thesis-breaking** — refutes the core claim or valuation bridge
2. **Major confidence reducer** — thesis may survive, but only with lower confidence or narrower conditions
3. **Minor correction** — fixes detail without changing the investment conclusion
4. **Unresolved** — needs a specific source, filing, or future event

Never let a subagent's unsupported assertion become the final verdict. Findings need evidence, a reasoning chain, or an explicit "unverified" label.

## Post-Review: Apply Corrections

After the review is delivered, the main agent should:
1. Immediately apply confirmed factual corrections to the source document (knowledge base, diagram, or thesis file)
2. Clearly label the changes so the user can verify
3. Update revision metadata to track the adversarial review pass

## Output Template

```markdown
## Adversarial Review: [Company / Thesis]

### Verdict
[Survives / Survives with conditions / Impaired / Broken / Unverifiable]

### Load-Bearing Claims
| Claim | Data status | Logic status | Impact |
|-------|-------------|--------------|--------|
| | Confirmed / Refuted / Unsupported / Stale | Valid / Weak / Contradictory | Thesis-breaking / Major / Minor |

### Highest-Impact Problems
- **[Severity] [Problem]:** [Evidence and why it matters.]

### Strongest Bear Case
[The most coherent contrary interpretation.]

### What Would Change the Verdict
[Specific evidence, filing, price/action data, customer proof, margin trend, or disproof window.]
```

See [EXAMPLES.md](EXAMPLES.md) for worked review patterns and reusable finding language.
