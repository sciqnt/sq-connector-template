"""sq_example.canonical — map the source's dialect into the canonical schema.

THE one file that holds all source-dialect knowledge. `to_canonical(raw)` must return
a canonical PortfolioSnapshot that passes the conformance suite. The template ships a
trivial empty mapping (no contract dependency yet) so it's green from the first CI run;
once `sq-contract` is published, import its schema + conformance and build the real map.
"""


def to_canonical(raw: dict) -> dict:
    """Map `raw` → canonical. Template: a trivial empty-but-shaped snapshot.
    Replace the return with real `sciqnt-contract` schema objects (Account / Position /
    CashBalance / Transaction …) once you depend on sq-contract."""
    return {"positions": list(raw.get("positions", [])),
            "cash": list(raw.get("cash", []))}
