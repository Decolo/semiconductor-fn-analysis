# UNIPASS CDP Notes

Canonical selectors, snippets, waits, and extraction helpers for Korea UNIPASS customs trade statistics automation.

## Page Architecture

- Entry URL: `https://unipass.customs.go.kr/ets/etsItemSrch.do?menuId=ETS_MNU_00000103`
- The site may redirect to `https://tradedata.go.kr/cts/index.do?menuId=ETS_MNU_00000103`.
- Initial navigation loads a menu shell. The real statistics form loads through:

```javascript
ets_f_prccMenuLoad('/cts/hmpg/openETS0100019Q.do', { menuId: 'ETS_MNK_10200000' });
```

- After loading, the form is inline DOM, not an iframe.

## Guarded Form Loader

Run this after opening the entry URL if the real form is missing. It waits for the menu loader, calls it, then polls for the HS controls. If it times out, reload the entry URL or redirected `tradedata.go.kr/cts/index.do?...` once and rerun.

```javascript
async function waitFor(predicate, timeoutMs = 10000, intervalMs = 200) {
  const start = Date.now();
  while (Date.now() - start < timeoutMs) {
    if (predicate()) return true;
    await new Promise(resolve => setTimeout(resolve, intervalMs));
  }
  return false;
}

async function loadUnipassItemForm() {
  const loaderReady = await waitFor(() => typeof window.ets_f_prccMenuLoad === 'function', 10000);
  if (!loaderReady) return { ok: false, reason: 'ets_f_prccMenuLoad undefined' };

  window.ets_f_prccMenuLoad('/cts/hmpg/openETS0100019Q.do', { menuId: 'ETS_MNK_10200000' });

  const formReady = await waitFor(() =>
    document.querySelector('#ETS0100019Q_hsSgn') &&
    document.querySelector('#ETS0100019Q_btnHsSgnPop') &&
    document.querySelector('.btnSearch.w50p')
  );

  return { ok: formReady, reason: formReady ? null : 'form controls missing after loader call' };
}
```

## Key Selectors

| Purpose | Selector / ID | Notes |
| --- | --- | --- |
| HS input | `#ETS0100019Q_hsSgn` | Placeholder resembles "HS 부호 입력 후 + 선택" |
| HS detail search | `#ETS0100019Q_btnHsSgnPop` | Opens `품목검색` modal |
| HS add button | `.cateNumBtn` | Small plus button near HS input |
| Selected HS hidden field | `#ETS0100019Q_checkdHsSgn` | Holds selected HS state |
| Search button | `.btnSearch.w50p` | `조회` |
| Start month | `#ETS0100019Q_formYearMonthPc` | Appears in monthly mode |
| End month | `#ETS0100019Q_toYearMonthPc` | Appears in monthly mode |
| Page size | `#ETS0100019Q_showPagingLine` | Options include 15, 30, 50, 100 rows |
| Country popup button | `.ebkCntyPop` | Not default workflow |
| Country text input | `#ETS0100019Q_cntyNameInput` | Country popup path only |
| Economic bloc | `#ETS0100019Q_economicCd` | Coarse grouping, not per-country extraction |

Use semantic postconditions as well as selectors: the selected statistics label must match the intended mode, selected HS state must contain the requested HS code, and result headers must match the expected schema.

## Statistics Item Options

| Korean label | Meaning | Recommended use |
| --- | --- | --- |
| `품목별` | By item | Aggregate HS-code rows |
| `국가별` | By country | Broad country rows, not HS-specific default |
| `품목별+국가별` | By item plus country | Default HS-code-by-country workflow |
| `성질별+국가별` | By property plus country | Specialized workflow |
| `경제권별` | By economic bloc | Bloc-level aggregation |

Switching `통계항목` can clear existing form state. Always verify HS selections after switching.

## Statistics Mode Selection

The exact `통계항목` selector can drift. Prefer selecting by visible label from the statistic-item select or custom dropdown near the top of the left sidebar, then verify the selected text. If a normal `<select>` is present, use this pattern:

```javascript
function selectOptionByText(select, text) {
  const option = [...select.options].find(opt => opt.textContent.trim() === text);
  if (!option) return { ok: false, reason: `option not found: ${text}` };
  select.value = option.value;
  select.dispatchEvent(new Event('change', { bubbles: true }));
  return { ok: true, value: option.value, text: option.textContent.trim() };
}

function selectStatisticsMode(label) {
  const selects = [...document.querySelectorAll('select')];
  for (const select of selects) {
    const result = selectOptionByText(select, label);
    if (result.ok) return result;
  }
  return { ok: false, reason: `statistics mode select not found for ${label}` };
}
```

