# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
from __future__ import unicode_literals
import scrapy


class SuperjobItem(scrapy.Item):
    NameVacancy = scrapy.Field()
    Salary = scrapy.Field()
    Age  = scrapy.Field()
