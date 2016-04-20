
from scrapy.spiders import Spider  
from scrapy.selector import Selector  

from tutorial.items import tutpyItem
  
class tutpySpider(Spider):  
    name = "tutpy"  
    allowed_domains = ["http://www.liaoxuefeng.com"]  
    start_urls = [  
        "http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000"
    ]  
  
#    def parse(self, response):  
#        filename = response.url.split("/")[-2]  
#        open(filename, 'wb').write(response.body)  


    def parse(self, response):  
        sel = Selector(response)  
        sites = sel.xpath('//ul/li')  
        items = [] 
        for site in sites:  
            item = tutpyItem()
            item['title'] = site.xpath('a/text()').extract()  
            item['link'] = site.xpath('a/@href').extract()  
            item['desc'] = site.xpath('text()').extract()  
            items.append( item)
        return items
