import pandas as pd
import numpy as np
from sqlalchemy import create_engine

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

#Genera conexion a la base de datos
#engine = create_engine('postgresql://postgres:password@localhost:port/dbname')

# Load 390 job offers from scrapped data
#query = "select * from lds_data_dataanalyst_ch"
#datos = pd.read_sql_query(query,con=engine)
#df = pd.DataFrame(data= datos)

df=pd.read_csv('alljobs.csv')
df.columns

browser=webdriver.Chrome("chromedriver.exe")
browser.get("https://www.linkedin.com")

username=browser.find_element_by_id("session_key")
username.send_keys("email")
password=browser.find_element_by_id("session_password")
password.send_keys("password")

login_buttom=browser.find_element_by_class_name("sign-in-form__submit-button")
login_buttom.click()

list_urls=df['Link']

i=0
idjob=[]
job_title=[]
company=[]
location=[]
job_description=[]
for url in list_urls:
    i+=1
    description=[]
    t=np.random.randint(2,4)
    time.sleep(t)
    browser.get(url)
    print()
    print()
    print('------------------> url #', i,'sleep: ',t, 'seg.')
    try:
        title=browser.find_element_by_css_selector('h1.t-24.t-bold').text
        print(title)
        firma=browser.find_element_by_css_selector('a.ember-view.t-black.t-normal').text
        print(firma)
        text_html=browser.find_elements_by_css_selector('div.jobs-description__content.jobs-description-content.jobs-description__content--condensed')
        for j in text_html:
            print(j.get_attribute("innerHTML"))
            description.append(j.get_attribute("innerHTML"))
        job_description.append(description)
        job_title.append(title)
        company.append(firma)
        idjob.append(url)
    except NoSuchElementException:
        title='N/A'
        firma='N/A'
        text_html='N/A'
        
print(len(job_title),len(company),len(job_description),len(idjob))

dataset=pd.DataFrame({"Job Title":job_title,"Company":company,"Job Details":job_description,"idjob":idjob})

dataset.to_csv("alljobs_scrapped.csv")

dataset.shape



