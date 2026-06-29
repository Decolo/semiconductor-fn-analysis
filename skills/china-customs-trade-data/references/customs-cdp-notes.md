# China Customs CDP Notes

Use this reference for live operation of `stats.customs.gov.cn`.

## Browser Target

Prefer reusing an existing tab already on:

```text
http://stats.customs.gov.cn/queryData/queryDataByWhere
```

or:

```text
http://stats.customs.gov.cn/queryData/queryDataList
```

Open a new tab only if no relevant customs tab exists or the current tab is stale.

## Form Workflow

1. Navigate to `queryDataByWhere` with parameters or plain form entry.
2. Set fields through DOM evaluation or manual form controls.
3. Click the query control. The query button is an `<a>` with id `doSearch`.
4. The site opens a layui CAPTCHA iframe at `/queryData/toCaptchaView?...`.
5. Ask the user to solve CAPTCHA manually in Chrome.
6. After success, the browser redirects to `queryDataList`.
7. Wait for async table rows before extracting.

Useful click:

```js
document.getElementById('doSearch').click()
```

## Direct Result URL

Direct `queryDataList` URLs can work intermittently. If they show:

```text
当前服务请求较多，请稍后重试
```

wait 30-60 seconds and retry once from a fresh tab. If repeated, use form + CAPTCHA.

## Extraction Hints

Start with visible text:

```js
document.body.innerText
```

If rows are present but text is noisy, extract table cells:

```js
Array.from(document.querySelectorAll('table tr')).map(tr =>
  Array.from(tr.cells).map(td => td.innerText.trim())
)
```

Keep a raw snapshot in the answer or notes when the platform is unstable.

## CDP Failure Modes

- `targetId required` for all commands can mean stale CDP daemon. Run `cdp.mjs stop` only when no other active browser task depends on the daemon, then retry.
- Runtime evaluate timeout across all commands usually means the customs site or tab is hung.
- Rapid repeated eval/click commands can trigger rate limits. Space actions by 10+ seconds.
- New tabs can return 429/500 during busy windows.

## CAPTCHA Rule

Do not bypass or automate CAPTCHA. Tell the user clearly:

```text
请在浏览器里完成验证码；完成后我继续读取结果页。
```
