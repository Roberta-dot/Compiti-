import scrapy

class TitleSpider(scrapy.Spider):
    name = 'titlespider'
    start_urls = ['http://www.bbc.co.uk']

    def parse(self, response):
        # Estrai i titoli dalla pagina
        titles = response.xpath('//h1/text()').getall()

        # Stampa i titoli
        self.log("Titles:")
        for title in titles:
            self.log(title)

        # Scrivi i titoli in un file di testo
        with open('Esercizio31.txt', 'w') as f:
            for title in titles:
                f.write(f"{title}\n")