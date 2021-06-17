from selenium.webdriver.support.ui import WebDriverWait
import time
import common_functions
import options


### Script ###
class FirstLaunchCreate(options.SetUppedTestCase):
    def test_case_first_launch(self):
        wait = WebDriverWait(self.driver, 100)

        common_functions.start_button(wait=wait)
        common_functions.first_launch_conditions(wait=wait, first_range=0, second_range=3)
        common_functions.select_currencies_toggle(wait=wait, first_range=28, second_range=42)
        start_create_time = time.time()
        common_functions.create_button(wait=wait)
        common_functions.refuse_password(wait=wait)
        end_create_time = time.time()
        creation_time = round(end_create_time - start_create_time, 2)
        print(f"wallet creation took {creation_time} s")

        time.sleep(100)
        self.driver.close()
        self.driver.quit()
