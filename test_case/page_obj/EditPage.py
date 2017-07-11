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
    menu_bar.action_expand_menu('Unknown Receipts')
    menu_bar.action_expand_menu('Resolve Unknown Receipts', False)
    reportPage = ReportPage(webdriver)
    reportPage.wait_page('Resolve Unknown Receipts')
    time.sleep(3)
    reportPage.action_click_cell(1,1)
    editPage = EditPage(webdriver)
    editPage.wait_page('Edit Resovle Unknown Receipt')
    print(editPage.action_get_all_labels_name(2))
    editPage.action_dropdown_select('Carrier Name','DHL', 1)
    editPage.action_dropdown_select('Status','Resolved',2)
    editPage.action_multiedit_input('Resolution Comments', 'comment',2)
    editPage.action_click_button('delete')

