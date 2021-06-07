from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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

    def test_first_start_case(self):
        print("Запуск!")
        driver = self.driver
        driver.get(url=url)
        wait = WebDriverWait(driver, 100)

        start_button = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//span")))
        start_button.click()
        print("start button is ok")
        time.sleep(0.5)

        for i in range(0, 3):
            checkbox = wait.until(EC.element_to_be_clickable((
                By.XPATH,
                f"//button[@id='checkbox-{i}-0']/span")))
            checkbox.click()
            print(f"chechbox {i} is ok")

        continue_button = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//div[2]/div/div/button/span")))
        continue_button.click()
        print("continue button is ok")
        time.sleep(0.5)

        for i in range(28, 42):
            select_coin = wait.until(EC.element_to_be_clickable((
                By.XPATH,
                f"//button[@id='toggle-{i}-0']/span")))
            select_coin.click()
            print(f"toggle {i} is ok")

        wallet_button = "//div/button/span"
        no_password = "//div[3]/button/span"
        no_password_2 = "//div[3]/button[2]/span"

        create_wallet = [wallet_button, no_password, no_password_2]
        for button in create_wallet:
            start_creating = wait.until(EC.element_to_be_clickable((
                By.XPATH,
                button)))
            start_creating.click()
            time.sleep(1)
            print(f"{button} is ok")

        time.sleep(60)
        driver.close()
        driver.quit()