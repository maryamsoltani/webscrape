#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 14:34:11 2021

@author: msoltani
"""
from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import panda as pd

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedrover")
url = 'https://www.bbc.com/'

driver.get()