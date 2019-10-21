# -*- coding: utf-8 -*-
import scrapy

from items import GameItem


class SteamSpider(scrapy.Spider):
    name = 'steamdb'
    allowed_domains = ['steamdb.info']
    start_urls = ['https://steamdb.info/']

    def parse(self, response):
        response.meta['proxy'] = 'http://199.195.251.143:3128'
        games = response.css('div.span6 table.table-products tbody tr.app')
        for game in games:
            next_page = game.css('a.css-truncate::attr(href)').extract_first()
            yield response.follow(next_page, callback=self.parse_game)


    def parse_game(self, response):
        item = GameItem()
        table = response.css('table.table-dark')
        item['name'] = table.xpath('//td[@itemprop="name"]/text()').extract_first()
        item['developer'] = table.xpath('//span[@itemprop="author"]/text()').extract_first()
        item['publisher'] = table.xpath('//span[@itemprop="publisher"]/text()').extract_first()
        item['supported_systems'] = table.xpath('//meta[@itemprop="operatingSystem"]/@content').extract_first()
        item['in_game'] = response.css('[id="js-graphs-button"] div.header-thing-good::text').extract_first()
        item['rating'] = response.css('div.span4 a.header-thing div.header-thing-number::text').extract_first()
        item['store_url'] = response.xpath('//nav/a[@itemprop="url"]/@href').extract_first()
        item['source_url'] = response.url
        item['day_player_peak'] = response.xpath('//*[@id="graphs"]/ul[1]/li[2]/strong/text()').extract_first()
        item['all_time_player_peak'] = response.xpath('//*[@id="graphs"]/ul[1]/li[3]/strong/text()').extract_first()
        yield item
