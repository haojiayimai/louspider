import scrapy

from louspider.items import CourseItem
from scrapy.selector import Selector

class LouSpider(scrapy.Spider):
    name = "mylouspider"
    #define allowed domain name
    allowed_domains = ["shiyanlou.com"]
    #define start_urls
    start_urls = ['https://www.shiyanlou.com/courses/?course_type=all&tag=all&free=yes']

    #decode and extract items
    def parse(self, response):
        hxs = Selector(response)
        courses = hxs.xpath('//div[@class="col-md-4 col-sm-6 course"]')
        for course in courses:
            item = CourseItem()
            item['name'] = course.xpath('.//div[@class="course-name"]/text()').extract()[0].strip()
            item['learned'] = course.xpath('.//span[@class="course-per-num pull-left"]/text()').extract()[1].strip()
            item['image'] = course.xpath('.//div[@class="course-img"]/img/@src').extract()[0].strip()
            yield item
