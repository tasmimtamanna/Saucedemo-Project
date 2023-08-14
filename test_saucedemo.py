import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


def login(username, password):
    # Finding WebElements
    username_element = driver.find_element(By.NAME, "user-name")
    password_element = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, "#login-button")

    # type username
    username_element.clear()
    username_element.send_keys(username)

    # Type Password
    password_element.clear()
    password_element.send_keys(password)

    # Click Login button
    login_button.click()
    time.sleep(5)

@pytest.fixture()
def browser_config():
    global driver

    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    driver.get('https://www.saucedemo.com/')
    time.sleep(5)

    yield
    driver.close()



def menu():
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    menu.click()
    time.sleep(3)

    # about
    about = driver.find_element(By.ID, "about_sidebar_link")
    about.click()
    time.sleep(3)
    driver.back()
    time.sleep(2)

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


def products():
    Sauce_Labs_Backpack = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
    Sauce_Labs_Backpack.click()
    time.sleep(4)

    Ad_to_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    Ad_to_cart.click()
    time.sleep(2)

    Back_to_product = driver.find_element(By.ID, "back-to-products")
    Back_to_product.click()
    time.sleep(2)

    Sauce_Labs_Bike_Light = driver.find_element(By.XPATH, '//*[@id="item_0_title_link"]/div')
    Sauce_Labs_Bike_Light.click()
    time.sleep(4)

    Ad_to_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
    Ad_to_cart.click()
    time.sleep(2)

    Back_to_product = driver.find_element(By.ID, "back-to-products")
    Back_to_product.click()
    time.sleep(2)

    Sauce_Labs_Bolt_Tshirt = driver.find_element(By.XPATH, '//*[@id="item_1_title_link"]/div')
    Sauce_Labs_Bolt_Tshirt.click()
    time.sleep(4)

    Ad_to_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    Ad_to_cart.click()
    time.sleep(2)

    Back_to_product = driver.find_element(By.ID, "back-to-products")
    Back_to_product.click()
    time.sleep(2)

    Sauce_Labs_Fleece_Jacket = driver.find_element(By.XPATH, '//*[@id="item_5_title_link"]/div')
    Sauce_Labs_Fleece_Jacket.click()
    time.sleep(3)

    Ad_to_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    Ad_to_cart.click()
    time.sleep(2)

    Back_to_product = driver.find_element(By.ID, "back-to-products")
    Back_to_product.click()
    time.sleep(2)

    Sauce_Labs_Onesiet = driver.find_element(By.XPATH, '//*[@id="item_2_title_link"]/div')
    Sauce_Labs_Onesiet.click()
    time.sleep(4)

    Ad_to_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
    Ad_to_cart.click()
    time.sleep(2)

    Back_to_product = driver.find_element(By.ID, "back-to-products")
    Back_to_product.click()
    time.sleep(2)

    Ad_to_cart = driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
    Ad_to_cart.click()
    time.sleep(2)


def cart():
    cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_button.click()
    time.sleep(2)

    details = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[4]/div[2]')
    details.click()
    time.sleep(3)
    remove = driver.find_element(By.ID, "remove-sauce-labs-bike-light")
    remove.click()
    time.sleep(3)

    cart = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    cart.click()
    time.sleep(3)

    Continue_shopping = driver.find_element(By.ID, "continue-shopping")
    Continue_shopping.click()
    time.sleep(3)


def checkout_button():
    # back to cart
    cart = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    cart.click()
    time.sleep(3)

    # checkout
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

def form():
    # form

    First_name = driver.find_element(By.ID, "first-name")
    First_name.clear()
    First_name.send_keys("Tasmim")
    time.sleep(3)

    Last_name = driver.find_element(By.ID, "last-name")
    Last_name.clear()
    Last_name.send_keys("Tamanna")
    time.sleep(3)

    Postal_code = driver.find_element(By.ID, "postal-code")
    Postal_code.clear()
    Postal_code.send_keys("1211")
    time.sleep(3)

    # continue button
    Continue_button = driver.find_element(By.ID, "continue")
    Continue_button.click()
    time.sleep(3)

def finish():
    # finish
    Finish_button = driver.find_element(By.ID, "finish")
    Finish_button.click()
    time.sleep(3)

    # back to home
    Back_to_home = driver.find_element(By.ID, "back-to-products")
    Back_to_home.click()

def footer():
    # footer
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

def logout():
    # logout
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    menu.click()
    time.sleep(3)

    logout = driver.find_element(By.ID, "logout_sidebar_link")
    logout.click()


def test_saucedemo(browser_config):
    login("standard_user", "secret_sauce")
    dropdown()
    menu()
    products()
    cart()
    checkout_button()
    form()
    finish()
    footer()
    logout()
