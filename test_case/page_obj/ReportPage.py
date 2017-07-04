# _*_ coding: utf-8 _*_
#!c:/Python36
#Filename: ReportPage.py

from test_case.page_obj.header import Header
from test_case.page_obj.LoginPage import LoginPage
from test_case.page_obj.SearchPage import SearchPage
from test_case.page_obj.MenuBar import MenuBar
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchAttributeException, NoSuchElementException
from selenium.webdriver.support import select
import time

class ReportPage(Header):
    url = ''

    #The container of header locator
    table_header_container_loc = (By.CSS_SELECTOR, 'div.k-grid-header')
    #The header locator
    table_headers_loc = (By.CSS_SELECTOR, 'th[class="k-header k-with-icon"]')

    def __get_header_elements(self):
        '''
        Return a list of header elements
        :return: a list of header elements
        '''
        headers_container = self.find_element(*self.table_header_container_loc)
        headers = self.find_child_elements(headers_container, *self.table_headers_loc)
        return headers

    def action_get_header_values(self):
        '''
        Return a list of all displayed headers' name
        :return: a list of headers' name
        '''
        headers = self.__get_header_elements()
        if len(headers):
            header_values=[]
            for header in headers:
                if header.get_attribute("style") == "display: none;":
                    continue
                header_values.append(header.get_attribute('data-title'))
            return header_values
        raise NoSuchElementException('<th> headers are not located')



if __name__ == '__main__':
    webdriver = webdriver.Firefox()
    webdriver.maximize_window()
    webdriver.implicitly_wait(10)
    login_page = LoginPage(webdriver)
    login_page.login()
    menu_bar = MenuBar(webdriver)
    menu_bar.wait_UI(menu_bar.menu_button_loc)
    menu_bar.action_toggle_menu()
    time.sleep(1)
    menu_bar.action_expand_app_group('Supply Chain Advantage')
    menu_bar.action_expand_menu('Advantage Dashboard')
    menu_bar.action_expand_menu('Receiving')
    menu_bar.action_expand_menu('ASNs', False)
    searchPage = SearchPage(webdriver)
    searchPage.wait_page('search page')
    print(searchPage.action_get_title())
    time.sleep(1)
    print(searchPage.action_get_all_labels_name(1))
    searchPage.action_dropdown_select('Warehouse ID', 'Warehouse2 - Warehouse 02')
    #searchPage.action_checkbox_check('Search by Date')
    searchPage.action_searchlike_input('ASN Number', 'ASN2')
    searchPage.action_click_button(searchPage.query_loc)
    reportPage = ReportPage(webdriver)
    reportPage.wait_page('report page')
    print(reportPage.action_get_title())
    print (reportPage.action_get_header_values())
