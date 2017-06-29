# _*_ coding: utf-8 _*_
#!c:/Python36
#Filename: SearchPage.py

from test_case.page_obj.header import Header
from test_case.page_obj.loginPage import loginPage
from test_case.page_obj.MenuBar import MenuBar
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchAttributeException, NoSuchElementException
from selenium.webdriver.support import select
from selenium.webdriver.common import action_chains
import time


class SearchPage(Header):
    url = ''

    '''
    The following section is to find the specific  hj-field-group-row. hj-field-group-row contains 
    label and the UI.hj-field-group-row is used as parent element to help locate the deeper UI controls
    '''
    # The locator of the all field groups
    field_groups_loc = (By.CSS_SELECTOR, 'div[data-hj-test-id="field-table"]>hj-field-table-row')

    def get_field_group_rows_path(self, groupIndex):
        '''
        Return field group locator according to the group index input.
        :param groupIndex: The field group user want
        :return: the css selector of all field group rows
        '''
        field_groups_list_length = len(self.find_elements(*self.field_groups_loc))
        if not isinstance(groupIndex, int):
            raise ValueError ('groupIndex must be int')
        elif groupIndex>field_groups_list_length:
            print(field_groups_list_length)
            raise IndexError ('The groupIndex is out of the number of groups')
        field_group_rows_path = 'div[data-hj-test-id="field-table"]>hj-field-table-row:nth-of-type(' + str(groupIndex) \
                                + ')>div[data-hj-test-id="field-table-row"]>hj-field-group>div[data-hj-test-id="field-group"]>div[data-hj-test-id="field-group-content"]>hj-field-group-row'
        return field_group_rows_path

    # The  CSS locator of the hj-field-label related to hj-field-group-row element
    field_label_path = 'hj-field-label[data-hj-test-id="field-label"]'
    # The CSS locator of the hj-field-control name related to hj-field-group-row element
    field_control_path = 'hj-field-control[data-hj-test-id="field-control"]'

    def get_field_control(self, name, groupIndex):
        '''
        Return the row number in hj-field-group-row by control's label name
        :param groupIndex: The field group the control located in
        :param name: The control's label name
        :return: Return the hj-field-control web element
        '''
        field_gorup_rows_path = self.get_field_group_rows_path(groupIndex)
        field_gorup_rows = self.find_elements(By.CSS_SELECTOR,
                                              field_gorup_rows_path) #Get all hj-field-group-row elements
        counter = 1
        if field_gorup_rows: # Go throuth each row, return hj-field-control if the text matches name input
            for row in field_gorup_rows:
                text = row.find_element_by_css_selector(self.field_label_path).text
                if text == name:
                    field_control = row.find_element_by_css_selector(self.field_control_path)
                    return field_control
                else:
                    counter+=1

    '''
    The following section is for the dropdown list operations. The functions are independent, not based
     on any other UI controls. 
    '''
    # The locator of all div<k-list-container>. k-list-container is the container of the dropdown list in the page
    list_container_loc = (By.CLASS_NAME, 'k-list-container')
    # The locator of the dropdown list items. It is related to the div<k-list-container> element.
    list_container_items_loc = (By.TAG_NAME, 'li')

    def get_list_container(self):
        '''
        Find all div<k-list-container>, but only return the one is displayed.
        :return: div<k-list-container>
        '''
        list_containers= self.find_elements(*self.list_container_loc)
        for list_container in list_containers:
            if list_container.is_displayed():
                return list_container

    def get_list_container_items(self):
        '''
        Get all options/items under dropdown list (div<k-list-container>). Before use the function, have to expand
        dropdown list first
        :return: the items list
        '''
        list_container = self.get_list_container()
        dropdown_list_items = list_container.find_elements_by_tag_name('li')
        items_text_list=[]
        for dropdown_list_item in dropdown_list_items:
            items_text_list.append(dropdown_list_item.text)
        return items_text_list

    def action_select_from_dropdown(self, text):
        '''
        Select specific text in dropdown list which provied by user
        :param text: The item in dropdown list want to be selected
        :return: None
        '''
        list_container = self.get_list_container()
        dropdown_list_items = list_container.find_elements_by_tag_name('li')
        for dropdown_list_item in dropdown_list_items:
            if dropdown_list_item.text == text:
                dropdown_list_item.click()
                return
        raise NoSuchElementException('The item in dropdown list is not located')

    def get_all_label_name(self, groups_number=1):
        '''
        Return all label names on the page
        :param groups_number: The number of field groups, default value is 1
        :return: a list contains all label names in the page
        '''
        if not isinstance(groups_number, int):
            raise ValueError('groups_numbers must be int')
        name_list = []
        for i in range(groups_number+1):
            field_gorup_rows_path = self.get_field_group_rows_path(i)
            field_gorup_rows = self.find_elements(By.CSS_SELECTOR,
                                                  field_gorup_rows_path)  # Get all hj-field-group-row elements
            if field_gorup_rows:  # Go throuth each row, return hj-field-control if the text matches name input
                for row in field_gorup_rows:
                    text = row.find_element_by_css_selector(self.field_label_path).text
                    name_list.append(text)
        return name_list

    # button locators
    query_loc = (By.CSS_SELECTOR, 'li[data-hj-test-id="query-button"]>a')
    reset_loc = (By.CSS_SELECTOR, 'li[data-hj-test-id="reset-button"]>a')
    refresh_loc = (By.CSS_SELECTOR, 'li[data-hj-test-id="refresh-page-button"]>a')

    def action_click_button(self, button_loc):
        '''
        The action to click the specific button
        :param button_loc: The locator of the button
        :return: None
        '''
        button = self.wait_UI(button_loc)
        button.click()

    #title locator
    title_locator = (By.CSS_SELECTOR,'span[data-hj-test-id="hj-active-page-title"]')

    def get_title(self):
        '''
        Return the page title by title_locator
        :return: The text of the page title
        '''
        title = self.wait_UI(self.title_locator)
        return self.find_element(*self.title_locator).text


    # The CSS locator of the hj-checkbox related to hj-field-control element
    checkbox_path = 'hj-checkbox>div>input.k-checkbox'

    def get_checkbox_element(self,name, groupIndex):
        '''
        Return the hj-checkbox web element
        :param groupIndex: The field group the control located in
        :param name: The control's label name
        :return: hj-checkbox element
        '''
        field_control = self.get_field_control(name, groupIndex)
        checkbox_element = field_control.find_element_by_css_selector(self.checkbox_path)
        if checkbox_element.get_attribute("type") == "checkbox":
            return checkbox_element
        else:
            raise NoSuchAttributeException('It is not a checkbox')

    def action_checkbox_select(self,name, groupIndex=1):
        '''
        Select/deselect the checkbox
        :param groupIndex: The field group the control located in, default is 1
        :param name: The control's label name
        :return: None
        '''
        checkbox_element = self.get_checkbox_element(groupIndex, name)
        checkbox_element.click()

    # The CSS locator of the hj-textbox and hj-password-text related to hj-field-control element
    edit_path = 'input.k-textbox'

    def get_edit_element(self,name, groupIndex):
        '''
        Return the hj-textbox and hj-password-textbox web element
        :param groupIndex: The field group the control located in
        :param name: The control's label name
        :return: hj-textbox or hj-passowrd-textbox element
        '''
        field_control = self.get_field_control(name, groupIndex)
        edit_element = field_control.find_element_by_css_selector(self.edit_path)
        return edit_element

    def action_edit_input(self,name, value, groupIndex=1):
        '''
        Input values to edit and masked edit control
        :param groupIndex: The field group the control located in, default is 1
        :param name: The control's label name
        :param value: The value input
        :return: None
        '''
        edit_element = self.get_edit_element(name, groupIndex)
        edit_element.send_keys(value)

    # The CSS locator of the hj-multiline-textbox related to hj-field-control element
    multiedit_path = 'hj-multiline-textbox>textarea.k-textbox'

    def get_multiedit_element(self,name, groupIndex):
        '''
        Return the hj-multieline-textbox web element
        :param groupIndex: The field group the control located in
        :param name: The control's label name
        :return: hj-multieline-textbox element
        '''
        field_control = self.get_field_control(name, groupIndex)
        multiedit_element = field_control.find_element_by_css_selector(self.multiedit_path)
        return multiedit_element

    def action_multiedit_input(self,name, value,groupIndex=1 ):
        '''
        Input values to multiedit control
        :param groupIndex: The field group the control located in, default is 1
        :param name: The control's label name
        :param value: The value input
        :return: None
        '''
        multiedit_element = self.get_multiedit_element(groupIndex, name)
        multiedit_element.send_keys(value)

    # The CSS locator of the searchlike control related to hj-field-control element
    #searchlike_dropdownlist_path = 'div.searchLike-control-dropdownlist-container>hj-dropdownlist>span>span>span.k-input'
    searchlike_textbox_path = 'div.searchLike-control-textbox-container>hj-textbox>input'
    searchlike_button_path = 'div.searchLike-control-dropdownlist-container>hj-dropdownlist>span>span>span.k-select'
    searchlike_path = [searchlike_button_path, searchlike_textbox_path]

    def get_searchlike_element(self, name, groupIndex):
        '''
        Get the searchlike components. The return is a list. list[0] is the dropdown list. list[1] is the button of the
        drop down list. list[2] is the textbox for search text input.
        :param groupIndex: The field group the control located in
        :param name: The control's label name
        :return: The searchlike control components list
        '''
        searchlike_elements=[]
        for path in self.searchlike_path:
            field_control = self.get_field_control(name, groupIndex)
            searchlike_element = field_control.find_element_by_css_selector(path)
            searchlike_elements.append(searchlike_element)
        return searchlike_elements

    def action_searchlike_select(self, name, value, groupIndex=1, search_type="Like"):
        '''
        Select the search type and then input the search value.
        :param name: The control's label name
        :param value: The search value
        :param groupIndex: The field group the control located in, default is 1
        :param search_type: The search type in the dropdown list, default is like. The acceptable value, is Like, Exactly
        :return: None
        '''
        searchlike_elements = self.get_searchlike_element(name, groupIndex)
        searchlike_elements[0].click()
        time.sleep(1)
        self.action_select_from_dropdown(search_type)
        searchlike_elements[1].send_keys(value)

    # The CSS locator of the dropdown input control related to hj-field-control element
    dropdown_input_path='hj-dropdownlist>span>span>span.k-input'
    # The CSS locator of the options in the dropdown list related to hj-field-control element
    dropdown_options_path = 'hj-dropdownlist>span>select'
    dropdown_button_path = 'hj-dropdownlist>span>span>span.k-select'

    def get_dropdown_options_text(self,name, groupIndex=1):
        field_control = self.get_field_control(name, groupIndex)
        dropdown_control= field_control.find_element_by_css_selector(self.dropdown_options_path)
        options_list = select.Select(dropdown_control).options
        print (options_list)

    def get_dropdown_input_element(self, name, groupIndex):
        field_control = self.get_field_control(name, groupIndex)
        dropdown_input_control = field_control.find_element_by_css_selector(self.dropdown_input_path)
        return dropdown_input_control

    def action_select_dropdown(self, name, value, groupIndex=1):
        dropdown_input_control = self.get_dropdown_input_element(name, groupIndex)
        action_chains.ActionChains(self.driver).click(dropdown_input_control)
        dropdown_input_control.send_keys(value)




if __name__ == '__main__':
    webdriver = webdriver.Firefox()
    webdriver.maximize_window()
    webdriver.implicitly_wait(10)
    login_page = loginPage(webdriver)
    login_page.login()
    menu_bar = MenuBar(webdriver)
    menu_bar.wait_UI(menu_bar.menu_button_loc)
    menu_bar.action_toggle_menu()
    time.sleep(1)
    menu_bar.action_expand_app_group('Supply Chain Advantage')
    menu_bar.action_expand_menu('Advantage Dashboard')
    menu_bar.action_expand_menu('searchTest', False)
    searchPage = SearchPage(webdriver)
    print(searchPage.get_title())
    time.sleep(1)
    searchPage.action_searchlike_select('searchLike', 'abc', 2)


