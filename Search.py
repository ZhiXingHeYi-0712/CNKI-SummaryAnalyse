import requests
from lxml import etree
import math


class Search():
    def search(self, page):
        headers = {
            'Cookie':"""Ecp_notFirstLogin=V59ot6; ASP.NET_SessionId=zv5xqtbcn4vz25skykndtdtt; Ecp_ClientId=2191101171902129079; LID=WEEvREdxOWJmbC9oM1NjYkZCbDdrNTBJL1FoVmhUdjYyT3U5bTd3bENGTlY=$R1yZ0H6jyaa0en3RxVUd8df-oHi7XMMDo7mtKT6mSmEvTuk11l2gFA!!; SID_kns=123113; SID_klogin=125144; Ecp_session=1; KNS_SortType=; SID_crrs=125134; RsPerPage=20; SID_krsnew=125133; cnkiUserKey=dc235810-905b-3d55-1d28-3cd1d31e0ace; SID_kcms=124105; c_m_LinID=LinID=WEEvREdxOWJmbC9oM1NjYkZCbDdrNTBJL1FoVmhUdjYyT3U5bTd3bENGTlY=$R1yZ0H6jyaa0en3RxVUd8df-oHi7XMMDo7mtKT6mSmEvTuk11l2gFA!!&ot=11/01/2019 23:58:08; c_m_expire=2019-11-01 23:58:08; Ecp_LoginStuts=%7B%22IsAutoLogin%22%3Afalse%2C%22UserName%22%3A%22DX0508%22%2C%22ShowName%22%3A%22%25E5%258C%2597%25E4%25BA%25AC%25E5%25B8%2588%25E8%258C%2583%25E5%25A4%25A7%25E5%25AD%25A6%25E7%258F%25A0%25E6%25B5%25B7%25E5%2588%2586%25E6%25A0%25A1%25E5%259B%25BE%25E4%25B9%25A6%25E9%25A6%2586%22%2C%22UserType%22%3A%22bk%22%2C%22r%22%3A%22V59ot6%22%7D"""
        }
        url = """https://kns.cnki.net/kns/brief/brief.aspx?curpage=1&RecordsPerPage=20&QueryID=5&ID=&turnpage=1&tpagemode=L&dbPrefix=SCDB&Fields=&DisplayMode=listmode&PageName=ASP.brief_default_result_aspx&ctl=ed734671-3476-4a27-aabe-79a33b9529de&Param=NVSM%e5%85%b3%e9%94%ae%e8%af%8d+%3d+%27%e5%ae%b6%e5%9b%bd%e6%83%85%e6%80%80%27&isinEn=1&"""\
            .format(page)
        r = requests.get(url=url, headers=headers)

        selector = etree.HTML(r.text)
        return selector.xpath("//tr[@bgcolor='#ffffff' or @bgcolor='#f6f7fb']/td/a[@class='fz14']/@href")

    def searchAll(self, totalNumber):
        pages = math.ceil(totalNumber/20)
        resultList = []
        for i in range(pages):
            print("Get Next Page.")
            resultList.extend(self.search(i))
        return resultList

    def getEnableLink(self, totalNumber):
        resultList = []
        initList = self.searchAll(totalNumber)
        for link in initList:
            resultList.append(link.replace('/kns/detail/detail.aspx?','/KCMS/detail/detail.aspx?')+"&v=MjYyMTN4ZEVlTU9VS3JpZlp1OXVGeW5sVUx6SUlsd1ZMVHpZYkxHNEg5ak5yNDVGWk9vS0R4Tkt1aGRobmo5OFRuanFx")
        return resultList
