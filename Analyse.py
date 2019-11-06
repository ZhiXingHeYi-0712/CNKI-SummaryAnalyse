import jieba
import sqlite3

def analyseText(fileLocation):
    with open(fileLocation, encoding="utf-8") as f:
        text = f.read()
        text = " ".join(jieba.cut(text)).split()
        print(text)

def statWords(fileLocation):
    with open("stopwords.txt", encoding='utf-8') as stopwordFile:
        stopwords = stopwordFile.read().split('\n')
    with open(fileLocation, encoding='utf-8') as f:
        text = f.read().split()

        wordSQL = sqlite3.connect('WordSQL')
        wordSQLCursor = wordSQL.cursor()
        existList = ''

        for word in text:
            if (word not in stopwords) and (word.__len__()>1):
                if word not in existList:
                    existList = existList + word
                    wordSQLCursor.execute("insert into words (word, seq) VALUES ('{}', 1)".format(word))
                else:
                    wordSQLCursor.execute("update words set seq = seq + 1 where word = '{}'".format(word))

        wordSQL.commit()
        wordSQL.close()
