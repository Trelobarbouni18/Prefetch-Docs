# Documentation project instructions

## About this project

- The documentation site for the Prefetch API (docs.prefetch.io), built on [Mintlify](https://mintlify.com).
- Pages are MDX files with YAML frontmatter. Configuration lives in `docs.json`.
- Run `mint dev` to preview locally, and `mint broken-links` to check links.
- For Mintlify components and configuration, install the Mintlify skill: `npx skills add https://mintlify.com/docs`.

## Structure

- **Docs tab:** Get started, Agents and MCP, Company data, Web data, Jobs and monitoring, Platform, Going to production.
- **Guides** live in `company-data/`, `web-data/`, `jobs/` and `monitors/`. They explain how an endpoint works, with examples in cURL, Node.js and Python.
- **Reference pages** live in `api-reference/endpoint/`. They're generated from `api-reference/openapi.json` via `openapi:` frontmatter, plus a one-paragraph summary, the cost, and a card linking to the guide. Don't add long explanations there.
- **Shared facts** live in `snippets/`: `credit-costs.mdx`, `plans.mdx`, `error-envelope.mdx`. Change a price or limit there, never by retyping it on a page.
- Keep reference page URLs stable. The MCP server's tool descriptions link to `/api-reference/endpoint/*` and `/mcp/tools#…`.
- When a page moves, add a redirect in `docs.json`.
- Add notable API changes to `changelog.mdx`.

## Terminology

- "Prefetch" or "the Prefetch API", not "PreFetch".
- "API key" for the `X-API-Key` secret. "Logo token" or "publishable token" for the logo CDN's `pk_` token.
- "Credits" for usage. "Monitor", "check", "target" and "goal" for monitoring. "Job" for crawls and batches.
- "Curated data" for answers from Prefetch's reviewed brand data, "live read" for answers that load the site.

## Style

- Use active voice and second person ("you").
- Keep sentences short: one idea per sentence. Lead with the rule, then the exception.
- Write headings, tabs, sidebar groups and buttons in sentence case. The theme uppercases navigation, labels and buttons in CSS to match prefetch.io, so don't type them in capitals.
- Don't use em dashes. Use a period, a colon, a comma or parentheses instead.
- Use US spelling.
- Bold UI elements: select **Settings**. Use code formatting for file names, commands, paths, endpoints, fields and parameters.
- Use real API responses in examples where possible, and mark shortened JSON with `…`.
- Don't invent facts about Prefetch: prices, limits, retention, compliance or behavior. If you can't confirm something from the API, the OpenAPI spec or existing docs, leave it out and flag it.

## Design

- The theme in `custom.css` mirrors prefetch.io and its dashboard, using the site's own token names (`--pf-bevel`, `--pf-bevel-well`, `--pf-win-dash`…). Build new styles from those tokens.
- Icons are [pixelarticons](https://pixelarticons.com), the set the dashboard uses. Use `icon: "/icons/<name>.svg"` in frontmatter and on cards. To add one, copy its SVG from the `pixelarticons` npm package into `/icons`, then run `python3 scripts/build-icon-css.py`.
- Reuse the dashboard's icon for each endpoint: `blocks` (enrich), `colors-swatch` (brand), `university` (company), `label` (classify), `shapes` (styleguide), `directions` (resolve), `receipt` (transaction), `image` (logo CDN), `file-text` (scrape), `search`, `algorithm` (map), `bug` (crawl), `camera` (screenshot), `book-open` (answers), `bell` (monitors).

## Content boundaries

- Don't document internal operations (deploys, Redis, Kubernetes) except where a customer sees the effect.
- Don't name the language model vendors behind features, beyond what the API itself returns.
