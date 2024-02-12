import scrapy

class MetaSpider(scrapy.Spider):
    name = 'metaspider'
    start_urls = ['https://www.bbc.co.uk']

    def parse(self, response):
        # Estrai le meta informazioni dalla pagina
        meta_tags = response.xpath('//meta')
        meta_info = {}
        for meta_tag in meta_tags:
            name = meta_tag.xpath('@name').get()
            content = meta_tag.xpath('@content').get()
            if name and content:
                meta_info[name] = content

        # Stampa le meta informazioni
        self.log("Meta Information:")
        for name, content in meta_info.items():
            self.log(f"{name}: {content}")

        # Scrivi le meta informazioni in un file di testo
        with open('exercise36.txt', 'w') as f:
            f.write("Meta Information:\n")
            for name, content in meta_info.items():
                f.write(f"{name}: {content}\n")