import scrapy
import json
import getRequests

class NewSpider (scrapy.Spider):
    name = "spideyman"
    allowed_domains = ['www.halice.com']
    start_urls = ['http://172.18.58.238/halice/']

    def start_requests(self):
        urls = [
            'http://172.18.58.238/halice/'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        pictures = response.xpath('//img/@src').extract()
        print(pictures)

        xpath_selector = '//img'
        for x in response.xpath(xpath_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }

            page_selector = '.next a ::attr(href)'
            next_page = response.css(page_selector).extract_first()
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
                )