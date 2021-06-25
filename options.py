import time
import unittest
from selenium import webdriver

chromedriver_path = "C:\MA\PY\Automations\duc_autotest\drivers\chrome\chromedriver.exe"
url = 'https://ducatuswallet.rocknblock.io/'
#url = "https://wallet.dicatus.io/"

class SetUppedTestCase(unittest.TestCase):
    def setUp(self):
        print("Запуск!")
        start_loading_time = time.time()
        self.driver = webdriver.Chrome(executable_path=chromedriver_path)
        self.driver.implicitly_wait(1000)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.get(url=url)
        end_loading_time = time.time()
        loading_time = round(end_loading_time - start_loading_time, 2)
        print(f"Page loaded in {loading_time} s")