Postconditions:

- For aggregate rows, selected label should be `품목별` and result headers should not include `국가`.
- For country rows, selected label should be `품목별+국가별` and result headers should include `국가`.
- After switching mode, re-check selected HS state because the platform can clear it.

## Period Mode Selection

For monthly rows, select `월별` before setting the date range. The exact selector can drift, so select by visible label and verify that the month fields are present.

```javascript
function clickVisibleLabel(label) {
  const candidates = [...document.querySelectorAll('label, button, a, span, input')];
  const el = candidates.find(node => {
    const text = (node.innerText || node.textContent || node.value || '').replace(/\s+/g, ' ').trim();
    return text === label && node.offsetParent !== null;
  });
  if (!el) return { ok: false, reason: `${label} control not found` };
  el.click();
  return { ok: true, text: label };
}

async function selectMonthlyPeriodMode() {
  const clicked = clickVisibleLabel('월별');
  if (!clicked.ok) return clicked;
  const ready = await waitFor(() =>
    document.querySelector('#ETS0100019Q_formYearMonthPc') &&
    document.querySelector('#ETS0100019Q_toYearMonthPc')
  );
  return { ok: ready, reason: ready ? null : 'monthly date fields missing after selecting 월별' };
}
```

Set the visible month fields only after `selectMonthlyPeriodMode()` returns `ok: true`.

## HS Search Popup

- Modal name: `품목검색`.
- Common tabs: `HS 코드로 찾기`, `품목명으로 찾기`.
- Hierarchical browse path can move through 2-digit, 4-digit, 6-digit, and 8-10 digit levels.
- The right panel lists selected HS codes.
- Use `적용` to commit the selected HS code back to the main form.

Example hierarchy for HS 282619:

```text
28 -> 2826 -> 282619 -> 적용
```

Primary CDP path when direct input works:

```javascript
function addHsCode(hsCode) {
  const input = document.querySelector('#ETS0100019Q_hsSgn');
  const addButton = document.querySelector('.cateNumBtn');
  if (!input || !addButton) return { ok: false, reason: 'HS input or add button missing' };

  input.value = hsCode;
  input.dispatchEvent(new Event('input', { bubbles: true }));
  input.dispatchEvent(new Event('change', { bubbles: true }));
  addButton.click();

  const hidden = document.querySelector('#ETS0100019Q_checkdHsSgn');
  const hiddenValue = hidden ? hidden.value : '';
  const visibleText = document.body.innerText;
  const selected = hiddenValue.includes(hsCode) || visibleText.includes(hsCode);
  return { ok: selected, hiddenValue, reason: selected ? null : 'HS selected state not found' };
}
```

If direct input fails, use the HS popup hierarchy and `적용`. The success assertion is the same: `#ETS0100019Q_checkdHsSgn` or visible selected-chip text contains the HS code.

## Result Tables

Aggregate `품목별` expected visible columns:

```text
기간 | HS코드 | 품목명 | 수출 중량 | 수출 금액 | 수입 중량 | 수입 금액 | 무역수지
```

Country-level `품목별+국가별` expected visible columns:

```text
기간 | 국가 | HS코드 | 품목명 | 수출 중량 | 수출 금액 | 수입 중량 | 수입 금액 | 무역수지
```

The page commonly displays unit text near results:

```text
[단위] 톤(TON), 천 달러
```

Preserve this as `metadata.units` for the result set.

## Search, Waits, Page Size, and Extraction

Search button:

```javascript
document.querySelector('.btnSearch.w50p')?.click();
```

After search, wait for one of these signals:

- populated result table with expected headers
- unit line containing `단위`
- visible no-data text such as `조회된 데이터가 없습니다`
- visible validation/error text near the form
- timeout, in which case capture the current URL, selected mode, selected HS state, and visible portal text

Largest page-size helper:

```javascript
function setLargestPageSize() {
  const select = document.querySelector('#ETS0100019Q_showPagingLine');
  if (!select) return { ok: false, reason: 'page-size select missing' };
  const numericOptions = [...select.options]
    .map(opt => ({ value: opt.value, n: Number((opt.textContent.match(/\d+/) || [opt.value])[0]) }))
    .filter(opt => Number.isFinite(opt.n));
  if (!numericOptions.length) return { ok: false, reason: 'no numeric page-size options' };
  const largest = numericOptions.sort((a, b) => b.n - a.n)[0];
  select.value = largest.value;
  select.dispatchEvent(new Event('change', { bubbles: true }));
  return { ok: select.value === largest.value, value: select.value, size: largest.n };
}
```

