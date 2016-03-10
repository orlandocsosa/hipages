import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class HiPagesSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search(self):
        driver = self.driver
        driver.get("http://www.homeimprovementpages.com.au/")
        element = driver.find_element_by_id("header_category_lookup")
        element.send_keys('plumber')
        element.send_keys(Keys.ENTER)
        result = driver.find_elements_by_class_name('search-result__item-title')
        first_result = result[0]
        assert "Pure Plumbing Professionals" in first_result.text

    def test_negative_search(self):
        driver = self.driver
        driver.get("http://www.homeimprovementpages.com.au/")
        element = driver.find_element_by_id("header_category_lookup")
        element.send_keys('lalalalaal')
        element.send_keys(Keys.ENTER)
        result = driver.find_elements_by_class_name('search-result__main-column')
        first_result = result[0]
        assert "was not found" in first_result.text

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
