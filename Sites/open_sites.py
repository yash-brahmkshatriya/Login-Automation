from selenium import webdriver as wbd
from selenium.webdriver.common.keys import Keys
import time

def openCF(details):
    details=details.split(' ')
    id_=details[0]
    pwd_=details[1]
    driver=wbd.Chrome("chromedriver.exe")
    driver.get('https://codeforces.com')
    time.sleep(2)
    elem=driver.find_element_by_xpath('//*[@id="header"]/div[2]/div[2]/a[1]')
    elem.click()
    time.sleep(2)
    elem=driver.find_element_by_xpath('//*[@id="handleOrEmail"]')             
    elem.click()
    elem.send_keys(id_)
    elem=driver.find_element_by_xpath('//*[@id="password"]')
    elem.click()
    elem.send_keys(pwd_)
    elem.send_keys(Keys.ENTER)
    time.sleep(10)
def openCC(details):
    details=details.split(' ')
    id_=details[0]
    pwd_=details[1]
    driver=wbd.Chrome("chromedriver.exe")
    driver.get('https://codechef.com')
    time.sleep(2)
    elem=driver.find_element_by_xpath('//*[@id="edit-name"]')
    elem.click()
    elem.send_keys(id_)
    elem=driver.find_element_by_xpath('//*[@id="edit-pass"]')
    elem.click()
    elem.send_keys(pwd_)
    elem.send_keys(Keys.ENTER)
    try:
        time.sleep(2)
        elem=driver.find_element_by_xpath('/html/body/section/div/div/ul/a')
        print('Login Successfull')
    except:
        print('Login Unsuccessfull')
    time.sleep(10)
def openSPOJ(details):
    details=details.split(' ')
    id_=details[0]
    pwd_=details[1]
    driver=wbd.Chrome("chromedriver.exe")
    driver.get('https://spoj.com')
    time.sleep(2)
    elem=driver.find_element_by_xpath('//*[@id="menu"]/div/nav/ul/li[6]/a')
    elem.click()
    elem=driver.find_element_by_xpath('//*[@id="login-form"]/div/div/input[3]')
    elem.click()
    elem.send_keys(id_)
    elem=driver.find_element_by_xpath('//*[@id="login-form"]/div/div/input[4]')
    elem.click()
    elem.send_keys(pwd_)
    elem.send_keys(Keys.ENTER)
    time.sleep(10)
    