# _*_ coding: utf-8 _*_
# !c:/Python36
# Filename: basepage.py

from test_case.page_obj.base import Base
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class BasePage(Base):
    url = ''

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

    # The CSS selector locator of three types of page
    __search_page_loc = (By.CSS_SELECTOR, '[data-hj-test-id="search-page"]')
    __edit_page_loc = (By.CSS_SELECTOR, '[data-hj-test-id="edit-page"]')
    __report_page_loc = (By.CSS_SELECTOR, '[data-hj-test-id="report-page"]')

    def wait_page(self, page_type):
        '''
        Wait the specific page loaded.
        :param page_type: The type of page you want to wait
        :return: None
        '''
        if page_type == 'search page':
            self.wait_UI(self.__search_page_loc)
            return
        if page_type == 'edit page':
            self.wait_UI(self.__edit_page_loc)
            return
        if page_type == 'report page':
            self.wait_UI(self.__report_page_loc)
            return
        else:
            raise Exception('The page_type must be search page, edit page or report page')

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


