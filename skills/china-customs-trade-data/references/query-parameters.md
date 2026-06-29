# China Customs Query Parameters

Use this reference when constructing `stats.customs.gov.cn` URLs.

## Entry Points

Form entry:

```text
http://stats.customs.gov.cn/queryData/queryDataByWhere
```

Results page:

```text
http://stats.customs.gov.cn/queryData/queryDataList
```

Direct results navigation may intermittently work, but it often returns service-busy messages. The reliable path is the form plus CAPTCHA.

## Core Parameters

| Parameter | Meaning | Common value |
|---|---|---|
| `iEType` | trade flow | `0` export, `1` import |
| `currencyType` | currency | `usd` |
| `year` | query year | e.g. `2026` |
| `startMonth` | start month | `1`-`12` |
| `endMonth` | end month | `1`-`12` |
| `monthFlag` | monthly mode | `1` |
| `codeLength` | HS code length | `8` for 8-digit code |
| `outerField1` | primary field | usually `CODE_TS` |
| `outerValue1` | primary value | HS code |
| `outerField2` | secondary field | `ORIGIN_COUNTRY` or `TRADE_CO_PORT` |
| `outerValue2` | secondary value | country code, or empty for all provinces |

## Field Values

| Value | Chinese label | Use |
|---|---|---|
| `CODE_TS` | 商品 | filter/group by HS code |
| `ORIGIN_COUNTRY` | 贸易伙伴 | country-level filter/group |
| `TRADE_MODE` | 贸易方式 | trade-mode filter/group |
| `TRADE_CO_PORT` | 收发货人注册地 | province/registered-location breakdown |

## Common Country Codes

| Code | Country |
|---:|---|
| `116` | Japan |
| `133` | Korea |

Do not reuse Japan/Korea e-Stat or UNIPASS country-code mappings here.

## Result URL Pattern

```text
http://stats.customs.gov.cn/queryData/queryDataList?pageNum=1
  &codeLength=8
  &selectTableState=1
  &orderType=CODE%20ASC%20DEFAULT
  &iEType=0
  &currencyType=usd
  &year=2026
  &startMonth=1
  &endMonth=5
  &monthFlag=1
  &outerField1=CODE_TS
  &outerValue1=28261930
  &outerField2=ORIGIN_COUNTRY
  &outerValue2=116
```

`current*` parameters reflect the platform's active data window. Do not fabricate them from the requested query period. When unsure, prefer the form page and let the site populate them. Only include `currentStartTime`, `currentEndTime`, `currentRecentTime`, or `currentDateBySource` when copied from the live form/page.
