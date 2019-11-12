library(RSQLite)
library(wordcloud2)
library(webshot)
library(htmlwidgets)
args <- commandArgs(T)
# 参数1：数据库名称
# 参数2：输出文件名称
# 参数3：查找条件

con <- dbConnect(RSQLite::SQLite(), dbname = args[1])

result <- dbSendQuery(con, paste("select * from words where ", args[3]))

infoFrame <- fetch(result)

my_graph <- wordcloud2(infoFrame)

saveWidget(my_graph,args[2],selfcontained = F) #先保存为网页格式
