from selenium import webdriver 
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup 
import requests
import time 
import csv 
import os
from selenium.webdriver.common.by import By
from lxml import etree
from selenium.webdriver.firefox.options import Options


options = Options()

options.set_preference("media.navigator.permission.disabled", True )

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install() , options=options)

driver.get('https://webex-eelu.webex.com')
time.sleep(5)
driver.find_element(By.ID, 'guest_signin_split_button-action').click()
time.sleep(5)

driver.find_element(By.ID, "IDToken1").send_keys("yousef21-01715@student.eelu.edu.eg")
driver.find_element(By.ID, 'IDButton2').click()

time.sleep(5)
driver.find_element(By.ID ,"IDToken2").send_keys("Agamista135#")
driver.find_element(By.ID , "Button1").click()

time.sleep(5)

html=driver.page_source 
soup = BeautifulSoup(html, 'html.parser') 

timeZone = soup.findAll("li" , attrs={"class" : "m_list_item"})

with open('meetting-time.csv' ,'w' ,newline='') as file :
   writer = csv.writer(file)
   writer.writerow([ "start time " , "day" ]) 
   for t in timeZone :
      listTime = t.find("div" ,{"class" :"list_t"}).text
      # listT =re.sub(r"^\s+|\s+$", "", listT)
      listDay = t.find("div" ,{"class" :"list_st"}).text 
      listTime = listTime[:listTime.find('-')]
      writer.writerow([listTime , listDay])