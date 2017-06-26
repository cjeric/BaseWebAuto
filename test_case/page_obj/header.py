# _*_ coding: utf-8 _*_
# !c:/Python36
# Filename: header.py

from test_case.page_obj.base import Base
from selenium.webdriver.common.by import By

class Header(Base):
    url = ''

    # page tiltle locator
    page_header_loc = (By.CSS_SELECTOR, 'div[data-hj-test-id="hj-active-thread-title"]')
    # Return the page title
    def get_header(self):
        return self.find_element(*self.page_header_loc).text