"""sq_example.live — the LIVE flavour (fetch from the source). Stub until implemented.

Read the user's OWN account with the user's OWN credentials, locally. Never circumvent
an access control. Credentials via the shared secrets substrate, never in the repo.
"""


class CredentialsMissing(RuntimeError):
    """Raised (not sys.exit) when creds aren't configured — the connector degrades to
    'skipped' rather than killing an aggregate."""


def fetch_live(account=None) -> dict:
    raise NotImplementedError("implement the live fetch; return raw in the source's shape")
