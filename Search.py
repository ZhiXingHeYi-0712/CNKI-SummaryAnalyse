import requests
from lxml import etree
import math


class Search():
    Cookie = ''
    Url = ''
    TotalNumber = 0

    def __init__(self, cookie, url, totalNumber):
        self.Cookie = cookie
        self.Url = url
        self.TotalNumber = totalNumber

    def search(self, page):
        headers = {
            'Cookie': self.Cookie
        }
        url = self.Url.format(page)
        r = requests.get(url=url, headers=headers)

        selector = etree.HTML(r.text)
        return selector.xpath("//tr[@bgcolor='#ffffff' or @bgcolor='#f6f7fb']/td/a[@class='fz14']/@href")

    def searchAll(self):
        pages = math.ceil(self.TotalNumber/20)
        resultList = []
        for i in range(pages):
            print("Get Next Page.")
            resultList.extend(self.search(i))
        return resultList

    def getEnableLink(self):
        resultList = []
        initList = self.searchAll()
        for link in initList:
            resultList.append(link.replace('/kns/detail/detail.aspx?','/KCMS/detail/detail.aspx?')+"&v=MjYyMTN4ZEVlTU9VS3JpZlp1OXVGeW5sVUx6SUlsd1ZMVHpZYkxHNEg5ak5yNDVGWk9vS0R4Tkt1aGRobmo5OFRuanFx")
        return resultList
