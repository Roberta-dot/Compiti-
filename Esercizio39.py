import scrapy

class RssSpider(scrapy.Spider):
    name = 'rssspider'
    start_urls = ['https://feeds.bbci.co.uk/news/world/rss']

    def parse(self, response):
        # Estrai i dati dal feed RSS
        items = response.xpath('//item')
        data = []

        for item in items:
            title = item.xpath('title/text()').get()
            link = item.xpath('link/text()').get()
            description = item.xpath('description/text()').get()
            pub_date = item.xpath('pubDate/text()').get()

            # Formatta i dati come desiderato
            data.append({
                'Title': title,
                'Link': link,
                'Description': description,
                'Publication Date': pub_date
            })

        # Stampa i dati
        self.log("RSS Data:")
        for item in data:
            self.log(item)

        # Scrivi i dati in un file di testo
        with open('Exercise39.txt', 'w') as f:
            for item in data:
                f.write(f"Title: {item['Title']}\n")
                f.write(f"Link: {item['Link']}\n")
                f.write(f"Description: {item['Description']}\n")
                f.write(f"Publication Date: {item['Publication Date']}\n")
                f.write("\n")