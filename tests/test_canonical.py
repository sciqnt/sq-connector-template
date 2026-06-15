"""Skeleton conformance: the discovery surface exists and to_canonical is shaped.

Self-contained (no sciqnt-contract dep yet) so a fresh repo from this template is
CI-green immediately. Once sq-contract is published, swap this for the real
`conformance.check_snapshot()` assertion against the canonical schema.
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import sq_example  # noqa: E402


class TestSkeleton(unittest.TestCase):
    def test_discovery_surface(self):
        self.assertTrue(callable(sq_example.snapshot))
        self.assertTrue(callable(sq_example.accounts))
        self.assertEqual(sq_example.accounts(), [])

    def test_to_canonical_shaped(self):
        snap = sq_example.snapshot()
        self.assertIn("positions", snap)
        self.assertIn("cash", snap)


if __name__ == "__main__":
    unittest.main()
