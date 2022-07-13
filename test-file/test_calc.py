#测试文件
import pytest
import sys
print(sys.path.append(('..')))

from pythoncode.calc import Calculator

# @pytest.mark.parametrize('a,b,c',[(1,1,3)])
# #@pytest.mark.flaky(reruns=5,reruns_delay=2)
# #@pytest.mark.parametrize('a',[1,2,3])
# #@pytest.mark.parametrize('b',[4,5,6])
# @pytest.mark.add
# def test_add(a,b,c):
#     cal=Calculator()
#     assert c == cal.add(a,b)
#     assert 5 == cal.add(1,4)

# def test_assume():
#     pytest.assume(1==2)
#     pytest.assume(1==1)
#     pytest.assume(1 == 3)
#@pytest.mark.run(order=-1)
# @pytest.mark.first
# def test_bar1():
#     assert True
#
# @pytest.mark.run(order=2)
# def test_foo():
#     assert True
#
# @pytest.mark.run(order=1)
# def test_bar():
#     assert True

