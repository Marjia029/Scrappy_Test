import scrapy


class ProductItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    image_urls = scrapy.Field()  # Field to store image URLs
    images = scrapy.Field()      # Field to store image metadata
