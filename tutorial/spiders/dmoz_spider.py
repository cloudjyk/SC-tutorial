# -*- coding: utf-8 -*-
from scrapy.spider import Spider  
  
class DmozSpider(Spider):  
    name = "dmoz"  
    allowed_domains = ["dmoz.org"]  
    start_urls = [  
        "https://tieba.baidu.com/p/5253653337/",  
        "https://tieba.baidu.com/p/5317249588/"  
    ]  
  
    def parse(self, response):  
        print('=========\n',response.url,'\n=========')
        filename = response.url.split("/")[-2]
        print('=========\n',filename,'\n=========')
        # print('=========\n',response.body,'\n=========')
        open(filename, 'wb').write(response.body)  