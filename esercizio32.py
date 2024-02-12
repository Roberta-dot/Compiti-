import scrapy

class LinksSpider(scrapy.Spider):
    name = 'links'
    start_urls = ['https://www.bbc.co.uk']

    def parse(self, response):
        # Extract all links using XPath
        links = response.xpath('//a/@href').getall()

        # Open a file in write mode to save the links
        with open('links.txt', 'w') as f:
            # Write each link to the file
            for link in links:
                f.write(link + '\n')