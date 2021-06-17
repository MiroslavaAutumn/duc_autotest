import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import private_keys


### First launch functions ###
def start_button(wait):
    start_button = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//span")))
    start_button.click()
    time.sleep(0.3)
    print("start button is ok")

def first_launch_conditions(wait, first_range, second_range):
    for i in range(first_range, second_range):
        checkbox = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            f"//button[@id='checkbox-{i}-0']/span")))
        checkbox.click()
        print(f"checkbox {i} is ok")
    confirm_and_finish_button = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//div[2]/div/div/button/span")))
    confirm_and_finish_button.click()
    print("continue button is ok")


### Create wallet functions ###
def select_currencies_toggle(wait, first_range, second_range):
    for i in range(first_range, second_range):
        select_coin = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            f"//button[@id='toggle-{i}-0']/span")))
        select_coin.click()
        print(f"toggle {i} is ok")

def create_button(wait):
    create_button = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//div/button/span")))
    create_button.click()
    print("create button is ok")


### Import wallet ###
def import_wallet_by_seed(wait):
    import_existing_wallet_button = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "(.//*[normalize-space(text()) and normalize-space(.)='Create'])[1]/following::span[1]")))
    import_existing_wallet_button.click()
    print("start import is ok")

    wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//textarea"))).send_keys(private_keys.wallet_key_1)
    print("key is ok")

    import_button = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//page-import-wallet/ion-header/ion-navbar/ion-buttons/button")))
    import_button.click()
    print("import is ok")

def import_wallet_by_seed_from_menu(wait):
    menu_button = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//ion-tab[@id='tabpanel-t1-1']/page-wallets/ion-header/ion-navbar/ion-buttons[2]/button")))
    menu_button.click()

    create_or_import_button = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "(.//*[normalize-space(text()) and normalize-space(.)='Create a new wallet'])[1]/following::div[3]")))
    create_or_import_button.click()

    import_wallet_button = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "(.//*[normalize-space(text()) and normalize-space(.)='Requires invitation to join'])[1]/following::div[3]")))
    import_wallet_button.click()
    print("start import is ok")

    wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//textarea"))).send_keys(private_keys.wallet_key_2)
    print("key is ok")

    import_button = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//page-import-wallet/ion-header/ion-navbar/ion-buttons/button")))
    import_button.click()
    print("import 2 is ok")

def refuse_password(wait):
    yes = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        f"//div[3]/button/span")))
    yes.click()
    print(f"yes button is ok")
    time.sleep(1)
    im_sure = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        f"//div[3]/button[2]/span")))
    im_sure.click()
    print(f"i'm sure button is ok")