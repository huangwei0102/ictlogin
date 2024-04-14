#!/usr/bin/env python
# -*-coding:utf-8-*-
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

os.environ["PATH"] += os.pathsep + os.path.dirname(os.path.realpath(__file__))
driver = webdriver.PhantomJS()
driver.get("https://gw.ict.ac.cn/cgi-bin/srun_portal")
print(driver.page_source)

# waitting until the username element is visible
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "username")))

input_username = driver.find_element_by_id("username")
input_username.send_keys("my_username")

# waitting until the password element is visible
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))

password = driver.find_element_by_id("password")
password.send_keys("my_password")

# waitting until the username element is visible
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "btn-login")))

btn = driver.find_element_by_class_name("btn-login")
btn.click()
# password.send_keys(Keys.RETURN)

time.sleep(1)
driver.quit()
