# _*_ coding: utf-8 _*_
#!c:/Python36
#Filename: loginPage.py

from test_case.page_obj.base import Base
from selenium import webdriver
from selenium.webdriver.common.by import By

class loginPage(Base):
    url = ''

    #username locator
    username_loc = (By.CSS_SELECTOR, 'hj-textbox[data-hj-test-id="username"]')

    #Function to input username
    def action_input_username(self, username='Administrator'):
        element = self.find_element(*self.username_loc)
        element.send_keys(username)

    #password_locator
    password_loc = (By.CSS_SELECTOR, 'hj-password-textbox[data-hj-test-id="password"]>input')

    #Function to input password
    def action_input_password(self, password='HJSPASS'):
        self.find_element(*self.password_loc).send_keys(password)

    #tenant_locator
    tenant_loc = (By.CSS_SELECTOR,'hj-textbox[data-hj-test-id="tenant"]>input' )

    #Function to input tenant
    def acton_input_tenant(self, tenant ='Tenant'):
        self.find_element(*self.tenant_loc).send_keys(tenant)

    #language locator
    language_dropdown_loc = (By.CSS_SELECTOR,'hj-dropdownlist[data-hj-test-id="language"]>span')
    language_input_loc = (By.CSS_SELECTOR, 'hj-dropdownlist[data-hj-test-id="language"]>span>span>span[class="k-input"]')

    #Function to select language
    def action_select_language(self, language):
        language_dropdown = self.find_element(*self.language_dropdown_loc)
        language_input = self.find_element(*self.language_input_loc)
        language_dropdown.click()
        language_input.send_keys(language)
        language_dropdown.click()

    #Login button locator
    login_button_loc = (By.CSS_SELECTOR, 'hj-button[data-hj-test-id="actionButton"]')

    #Function to click Login button
    def action_click_login(self):
        self.find_element(*self.login_button_loc).click()

    # login in HJ1
    def login(self):
        self.open()
        self.wait_UI(self.username_loc)
        self.action_input_username()
        self.action_input_password()
        self.action_click_login()


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    login_page = loginPage(driver)
    login_page.open()
    login_page.wait_UI(login_page.username_loc)
    login_page.action_input_username()
    login_page.action_input_password()
    login_page.action_click_login()

