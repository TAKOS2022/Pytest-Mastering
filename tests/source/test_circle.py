import pytest

import pytest_mastering.source.shapes as shapes


class TestCircle:

    def setup_method(self, method):
        print(f"Setting up {method}")

    def teardown_method(self, method):
        print(f"Tearing down {method}")

    def test_one(self):
        assert True