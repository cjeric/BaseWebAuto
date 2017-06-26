# _*_ coding: utf-8 _*_
#!c:/Python36
#Filename: searchPage.py

from test_case.page_obj.header import Header
from test_case.page_obj.loginPage import loginPage
from test_case.page_obj.menuBar import menuBar
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class searchPage(Header):
    # button locators
    query_loc = (By.CSS_SELECTOR, 'li[data-hj-test-id="query-button"]>a')
    reset_loc = (By.CSS_SELECTOR, 'li[data-hj-test-id="reset-button"]>a')
    refresh_loc = (By.CSS_SELECTOR, 'li[data-hj-test-id="refresh-page-button"]>a')
    #Click button on action bar
    def click_button(self,button_loc):
        button = self.wait_UI(button_loc)
        button.click()

    #title locator
    title_locator = (By.CSS_SELECTOR,'span[data-hj-test-id="hj-active-page-title"]')
    def get_title(self):
        title = self.wait_UI(*self.title_locator)
        return self.find_element(*self.title_locator).text

    field_groups_loc = (By.CSS_SELECTOR, 'div#"field-table">hj-field-table-row')
    #Get field group locator
    def get_field_group_loc(self, groupIndex):
        field_groups_list_length = len(self.find_elements(*self.field_groups_loc))
        if not isinstance(groupIndex, int):
            raise ValueError
        elif groupIndex>field_groups_list_length:
            raise IndexError
        field_group_path = 'div#"field-table">hj-field-table-row['+ str(groupIndex)+']'
        return field_group_path

    def get_field_group_name(self, groupIndex):
        pass



if __name__ == '__main__':
    webdriver = webdriver.Firefox()
    login_page = loginPage(webdriver)
    login_page.login()
    menu_bar = menuBar(webdriver)
    menu_bar.wait_UI(menu_bar.menu_button_loc)
    menu_bar.menu_toggle()
    time.sleep(1)
    menu_bar.extend_app_group('Supply Chain Advantage')
    menu_bar.extend_menu('Advantage Dashboard')
    menu_bar.extend_menu('Receiving')
    menu_bar.extend_menu('ASNs', False)
    searchPage = searchPage(webdriver)
    print(searchPage.get_title())
    #searchPage.click_button(searchPage.query_loc)


