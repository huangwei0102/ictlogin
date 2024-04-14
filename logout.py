#!/usr/bin/env python
# -*-coding:utf-8-*-
import os

from selenium import webdriver

os.environ["PATH"] += os.pathsep + os.path.dirname(os.path.realpath(__file__))
driver = webdriver.PhantomJS()
driver.set_window_size(1124, 850)
driver.get("https://gw.ict.ac.cn/srun_portal_success?ac_id=1&theme=pro")
driver.find_element_by_css_selector("button#logout").click()
print("Logout successfully.")
driver.quit()
