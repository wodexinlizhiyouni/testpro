import pytest
import allure

def test_with_nolevel():
    print("no level")
@allure.title("这是测试normal函数")
@allure.severity(allure.severity_level.NORMAL)
def test_with_level_normal01():
    print("fun  normal")

@allure.severity(allure.severity_level.CRITICAL)
def test_with_level_critical01():
    print("fun  critical")

@allure.severity(allure.severity_level.NORMAL)
class Test_level:
    def test_with_level_normal(self):
        print("normal")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_with_level_critical(self):
        print("critial")
