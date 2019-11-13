import requests
from lxml import etree


class Article:
    Link = ''

    def __init__(self, link):
        self.Link = "https://kns.cnki.net" + link

    def crawl(self):
        print("Crawl Article")
        return requests.get(self.Link).text

    def getSummary(self):
        html = self.crawl()

        selector = etree.HTML(html)
        link = selector.xpath("//span[@id='ChDivSummary']")
        if len(link) > 0:
            return link[0].text
        else:
            return ''
