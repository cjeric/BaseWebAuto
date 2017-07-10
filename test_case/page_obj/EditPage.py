# _*_ coding: utf-8 _*_
#!c:/Python36
#Filename: ReportPage.py

from test_case.page_obj.LoginPage import LoginPage
from test_case.page_obj.SearchPage import SearchPage
from test_case.page_obj.ReportPage import ReportPage
from test_case.page_obj.MenuBar import MenuBar
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchAttributeException, NoSuchElementException
from selenium.webdriver.support import select
import time

class EditPage(SearchPage):
    url=''


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
    menu_bar.action_expand_menu('Inbound Orders', False)
    searchPage = SearchPage(webdriver)
    searchPage.wait_page('Search Inbound Orders')
    time.sleep(1)
    print(searchPage.action_get_all_labels_name())
    searchPage.action_dropdown_select('Warehouse ID', 'Warehouse2 - Warehouse 02')
    searchPage.action_searchlike_input('PO Number', 'PO1')
    searchPage.action_click_button('query')
    reportPage = ReportPage(webdriver)
    reportPage.wait_page('Inbound Orders')
    reportPage.action_click_cell(1,2)
    editPage = EditPage(webdriver)
    editPage.wait_page('Edit Inbound Order')
    print(editPage.action_get_all_labels_name(2))
    editPage.action_dropdown_select('Type','Transfer Orders', 1)
    editPage.action_edit_input('Name' 'Jack',2)
    editPage.action_edit_input('Postal Code', '200333',2)

