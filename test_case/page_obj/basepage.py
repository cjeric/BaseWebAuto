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
    #TODO functions to operate page

    #The css selector of the current displayed page wrap
    __page_wrap_loc = (
    By.CSS_SELECTOR, 'div[class="hj-spaces-page-wrap supply-chain-advantage"][style="outline: medium none;"]')

    def get_current_page_wrap(self):
        '''
        Get the current displayed page wrap element
        :return: page wrap web element
        '''
        return self.wait_UI(self.__page_wrap_loc)

    # page header locator
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

    # __footertext_loc = (By.CSS_SELECTOR, 'span.footer-text')

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

    __previous_button_loc = (By.XPATH, '//a[@data-hj-test-id="active-thread-previous-button"]')
    __next_button_loc = (By.XPATH, '//a[@data-hj-test-id="active-thread-next-button"]')

    def action_page_next(self):
        if EC.element_to_be_clickable(self.__next_button_loc):
            self.find_element(*self.__next_button_loc).click()
        else:
            raise Exception('The next button is not clickable')

    def action_page_previous(self):
        if EC.element_to_be_clickable(self.__previous_button_loc):
            self.find_element(*self.__previous_button_loc).click()
        else:
            raise Exception('The previous button is not clickable')

    # TODO functions to click buttons
    # button locators
    __query_loc = (By.CSS_SELECTOR, 'li[data-hj-test-id="query-button"]>a')
    __reset_loc = (By.CSS_SELECTOR, 'li[data-hj-test-id="reset-button"]>a')
    __refresh_loc = (By.CSS_SELECTOR, 'li[data-hj-test-id="refresh-page-button"]>a')
    __update_loc = (By.CSS_SELECTOR, 'li[data-hj-test-id="update-button"]>a')
    __delete_loc = (By.CSS_SELECTOR, 'li[data-hj-test-id="delete-button"]>a')
    __cancel_loc = (By.CSS_SELECTOR, 'li[data-hj-test-id="cancel-button"]>a')

    def action_page_click_button(self, button):
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

    # TODO functions to operate information dialog

    #The xpath locator of the information dialog
    __info_dialog_loc = (By.XPATH, '//hj-information-dialog[@data-hj-test-id="hj-workspace-page-information-dialog"]')
    #The xpath locator of the information dialog title related to information dialog element
    __info_dialog_title_loc = (By.XPATH, './/span[@data-hj-test-id="information-dialog-title"]')
    # The xpath locator of the information dialog header related to information dialog element
    __info_dialog_header_loc = (By.XPATH, './/span[@data-hj-test-id="information-dialog-header"]')
    # The xpath locator of the information dialog message related to information dialog element
    __info_dialog_message_loc = (By.XPATH, './/div[@data-hj-test-id="information-dialog-message"]')
    # The xpath locator of the all type of dialog buttons related to dialog element
    __dialog_buttons_loc = (By.XPATH, './/button[@class="k-button"]')

    def __get_information_dialog(self):
        '''
        Get information dailog element
        :return: information dialog web element
        '''
        return self.wait_UI(self.__info_dialog_loc)

    def __get_information_buttons(self):
        '''
        Get buttons of the information dialog
        :return: a list of button elements
        '''
        info_dialog = self.__get_information_dialog()
        return self.find_child_elements(info_dialog, *self.__dialog_buttons_loc)

    def action_info_dialog_get_title(self):
        '''
        Return the info dialog title text
        :return: string: the info dialog title text
        '''
        info_dialog = self.__get_information_dialog()
        return self.find_child_element(info_dialog, *self.__info_dialog_title_loc).text

    def action_info_dialog_get_header(self):
        '''
        Return the info dialog header text
        :return: string: the info dialog header text
        '''
        info_dialog = self.__get_information_dialog()
        return self.find_child_element(info_dialog, *self.__info_dialog_header_loc).text

    def action_info_dialog_get_message(self):
        '''
        Return the info dialog message text
        :return: string: the info dialog message text
        '''
        info_dialog = self.__get_information_dialog()
        return self.find_child_element(info_dialog, *self.__info_dialog_message_loc).text

    def action_info_dialog_click_button(self,button_name):
        '''
        Click the button by provided name
        :param button_name: string, the name of the button
        :return: None
        '''
        buttons = self.__get_information_buttons()
        if len(buttons):
            for button in buttons:
                if button.text == button_name:
                    button.click()
        raise NoSuchElementException('No buttons found or the button_name is not correct')

    # TODO functions to operate error dialog

    #The xpath locator of the information dialog
    __error_dialog_loc = (By.XPATH, '//hj-error-dialog[@data-hj-test-id="hj-workspace-page-error-dialog"]')
    # The xpath locator of the information dialog message related to information dialog element
    __error_dialog_message_loc = (By.XPATH, './/div[@class="hj-dlg-content"]')

    def __get_error_dialog(self):
        '''
        Get error dailog element
        :return: error dialog web element
        '''
        return self.wait_UI(self.__error_dialog_loc)

    def __get_error_buttons(self):
        '''
        Get buttons of the error dialog
        :return: a list of button elements
        '''
        info_dialog = self.__get_error_dialog()
        return self.find_child_elements(info_dialog, *self.__dialog_buttons_loc)

    def action_error_dialog_get_message(self):
        '''
        Return the error dialog message text
        :return: string: the error dialog message text
        '''
        info_dialog = self.__get_error_dialog()
        return self.find_child_element(info_dialog, *self.__error_dialog_message_loc).text

    def action_error_dialog_click_button(self,button_name):
        '''
        Click the button by provided name
        :param button_name: string, the name of the button
        :return: None
        '''
        buttons = self.__get_error_buttons()
        if len(buttons):
            for button in buttons:
                if button.text == button_name:
                    button.click()
                    return
        raise NoSuchElementException('No buttons found or the button_name is not correct')


