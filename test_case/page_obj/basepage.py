# _*_ coding: utf-8 _*_
# !c:/Python36
# Filename: basepage.py

from test_case.page_obj.base import Base
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BasePage(Base):
    url = ''

    home_page = 'http://sca12r2ss12c:30000/core/Default.html'

    # def __init__(self,driver, base_url = home_page, parent = None ):
    #     Base.__init__(self,driver, base_url, parent)
    #     self.__page_wrap_loc = (By.CSS_SELECTOR, 'div[class="hj-spaces-page-wrap supply-chain-advantage"][style="outline: medium none;"]')
    #     self.page_wrap = self.wait_UI(self.__page_wrap_loc)

    __page_wrap_loc = (
    By.CSS_SELECTOR, 'div[class="hj-spaces-page-wrap supply-chain-advantage"][style="outline: medium none;"]')

    def get_current_page_wrap(self):
        return self.wait_UI(self.__page_wrap_loc)

    # page tiltle locator
    page_header_loc = (By.CSS_SELECTOR, 'div[data-hj-test-id="hj-active-thread-title"]')
    # Return the page title
    def get_header(self):
        return self.find_element(*self.page_header_loc).text

    #title locator
    page_title_loc = (By.CSS_SELECTOR, 'span[data-hj-test-id="hj-active-page-title"]')

    def action_get_page_title(self):
        '''
        Return the page title by title_locator
        :return: The text of the page title
        '''
        title = self.wait_UI(self.page_title_loc)
        return self.find_element(*self.page_title_loc).text

    __footertext_loc = (By.CSS_SELECTOR, 'span.footer-text')

    def wait_page(self, page_title):
        '''
        Wait the specific page loaded.
        :param page_type: The type of page you want to wait
        :return: None
        '''

        counter = 0
        for i in range(self.timeout):
            if counter > i:
                raise TimeoutException('The page is not found')
            else:
                title = self.action_get_page_title()
                if page_title == title:
                    return True
                else:
                    time.sleep(1)
                    counter=+1

    # button locators
    __query_loc = (By.CSS_SELECTOR, 'li[data-hj-test-id="query-button"]>a')
    __reset_loc = (By.CSS_SELECTOR, 'li[data-hj-test-id="reset-button"]>a')
    __refresh_loc = (By.CSS_SELECTOR, 'li[data-hj-test-id="refresh-page-button"]>a')
    __update_loc = (By.CSS_SELECTOR, 'li[data-hj-test-id="update-button"]>a')
    __delete_loc = (By.CSS_SELECTOR, 'li[data-hj-test-id="delete-button"]>a')
    __cancel_loc = (By.CSS_SELECTOR, 'li[data-hj-test-id="cancel-button"]>a')

    def action_click_button(self, button):
        '''
        The action to click the specific button
        :param button: The button name
        :return: None
        '''
        button.lower()
        if button == 'query':
            button_loc = self.__query_loc
        elif button == 'reset':
            button_loc = self.__reset_loc
        elif button == 'refresh':
            button_loc = self.__refresh_loc
        elif button == 'update':
            button_loc = self.__update_loc
        elif button == 'delete':
            button_loc = self.__delete_loc
        elif button == 'cancel':
            button_loc = self.__cancel_loc
        else:
            raise NoSuchElementException('The button name does not exist')
        button = self.wait_UI(button_loc)
        button.click()


