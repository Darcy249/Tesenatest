import pytest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Cesta pro ukládání screenshotů
SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

@pytest.fixture(scope="session")
def driver():
    """Inicializuje WebDriver a zajistí, že se spustí pouze jednou"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def take_screenshot(driver, name):
    """Uloží screenshot do složky screenshots"""
    filepath = os.path.join(SCREENSHOT_DIR, f"{name}.png")
    driver.save_screenshot(filepath)
    print(f"Screenshot uložen: {filepath}")

def test_search_and_open_product(driver):
    """Test hledání a otevření produktu 'Blue Top'"""
    wait = WebDriverWait(driver, 10)

    print("Před otevřením stránky")
    driver.get("https://automationexercise.com/products")
    print("Stránka otevřena:", driver.current_url)
    take_screenshot(driver, "01_opened_page")

    # Kliknutí na tlačítko Souhlas (pokud existuje)
    try:
        consent_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Souhlas']")))
        consent_button.click()
        take_screenshot(driver, "02_consent_clicked")
    except:
        print("Souhlas se neobjevil.")

    # Hledání produktu "Blue Top"
    search_box = wait.until(EC.presence_of_element_located((By.ID, "search_product")))
    search_box.send_keys("Blue Top")
    search_box.send_keys(Keys.RETURN)
    take_screenshot(driver, "03_search_results")

    # Kliknutí na tlačítko "View Product"
    try:
        product_link = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[2]/ul/li/a")))
        product_link.click()
        print("Kliknuto na 'View Product'")
        take_screenshot(driver, "04_product_opened")
    except:
        print("Produkt se nenašel nebo nebylo možné na něj kliknout.")
        take_screenshot(driver, "error_product_not_found")

    # Ověření, že jsme na stránce produktu
    time.sleep(2)  # Počkej, než se stránka přesměruje
    print("Po otevření produktu:", driver.current_url)
    take_screenshot(driver, "05_final_page")
