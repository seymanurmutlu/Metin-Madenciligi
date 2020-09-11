# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import nltk
from snowballstemmer import TurkishStemmer

#nltk.download()

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

##KELİMELERİN SIKLIĞI
#Frequency distributon 
dist = FreqDist(text7)
print(len(dist))

vocab1 = dist.keys()
#vocab1[:10] 
# In Python 3 dict.keys() returns an iterable view instead of a list
print(list(vocab1)[:10])

print(dist['four'])

freqwords = [w for w in vocab1 if len(w) > 5 and dist[w] > 100]
print(freqwords)

#Normalleştirme ve Kelimenin Kökünü Bulma
#Normalleştirme, bir kelimeyi aynı şekilde görünmesi için dönüştürmeniz veya çok farklı görünmelerine rağmen saymanız gereken zamandır. 
#Örneğin, aynı kelimenin geçtiği farklı biçimler olabilir.

input1 = "List listed lists listing listings"
words1 = input1.lower().split(' ')
print(words1)

#Stemming, kelimenin kökünü bulmak anlamına gelir.
#Stemming için bir sürü algoritma kullanabiliriz, şu an oldukça populer ve kullanımı yüksek olan
#porter stemmer'ı kullanacağız.
porter = nltk.PorterStemmer()
[print(porter.stem(t)) for t in words1]

#Turcke stemming için snowballstemmer'ı kullandım ama başarılı bir sonuca ulaşamadım.
inputTr = "Dizi diziler dizdi"
wordsTr = inputTr.lower().split(' ')
print(wordsTr)

turkStem=TurkishStemmer()
[print(turkStem.stemWord(t)) for t in wordsTr]

#LEMMATINAZITON
#Lemmatizasyon, ortaya çıkan kelimelerin gerçekten anlamlı olmasını istediğiniz yerdir.
#Anlamlı kelimeler çıkartan stemming işlemi 
udhr = nltk.corpus.udhr.words('English-Latin1')
print(udhr[:20])

#Lemmatization devam
[print(porter.stem(t)) for t in udhr[:20]] 


WNlemma = nltk.WordNetLemmatizer()
[WNlemma.lemmatize(t) for t in udhr[:20]]

#TOKENIZATION
text11 = "Children shouldn't drink a sugary drink before bed."
text11.split(' ')
print(nltk.word_tokenize(text11))

text12 = "This is the first sentence. A gallon of milk in the U.S. costs $2.99. Is this the third sentence? Yes, it is!"
sentences = nltk.sent_tokenize(text12)
print(len(sentences))
print(sentences)