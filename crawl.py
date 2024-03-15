from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# available topics
politics = ["https://www.wsj.com/politics?mod=nav_top_section", "https://www.nytimes.com/section/politics", "https://www.bbc.com/news/us-canada"]
business = ["https://www.bbc.com/business", "https://www.nytimes.com/section/business", "https://www.wsj.com/business?mod=nav_top_section"]
tech = ["https://www.wsj.com/tech?mod=nav_top_section", "https://www.nytimes.com/section/technology", "https://www.bbc.com/innovation/technology"]

class mySpider(CrawlSpider):
    name = "spy"
    allowed_domains = ["www.nytimes.com", "www.wsj.com", "www.bbc.com"]

    # make this change from tech to a prompt that gives them 3 options
    start_urls = tech

    rules = (
        Rule(LinkExtractor(allow=r'/\d{4}/\d{2}/\d{2}/'), callback='parse_article'),
        Rule(LinkExtractor(allow=r'/innovation/technology'), callback='parse_article'),
        Rule(LinkExtractor(allow=r'/tech?mod=nav_top_section'), callback='parse_article'),
    )

    def parse_article(self, response):  
        # Extract headlines and summary here
        headline = response.css('h1::text').get()
        summary = response.css('meta[name="description"]::attr(content)').get()

        # You can further process or store the data as needed
        yield {
            'headline': headline,
            'summary': summary,
            'url': response.url,
        }


# filter the same date of the articles as todays date