import scrapy

class ImageSpider(scrapy.Spider):
    name = 'imagespider'
    start_urls = ['https://www.bbc.co.uk']

    def parse(self, response):
        # Estrai gli URL delle immagini dalla pagina
        image_urls = response.css('img::attr(src)').getall()

        # Stampa gli URL delle immagini
        self.log("Image URLs:")
        for url in image_urls:
            self.log(url)

        # Scrivi gli URL delle immagini in un file di testo
        with open('Exercise38.txt', 'w') as f:
            f.write("Image URLs:\n")
            for url in image_urls:
                f.write(f"{url}\n")