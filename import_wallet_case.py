from selenium.webdriver.support.ui import WebDriverWait
import time
import common_functions
import options


### first launch ###
def import_wallets(wait):
    common_functions.start_button(wait=wait)
    common_functions.first_launch_conditions(wait=wait, first_range=0, second_range=3)

    start_import_time = time.time()

    common_functions.import_wallet_by_seed(wait=wait)
    common_functions.refuse_password(wait=wait)

    end_import_time = time.time()
    import_time = round(end_import_time - start_import_time, 2)
    print(f"wallet import took {import_time} s")

    ### from menu ###
    start_import_2_time = time.time()
    common_functions.import_wallet_by_seed_from_menu(wait=wait)
    common_functions.refuse_password(wait=wait)
    end_import_2_time = time.time()
    import_time = round(end_import_2_time - start_import_2_time, 2)
    print(f"wallet import took {import_time} s")

### Script ###
class FirstLaunchImport(options.SetUppedTestCase):
    def test_case_first_launch(self):
        wait = WebDriverWait(self.driver, 100)
        import_wallets(wait=wait)

        time.sleep(60)
        self.driver.close()
        self.driver.quit()
