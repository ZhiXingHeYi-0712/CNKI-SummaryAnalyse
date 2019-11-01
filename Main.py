from Search import Search
from Analyse import ArticleAnalyse

search = Search()
links = search.getEnableLink(1000)
with open("Summary",'a+',encoding='utf-8') as f:
    for i in links:
        analyse = ArticleAnalyse(i,f)
        analyse.writeFile()





