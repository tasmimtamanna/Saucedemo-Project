import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


@pytest.fixture()
def browser_config():
    global driver

    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    driver.get('https://www.saucedemo.com/')
    time.sleep(5)

    yield
    driver.close()


def test_browser(browser_config):
    print("Browser Launch Successfully")


def login(username, password):
    # Finding WebElements
    username_element = driver.find_element(By.NAME, "user-name")
    password_element = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, "#login-button")

    # Type Email
    username_element.clear()
    username_element.send_keys(username)

    # Type Password
    password_element.clear()
    password_element.send_keys(password)

    # Click Login button
    login_button.click()


def test_login_valid_testCase01(browser_config):
    login("standard_user", "secret_sauce")



def dropdown():
    dropdown_element = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select')
    all_option = Select(dropdown_element)
    all_option.select_by_visible_text("Name (Z to A)")
    time.sleep(3)

    dropdown_element = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select')
    all_option = Select(dropdown_element)
    all_option.select_by_visible_text("Price (low to high)")
    time.sleep(3)

    dropdown_element = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select')
    all_option = Select(dropdown_element)
    all_option.select_by_visible_text("Price (high to low)")
    time.sleep(3)


def test_dropdown(browser_config):
    login("standard_user", "secret_sauce")
    dropdown()



def menu():
    menu = driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]')
    menu.click()
    time.sleep(3)

    # about
    about = driver.find_element(By.XPATH, '//*[@id="about_sidebar_link"]')
    about.click()
    time.sleep(3)
    driver.back()
    time.sleep(2)

def test_menu(browser_config):
    login("standard_user", "secret_sauce")
    menu()
    driver.close()


def Sauce_Labs_Backpack():
    Sauce_Labs_Backpack = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
    Sauce_Labs_Backpack.click()
    time.sleep(4)


    Ad_to_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    Ad_to_cart.click()
    time.sleep(2)

    Back_to_product = driver.find_element(By.ID, "back-to-products")
    Back_to_product.click()
    time.sleep(2)


def test_Sauce_Labs_Backpack(browser_config):
    login("standard_user", "secret_sauce")
    Sauce_Labs_Backpack()
    driver.close()


def Sauce_Labs_Bike_Light():
    Sauce_Labs_Bike_Light = driver.find_element(By.XPATH, '//*[@id="item_0_title_link"]/div')
    Sauce_Labs_Bike_Light.click()
    time.sleep(4)

    Ad_to_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
    Ad_to_cart.click()
    time.sleep(2)

    Back_to_product = driver.find_element(By.ID, "back-to-products")
    Back_to_product.click()
    time.sleep(2)


def test_Sauce_Labs_Bike_Light(browser_config):
    login("standard_user", "secret_sauce")
    Sauce_Labs_Bike_Light()



def Sauce_Labs_Bolt_Tshirt():
    Sauce_Labs_Bolt_Tshirt = driver.find_element(By.XPATH, '//*[@id="item_1_title_link"]/div')
    Sauce_Labs_Bolt_Tshirt.click()
    time.sleep(4)

    Ad_to_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    Ad_to_cart.click()
    time.sleep(2)

    Back_to_product = driver.find_element(By.ID, "back-to-products")
    Back_to_product.click()
    time.sleep(2)


def test_Sauce_Labs_Bolt_Tshirt(browser_config):
    login("standard_user", "secret_sauce")
    Sauce_Labs_Bolt_Tshirt()



def Sauce_Labs_Fleece_Jacket():
    Sauce_Labs_Fleece_Jacket = driver.find_element(By.XPATH, '//*[@id="item_5_title_link"]/div')
    Sauce_Labs_Fleece_Jacket.click()
    time.sleep(3)

    Ad_to_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    Ad_to_cart.click()
    time.sleep(2)

    Back_to_product = driver.find_element(By.ID, "back-to-products")
    Back_to_product.click()
    time.sleep(2)


def test_Sauce_Labs_Fleece_Jacket(browser_config):
    login("standard_user", "secret_sauce")
    Sauce_Labs_Fleece_Jacket()



def Sauce_Labs_Onesiet():
    Sauce_Labs_Onesiet = driver.find_element(By.XPATH, '//*[@id="item_2_title_link"]/div')
    Sauce_Labs_Onesiet.click()
    time.sleep(4)

    Ad_to_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
    Ad_to_cart.click()
    time.sleep(2)

    Back_to_product = driver.find_element(By.ID, "back-to-products")
    Back_to_product.click()
    time.sleep(2)


