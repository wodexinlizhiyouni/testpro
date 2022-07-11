#测试文件
import pytest

from pythoncode.calc import Calculator

@pytest.mark.parametrize('a,b,c',[(1,1,2),(2,0,1),(3,10,13)])
@pytest.mark.add
def test_add(a,b,c):
    cal=Calculator()
    assert c == cal.add(a,b)


def test_div(a,b,c):
    cal=Calculator()
