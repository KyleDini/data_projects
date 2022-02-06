# Scrapy can handle HTTP requests, extraction of data, and writing to a file
# makes it way easier to do impressive scraping, but you have to follow it's rules (such as specific variable names)
# the syntax for this package is different than the syntax for beautifulsoup
# In this example, we're going to scrape the data from a website that has 50 pages of books for sale
# what we're creating is called a spider, which is a class that defines how a certain cite or cites are scraped
# you can scrape multiple websites at a time

# url = http://books.toscrape.com/

import scrapy

class BookSpider(scrapy.Spider):
    name = "bookspider"
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        # response refers to what we get back from the HTTP request
        for article in response.css('article.product_pod'):
            yield {
                'price': article.css(".price_color::text").extract_first(),
                'title': article.css("h3 > a::attr(title)").extract_first()
            }
            next = response.css('.next > a::attr(href)').extract_first()
            if next:
                yield response.follow(next, self.parse)