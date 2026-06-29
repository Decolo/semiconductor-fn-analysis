# semiconductor-fn-analysis

Framework collection for semiconductor investing and market-context analysis. Each skill covers a distinct valuation archetype or market-structure use case — choose the right tool for the right question.

## Skills

| Skill | Framework | Archetype | When to Use |
|-------|-----------|-----------|-------------|
| [pb-semiconductor](skills/pb-semiconductor/SKILL.md) | PB ÷ Gross Margin | Heavy-asset cyclicals (MLCC, foundries, memory, specialty chemicals) | 市净率, 重资产周期品, MLCC valuation |
| [peg-semiconductor](skills/peg-semiconductor/SKILL.md) | PEG / PSG | Asset-light growth (optical modules, fabless chip design, AI power ICs) | PEG, PSG, 成长股估值, 光模块 |
| [options-market-structure](skills/options-market-structure/SKILL.md) | Options structure → trend regime | Broad equity index context, growth tapes, semiconductor overlays | 期权结构, moneyness-aware put/call, IV, skew, gamma, 趋势交易辅助 |
| [speculative-narrative-audit](skills/speculative-narrative-audit/SKILL.md) | Claim-chain audit → proof/disproof windows | Viral concept-stock essays, obscure materials, unverified supply-chain mappings | 小作文, 产业链传闻, 唯一/唯二, 预期差, 证伪节点 |
| [fn-adversarial-review](skills/fn-adversarial-review/SKILL.md) | Data / logic / contradiction stress test | Existing semiconductor investment theses and agent conclusions | review thesis, 数据真实性, 逻辑冲突, 反方审阅, bear case |
| [retail-sentiment-scanner](skills/retail-sentiment-scanner/SKILL.md) | Cross-platform retail sentiment audit (X/Reddit/Substack) | Pre-position sentiment check, crowded trade detection | 散户情绪, 拥挤交易, FOMO, Reddit, Twitter, Substack |
| [china-customs-trade-data](skills/china-customs-trade-data/SKILL.md) | China Customs CDP workflow → structured trade rows | China customs import/export extraction by HS code, country, and province | 中国海关, 海关总署, CDP, 验证码, HS code, WF6 |
| [korea-customs-trade-data](skills/korea-customs-trade-data/SKILL.md) | UNIPASS CDP workflow → structured trade rows | Korea customs import/export extraction by HS code and country | 韩国海关, UNIPASS, CDP, HS code, 进出口数据 |
| [japan-customs-trade-data](skills/japan-customs-trade-data/SKILL.md) | e-Stat CSV workflow → monthly trade rows | Japan customs import/export extraction by statistical code and country | 日本海关, e-Stat, HS code, 月度进出口, WF6 proxy |

## How to Use

This is an **agent skill collection** — plain markdown files readable by any AI coding agent (Claude Code, Codex, Hermes, etc.).

### Quick Decision: Which Skill?

**Need customs rows instead of analysis?**

```
需要海关进出口数据、HS/statistical code × country rows、页面状态恢复？

中国海关 / 海关总署统计平台 / CAPTCHA / 省份拆分 / WF6 28261930？
→ china-customs-trade-data

日本海关 / e-Stat / 9位统计码 / WF6 proxy / 月度 CSV？
→ japan-customs-trade-data

韩国海关 / UNIPASS / HSK code / CDP 表单操作？
→ korea-customs-trade-data

常见场景:
- 操作中国海关总署统计查询平台并等待用户完成验证码
- 提取中国某 HS code 出口/进口按国家或省份拆分的数据
- 构造 `queryDataList` URL 并验证 `CODE_TS`, `ORIGIN_COUNTRY`, `TRADE_CO_PORT` 参数
- 提取日本某 9 位统计码的进口/出口月度表
- 提取日本某 HS/statistical code 按国家拆分的数据
- 判断日本是否能单独隔离某商品，如 WF6
- 提取韩国某 HS code 的进口/出口月度表
- 提取韩国某 HS code 按国家拆分的数据
- UNIPASS 只打开 shell、表单丢状态、country popup 不稳定
```

**Ten-second framework selector:**

```
公司是重资产制造（有工厂/设备/产能）？
  │
  ├── YES → 利润高波动，跟着周期走？
  │         └── pb-semiconductor  (PB ÷ 毛利率, 四维打分)
  │         例: 村田、台积电、风华高科、三环、中船特气
  │
  └── NO → 轻资产（设计/IP 驱动），增长快？
            │
            ├── 盈利且毛利稳定/上升？
            │   └── peg-semiconductor → PEG
            │   例: 中际旭创、MPS (MPWR)
            │
            └── 亏损或利润率极薄？
                └── peg-semiconductor → PSG + 毕业追踪
                例: 杰华特、晶丰明源 (HPC业务)
```

**Not valuing a company, but reading market conditions?**

```
你不是在问“这家公司值多少钱”，而是在问：
“现在期权市场是在支持上涨、支持下跌，还是更容易震荡/挤仓/恐慌？”

→ options-market-structure

常见场景:
- 看 SPY / QQQ / SOXX 的期权结构是否确认趋势
- 判断 NVDA 的期权狂热是在带动板块还是扭曲板块
- 把 moneyness-aware put/call, IV, skew, gamma 翻译成趋势环境
```

**Auditing a viral stock narrative instead of valuing a confirmed business?**

```
帖子/传闻是否把真实产业事件嫁接到一个未证实公司映射上？
是否出现 "国内唯一 / 全球唯二 / 隐形供应商 / 价格翻倍 / 利润爆发"？

→ speculative-narrative-audit

常见场景:
- 拆解半导体/材料小作文
- 判断预期差是基本面机会还是交易性叙事
- 找核心 kill-switch claim 和证伪时间点
```

