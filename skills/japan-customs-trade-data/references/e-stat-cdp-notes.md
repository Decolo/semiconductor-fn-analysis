# e-Stat CDP Notes

Use CDP for live diagnosis or page discovery. Prefer the direct CSV workflow for normal extraction.

## Entry URL

```text
https://www.e-stat.go.jp/en/stat-search/files?page=1&layout=dataset&toukei=00350300&tstat=000001013141&cycle_facet=cycle&data=1&metadata=1
```

Use `layout=dataset`. `layout=datalist` can render as a JS-heavy shell with less useful static HTML.

## What to Inspect

From the page DOM, collect:

- `statInfId` from CSV links
- `Survey date`
- update date
- table label such as `Commodity by Country / Export` or `Country by Commodity / Export`
- whether the row is export or import

Then verify by downloading the CSV and checking row contents. The DOM label is not enough.

## Useful CDP Pattern

```js
Array.from(document.querySelectorAll('a[href*="file-download"]'))
  .map(a => ({
    text: a.innerText.trim(),
    href: a.href,
    context: a.closest('article,li,div')?.innerText?.replace(/\s+/g, ' ').slice(0, 500)
  }))
```

If the page structure changes, fall back to searching the raw HTML around `statInfId=`.

## Recovery

- If no CSV links are visible, confirm `layout=dataset`.
- If the UI says there are datasets but links are missing, read the raw HTML instead of relying on the rendered view.
- If page labels and CSV contents disagree, trust the parsed CSV for row extraction and report the label ambiguity.
- If direct CSV download fails, retry with `User-Agent: Mozilla/5.0` and `Referer: https://www.e-stat.go.jp/`.
