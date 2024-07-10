from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class YandexAuthTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://passport.yandex.ru/auth")

    def test_auth(self):
        driver = self.driver
        username_field = driver.find_element_by_name("login")
        password_field = driver.find_element_by_name("passwd")

        username_field.send_keys("Ваш_логин") # Замените на ваш логин
        password_field.send_keys("Ваш_пароль") # Замените на ваш пароль
        password_field.send_keys(Keys.RETURN)

        self.assertIn("https://passport.yandex.ru/profile", driver.current_url)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
