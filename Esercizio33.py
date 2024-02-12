import scrapy
import json

class HMSpider(scrapy.Spider):
    name = 'hm_spider'
    start_urls = ['https://www2.hm.com/it_it/neonato/trend-stagionale/personaggi.html']

    def parse(self, response):
        # Estrai informazioni sui prodotti dalla pagina
        products = response.xpath('//li[@class="product-item"]')
        for product in products:
            yield {
                'name': product.xpath('.//a[@class="link"]/text()').get(),
                'price': product.xpath('.//span[@class="price regular"]/text()').get()
            }

        # Naviga alla pagina successiva (se presente) e chiama la funzione di analisi di nuovo
        next_page = response.xpath('//a[@class="next"]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

def main():
    # Avvia lo spider
    process = scrapy.crawler.CrawlerProcess()
    process.crawl(HMSpider)
    process.start()

    # Salva i risultati in un file JSON
    with open('hm_products.json', 'w') as f:
        json.dump(results, f)

if __name__ == "__main__":
    main()