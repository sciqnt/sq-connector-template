# sq-connector-template

**The skeleton for a sciqnt connector repo.** Click **“Use this template”** (or tell your
coding agent *“build a sciqnt connector for &lt;source&gt;”*) and you get a connector that is
**CI-green from the first run** and **inherits the org governance** automatically.

A connector maps one broker / exchange / data source into sciqnt's canonical schema. It
reads the **user's own account with the user's own credentials, locally** — that's
interoperability. Keep it on that side: **own-account only, never circumvent an access
control**, nominative trademark use, and keep `NOTICE.md` accurate.

## What you get

| File | What |
|---|---|
| `src/sq_example/__init__.py` | the discovery surface (`snapshot()` / `accounts()`) — the platform lists you by this |
| `src/sq_example/canonical.py` | **the one file** holding all source-dialect knowledge — `to_canonical(raw)` |
| `src/sq_example/live.py` | the live fetch (stub) |
| `manifest.yaml` | capabilities, flavour, `risk_tier`, `provenance`, the `contract` major it targets |
| `NOTICE.md` | the disclaimer (not affiliated / interop / own-account / no-circumvention) |
| `FINDINGS.md` | the living quirks log |
| `tests/` | a green skeleton test (swap for real conformance once `sq-contract` is published) |
| `.github/workflows/` | **inherited** CI / principle-review / `@claude` / issue-triage (call `sq-constitution@v1`) |

## After “Use this template”

1. **Rename** `sq_example` → `sq_<source>` (the package dir, `pyproject.toml` name, manifest).
2. **Fill in** `canonical.py` (`to_canonical`) + `live.py` (the real fetch). Money is
   `Decimal`; every fact carries a currency; facts are bitemporal.
3. **Wire conformance** — once `sq-contract` is published, depend on `sciqnt-contract>=0,<1`
   and replace the skeleton test with `conformance.check_snapshot(snapshot())`.
4. **Keep `NOTICE.md` accurate** and set the manifest `risk_tier` / `flavours.<f>.risk`.
5. Push — the inherited workflows run CI + the principle-review agent; a human merges.

## Governance

This repo inherits everything from
**[`sq-constitution`](https://github.com/sciqnt/sq-constitution)** — one constitution, one
gated flow, across every connector. DCO, not CLA. MIT.
