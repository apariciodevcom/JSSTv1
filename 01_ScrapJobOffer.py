import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

import numpy as np
from sqlalchemy import create_engine

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

browser=webdriver.Chrome("chromedriver.exe")
browser.get("https://www.yyy.zzz") #Enter web to scrap

username=browser.find_element_by_id("session_key")
username.send_keys("email@of.user")
password=browser.find_element_by_id("session_password")
password.send_keys("thepassword")

login_buttom=browser.find_element_by_class_name("sign-in-form__submit-button")
login_buttom.click()

browser.get("https://www.linkedin.com/jobs/search/?geoId=101165590&keywords=data%20analyst&location=United%20Kingdom&start=675")

# disabled ember-view job-card-container__link job-card-list__title

job=browser.find_elements_by_class_name("job-card-list__title")
c=[]
href=[]
for i in job:
    try:
        c.append(i.text)
        href.append(i.get_attribute('href'))
    except NoSuchElementException:
        print('error')
print()
print(len(c))

#job-card-container__link job-card-container__company-name ember-view

job2=browser.find_elements_by_class_name("job-card-container__company-name")
company=[]
for j in job2:
    try:
        comp=j.text
        company.append(comp)
    except NoSuchElementException:
        comp='N/A'
        company.append(comp)
        

print(len(company))

job3=browser.find_elements_by_class_name("job-card-container__metadata-wrapper")
location=[]
for k in job3:
    try:
        location.append(k.text)
    except NoSuchElementException:
        print('error')
print(len(location))

col=["Company Name","Job Position","Location","Link"]
df=pd.DataFrame({"Company Name":company,"Job Position":c,"Location":location, "Link":href})

df.to_csv("data_analyst_60.csv")
