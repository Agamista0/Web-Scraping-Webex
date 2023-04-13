from selenium import webdriver 
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup 
import requests
import time 
from selenium.webdriver.common.by import By
from lxml import etree
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 

options = Options()

options.set_preference("media.navigator.permission.disabled", True )

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install() , options=options)

driver.get('https://web.webex.com/sign-in/enter-email')
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys("yousefmyiu@gmail.com")
driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div[2]/div/div[4]/form/div[2]/button').click()

time.sleep(5)
driver.find_element(By.XPATH ,"/html/body/main/div/div[2]/div[2]/div/button" ).click()

time.sleep(5)
driver.find_element(By.ID ,"IDToken2").send_keys("###########")
driver.find_element(By.ID , "Button1").click()

time.sleep(5)
driver.get("https://web.webex.com/meetings")
time.sleep(5)

html=driver.page_source 
soup = BeautifulSoup(html, 'html.parser') 
time.sleep(5)

is_ok = "5:35 AM "

prodects = soup.find_all('li' ,attrs={"class" : "md-meeting-list-item-wrapper"})
for prodect in prodects :
    data = prodect.find("small" , {"class" : "md-text-wrapper"}).text
    handel_data=data[:data.index("-")]
    if(is_ok == handel_data ):
        driver.find_element(By.CSS_SELECTOR, "button[data-color = 'join']").click()
        time.sleep(5)
        
        p = driver.current_window_handle
        chwd = driver.window_handles
        for w in chwd:
            driver.switch_to.window(w)
            if driver.title == "Webex" :
                driver.close() 
            
        link_ = driver.current_url 
        driver.switch_to.new_window("window")
        driver.get(link_)
        time.sleep(3)

        html=driver.page_source 
        print(html)
        
        driver.find_element(By.ID , "push_download_join_by_browser").click()
       
        time.sleep(5)
        
       
        driver.find_element(By.CSS_SELECTOR , "button#interstitial_start_btn").click()
        
