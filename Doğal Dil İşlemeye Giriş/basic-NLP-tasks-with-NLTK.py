# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import nltk

nltk.download()

from nltk.book import *

##KELİME DAĞARCIĞI SAYMA

#örnek kütüphanedeki text7'yi bas.
print(text7)

#örnek kütüphanedeki sent7'yi bas.
print(sent7)
#sent7'nin kelime sayısını bas.
print(len(sent7))
#DİKKAT! noktalama işaretleri de birer kelime sayılmıştır.

#Şimdi daha önce baktığımız Wall Street Journal yani text7'nin kelime sayısını bas.
print(len(text7))
#text7 içerisindeki benzersiz kelimelerin sayısını bas.
print(len(set(text7)))
#benzersiz kelimeler listesindeki ilk 10 kelimeyi bas.
print(list(set(text7))[:10])