Result extraction helper. If the page has multiple tables, choose the visible table whose headers include `기간` and either `HS코드` or `국가`. The helper returns schema-shaped row objects, not raw cell arrays.

```javascript
function visibleText(el) {
  return (el?.innerText || el?.textContent || '').replace(/\s+/g, ' ').trim();
}

function normalizeHeader(header) {
  if (header.includes('기간')) return 'period';
  if (header.includes('국가')) return 'country';
  if (header.includes('HS')) return 'hs_code';
  if (header.includes('품목')) return 'item_name';
  if (header.includes('수출') && header.includes('중량')) return 'export_weight';
  if (header.includes('수출') && header.includes('금액')) return 'export_value';
  if (header.includes('수입') && header.includes('중량')) return 'import_weight';
  if (header.includes('수입') && header.includes('금액')) return 'import_value';
  if (header.includes('무역수지')) return 'trade_balance';
  return header;
}

function extractUnipassResultTable() {
  const tables = [...document.querySelectorAll('table')].filter(t => t.offsetParent !== null);
  const table = tables.find(t => {
    const text = visibleText(t);
    return text.includes('기간') && (text.includes('HS코드') || text.includes('국가'));
  });
  if (!table) return { ok: false, reason: 'result table not found' };

  const headers = [...table.querySelectorAll('thead th, tr:first-child th, tr:first-child td')]
    .map(visibleText)
    .filter(Boolean)
    .filter(h => h !== '선택');

  const bodyRows = table.querySelector('tbody')
    ? [...table.querySelectorAll('tbody tr')]
    : [...table.querySelectorAll('tr')].slice(1);

  const rows = bodyRows.map(tr =>
    [...tr.querySelectorAll('td')]
      .map(visibleText)
      .filter(cell => cell && cell !== '선택')
  ).filter(cells => cells.length >= headers.length && /\d{4}/.test(cells[0]));

  const schemaKeys = headers.map(normalizeHeader);
  const mappedRows = rows.map(cells => Object.fromEntries(
    schemaKeys.map((key, idx) => [key, cells[idx] || ''])
  ));

  const unitsText = [...document.querySelectorAll('caption, .unit, .txt_unit, p, span, div')]
    .map(visibleText)
    .filter(text => text.includes('단위') && (text.includes('톤') || text.includes('$') || text.includes('달러')))
    .sort((a, b) => a.length - b.length)[0] || null;

  const paginationText = [...document.querySelectorAll('body *')]
    .map(visibleText)
    .filter(text => /\\d+\\s*\\/\\s*\\d+|다음|이전/.test(text))
    .slice(0, 20);

  return { ok: true, headers, schemaKeys, rows: mappedRows, metadata: { units: unitsText, paginationText } };
}
```

Pagination rule:

- If page-size is 100 and pagination indicates more than one page, do not claim extraction is complete.
- Either paginate and collect each page with the same schema, or report that the result is truncated and include `metadata.paginationText`.

## Country Popup Caveat

The country checkbox popup on the aggregate `품목별` path is not the default CDP route.

Observed issues:

- Country checkboxes such as `cntySelectJP`, `cntySelectCN`, `cntySelectUS`, and `cntySelectKR` can exist in the DOM.
- Direct JS `.click()` or checked-state manipulation can fail to update the page's selected-country state.
- The popup has no reliable apply button; selection appears intended to be live.
- Closing the popup can leave the visible checked state disconnected from the query state.

Use `품목별+국가별` and filter extracted rows by country instead.

## data.go.kr API Notes

Secondary endpoint previously identified:

```text
http://apis.data.go.kr/1220000/Itemtrade/getItemtradeList
```

Typical parameters:

```text
serviceKey=<encoded service key>
numOfRows=100
pageNo=1
searchBgnDe=YYYYMM
searchEndDe=YYYYMM
statCd=<HS/HSK code>
type=json
```

Do not default to this path without credentials. Registration can require Korean phone or i-PIN verification.

## Granularity Caveat

Korea uses 10-digit HSK codes, but not every material has a dedicated code. For some materials the available HS/HSK category can be a catch-all bucket. Extract the platform rows faithfully and report the granularity caveat separately from any analysis.
