import unittest
from selenium import webdriver
from time import sleep
import datetime

class Logintest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def test_login(self):
        self.log_in('http://101.207.139.52:30501/jac/#/jac/login','root','root')
        self.message_send()
        self.holiday_send()

    def log_in(self,url,usr,pwd):
        self.driver.get(url)
        sleep(1)
        username = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/form/div[1]/div/div/input')
        username.clear()
        password = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/form/div[2]/div/div/input')
        password.clear()
        username.send_keys(usr)
        password.send_keys(pwd)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/button').click()

    def message_send(self):
        #信息推送
        message = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/a[12]/div[2]/span').click()
        sleep(1)
    def holiday_send(self):
        self.driver.find_element_by_xpath('//*[@id="app"]//span[text()="节日慰问"]').click()
        sleep(1)
        #增加
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/form/div/button[1]').click()
        #主题
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/form/div[1]/div/div[1]/input').send_keys("节日慰问"+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        #内容概览
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div[1]/textarea').send_keys("节日慰问"+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        self.driver.switch_to.frame('ueditor_0')
        self.driver.find_element_by_xpath('/html/body').send_keys("节日慰问"+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        sleep(1)
        self.driver.switch_to.default_content()
        #保存并发布
        send = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/div/button[1]/span')
        send.click()
        sleep(2)

    def tearDown(self):
       self.driver.quit()


    def vehicle_manage(self):
        vehicle_manage = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/a[3]/div[2]/span')
        vehicle_manage.click()

        sleep(5)

        multe = self.driver.find_element_by_xpath( '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/form/div[1]/span[1]/i')

        multe.click()
        sleep(5)

        vehicle_seriers = self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/form/div[2]/div[1]/div[1]/div/div/div[1]/input[2]')
        vehicle_seriers.click()
        sleep(5)
        select = self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/form/div[2]/div[1]/div[1]/div/div/div[2]/ul[2]/li[1]')

        select.click()

        sleep(5)

        search_button = self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/form/div[1]/button[2]')
        search_button.click()

        sleep(30)
    if __name__ == '__main__':
        unittest.main(verbosity=2)



