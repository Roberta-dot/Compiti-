import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://shoegazeblog.com/2020/10/02/radiohead-kid-a/']

    def parse(self, response):
        # Estrai i commenti dalla pagina
        comments = response.xpath('//div[@class="comment"]//p/text()').getall()

        # Stampa i commenti
        self.log("Comments:")
        for comment in comments:
            self.log(comment)

        # Scrivi i commenti in un file di testo
        with open('exercise37.txt', 'w') as f:
            f.write("Comments:\n")
            for comment in comments:
                f.write(f"{comment}\n")