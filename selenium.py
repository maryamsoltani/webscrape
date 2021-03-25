#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 12:52:45 2021

@author: msoltani
"""

import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.get ('http://www.google.com/')
time.sleep(5)
driver.quit()


