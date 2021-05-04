import scrapy

class InvestorSpider(scrapy.Spider):

    name = "investor"

    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}

        for i in range(100000, 999999): # https://angel.co/startups/{i} redirects to company pages
            yield scrapy.Request(url=f'https://angel.co/startups/{i}', headers=headers, callback=self.parse)


    def parse(self, response):
        yield {
            'company_name': response.xpath('//*[@id="main"]/div[4]/div/div/div/section/div/div[2]/div/div[1]/h1/a//text()').get().strip(),
            'employee_range': response.xpath('//*[@id="main"]/div[4]/div/aside/div/div/dl/dt[3]/text()[1]').get().strip(),
            'headquarters_location': response.xpath('//*[@id="main"]/div[4]/div/aside/div/div/dl/dt[2]/ul/li/text()').get().strip(),
            'amount_of_available_jobs': response.xpath('//*[@id="main"]/div[4]/div/div/div/nav/div/div[1]/a/text()[2]').get().strip(),
            'funding_amount': response.xpath('//*[@id="main"]/div[4]/div/div/div/div[1]/div/section/div[4]/div[2]/div[1]/h4//text()').get().strip(),
        }