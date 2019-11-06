import requests
from lxml import etree


class ArticleAnalyse:
    Link = ''
    File = ''

    def __init__(self, link, file):
        self.Link = "https://kns.cnki.net" + link
        self.File = file

    def crawl(self):
        return requests.get(self.Link).text

    def getSummary(self):
        html = self.crawl()

        selector = etree.HTML(html)
        link = selector.xpath("//span[@id='ChDivSummary']")
        if len(link) > 0:
            return link[0].text
        else:
            return ''

    def writeFile(self):
        print("Write File.")
        self.File.write(self.getSummary())
