# _*_ coding: utf-8 _*_
#!c:/Python36
#Filename: Base.py
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base(object):
    '''base page object'''

    home_page = 'http://sca12r2ss12c:30000/core/Default.html'

    def __init__(self, driver, base_url = home_page, parent = None):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30
        self.parent = parent

    def _open(self,url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), 'Did not access to %s' % url

    def find_element(self, *locators):
        return self.driver.find_element(*locators)

    def find_elements(self, *locators):
        return self.driver.find_elements(*locators)

    def find_child_element(self, webelement, *locators):
        return webelement.find_element(*locators)

    def find_child_elements(self, webelement, *locators):
        return webelement.find_elements(*locators)

    def open(self):
        self._open(self.url)

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def script(self, src):
        return self.driver.execute_script(src)

    def wait_UI(self, *locators):
        return WebDriverWait(self.driver, self.timeout, 0.5).until(EC.visibility_of_element_located(*locators))




if __name__ == '__main__':
    driver = webdriver.Firefox()
    page = Base(driver)
