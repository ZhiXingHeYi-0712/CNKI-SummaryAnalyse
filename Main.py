from Search import Search
from Article import ArticleAnalyse
import Analyse

search = Search()
links = search.getEnableLink(1000)
with open("Summary",'a+',encoding='utf-8') as f:
    for i in links:
        analyse = ArticleAnalyse(i,f)
        analyse.writeFile()

Analyse.statWords("Summary_Fans.txt _jieba.txt")