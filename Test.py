#_*_coding:utf-8_*_
#!C:\Python27
#Filename: test.py

from selenium import webdriver
import time
from selenium.webdriver.common import action_chains
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("http://sca12r2ss12c:30000/core/Default.html")
time.sleep(5)
username = driver.find_element_by_css_selector('hj-textbox[data-hj-test-id="username"]')
username.send_keys("Administrator")
password = driver.find_element_by_css_selector('hj-password-textbox[data-hj-test-id="password"]>input')
password.send_keys("HJSPASS")
# element2 = driver.find_element_by_css_selector('hj-dropdownlist[data-hj-test-id="language"]>span>span>span[class="k-input"]')
# element1 = driver.find_element_by_css_selector('hj-dropdownlist[data-hj-test-id="language"]>span')
# element1.click()
# element2.send_keys("Default")
# element1.click()
login = driver.find_element_by_css_selector('hj-button[data-hj-test-id="actionButton"]')
login.click()
time.sleep(15)
menu = driver.find_element_by_id('menuButtonToggle')
menu.click()
time.sleep(1)
scamenu = driver.find_element_by_xpath('//nav[@id="menu"]/ul/li[@class="with-children closed"][2]/a')
scamenu.click()
# time.sleep(2)
# wamenu = driver.find_element_by_xpath('//nav[@id="menu"]/ul/li[3]')
# print (wamenu.get_attribute('class'))
# wamenu.click()
# time.sleep(1)
# clients = driver.find_element_by_xpath('//nav[@id="menu"]/ul/li[@class="with-children open ancestor"]/ul/li[@class="with-children open current"]/ul/li/a')
# clients.click()


#driver.close()

