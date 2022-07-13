from typing import List

import pytest
@pytest.fixture(scope='session',params=['user1','user2','user3'])
#@pytest.fixture(autouse=True)  为每一个测试用例自动调用此方法
def login(request):
    print("登录")
    print(request.param)
    yield ['username','password']
    print('teardown')

#对测试用例实现定制化功能
def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    """Called after collection has been performed. May filter or re-order
    the items in-place.

    :param pytest.Session session: The pytest session object.
    :param pytest.Config config: The pytest config object.
    :param List[pytest.Item] items: List of item objects.
    """
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")     #group 将下面所有的 option都展示在这个group下。
    mygroup.addoption("--env",    #注册一个命令行选项
                      default='test',
                      dest='env',
                      help='set your run env'
                      )
@pytest.fixture(scope='session')
def cmdoption(request):
    return request.config.getoption("--env", default='test')
