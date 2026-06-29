# e-Stat CSV Contract

Use this reference when extracting Japan Trade Statistics rows from e-Stat.

## Endpoints

Browse page:

```text
https://www.e-stat.go.jp/en/stat-search/files?page=1&layout=dataset&toukei=00350300&tstat=000001013141&cycle_facet=cycle&data=1&metadata=1
```

CSV download:

```text
https://www.e-stat.go.jp/stat-search/file-download?statInfId=STAT_INF_ID&fileKind=1
```

`fileKind=1` is CSV. `fileKind=0` returns Excel.

## Dataset Codes

Trade Statistics of Japan uses:

```text
toukei=00350300
```

Common views:

- `tstat=000001013141`: commodity/country-oriented tables. This is the preferred view for HS code plus country rows.
- `tstat=000001013142`: country/commodity-oriented tables.
- `tstat=000001013143`: value-by-commodity aggregate tables.

The page label can say `Commodity by Country` or `Country by Commodity`; always verify the downloaded CSV has `HS` and `Country` columns and contains the requested rows.

## CSV Columns

The expected country-level CSV shape is:

```text
Exp or Imp,Year,HS,Country,Unit1,Unit2,Quantity1-Year,Quantity2-Year,Value-Year,
Quantity1-Jan,Quantity2-Jan,Value-Jan,...
```

Rules:

- `Exp or Imp`: `1` export, `2` import.
- `HS`: Japan 9-digit statistical code, often quoted as text.
- `Country`: Japan customs 3-digit country code.
- `Unit2`: the common quantity unit for chemical rows, usually `KG`.
- `Quantity2-*`: preferred quantity field for `KG`.
- `Value-*`: value in `千円`.

For month `Jan` through `Dec`, read fields by name, not by column index.

## Discovery Strategy

The most robust workflow is:

1. Request e-Stat dataset pages with known `tclass1/tclass2` candidates.
2. Extract candidate `statInfId` values.
3. Download each candidate CSV.
4. Keep the candidate only if parsed rows contain the requested HS/prefix and country.
5. Prefer rows with non-empty `Country` when the user requested a country-level query.

This is more reliable than trusting UI labels alone.

## Value Conversion

CSV value fields are in `千円`.

- million yen = `value_thousand_yen / 1000`
- oku yen = `value_thousand_yen / 100000`
- yen per kg = `value_thousand_yen * 1000 / quantity_kg`

Keep original units in metadata when converting.
