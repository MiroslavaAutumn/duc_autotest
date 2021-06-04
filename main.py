from selenium import webdriver
import unittest
import time
import options

### Browser and url ###
driver = webdriver.Chrome(executable_path=options.chromedriver_path)
url = 'https://ducatuswallet.rocknblock.io/'

### Script ###
class FirstStart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=options.chromedriver_path)
        self.driver.implicitly_wait(1000)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_first_start_test_case(self):
        driver = self.driver
        driver.get(url=url)

        driver.find_element_by_xpath("//span").click()
        time.sleep(1)

        for i in range(0, 3):
            driver.find_element_by_xpath(f"//button[@id='checkbox-{i}-0']/span").click()
            time.sleep(0.1)

        driver.find_element_by_xpath("//div[2]/div/div/button/span").click()
        time.sleep(1)

        for i in range(28, 42):
            driver.find_element_by_xpath(f"//button[@id='toggle-{i}-0']/span").click()
            time.sleep(0.1)

        driver.find_element_by_xpath("//div/button/span").click()
        time.sleep(15)
        driver.find_element_by_xpath("//div[3]/button/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[3]/button[2]/span").click()
        time.sleep(10)

        driver.close()
        driver.quit()