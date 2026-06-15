"""sq_example — a sciqnt connector skeleton (rename to sq_<source>).

The discovery contract: expose `snapshot()` (+ `accounts()`) and the platform LISTS
and aggregates you. Broker-dialect knowledge lives in `canonical.py`; quirks in
`FINDINGS.md`. Money is always Decimal; every fact carries a currency.
"""
from .canonical import to_canonical


def accounts():
    """Connected account labels (None = legacy single-account). [] = nothing connected."""
    return []


def snapshot(asof=None, *, account=None):
    """Return a canonical PortfolioSnapshot for `account`. The template returns an
    empty-but-valid snapshot so the connector is conformance-green from the start —
    replace with a real fetch + `to_canonical(raw)`."""
    return to_canonical(_example_raw())


def _example_raw() -> dict:
    """A minimal synthetic payload in THIS source's shape — replace with the real one."""
    return {"positions": [], "cash": []}
