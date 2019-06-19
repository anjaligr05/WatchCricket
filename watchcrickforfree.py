import time
import sys
from selenium.webdriver.support.ui import WebDriverWait
def get_clear_button(driver):
    root1 = driver.find_element_by_css_selector(("settings-ui"))
    shadow_root1 = driver.execute_script('return arguments[0].shadowRoot', root1);
    root2 = shadow_root1.find_element_by_css_selector(("settings-main"));
    shadow_root2 = driver.execute_script('return arguments[0].shadowRoot', root2)
    root3 = shadow_root2.find_element_by_css_selector(("settings-basic-page"));
    shadow_root3 = driver.execute_script('return arguments[0].shadowRoot', root3)
    root4 = shadow_root3.find_element_by_css_selector(("settings-section > settings-privacy-page"));
    shadow_root4 = driver.execute_script('return arguments[0].shadowRoot', root4)
    root5 = shadow_root4.find_element_by_css_selector(("settings-clear-browsing-data-dialog"));
    shadow_root5 = driver.execute_script('return arguments[0].shadowRoot', root5)
    root6 = shadow_root5.find_element_by_css_selector(("#clearBrowsingDataDialog"));
    clearDataButton = root6.find_element_by_css_selector(("#clearBrowsingDataConfirm"));
    return clearDataButton
def clear_chrome_cache(driver, timeout=60):
    driver.get('chrome://settings/clearBrowserData')
    clearDataButton = get_clear_button(driver)
    clearDataButton.click();
from selenium import webdriver
while True:
    if len(sys.argv)<2:
        print 'Usage: python watchcrickforfree.py <link-name (no quotes)>'
        exit()
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    driver.get(sys.argv[1])
    time.sleep(1)
    driver.find_element_by_class_name('vjs-big-play-button').click()
    time.sleep(300)
    clear_chrome_cache(driver)
    driver.quit()
