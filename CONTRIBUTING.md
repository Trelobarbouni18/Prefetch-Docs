# Contributing to the Prefetch docs

Thanks for helping. Small fixes are welcome as pull requests: a wrong field, a broken link, a confusing sentence.

## Before you open a pull request

1. Run `mint dev` and read your page in both light and dark mode.
2. Run `mint broken-links`.
3. If you changed a price, a plan limit or the error envelope, change it in `snippets/`, not on the page.
4. If you added a page, add it to `docs.json`.

## How we write

- Second person and active voice: "You get a webhook", not "A webhook is sent".
- One idea per sentence. Lead with the rule, then the exception.
- Sentence case for headings and labels.
- No em dashes. Use a period, a colon, a comma or parentheses.
- Bold for UI elements: select **Settings**. Code formatting for endpoints, fields, parameters, files and commands.
- US spelling: color, organization, summarize.
- Examples use real responses where we can. Mark shortened JSON with `…`.
- Every code example comes in cURL, Node.js and Python where it makes sense.

## Guides and reference

Each endpoint has two pages:

- A **guide** (`company-data/`, `web-data/`, `jobs/`, `monitors/`) explains how it works, with examples.
- A **reference page** (`api-reference/endpoint/`) is generated from the OpenAPI spec, with a short summary and a link to the guide.

Put explanations in the guide. Keep reference pages short.
