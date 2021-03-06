#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 11:18:22 2021

@author: msoltani
"""

import requests
from bs4 import BeautifulSoup
import panda as pd
import time


def review_count_scrape():
    url ='https://www.amazon.com/Best-Sellers/zgbs'
    headers = ({'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537',
                'Accept-Language': 'en-US, en; q=0.5''})
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text,'Lxml')
        print(r.status_code)
        
        product_total_review= [i.text for i in soup.findAll('a', {'class': 'a-small a-link normall'}]
        df =pd.DataFrame(product_total_review)
        print (df)
        
        time.sleep(60)
        
        end_timer =time.time() +60 * 2
        while time.time() < end t