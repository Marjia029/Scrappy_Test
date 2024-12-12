import scrapy
from scrapingcourse_scraper.items import ProductItem


class ProductsSpider(scrapy.Spider):
    name = "products"
    start_urls = ["https://www.scrapingcourse.com/ecommerce/"]

    def parse(self, response):
        products = response.css(".product")
        for product in products:
            item = ProductItem()
            item["url"] = product.css("a").attrib["href"]
            item["name"] = product.css("h2::text").get()
            item["price"] = "".join(product.css(".price *::text").getall())
            item["image_urls"] = [product.css("img").attrib["src"]]
            yield item
