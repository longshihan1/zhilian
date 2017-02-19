import scrapy
from scrapy import Request
from scrapy.selector import HtmlXPathSelector, Selector

from zhilian.items import ZhilianItem
from scrapy import log


class ZhiLianSpider(scrapy.Spider):
    name = "zhilian"
    start_urls = (
        'http://sou.zhaopin.com/jobs/searchresult.ashx?bj=160000&sj=679%3B863%3B2039&in=210500&jl=%E4%B8%8A%E6%B5%B7&sm=0&isfilter=1&p=1&sf=10001&st=15000',
    )

    def parse(self, response):
        response_selector = Selector(response)
        idsvalue = response_selector.xpath(
            u'//table[contains(@class, "newlist")]')
        item_url = idsvalue.xpath(u'//td[contains(@class, "zwmc")]/div/a/@href').extract()
        for item in item_url:
            yield Request(item, callback=self.parse_detail)
        urls = response_selector.xpath(u'//div[contains(@class, "pagesDown")]/ul/li/a/@href').extract()
        urls.pop(-1)
        urls.pop(0)
        for urlitem in urls:
            yield Request(urlitem, callback=self.parseurl)

    def parse_detail(self, response):
        zhilian = ZhilianItem()
        zls = Selector(response)
        zhilian['bussiessname'] = zls.xpath('//div[@class="inner-left fl"]/h2/a/text()').extract()
        zhilian['bussiessurl'] = zls.xpath('//div[@class="inner-left fl"]/h2/a/@href').extract()
        zhilian['jobname'] = zls.xpath('//div[@class="inner-left fl"]/h1/text()').extract()
        bussiessaddress = zls.xpath('//div[contains(@class, "tab-inner-cont")]/h2/text()').extract()
        zhilian['bussiessaddress'] = ''.join(bussiessaddress).strip()
        zhilian['workaddress'] = zls.xpath(
            '//div[contains(@class, "terminalpage-left")]/ul[contains(@class, "terminal-ul clearfix")]/li[2]/strong/a/text()').extract()
        zhilian['money'] = zls.xpath(
            '//div[contains(@class, "terminalpage-left")]/ul[contains(@class, "terminal-ul clearfix")]/li[1]/strong/text()').extract()
        zhilian['education'] = zls.xpath(
            '//div[contains(@class, "terminalpage-left")]/ul[contains(@class, "terminal-ul clearfix")]/li[6]/strong/text()').extract()
        zhilian['releasetime'] = zls.xpath(
            '//div[contains(@class, "terminalpage-left")]/ul[contains(@class, "terminal-ul clearfix")]/li[5]/strong/text()').extract()
        zhilian['num'] = zls.xpath(
            '//div[contains(@class, "terminalpage-left")]/ul[contains(@class, "terminal-ul clearfix")]/li[7]/strong/text()').extract()
        description = zls.xpath('//div[contains(@class, "tab-inner-cont")]/p/text()').extract()
        descriptionStr = ''
        for des in description:
            currentdes = des.strip()
            descriptionStr += currentdes
        zhilian['description'] = descriptionStr
        yield zhilian

    def parseurl(self, response):
        response_selector = Selector(response)
        idsvalue = response_selector.xpath(
            u'//table[contains(@class, "newlist")]')
        item_url = idsvalue.xpath(u'//td[contains(@class, "zwmc")]/div/a/@href').extract()
        for item in item_url:
            yield Request(item, callback=self.parse_detail)
