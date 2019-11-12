from Analyse import Analyser

an = Analyser("Summary_Fans.txt", "Fans_words.txt", "FansSql", "FansCloud.html")

an.analyse("(seq > 15 and seq < 1000)")