import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/page/1/",
        "https://quotes.toscrape.com/page/2/",
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }
        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None: 
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
            
          # my accoutn free  
# 45.127.248.127:5128
# 207.244.217.165:6712
# 134.73.69.7:5997
# 64.64.118.149:6732
# 157.52.253.244:6204
# 167.160.180.203:6754
# 166.88.58.10:5735
# 173.0.9.70:5653
# 204.44.69.89:6342
# 173.0.9.209:5792

#internet free
# 140.227.204.70:3128
# 103.127.106.249:8090	
# 130.61.120.213:8888
# 134.209.29.120:3128
# 132.148.245.112:19483
# 102.220.142.193:8080
# 102.215.197.202:9999
# 101.255.167.110:3125
# 1.179.151.165:31948
# 103.111.22.65:31948


#internet free
# 1.0.170.50:8080
# 137.59.5.171:6654
# 103.105.196.30:80
# 102.66.110.172:9999
# 103.110.10.190:3128
# 130.61.120.213:8888
# 103.105.196.56:80
# 130.255.162.199:44234		
# 136.226.232.198:11197
# 136.226.81.15:10230
# 136.226.67.28:10160
# 136.226.65.108:10160
# 102.68.131.31:8080
# 1.179.148.9:36476
# 103.115.255.94:36331