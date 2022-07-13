import pytest


@pytest.mark.xdist_group(name="group1")
def test1():
    pass


class TestA:
    @pytest.mark.xdist_group("group1")
    def test2(self):
        pass