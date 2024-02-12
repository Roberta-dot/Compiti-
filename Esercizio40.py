import scrapy

class ForumSpider(scrapy.Spider):
    name = 'forumspider'
    start_urls = ['https://scatterbrain.altervista.org/mb/index.php?/forum/1-generale']

    def parse(self, response):
        # Estrai i post dalla pagina corrente
        posts = response.xpath('//div[@class="post"]')

        # Estrai i dati da ogni post
        data = []
        for post in posts:
            username = post.xpath('.//span[@class="username"]/text()').get()
            content = post.xpath('.//div[@class="content"]/text()').get()
            data.append({'Username': username, 'Content': content})

        # Stampa i post
        self.log("Posts:")
        for post in data:
            self.log(post)

        # Scrivi i post in un file di testo
        with open('Exercise40.txt', 'a') as f:
            for post in data:
                f.write(f"Username: {post['Username']}\n")
                f.write(f"Content: {post['Content']}\n")
                f.write("\n")

        # Segui il link alla pagina successiva, se presente
        next_page = response.xpath('//a[@class="next-page"]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)