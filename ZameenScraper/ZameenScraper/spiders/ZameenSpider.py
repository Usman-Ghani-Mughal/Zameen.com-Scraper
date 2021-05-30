# <*> --------------------------------------------------------------------------------------------------------- <*>
"""
    This module is used for scraping news from Geo which is pakistani news channel
    link of its web site is : 'https://www.geo.tv/'

    In this module we have Class named as GeoSpider which inherits the class Spider which is a part of 'Scrapy'
    frame work, in this class we have a parse method which we overrides it. This method gets a response object
    from 'Scrapy' frame work, we have written all the logic of scraping news in this method.
    https://www.zameen.com/Plots/Islamabad-3-1.html
"""
# <*> --------------------------------------------------------------------------------------------------------- <*>

# Imports
import scrapy
from ..items import ZameenscraperItem


class ZamenSpider(scrapy.Spider):
    # Name of the spider
    name = 'zameen_Spider'
    basic_url = "https://www.zameen.com"
    # urls to crawl

    start_urls = [
        'https://www.zameen.com/Plots/Islamabad_Bahria_Town_Bahria_Enclave-1705-1.html',
    ]
    page_no = 1
    TOTAL_PAGES = ""

    def parse(self, response):
        """
        This method is used for Extracting data from a website it receives the response object which contains an html
        page return from a given url and write a logic for extracting required data from that html page in this method
        :param response:
        :return: News
        """

        if response.status == 200:
            items = ZameenscraperItem()
            # ----------------  Extracting the total number of Pages ------------------
            if self.page_no == 1:
                total_pages = response.css("._2aa3d08d ::text").extract()
                total_pages = total_pages[0]
                for char in total_pages:
                    if char == ' ':
                        break
                    elif char == ',':
                        continue
                    self.TOTAL_PAGES += char
                self.TOTAL_PAGES = int(self.TOTAL_PAGES)
                print("Total pages : {}".format(self.TOTAL_PAGES))
            # -----------------------------------------------------------------------

            # ---------------------- All Title ------------------------------
            titles = response.css("._162e6469 ::text").extract()
            prices = response.css(".f343d9ce ::text").extract()
            areas = response.css(".b6a29bc0 span::text").extract()
            extra_info = response.css(".c0df3811 ::text").extract()
            details = response.css(".ee550b27 ::text").extract()
            links = response.css(".f74e80f3 a").xpath("@href").extract()
            self.page_no += 1
            if len(titles) == len(prices) and len(titles) == len(areas) and len(titles) == len(extra_info) and len(titles) == len(details) and len(titles) == len(links):
                for index in range(len(titles)):
                    items['Title'] = titles[index]
                    items['Area'] = areas[index]
                    items['Price'] = prices[index]
                    items['Extra_info'] = extra_info[index]
                    items['Details'] = details[index]
                    items['Link'] = self.basic_url + links[index]

                    yield items

            if self.page_no <= self.TOTAL_PAGES:
                next_url = self.start_urls[0][:-6]
                next_url = next_url + str(self.page_no) + ".html"
                print("<***> Next Url is : {} <***>".format(next_url))
                yield response.follow(next_url, callback=self.parse)





