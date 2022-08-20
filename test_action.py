import pytest
import time
import logging


from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select


logging.basicConfig(level=logging.INFO)
my_log = logging.getLogger()

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrom_driver_path = "C:\selenium\chromedriver.exe"


# drag & drop

def test_drag_drop():
    driver_drag_drop = webdriver.Chrome(chrom_driver_path, chrome_options=chrome_options)
    driver_drag_drop.get('https://demo.guru99.com/test/drag_drop.html')
    driver_drag_drop.maximize_window()

    my_log.info("testing to  drag & drop")

    block13_btn = driver_drag_drop.find_element(By.CLASS_NAME, "block13 ")
    shopping_card1 = driver_drag_drop.find_element(By.ID, "shoppingCart1")
    bank_btn = driver_drag_drop.find_element(By.ID, "credit2")
    btn_5000 = block13_btn.find_element(By.CLASS_NAME, "button")
    btn_c = driver_drag_drop.find_element(By.ID, "credit1")
    drop2 = shopping_card1.find_element(By.CLASS_NAME, "ui-widget-content")
    drop1 = driver_drag_drop.find_element(By.ID, "shoppingCart4")
    drop3 = driver_drag_drop.find_element(By.ID, "shoppingCart3").find_element(By.ID, "loan")
    drop4 = driver_drag_drop.find_element(By.ID, "amt8")

    result = driver_drag_drop.find_element(By.CLASS_NAME, "table4_result")
    result_btn = result.find_element(By.CLASS_NAME, "button")
    action = ActionChains(driver_drag_drop)
    action.drag_and_drop(btn_5000, drop1).perform()
    action.drag_and_drop(bank_btn, drop2).perform()
    action.drag_and_drop(btn_5000, drop4).perform()
    action.drag_and_drop(btn_c, drop3).perform()
    result_btn.click()
    a = (drop1.text[7::], drop2.text, drop4.text, drop3.text)
    b = ("5000", "BANK", "5000", "SALES")
    assert a == b
    driver_drag_drop.quit()


# IFRAME
# יש שגיאה - לפעמים זה עובד ולפעמים לא - צריך לבדוק

def test_iframe():
    my_email = 'deborah270401@gmail.com'
    my_password = 'deborah21'
    my_account = 'deborah'

    driver_iframe = webdriver.Chrome(chrom_driver_path, chrome_options=chrome_options)
    driver_iframe.get('http://automationpractice.com/index.php')
    driver_iframe.set_window_size(800, 800)
    window_name = driver_iframe.window_handles[0]
    my_log.info("testing of iframe")

    container = driver_iframe.find_element(By.CLASS_NAME, "product-container")
    container.find_element(By.CLASS_NAME, 'icon-eye-open').click()

    driver_iframe.switch_to.frame(driver_iframe.find_element(By.CLASS_NAME, "fancybox-iframe"))
    time.sleep(2)
    add_to_my_card = driver_iframe.find_element(By.ID, "add_to_cart")
    add_to_my_card.click()
    time.sleep(2)

    driver_iframe.switch_to.window(window_name)
    driver_iframe.find_element(By.CSS_SELECTOR, '.button-container a').click()
    time.sleep(2)

    btn1 = driver_iframe.find_element(By.CLASS_NAME, "cart_navigation.clearfix")
    btn1.find_element(By.CLASS_NAME, "button.btn.btn-default.standard-checkout.button-medium").click()
    time.sleep(2)
    driver_iframe.find_element(By.ID, "email").send_keys(my_email)
    driver_iframe.find_element(By.ID, "passwd").send_keys(my_password)
    driver_iframe.find_element(By.CLASS_NAME, "icon-lock").click()
    time.sleep(2)
    driver_iframe.find_element(By.CSS_SELECTOR, '[name=processAddress]').click()
    time.sleep(2)
    driver_iframe.find_element(By.CSS_SELECTOR, '[type=checkbox]').click()
    time.sleep(2)
    driver_iframe.find_element(By.CSS_SELECTOR, '[name=processCarrier]').click()
    time.sleep(2)
    driver_iframe.find_element(By.CLASS_NAME, "bankwire").click()
    time.sleep(2)
    driver_iframe.find_element(By.CSS_SELECTOR, "button.button-medium").click()
    time.sleep(2)
    cmp = driver_iframe.find_element(By.CLASS_NAME, "cheque-indent").find_element(By.CLASS_NAME, "dark")
    assert "Your order on My Store is complete." in cmp.text
    driver_iframe.close()


# Alerts

def test_alert():
    driver_alert = webdriver.Chrome(chrom_driver_path, chrome_options=chrome_options)
    driver_alert.get('http://the-internet.herokuapp.com/javascript_alerts')
    driver_alert.set_window_size(800, 800)

    my_log.info("testing of alerts")

    scripts = ("jsAlert()", "jsConfirm()", "jsPrompt()")
    result = driver_alert.find_element(By.ID, "result")
    list_result = list()
    for script in scripts:
        driver_alert.execute_script(script)
        alert = driver_alert.switch_to.alert
        if 'prompt' in alert.text:
            alert.send_keys("Hello deborah")
        alert.accept()
        list_result.append(result.text)
        time.sleep(5)

    assert list_result[0] == "You successfully clicked an alert"
    assert list_result[1] == "You clicked: Ok"
    assert list_result[2] == "You entered: Hello deborah"
    driver_alert.close()


# selection

def test_selection():
    driver_selection = webdriver.Chrome(chrom_driver_path, chrome_options=chrome_options)
    driver_selection.maximize_window()
    driver_selection.get('https://demo.guru99.com/test/newtours/register.php')

    my_log.info("testing of selection")

    driver_selection.find_element(By.NAME, "firstName").send_keys("deborah")
    driver_selection.find_element(By.NAME, "lastName").send_keys("shoushana")
    driver_selection.find_element(By.NAME, "phone").send_keys("0585123646")
    driver_selection.find_element(By.NAME, "userName").send_keys("deborah")
    time.sleep(3)
    driver_selection.find_element(By.NAME, "address1").send_keys("klosner 22")
    driver_selection.find_element(By.NAME, "city").send_keys("raanana")
    driver_selection.find_element(By.NAME, "state").send_keys("מרכז")
    driver_selection.find_element(By.NAME, "postalCode").send_keys("4336711")
    country = driver_selection.find_element(By.NAME, "country")
    select = Select(country)
    select.select_by_value("ISRAEL")
    time.sleep(3)
    driver_selection.find_element(By.NAME, "email").send_keys("deborah270401@gmail.com")
    driver_selection.find_element(By.NAME, "password").send_keys("deborah21")
    confirm_passwd = driver_selection.find_element(By.NAME, "confirmPassword")
    confirm_passwd.send_keys("deborah21")
    confirm_passwd.send_keys(Keys.ENTER)
    time.sleep(3)
    assert driver_selection.find_element(By.CSS_SELECTOR, "img[src='images/mast_register.gif']")
    driver_selection.close()
