from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logging.basicConfig(level=logging.INFO)

def init_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def login(driver):
    driver.get('https://the-internet.herokuapp.com/login')
    logging.info("Завантажено сторінку входу...")

    try:
        username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
        password = driver.find_element(By.ID, 'password')
        login_button = driver.find_element(By.CSS_SELECTOR, 'button.radius')
        logging.info("Елементи знайдено...")

        username.send_keys('tomsmith')
        password.send_keys('SuperSecretPassword!')
        login_button.click()
        logging.info("Натиснута кнопка входу...")

        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.flash.success'))
        )

        assert 'You logged into a secure area!' in success_message.text
        logging.info("Тест пройшов успішно!")

    except Exception as e:
        logging.error(f"Помилка: {e}")

def main():
    driver = init_driver()
    try:
        login(driver)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
