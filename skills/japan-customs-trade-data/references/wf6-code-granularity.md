# WF6 Code Granularity

Use this reference when the user asks about tungsten hexafluoride, WF6, or 六フッ化タングステン in Japan customs data.

## Key Rule

Japan customs data does not isolate WF6 as a direct product code in the verified workflow. Treat Japan WF6 rows as proxy buckets, not pure WF6.

## Practical Mapping

For WF6-related Japan trade monitoring:

| Direction | Japan code | Use as | Caveat |
|---|---:|---|---|
| Export | `282619900` | possible WF6 export proxy | "Other fluorides"; not pure WF6 |
| Import | `282619090` | possible WF6 import proxy | "Other fluorides"; not pure WF6 |

Do not mix `282619100` or `282619010` into WF6 proxy analysis unless the user explicitly asks for the broader `282619` family.

## Verification Sources to Check

To decide whether a product has a direct Japan code:

1. Export statistical schedule: `https://www.customs.go.jp/yusyutu/2026_01_01/data/j_XX.htm`
2. Import tariff schedule: `https://www.customs.go.jp/tariff/2026_01_01/data/j_XX.htm`
3. Principal Commodity Code: `https://www.customs.go.jp/toukei/sankou/code/GH202601e.html`
4. Special Classification: `https://www.customs.go.jp/toukei/sankou/code/TH202601e.html`

`customs.go.jp` pages can be Shift-JIS encoded. Decode them before searching Japanese text.

## Required Wording

Use wording like:

```text
This is 282619900, a proxy bucket for possible WF6 exports, not pure WF6.
```

Avoid wording like:

```text
Japan exported X kg of WF6.
```

unless a direct product-specific source outside customs data proves the shipment was WF6.
