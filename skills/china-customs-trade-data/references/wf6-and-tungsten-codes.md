# WF6 and Tungsten Codes

Use this reference for China customs HS-code selection around WF6 and tungsten feedstocks.

## WF6

| Code | Product |
|---:|---|
| `28261930` | 六氟化钨, 8-digit customs query code |
| `2826193000` | 六氟化钨, 10-digit full code when required |

Critical pitfall:

```text
28129011 is nitrogen trifluoride (NF3), not WF6.
```

## Tungsten Upstream Codes

| HS Code | Chinese | English |
|---:|---|---|
| `28259012` | 三氧化钨 | tungsten trioxide |
| `28259019` | 其他钨的氧化物及氢氧化物 | other tungsten oxides/hydroxides |
| `28418010` | 仲钨酸铵(APT) | ammonium paratungstate |
| `28418040` | 偏钨酸铵(AMT) | ammonium metatungstate |
| `81011000` | 钨粉 | tungsten powder |
| `81019400` | 未锻轧钨，包括简单烧结条杆 | unwrought tungsten, including sintered bars |
| `28499020` | 碳化钨 | tungsten carbide |
| `26110000` | 钨矿砂及其精矿 | tungsten ores and concentrates |

Do not treat `81019400` as a direct WF6 feedstock signal. It is a finished metal product bucket, not a chemical intermediate.

## Common WF6 Queries

China WF6 exports to Japan:

```text
HS=28261930
iEType=0
outerField2=ORIGIN_COUNTRY
outerValue2=116
```

China WF6 exports to Korea:

```text
HS=28261930
iEType=0
outerField2=ORIGIN_COUNTRY
outerValue2=133
```

China WF6 export province breakdown:

```text
HS=28261930
iEType=0
outerField2=TRADE_CO_PORT
outerValue2=
```
