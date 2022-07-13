# content of test_sample.py
import pytest
import yaml


def inc(x):
    return x + 1

# @pytest.mark.parametrize('a,b',[
#     (1,2),
#     (10,20),
#     (11,12)
#
# ])

@pytest.mark.parametrize(("a","b"),yaml.safe_load(open("./data.yaml")))
def test_answer(a,b):
    assert int(a) == b


def test_answer1():
    assert int(3) == 5


def test_answer2():
    assert int(2) == 3

@pytest.fixture()
def login():
    print("登录操作")
    username='jery'
    return username
    yield
    print('teardown')

class  TestDemo:
    def test_a(self,login):
        print(f"test_a  username={login}")
    def test_b(self):
        print("test_b")
    def taesta(self):
        print("hh")




if __name__ == '__main__':
    pytest.main(['test_a.py'])