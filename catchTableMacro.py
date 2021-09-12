from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.common.action_chains import ActionChains

import time

webdriver_url = './chromedriver_win32/chromedriver.exe'
target_url = 'https://app.catchtable.co.kr/'

driver=webdriver.Chrome(webdriver_url)
driver.implicitly_wait(3)
driver.get(target_url)


#close popup
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/a').click()

driver.implicitly_wait(3)
driver.find_element_by_xpath('/html/body/div[4]/div[2]/footer/button').click()

driver.implicitly_wait(3)
driver.find_element_by_xpath('/html/body/div[5]/div/footer/button').click()

#on search
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="btn-icon-search"]').click()

restaurant = "문츠바베큐"
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="header"]/div/div/form/input').click()
driver.find_element_by_xpath('//*[@id="header"]/div/div/form/input').send_keys(restaurant)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="main"]/div/div/section/div/div/div[2]/div[1]/div/div[2]/h4/span/span').click()


#달력 open
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="main"]/section[3]/div/div/div[1]/a/span/span').click()

#다음 달로
driver.implicitly_wait(3)
driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div/button[3]').click()

#날짜 클릭
driver.implicitly_wait(3)
date_url = '/html/body/div[4]/div[3]/div/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[3]/div[7]/div'
date_elem = driver.find_element_by_xpath(date_url)
date_elem.click()

time.sleep(1)
#시간 클릭
time_text=("오후 12:00")
time_elem = driver.find_element_by_link_text(time_text)
time_elem.click()

#메뉴선택
driver.implicitly_wait(3)
driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/div[4]/div[2]/button[2]').click()

