# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from __future__ import unicode_literals
import sys
import MySQLdb
from superjob.items import SuperjobItem


class SuperjobPipeline(object):
    def __init__(self):
            self.conn = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="133737Aa",  # your password
                     db="hh")
            self.cursor = self.conn.cursor()
            self.conn.set_character_set('utf8')
            self.cursor.execute('SET NAMES utf8;')
            self.cursor.execute('SET CHARACTER SET utf8;')
            self.cursor.execute('SET character_set_connection=utf8;')   
    
    
    
    
    

    def process_item(self, item, spider):
        
            try:
                self.cursor.execute("""INSERT INTO hhemployee (NameVacancy,Salary,Age) 
                        VALUES (%s, %s,%s);""", 
                       (item['NameVacancy'],item['Salary'],item['Age']))
   
                self.conn.commit()            
            except MySQLdb.Error, e:
                print "Error %d: %s" % (e.args[0], e.args[1])
            return item
