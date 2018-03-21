import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

USER="it101"
PASSWORD="it101"

class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_logging_in(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        self.assertIn("Tasks",driver.title)

        username_elem = driver.find_element_by_name("username")
        password_elem = driver.find_element_by_name("password")

        username_elem.clear()
        username_elem.send_keys(USER)

        password_elem.clear()
        password_elem.send_keys(PASSWORD)

        password_elem.send_keys(Keys.RETURN)

        assert "Task List" in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__=="__main__":
    unittest.main()
