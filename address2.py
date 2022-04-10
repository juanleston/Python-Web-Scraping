#Import Packages:
import scrapy
import pandas as pd

#Load second part of the start url's file:
url_df = pd.read_csv('/Users/juan/Documents/Data Science Portfolio/pythonscrapy/starturlsvietnam2.csv')

class AddressSpider(scrapy.Spider):
    name = 'address2'
    start_urls = url_df['url'].tolist()

    def parse(self, response):
        for place in response.xpath("//body"):
            yield{
                'country': place.xpath("(.//div[@class = 'breadcrumb']//a[@itemprop = 'item']/span[@itemprop = 'name']/descendant::text())[1]").extract(),
                'subregion': place.xpath("(.//div[@class = 'breadcrumb']//a[@itemprop = 'item']/span[@itemprop = 'name']/descendant::text())[2]").extract(),
                'province': place.xpath("(.//div[@class = 'breadcrumb']//a[@itemprop = 'item']/span[@itemprop = 'name']/descendant::text())[3]").extract(),
                'city_postal': place.xpath(".//div[@class = 'codes']/div[@class = 'units noletters']//div/*/text()").extract()
            }