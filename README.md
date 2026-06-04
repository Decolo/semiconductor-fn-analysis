# semiconductor-fn-analysis

Valuation framework collection for semiconductor investing. Each skill covers a distinct company archetype — choose the right tool for the right business model.

## Skills

| Skill | Framework | Archetype | When to Use |
|-------|-----------|-----------|-------------|
| [pb-semiconductor](skills/pb-semiconductor/SKILL.md) | PB ÷ Gross Margin | Heavy-asset cyclicals (MLCC, foundries, memory, specialty chemicals) | 市净率, 重资产周期品, MLCC valuation |
| [peg-semiconductor](skills/peg-semiconductor/SKILL.md) | PEG / PSG | Asset-light growth (optical modules, fabless chip design, AI power ICs) | PEG, PSG, 成长股估值, 光模块 |

## How to Use

This is an **agent skill collection** — plain markdown files readable by any AI coding agent (Claude Code, Codex, Hermes, etc.).

### Quick Decision: Which Skill?

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

### Grey-Zone Companies

Some semiconductor companies don't fit neatly. Here's what to use:

| Company Type | Example | Primary Framework | Why |
|-------------|---------|-------------------|-----|
| Fab-lite IDM (部分自产部分外发) | 士兰微 | PB (自有产能部分) | 重资产属性 > 设计属性 |
| Equipment makers | 北方华创, ASML | PE + order book | 产品是设备不是芯片，PB 不适用 |
| IP licensors | ARM, Ceva | EV/Sales + royalty CAGR | 极轻资产，PEG 偏差大 |
| SiC substrate pure-plays | 天岳先进, 天科合达 | PB + supply-side analysis | 衬底是重资产大宗品，和 MLCC 同理 |
| Distributors | 艾睿电子, 大联大 | PB + inventory cycle | 库存周期驱动，不是设计驱动 |

### Install

```bash
git clone https://github.com/Decolo/semiconductor-fn-analysis.git
```

Or reference individual skill files directly in your agent's context.

## Structure

```
semiconductor-fn-analysis/
├── README.md
└── skills/
    ├── pb-semiconductor/
    │   ├── SKILL.md        # Scope gate, four-dimensional screen, output template
    │   ├── REFERENCE.md    # Why PB > PE, detailed methodology, pitfalls
    │   └── EXAMPLES.md     # 风华高科 vs 三环, Intel, 中船特气
    └── peg-semiconductor/
        ├── SKILL.md        # Scope gate, PEG/PSG formulas, graduation tracker
        ├── REFERENCE.md    # PEG traps, growth quality, cross-framework map
        └── EXAMPLES.md     # 中际旭创, 杰华特, 晶丰明源, MPS, PEG misfire
```

## License

MIT
