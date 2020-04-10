import scrapy
import random

const_url = "https://en.wikipedia.org/"
class WikiSpider(scrapy.Spider):
    name = 'wikispider'
    start_urls = ['https://en.wikipedia.org/wiki/India']
    def parse_another_page(self, response):
        result_another_link = {}
        id = 1
        another_links_count = {}
        another_links_id = {}
        for link in response.css('a').xpath('@href').extract():
            if link in another_links_count:
                if 'https://' in link:
                    another_links_count[link] += 1
                else:
                    link = const_url + link
                    another_links_count[link] += 1
                
            else:
               if 'https://' in link:
                   another_links_count[link] = 1
                   another_links_id[link] = id
                   id = id+1
               else:
                    link = const_url + link
                    another_links_count[link] = 1
                    another_links_id[link] = id
                    id = id+1
        result_another_link['another_links_count'] = another_links_count
        result_another_link['another_links_id'] = another_links_id
        yield result_another_link
    def parse(self, response):
        result_link = {}
        id = 1
        links_count = {}
        links_id = {}
        for link in response.css('a').xpath('@href').extract():
            if link in links_count:
                if 'https://' in link:
                    links_count[link] += 1
                else:
                    link = const_url + link
                    links_count[link] += 1
                
            else:
               if 'https://' in link:
                   links_count[link] = 1
                   links_id[link] = id
                   id = id+1

               else:
                    link = const_url + link
                    links_count[link] = 1
                    links_id[link] = id
                    id = id+1
        url = random.choice(list(links_count.keys()))
        yield  scrapy.Request(url, self.parse_another_page)
        result_link['links_count'] = links_count
        result_link['links_id'] = links_id
        yield result_link
