from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import options
import time
from import_wallet_case import import_wallets


class Transaction(options.SetUppedTestCase):
    def test_case_first_launch(self):
        wait = WebDriverWait(self.driver, 100)

        import_wallets(wait=wait)

        open_wallet = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//ion-label[@id='lbl-85']/div")))
        open_wallet.click()
        time.sleep(1)
        print("open sourse wallet is ok")

        send_button = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "/html/body/ion-app/ng-component/ion-nav/ng-component/ion-tabs/page-wallet-details/ion-content/div[2]"
            "/div/expandable-header/expandable-header-footer/div[2]/button[2]")))
        send_button.click()
        time.sleep(1)
        print("send button is ok")

        select_dest_wallet = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "/html/body/ion-app/ng-component/ion-nav/ng-component/ion-tabs/page-send/wide-header-page/"
            "ion-content/div[2]/div/div/div/div/page-transfer-to/div[1]/div/ion-list/div[2]/div[2]/"
            "wallet-item-content/ion-item/div[1]/div")))
        select_dest_wallet.click()
        print("select destination wallet is ok")
        time.sleep(1)

        enter_amount = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "(.//*[normalize-space(text()) and normalize-space(.)='DUC'])[5]/following::span[1]")))
        enter_amount.click()
        time.sleep(1)
        print("enter amount is ok")

        continue_button = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "(.//*[normalize-space(text()) and normalize-space(.)='.'])[1]/following::span[3]")))
        continue_button.click()
        time.sleep(1)
        print("continue button is ok")

        click_to_send_button = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "/html/body/ion-app/ng-component/ion-nav/ng-component/ion-tabs/page-confirm/wide-header-page/"
            "ion-footer/div/ion-toolbar/div[2]/button/span")))
        click_to_send_button.click()
        time.sleep(5)
        print("click to send button is ok")

        ok_button = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//html/body/ion-app/ion-modal/div/page-finish/div/div[2]")))
        ok_button.click()
        print("transaction sent")

        time.sleep(60)
        self.driver.close()
        self.driver.quit()
