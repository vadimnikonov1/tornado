import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import os
from dotenv import load_dotenv

# Initialization

load_dotenv()

chrome_options = ChromeOptions()
chrome_options.add_extension(os.getenv('EXTENSION'))

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

try:

    driver.get(os.getenv('LINK'))
    time.sleep(3)

    window_before = driver.window_handles[0]
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_before)

    # Wallet adding

    start = driver.find_element(By.TAG_NAME, 'button')
    start.click()
    import_wallet = driver.find_element(By.XPATH, '//button[text()="Import wallet"]')
    import_wallet.click()
    agree = driver.find_element(By.XPATH, '//button[text()="I Agree"]')
    agree.click()

    grid1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                            '.import-srp__srp>.import-srp__srp-word:nth-child(1)'
                                            '>.MuiFormControl-root>.MuiInput-formControl>input')))

    # Secret phrase

    grid1.send_keys(os.getenv('PHRASE1'))

    grid2 = driver.find_element(By.CSS_SELECTOR, '.import-srp__srp>.import-srp__srp-word:nth-child(2)'
                                                 '>.MuiFormControl-root>.MuiInput-formControl>input')
    grid2.send_keys(os.getenv('PHRASE2'))

    grid3 = driver.find_element(By.CSS_SELECTOR, '.import-srp__srp>.import-srp__srp-word:nth-child(3)'
                                                 '>.MuiFormControl-root>.MuiInput-formControl>input')
    grid3.send_keys(os.getenv('PHRASE3'))

    grid4 = driver.find_element(By.CSS_SELECTOR, '.import-srp__srp>.import-srp__srp-word:nth-child(4)'
                                                 '>.MuiFormControl-root>.MuiInput-formControl>input')
    grid4.send_keys(os.getenv('PHRASE4'))

    grid5 = driver.find_element(By.CSS_SELECTOR, '.import-srp__srp>.import-srp__srp-word:nth-child(5)'
                                                 '>.MuiFormControl-root>.MuiInput-formControl>input')
    grid5.send_keys(os.getenv('PHRASE5'))

    grid6 = driver.find_element(By.CSS_SELECTOR,
                                '.import-srp__srp>.import-srp__srp-word:nth-child(6)'
                                '>.MuiFormControl-root>.MuiInput-formControl>input')
    grid6.send_keys(os.getenv('PHRASE6'))

    grid7 = driver.find_element(By.CSS_SELECTOR,
                                '.import-srp__srp>.import-srp__srp-word:nth-child(7)'
                                '>.MuiFormControl-root>.MuiInput-formControl>input')
    grid7.send_keys(os.getenv('PHRASE7'))

    grid8 = driver.find_element(By.CSS_SELECTOR,
                                '.import-srp__srp>.import-srp__srp-word:nth-child(8)'
                                '>.MuiFormControl-root>.MuiInput-formControl>input')
    grid8.send_keys(os.getenv('PHRASE8'))

    grid9 = driver.find_element(By.CSS_SELECTOR,
                                '.import-srp__srp>.import-srp__srp-word:nth-child(9)'
                                '>.MuiFormControl-root>.MuiInput-formControl>input')
    grid9.send_keys(os.getenv('PHRASE9'))

    grid10 = driver.find_element(By.CSS_SELECTOR,
                                 '.import-srp__srp>.import-srp__srp-word:nth-child(10)'
                                 '>.MuiFormControl-root>.MuiInput-formControl>input')
    grid10.send_keys(os.getenv('PHRASE10'))

    grid11 = driver.find_element(By.CSS_SELECTOR,
                                 '.import-srp__srp>.import-srp__srp-word:nth-child(11)'
                                 '>.MuiFormControl-root>.MuiInput-formControl>input')
    grid11.send_keys(os.getenv('PHRASE11'))

    grid12 = driver.find_element(By.CSS_SELECTOR,
                                 '.import-srp__srp>.import-srp__srp-word:nth-child(12)'
                                 '>.MuiFormControl-root>.MuiInput-formControl>input')
    grid12.send_keys(os.getenv('PHRASE12'))

    new_password = driver.find_element(By.ID, 'password')
    new_password.send_keys(os.getenv('PASSWORD'))

    confirm_password = driver.find_element(By.ID, 'confirm-password')
    confirm_password.send_keys(os.getenv('PASSWORD'))

    check_box = driver.find_element(By.ID, 'create-new-vault__terms-checkbox')
    check_box.click()

    import_button = driver.find_element(By.XPATH, '//button[text()="Import"]')
    import_button.click()

    all_button = wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="All Done"]')))
    all_button.click()

    time.sleep(3)
    close = driver.find_element(By.CSS_SELECTOR,
                                '.popover-wrap.whats-new-popup__popover>div:nth-child(1)'
                                '>.popover-header__title>button')
    close.click()

    # Switch on testing network

    driver.find_element(By.CLASS_NAME, 'identicon__address-wrapper').click()

    settings = driver.find_element(By.CSS_SELECTOR, '.account-menu>div:nth-child(11)')
    settings.click()

    advance = driver.find_element(By.CSS_SELECTOR, '.tab-bar>button:nth-child(2)')
    advance.click()

    test_enable = driver.find_element(By.CSS_SELECTOR, '.settings-page__body>div:nth-child(7)>'
                                                       'div:nth-child(2)>div>.toggle-button>div:nth-child(1)')
    test_enable.click()

    select_network = driver.find_element(By.CLASS_NAME, 'network-display')
    select_network.click()

    select_goerli = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.network-dropdown-list>li:nth-child(5)')))
    select_goerli.click()

    go_to_start_page = driver.find_element(By.CSS_SELECTOR, '.app-header__logo-container--clickable')
    go_to_start_page.click()

    account_id = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'selected-account__clickable')))
    account_id.click()
    time.sleep(2)

    # Input data for transaction

    driver.get(os.getenv('LINK'))

    input_id = driver.find_element(By.CSS_SELECTOR, '[name="address"]')
    input_id.send_keys(Keys.CONTROL, 'v')

    amount = driver.find_element(By.CSS_SELECTOR, '[name="amount"]')
    amount.click()
    amount.send_keys('10000')

    connect = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.button.is-primary')))
    connect.click()

    # Connecting with Metamask

    metamask = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.is-grouped>.control>.is-metamask')))
    metamask.click()

    time.sleep(3)
    wait.until(EC.number_of_windows_to_be(3))

    for window_handle in driver.window_handles:
        if window_handle != window_before and window_handle != window_after:
            driver.switch_to.window(window_handle)
            button_next = driver.find_element(By.XPATH, '//button[text()="Next"]')
            button_next.click()
            button_connect = driver.find_element(By.XPATH, '//button[text()="Connect"]')
            button_connect.click()

    # Mint tokens

    driver.switch_to.window(window_before)
    mint_tokens = driver.find_element(By.CSS_SELECTOR, '.button.is-primary')
    mint_tokens.click()

    time.sleep(3)

    for window_handles in driver.window_handles:
        if window_handles != window_before and window_handles != window_after:
            driver.switch_to.window(window_handles)
            button_confirm = wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="Confirm"]')))
            button_confirm.click()
            print("Successfully")

finally:
    driver.quit()