**Already have a thesis and want to attack it?**

```
已有结论需要复核，而不是重新生成一个估值框架？
需要检查数据真假、逻辑是否跳跃、估值口径是否冲突、反方论点是否足够强？

→ fn-adversarial-review

常见场景:
- review agent 之前给出的投资结论
- 检查 PB / PEG / PSG 结论里的数据口径和逻辑链
- 找 thesis-breaking claim、最强 bear case 和下一步证伪窗口
```

### Grey-Zone Companies

Some semiconductor companies don't fit neatly. Here's what to use:

| Company Type | Example | Primary Framework | Why |
|-------------|---------|-------------------|-----|
| Fab-lite IDM (部分自产部分外发) | 士兰微 | PB (自有产能部分) | 重资产属性 > 设计属性 |
| Equipment makers | 北方华创, ASML | PE + order book | 产品是设备不是芯片，PB 不适用 |
| IP licensors | ARM, Ceva | EV/Sales + royalty CAGR | 极轻资产，PEG 偏差大 |
| SiC substrate pure-plays | 天岳先进, 天科合达 | PB + supply-side analysis | 衬底是重资产大宗品，和 MLCC 同理 |
| Distributors | 艾睿电子, 大联大 | PB + inventory cycle | 库存周期驱动，不是设计驱动 |
| Market structure / tape reading | SPY, QQQ, SOXX, NVDA | Options structure framework | 不是估值问题，而是趋势环境判断 |

### Install

```bash
git clone https://github.com/Decolo/semiconductor-fn-analysis.git
```

Or reference individual skill files directly in your agent's context.

### Local Agent Exposure

Repo `skills/` directories are the canonical source. Agent-private directories should link to this repo, not hold divergent copies. When Codex already loads `.agents/skills`, do not duplicate the same skill again under `.codex/skills`.

```bash
src="$PWD/skills/korea-customs-trade-data"
ln -sfn "$src" /Users/decolo/.agents/skills/korea-customs-trade-data
ln -sfn "$src" /Users/decolo/.hermes/skills/finance/korea-customs-trade-data
ln -sfn ../../.agents/skills/korea-customs-trade-data /Users/decolo/.claude/skills/korea-customs-trade-data

src="$PWD/skills/japan-customs-trade-data"
ln -sfn "$src" /Users/decolo/.agents/skills/japan-customs-trade-data
ln -sfn "$src" /Users/decolo/.hermes/skills/finance/japan-customs-trade-data
ln -sfn ../../.agents/skills/japan-customs-trade-data /Users/decolo/.claude/skills/japan-customs-trade-data

src="$PWD/skills/china-customs-trade-data"
ln -sfn "$src" /Users/decolo/.agents/skills/china-customs-trade-data
ln -sfn "$src" /Users/decolo/.hermes/skills/finance/china-customs-trade-data
ln -sfn ../../.agents/skills/china-customs-trade-data /Users/decolo/.claude/skills/china-customs-trade-data
```

## Structure

```text
semiconductor-fn-analysis/
├── docs/
│   ├── brainstorms/
│   ├── ideation/
│   └── plans/
├── README.md
└── skills/
    ├── pb-semiconductor/
    │   ├── SKILL.md        # Scope gate, four-dimensional screen, output template
    │   ├── REFERENCE.md    # Why PB > PE, detailed methodology, pitfalls
    │   └── EXAMPLES.md     # 风华高科 vs 三环, Intel, 中船特气
    ├── peg-semiconductor/
    │   ├── SKILL.md        # Scope gate, PEG/PSG formulas, graduation tracker
    │   ├── REFERENCE.md    # PEG traps, growth quality, cross-framework map
    │   └── EXAMPLES.md     # 中际旭创, 杰华特, 晶丰明源, MPS, PEG misfire
    ├── options-market-structure/
    │   ├── SKILL.md        # Six-check workflow for reading options structure as trend context
    │   ├── REFERENCE.md    # Signal layer, regime layer, data-confidence ladder, semi lens
    │   └── EXAMPLES.md     # Trend confirmation, fragile rally, squeeze, panic, NVDA/SOXX/QQQ
    ├── speculative-narrative-audit/
    │   ├── SKILL.md        # Claim-chain audit, kill-switch claim, proof/disproof windows
    │   └── EXAMPLES.md     # Concept essay case pattern and reusable verdict language
    ├── fn-adversarial-review/
    │   ├── SKILL.md        # Subagent-based adversarial review for existing investment theses
    │   └── EXAMPLES.md     # Thesis review, data authenticity, and contradiction examples
    ├── retail-sentiment-scanner/
    │   ├── SKILL.md        # Cross-platform retail sentiment audit (X, Reddit, Substack)
    │   └── EXAMPLES.md     # Storage manufacturer position review, pre-earnings check template
    ├── china-customs-trade-data/
    │   ├── SKILL.md        # China Customs CDP operation playbook
    │   ├── scripts/         # Query URL construction helper
    │   └── references/      # Parameters, CDP, WF6, fallback, and smoke notes
    ├── korea-customs-trade-data/
    │   ├── SKILL.md        # UNIPASS CDP operation playbook for Korea trade data extraction
    │   └── references/     # CDP notes and live-portal smoke checklist
    └── japan-customs-trade-data/
        ├── SKILL.md        # e-Stat CSV workflow for Japan trade data extraction
        ├── scripts/         # Deterministic CSV extraction CLI
        └── references/      # e-Stat, WF6, country-code, CDP, and smoke notes
```

## License

MIT
