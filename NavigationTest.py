#!usr/bin/python
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

class NavigationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('https://www.baidu.com/')

    def testBrowserNavigation(self):
        driver = self.driver
        search_field = driver.find_element_by_name('wd')
        search_field.clear()
        print('一个小小的里程碑')

        search_field.send_keys('圣女果')
        search_field.submit()
        time.sleep(1)

        self.assertEqual('圣女果_百度搜索',driver.title)

        driver.back()
        self.assertTrue(WebDriverWait(self.driver,30).until(expected_conditions.title_contains('百度一下')))
    def tearDown(self):
        driver = self.driver
        driver.quit()

if __name__ == "__main__":
    unittest.main()