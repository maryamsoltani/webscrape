# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#section 1
import scrapy

#section 2
class FirstSpider(scrapy.Spider):
    name = "Books"
    start_urls = [
        "https://www.books.toscrape.com/"
        ]
    
                 
    
    
    #section 3
    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = 'books-%s.html' % page
        with open(filename, "wb") as f:
            f.write(response.body)
            