from Analyse import Analyser
from Search import Search
from Article import Article

search = Search("""Ecp_notFirstLogin=7Tu04O; Ecp_ClientId=2191101171902129079; RsPerPage=20; cnkiUserKey=dc235810-905b-3d55-1d28-3cd1d31e0ace; ASPSESSIONIDQSRDCQCD=HADIOGEBKAPBBKAHECJLMFOP; SID_kns_new=123114; c_m_LinID=LinID=WEEvREcwSlJHSldRa1FhcTdWa2FjVDJyb1l0cWw0WEo1aUg2S2JCeERUQT0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&ot=11/13/2019 15:01:27; LID=WEEvREcwSlJHSldRa1FhcTdWa2FjVDJyb1l0cWw0WEo1aUg2S2JCeERUQT0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!; c_m_expire=2019-11-13 15:01:27; Ecp_LoginStuts=%7B%22IsAutoLogin%22%3Afalse%2C%22UserName%22%3A%22DX0508%22%2C%22ShowName%22%3A%22%25E5%258C%2597%25E4%25BA%25AC%25E5%25B8%2588%25E8%258C%2583%25E5%25A4%25A7%25E5%25AD%25A6%25E7%258F%25A0%25E6%25B5%25B7%25E5%2588%2586%25E6%25A0%25A1%25E5%259B%25BE%25E4%25B9%25A6%25E9%25A6%2586%22%2C%22UserType%22%3A%22bk%22%2C%22r%22%3A%227Tu04O%22%7D; ASP.NET_SessionId=3r1ydufrs53uevpccb5odygx; SID_kns=123123; Ecp_session=1; SID_crrs=125132; SID_klogin=125143; KNS_SortType=; SID_krsnew=125132""",
                """https://kns.cnki.net/kns/brief/brief.aspx?curpage=1&RecordsPerPage=20&QueryID=5&ID=&turnpage=1&tpagemode=L&dbPrefix=SCDB&Fields=&DisplayMode=listmode&PageName=ASP.brief_default_result_aspx&ctl=17b4db4d-f624-4000-b97b-2c7310648f90&Param=NVSM%e5%85%b3%e9%94%ae%e8%af%8d+%3d+%27%e5%ae%b6%e5%9b%bd%e6%83%85%e6%80%80%27&isinEn=1&""",
                300)

Links = search.getEnableLink()

with open("Summary_Nation.txt",'w',encoding='utf-8') as f:
    outPut = ''
    for link in Links:
        art = Article(link)
        outPut = outPut + art.getSummary()
    f.write(outPut)

an = Analyser("Summary_Nation.txt", "Nation_words.txt", "NationSql", "NationCloud.html")

an.analyse("(seq > 15)")