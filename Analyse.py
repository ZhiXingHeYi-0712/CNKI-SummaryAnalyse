import jieba
import sqlite3
import os

class Analyser:
    InputFileLocation = ''
    OutputFileLocation = ''
    SQLLocation = ''
    WordCloudLocation = ''

    def __init__(self, inputFileLocation, outputFileLocation, sqlLocation, wordCloudLocation):
        self.InputFileLocation = inputFileLocation
        self.OutputFileLocation = outputFileLocation
        self.SQLLocation = sqlLocation
        self.WordCloudLocation = wordCloudLocation

    def analyse(self, findCommand):
        self.analyseText()
        self.statWords()
        self.paintWordCloud(findCommand)

    def analyseText(self):
        with open(self.InputFileLocation, encoding="utf-8") as f:
            text = f.read()
            text = " ".join(jieba.cut(text)).split()

        with open(self.OutputFileLocation, 'w', encoding='utf-8') as f:
            f.writelines(" ".join(text))

    def statWords(self):
        with open("stopwords.txt", encoding='utf-8') as stopwordFile:
            stopwords = stopwordFile.read().split('\n')
        with open(self.OutputFileLocation, encoding='utf-8') as f:
            text = f.read().split()

            wordSQL = sqlite3.connect(self.SQLLocation)
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

    def paintWordCloud(self, findCommand):
        cmd = """ Rscript.exe RScript/WordCloudPaint.R {} {} "{}" """\
            .format(self.SQLLocation, self.WordCloudLocation, findCommand)
        os.system(cmd)

        