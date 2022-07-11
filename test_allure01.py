
import pytest
import allure
test_case_link="https://www.teambition.com/organization/5e4264c107d2130001c2905d/testhub/5ed8db1829e2a400202dc96c/testgroup/61138be2bc682d0017540f56/usercase/5f0c3d8014220d0020839106"
@allure.testcase(test_case_link,'测试链接')
#@allure.feature("search模块")
class Testsearch:
    def test_search1(self):
        print("search1")
        print("2")

    def test_search2(self):
        print("search2")

@allure.feature("登录模块")
class Testlogin:
    @allure.story("登录成功")
    def test_login_success(self):
        with allure.step("步骤1：打开应用"):
            print("打开应用")
        with allure.step("步骤2：进入登录页面"):
            print("进入登录页面")
        print("登录成功")

    @allure.story("登录失败")
    def test_login_fail(self):
        print("登录失败")


if __name__ == '__main__':
    pytest.main(['test_a.py'])