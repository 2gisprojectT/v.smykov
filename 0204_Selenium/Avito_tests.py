from selenium import webdriver
from unittest import TestCase
import unittest
from selenium.webdriver.support.ui import Select

class SleniumTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.avito.ru/novosibirsk")

    def test_search(self):
        select = Select(self.driver.find_element_by_id("category"))
        select.select_by_visible_text("Ноутбуки")

        search = self.driver.find_element_by_id("search")
        search.send_keys("DELL")
        search.submit()
        assert "Купить ноутбук" in self.driver.title

    def test_2(self):
        element = self.driver.find_element_by_name("name")
        elem_id = element.get_attribute("id")

        self.assertEqual("search_greyed", elem_id)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
