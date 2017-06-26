# _*_ coding: utf-8 _*_
#!c:/Python36
#Filename: menuBar.py

from test_case.page_obj.base import Base
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class menuBar(Base):
    url = ''

    #Menu button locator
    menu_button_loc = (By.ID,'menuButtonToggle')
    #Function to click menu button
    def menu_toggle(self):
        self.find_element(*self.menu_button_loc).click()

    #Menu locators for different status
    menu_current_loc = (By.XPATH, '//nav[@id="menu"]/ul/li[@class="home current"]/a')
    menu_ancestor_loc = (By.XPATH, '//nav[@id="menu"]/ul/li[@class="home ancestor"]/a')

    def backto_menu(self):
        self.find_element(*self.menu_ancestor_loc).click()

    #Entry menu locator
    app_group_loc = (By.XPATH,'//nav[@id="menu"]/ul/li[@class="with-children closed"]/a')
    #Extend app group
    def extend_app_group(self,groupName):
        group_list = self.find_elements(*self.app_group_loc)
        for group in group_list:
            if group.text == groupName:
                group.click()
                break
    # The locator of the opened menu
    current_open_menu_loc = (By.XPATH,'//li[@class="with-children current open"]')
    # The locator of the sub menu
    menu_extend_loc = (By.XPATH, './/li[@class="with-children closed"]/a')
    # The locator of the page
    menu_open_loc = (By.XPATH, './/li[@class="without-children closed"]/a')

    # Click the submenu or page under the current opened menu
    def extend_menu(self, menuName, whetherMenu = True):
        '''

        :param menuName:
        :param whetherMenu: whether the link is a submenu
        :return:
        '''
        open_menu = self.wait_UI(self.current_open_menu_loc)
        if whetherMenu:
            menu_items_loc = self.menu_extend_loc
        else:
            menu_items_loc = self.menu_open_loc
        menu_items = open_menu.find_elements(*menu_items_loc)
        for menu_item in menu_items:
            if menu_item.text == menuName:
                menu_item.click()
                break

    #The locator of the current opened menu's parent menus
    ancestor_menu_loctor = (By.XPATH,'//li[@class="with-children open ancestor"]/a')
    #Click the parent menu of the current opened one
    def collapse_menu(self,menuName):
        menu_items = self.find_elements(*self.ancestor_menu_loctor)
        for menu_item in menu_items:
            if menu_item.text == menuName:
                menu_item.click()
                break



if __name__ == '__main__':
    pass
    # webdriver = webdriver.Firefox()
    # login_page = loginPage(webdriver)
    # login_page.login()
    # menu_bar = menuBar(webdriver)
    # menu_bar.wait_UI(menu_bar.menu_button_loc)
    # menu_bar.menu_toggle()
    # time.sleep(1)
    # menu_bar.extend_app_group('Supply Chain Advantage')
    # menu_bar.extend_menu('Advantage Dashboard')
    # menu_bar.extend_menu('Receiving')
    # menu_bar.extend_menu('ASNs', False)
    # menu_bar.menu_toggle()
    # time.sleep(1)
    # menu_bar.collapse_menu('Advantage Dashboard')

