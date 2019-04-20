import pytest


class TestGdb:
    @pytest.mark.complete("gdb - ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("gdb foo ", cwd="gdb")
    def test_2(self, completion):
        assert completion == sorted(
            "core core.12345 "
            "core.weston.1000.bc46148827504908898ad152f43bffb2.5308."
            "1555362132000000".split()
        )