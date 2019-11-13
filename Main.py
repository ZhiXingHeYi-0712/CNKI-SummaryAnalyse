from Analyse import Analyser
from Search import Search
from Article import Article

search = Search("""cnkiUserKey=37077a91-56b1-e799-a114-60fa62079318; Ecp_ClientId=5191028193401977778; RsPerPage=20; amid=348964eb-d453-43e3-9711-e86275d43b31; UM_distinctid=16e31049dfb23b-0f39744427f5db-b363e65-144000-16e31049dfc58d; Hm_lvt_6e967eb120601ea41b9d312166416aa6=1573027077,1573262387; LID=WEEvREcwSlJHSldRa1FhdXNXaEhoOGhSL2kwK1J2aFJEakc2UzhWRjFxQT0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!; ASP.NET_SessionId=dj0jzj0pzhvqcjstare1xoii; SID_kns=123119; SID_klogin=125141; SID_crrs=125134; KNS_SortType=; Ecp_session=1; _pk_ref=%5B%22%22%2C%22%22%2C1573630944%2C%22https%3A%2F%2Fwww.cnki.net%2F%22%5D; _pk_ses=*; SID_kns_new=123116; __lfcc=1; SID_krsnew=125133""",
                """https://kns.cnki.net/kns/brief/brief.aspx?curpage={}&RecordsPerPage=20&QueryID=5&ID=&turnpage=1&tpagemode=L&dbPrefix=SCDB&Fields=&DisplayMode=listmode&PageName=ASP.brief_default_result_aspx&ctl=746420fc-66a8-4f48-bfb2-dba1c939b543&Param=NVSM%e5%85%b3%e9%94%ae%e8%af%8d+%3d+%27%e5%ae%b6%e5%9b%bd%e6%83%85%e6%80%80%27&isinEn=1&""",
                500)

Links = search.getEnableLink()

with open("Summary_Nation.txt",'w',encoding='utf-8') as f:
    outPut = ''
    for link in Links:
        art = Article(link)
        outPut = outPut + art.getSummary()
    f.write(outPut)

an = Analyser("Summary_Nation.txt", "Nation_words.txt", "NationSql", "NationCloud.html")
# an = Analyser("Summary_Fans.txt", "Fans_words.txt", "FansSql", "FansCloud.html")

an.analyse("(seq > 15)")

