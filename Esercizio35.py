import scrapy

class MySpider(scrapy.Spider):
    name = 'exercise35'
    start_urls = ['https://www.bbc.co.uk']

    def parse(self, response):
        # Esempio di utilizzo di XPath per estrarre il titolo della pagina
        title = response.xpath('//title/text()').get()
        with open('Ex35Title.txt', 'a') as f:
            f.write(f'Title: {title}\n')

        # Esempio di utilizzo di XPath per estrarre i link presenti nella pagina
        links = response.xpath('//a/@href').getall()
        with open('Ex35Links.txt', 'a') as f:
            f.write('Links:\n')
            for link in links:
                f.write(f'{link}\n')

        # Esempio di utilizzo di XPath per estrarre il testo di un elemento specifico
        paragraph_text = response.xpath('//p[@class="example-class"]/text()').get()
        with open('Ex35Elemento.txt', 'a') as f:
            f.write(f'Paragraph Text: {paragraph_text}\n')

        # Esempio di utilizzo di XPath per estrarre dati da una tabella HTML
        rows = response.xpath('//table[@id="example-table"]//tr')
        with open('Ex35Tabella.txt', 'a') as f:
            f.write('Table Data:\n')
            for row in rows:
                cell1 = row.xpath('td[1]/text()').get()
                cell2 = row.xpath('td[2]/text()').get()
                f.write(f'Cell 1: {cell1}, Cell 2: {cell2}\n')

                # Puoi anche estrarre altri dati o seguire ulteriori link
                # Utilizzando response.follow() o scrapy.Request() come appropriato