def test_Sauce_Labs_Onesiet(browser_config):
    login("standard_user", "secret_sauce")
    Sauce_Labs_Onesiet()



def Sauce_Labs_TShirt():
    Ad_to_cart = driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
    Ad_to_cart.click()
    time.sleep(2)


def test_Sauce_Labs_Tshirt(browser_config):
    login("standard_user", "secret_sauce")
    Sauce_Labs_TShirt()



# Cart

def cart():
    cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_button.click()
    time.sleep(3)


def test_cart(browser_config):
    login("standard_user", "secret_sauce")
    Sauce_Labs_TShirt()
    Sauce_Labs_Onesiet()
    Sauce_Labs_Bike_Light()
    Sauce_Labs_Fleece_Jacket()
    cart()


def continue_shopping():
    Continue_shopping = driver.find_element(By.ID, "continue-shopping")
    Continue_shopping.click()
    time.sleep(3)

    #back to cart again
    cart = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    cart.click()
    time.sleep(3)



def test_continue_shopping(browser_config):
    login("standard_user", "secret_sauce")
    Sauce_Labs_TShirt()
    Sauce_Labs_Onesiet()
    Sauce_Labs_Fleece_Jacket()
    cart()
    continue_shopping()


def checkout_button():
    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()
    time.sleep(3)

    # cancel
    Cancel = driver.find_element(By.ID, "cancel")
    Cancel.click()
    time.sleep(3)

    # again checkout
    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()
    time.sleep(3)

def test_checkout_button(browser_config):
    login("standard_user", "secret_sauce")
    Sauce_Labs_TShirt()
    Sauce_Labs_Onesiet()
    Sauce_Labs_Fleece_Jacket()
    cart()
    continue_shopping()
    checkout_button()


def form(firstname, lastname, postalcode):
    First_name = driver.find_element(By.ID, "first-name")
    First_name.clear()
    First_name.send_keys(firstname)

    Last_name = driver.find_element(By.ID, "last-name")
    Last_name.clear()
    Last_name.send_keys(lastname)

    Postal_code = driver.find_element(By.ID, "postal-code")
    Postal_code.clear()
    Postal_code.send_keys(postalcode)
    time.sleep(2)

    #continue

    Continue_button = driver.find_element(By.ID, "continue")
    Continue_button.click()
    time.sleep(3)


def test_form(browser_config):
    login("standard_user", "secret_sauce")
    Sauce_Labs_TShirt()
    Sauce_Labs_Onesiet()
    Sauce_Labs_Fleece_Jacket()
    cart()
    continue_shopping()
    checkout_button()
    form("Tasmim", "Islam", "1211")

def finish():
    Finish_button = driver.find_element(By.ID, "finish")
    Finish_button.click()
    time.sleep(3)

    # back to home

    Back_to_home = driver.find_element(By.ID, "back-to-products")
    Back_to_home.click()

def test_finish(browser_config):
    login("standard_user", "secret_sauce")
    Sauce_Labs_TShirt()
    Sauce_Labs_Onesiet()
    Sauce_Labs_Fleece_Jacket()
    cart()
    continue_shopping()
    checkout_button()
    form("Tasmim", "Islam", "1211")
    finish()


def footer():
    parent_window = driver.current_window_handle

    child_window_link = driver.find_element(By.LINK_TEXT, 'Twitter')
    child_window_link.click()

    second_window_link = driver.find_element(By.LINK_TEXT, 'Facebook')
    second_window_link.click()

    third_window_link = driver.find_element(By.LINK_TEXT, 'LinkedIn')
    third_window_link.click()
    all_windows = driver.window_handles
    time.sleep(2)

    # Switching child_window
    for child_window in all_windows:
        if child_window not in parent_window:
            driver.switch_to.window(child_window)
            time.sleep(4)
            print('Child window Title: ', driver.title)

    for child_window in all_windows:
        if child_window not in parent_window:
            driver.switch_to.window(parent_window)
            time.sleep(2)
            print("Parent window Title: ", driver.title)


def test_footer(browser_config):
    login("standard_user", "secret_sauce")
    footer()


def logout():
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    menu.click()
    time.sleep(3)

    logout = driver.find_element(By.ID, "logout_sidebar_link")
    logout.click()

def test_logout(browser_config):
    login("standard_user", "secret_sauce")
    logout()
