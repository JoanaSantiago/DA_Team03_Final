import TestProject
import scrapy
import getRequests

class NewSpider (scrapy.Spider):
    name = "spideyman"
    allowed_domains = ['www.halice.com']
    start_urls = ['http://192.168.139.131/halice/']

    def start_requests(self):
        urls = [
            'http://192.168.139.131/halice/'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
            
        pictures = response.xpath('//img/@src').extract()
        print(pictures)

        xpath_selector = '//img'
        for x in response.xpath(xpath_selector):
            newsies = '@src'
            yield {
                'Image Link': x.xpath(newsies).extract_first(),
            }

            page_selector = '.next a ::attr(href)'
            next_page = response.css(page_selector).extract_first()
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
                )