# _*_ coding: utf-8 _*_
#!c:/Python36
#Filename: ReportPage.py

from test_case.page_obj.basepage import BasePage
from test_case.page_obj.LoginPage import LoginPage
from test_case.page_obj.SearchPage import SearchPage
from test_case.page_obj.MenuBar import MenuBar
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchAttributeException, NoSuchElementException
from selenium.webdriver.support import select
import time

class ReportPage(BasePage):
    url = ''

    __page_action_buttons_loc = (By.XPATH, '//div[@data-hj-test-id="page-actions"]/ul/li')

    def action_click_page_action_button(self, button):
        pass



    #The container of header locator
    __table_header_container_loc = (By.CSS_SELECTOR, 'div.k-grid-header')
    #The header locator
    __table_headers_loc = (By.CSS_SELECTOR, 'th[class="k-header k-with-icon"]')

    def __get_header_elements(self):
        '''
        Return a list of header elements
        :return: a list of header elements
        '''
        headers_container = self.find_element(*self.__table_header_container_loc)
        headers = self.find_child_elements(headers_container, *self.__table_headers_loc)
        return headers

    def action_get_header_values(self):
        '''
        Return a list of all displayed headers' name, not inculde row number
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

    # The xpath locator of table rows
    __table_row_loc = (By.XPATH, '//table/tbody/tr[@class="k-master-row " or @class="k-alt k-master-row " or @class="k-master-row" or @class="k-alt k-master-row"]')

    def __get_table_row_elements(self):
        '''
        Return the list of table rows
        :return: a list of table rows
        '''
        table_rows = self.find_elements(*self.__table_row_loc)
        if len(table_rows):
            #print (len(table_rows))
            return table_rows
        raise NoSuchElementException('<tr> rows in table are not located')

    # The xpath locator of table cells related to table row element
    __table_cell_loc = (By.XPATH,'./td[not(@style) and @class!="row-indicator-cell "]')

    def __get_table_cell_elements(self):
        '''
        Return a list of table cells. The list is composed of Table[Row][column]. For Example, get 2nd cell in 1st row, then
        it should table[0][1]
        :return: a list of tabel cells, include + cell
        '''
        tabel_rows = self.__get_table_row_elements()
        table = []
        for row in tabel_rows:
            cells = self.find_child_elements(row, *self.__table_cell_loc) #get cell elements of each row
            if len(cells):
                cells.pop() #Drop the last cell element in the list, as the last cell is an empty cell without value.
                #print (len(cells))
                table.append(cells) # Add a list of cell elements in one row to the table list.
            else:
                raise NoSuchElementException('<td> cells in table not located')
        return table

    def action_get_values_by_row(self, row):
        '''
        Get all cell values of one row in the table. The row_number starts with 1. It is actual number in the table,
        :param row: The number of row in the table
        :return: a list of values in a specific row, include row number cell
        '''
        table = self.__get_table_cell_elements()
        if not isinstance(row, int):
            raise ValueError ('row must be int')
        elif row>len(table):
            raise IndexError ('The row is out of the number of rows')
        cell_values = []
        for cell in table[row-1]:
            if cell.get_attribute('class') == "": # Getting rid of + cell, only add the business values to the list
                cell_values.append(cell.text)
        return cell_values

    # The xpath locator of link in table related to a cell element
    __fieldlink_loc = (By.XPATH, './/span | .//a')

    def action_click_cell(self, row, column):
        '''
        Click the cell in the table. The row and column is the actual row number and column number in the table. This
        function can be used to click field link, row number, extend row details and click a label cell to highlight a
        row
        :param row: The row number of the link
        :param column: The column number of the link
        :return: None.
        '''
        table = self.__get_table_cell_elements()
        if not (isinstance(row,int) and isinstance(column,int)):
            raise ValueError('row or column must be int')
        elif row>len(table):
            raise IndexError('The row is out of the number of rows')
        elif column > len(table[row]):
            raise IndexError('The column is out of the number of columns')
        self.find_child_element(table[row-1][column-1], *self.__fieldlink_loc).click()



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
    list = reportPage.action_get_values_by_row(1)
    print (list)
    reportPage.action_click_cell(1, 1)

