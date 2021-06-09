from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import time
import options
import private_keys

### Browser and url ###
driver = webdriver.Chrome(executable_path=options.chromedriver_path)
url = 'https://ducatuswallet.rocknblock.io/'


### Script ###
class import_wallet(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=options.chromedriver_path)
        self.driver.implicitly_wait(1000)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_import_wallet_test_case(self):
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

        import_start = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//button[2]/span")))
        import_start.click()
        print("start import is ok")

        driver.find_element_by_xpath("//textarea").click()
        driver.find_element_by_xpath("//textarea").clear()
        driver.find_element_by_xpath("//textarea").send_keys(private_keys.wallet_key_1)
        print("key is ok")

        import_wallet = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//page-import-wallet/ion-header/ion-navbar/ion-buttons/button")))
        import_wallet.click()
        print("import key is ok")
        time.sleep(1)

        no_password = "//div[3]/button/span"
        no_password_2 = "//div[3]/button[2]/span"
        refuse_password = [no_password, no_password_2]
        for button in refuse_password:
            ok = wait.until(EC.element_to_be_clickable((
                By.XPATH,
                button)))
            ok.click()
            time.sleep(2)
            print("refuse password is ok")

    ### import from menu ###
        import_from_menu = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//ion-tab[@id='tabpanel-t1-1']/page-wallets/ion-header/ion-navbar/ion-buttons[2]/button")))
        import_from_menu.click()
        print("start import2 is ok")

        driver.find_element_by_xpath("//div[2]/ion-list/button/div/div").click()
        driver.find_element_by_xpath("//div[2]/div/div/ion-list/button[4]/div/div").click()
        driver.find_element_by_xpath("//textarea").click()
        driver.find_element_by_xpath("//textarea").clear()
        driver.find_element_by_xpath("//textarea").send_keys(private_keys.wallet_key_2)
        print("key is ok")

        import_wallet = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//page-import-wallet/ion-header/ion-navbar/ion-buttons/button")))
        import_wallet.click()
        print("import key is ok")
        time.sleep(1)

        no_password = "//div[3]/button/span"
        no_password_2 = "//div[3]/button[2]/span"
        refuse_password = [no_password, no_password_2]
        for button in refuse_password:
            ok = wait.until(EC.element_to_be_clickable((
                By.XPATH,
                button)))
            ok.click()
            time.sleep(1)
            print("refuse password is ok")


        time.sleep(60)
        driver.close()
        driver.quit()