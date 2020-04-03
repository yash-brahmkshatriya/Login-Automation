from selenium import webdriver as wbd
from selenium.webdriver.common.keys import Keys
import time

def openCF(id_,pwd_):
    driver=wbd.Chrome("C:/Users/Dilip/Downloads/chromedriver.exe")
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

def openCC(id_,pwd_):
    driver=wbd.Chrome("C:/Users/Dilip/Downloads/chromedriver.exe")
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
def openSPOJ(id_,pwd_):
    driver=wbd.Chrome("C:/Users/Dilip/Downloads/chromedriver.exe")
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
        
    
# openCC('yash3110','Codechef@yash31')
# openCF('noob2831','codeforces@yahoo')
# openSPOJ('yash_31','spoj@yash31')