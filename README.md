# Prefetch API docs

The source for [docs.prefetch.io](https://docs.prefetch.io), built with [Mintlify](https://mintlify.com).

## Run it locally

```bash
npm i -g mint
mint dev
```

Then open http://localhost:3000. Check links before you push:

```bash
mint broken-links
```

Changes to the default branch deploy automatically.

## Where things live

| Folder | What's in it |
|---|---|
| `index.mdx`, `quickstart.mdx`, `agent-quickstart.mdx` | Get started |
| `company-data/`, `web-data/`, `jobs/`, `monitors/` | Product guides: how each endpoint works, with examples |
| `concepts/` | Platform pages: auth, credits, rate limits, errors, webhooks, async jobs, caching, production |
| `recipes/` | End-to-end examples, each with a prompt for coding agents |
| `integrations/` | No-code tools |
| `compare/`, `migrate/` | Comparisons with other APIs, and migration guides. Recheck competitor facts against their docs when you edit. |
| `mcp/` | The MCP server and its tools |
| `api-reference/` | One page per endpoint, generated from `api-reference/openapi.json` |
| `snippets/` | Shared tables (prices, plans, the error envelope). Edit facts here, once. |
| `icons/` | Pixel icons from [pixelarticons](https://pixelarticons.com) (MIT). After adding one, run `python3 scripts/build-icon-css.py`. |
| `custom.css` | The theme, built from prefetch.io's own design tokens. |
| `changelog.mdx` | What changed, newest first |

See [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md) for writing rules.
