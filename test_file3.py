import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

headless_option = webdriver.ChromeOptions()
headless_option.add_argument("headless")


class Test_Pytest:
    def test_cred_06(self):
        # driver = webdriver.Chrome()
        # driver = webdriver.Firefox()
        driver = webdriver.Chrome(options=headless_option)
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(2)

        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.CLASS_NAME, "oxd-button").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
        driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()

        time.sleep(5)

    def test_cred_07(self):
        # driver = webdriver.Chrome()
        # driver = webdriver.Firefox()
        driver = webdriver.Chrome(options=headless_option)
        driver.maximize_window()
        driver.get("https://automation.credence.in/shop")
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
        driver.find_element(By.XPATH, "//input[@id='name']").send_keys("George")
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("gixej4625@aramask.com")
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Cred@1234")
        driver.find_element(By.XPATH, "//input[@id='password-confirm']").send_keys("Cred@1234")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)

        try:
            driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print("Registration Complete")
        except NoSuchElementException:
            print("Registration Is failed ")
