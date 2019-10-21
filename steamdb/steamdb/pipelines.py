# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2

class SteamdbPipeline(object):

    def open_spider(self, spider):
        hostname = '127.0.0.1'
        username = 'admin'
        password = 'admin'
        database = 'admin'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        sql = "INSERT INTO steamdb(publisher,name,rating,store_url,source_url,supported_systems,in_game,day_player_peak,all_time_player_peak,developer) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        self.cur.execute(sql,(item['publisher'], item['name'], item['rating'], item['store_url'], item['source_url'], item['supported_systems'], item['in_game'], item['day_player_peak'], item['all_time_player_peak'], item['developer']))
        self.connection.commit()
        return item
