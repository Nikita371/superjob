# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from superjob.items import
import re

class VacancySpider(CrawlSpider):
   
    name = 'superjob_scraper'
    allowed_domains = ['superjob.ru']
    start_urls = ["https://www.superjob.ru/resume/search_resume.html?sort_order=ORDER%20BY%20resume1.rank%20DESC&detail_search=1&sbmit=1&catalogues%5B0%5D=33&t%5B0%5D=4&payment_no_agreement=1"]
    for i in range(1, 5):
         start_urls.append("https://www.superjob.ru/resume/search_resume.html?sort_order=ORDER%20BY%20resume1.rank%20DESC&detail_search=1&sbmit=1&catalogues%5B0%5D=33&t%5B0%5D=4&payment_no_agreement=1&page="+str(i)+"")       
  
                  
                 
  

                 
    


    def parse(self, response):
        yield item
            
        
        