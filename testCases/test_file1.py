import pytest
from selenium import webdriver


class Test_Pytest:
    @pytest.mark.skip
    def test_sum_01(self):
        a = 5
        b = 10
        addition = a + b
        print(addition)
        if addition == 15:
            assert True
        else:
            assert False

    @pytest.mark.xfail
    def test_sum_02(self):
        a = 10
        b = 10
        add = a + b
        print(add)

    @pytest.mark.sanity
    def test_multi_01(self):
        a = 5
        b = 10
        multi = a * b
        print(multi)
        if multi == 50:
            assert True
        else:
            assert False

    @pytest.mark.sanity
    def test_cred_url(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        if driver.title == "Credence":
            print("You are at Heaven")
        else:
            print("You are at Hell")

#pytest -v -n=3 --html=Reports/myreport.html