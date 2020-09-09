#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 18:00:15 2020

@author: seyma
"""
import nltk
from nltk.book import *
from nltk.corpus import treebank

##NLTK fonksiyonlarını daha hızlı öğrenmek için bu dokümanda örnek cümleler ingilizce kullanılmıştır.
# Konular;
#POS Etiketleme / Part-of-Speech (POS) Tagging
#Cümle Yapısını parse etme



#
#CC -> Conjunction -> Baglaç CD -> Cardinal -> ? DT -> Determiner -> Belirteç IN -> 
#Preposition -> Edat JJ -> Adjective -> Sıfat MD -> Modal -> Kip NN -> Noun -> 
#İsim POS -> Possessive -> İyelik PRP -> Pronoun -> Zamir RB -> Adverb -> Zarf SYM -> 
#Symbol -> İşaret VB -> Verb -> Fiil

#HELP - yardım komutu vererek kelime sınıfları hakkında daha fazla bilgi edinme.
print("İngilizce'de kipler hakkinda bilgi :",nltk.help.upenn_tagset('MD'), "\n") #İngilizce'de kipler hakkinda bilgi verir.

print("İngilizce'de sıfatlar hakkinda bilgi :",nltk.help.upenn_tagset('JJ'), "\n") #İngilizce'de sıfatlar hakkinda bilgi verir.

print("İngilizce'de iyelikler hakkinda bilgi :",nltk.help.upenn_tagset('POS'), "\n") #İngilizce'de iyelikler hakkinda bilgi verir.

text1 = "Children shouldn't drink a sugary drink before bed."
text2 = nltk.word_tokenize(text1) #cumleyi kelimelerine ayir.

print("text2 : ",text2, "\n")

print("Text2 pos etiketleme : ",nltk.pos_tag(text2), "\n")#pos etikle.

#POS Tagglemede Belirsizlikler

text3 = nltk.word_tokenize("Visiting aunts can be a nuisance")
#Teyzeleri ziyaret etmek mi sıkıntı yoksa ziyaret eden teyzeler mi sıkıntı olabilir burada bir belirsizlik bulunmakta.

print("text3 pos etkiketleme :",nltk.pos_tag(text3), "\n")
#alternatif olarak visinting burada sifat olabilirdi.
#Genelde Visiting'i sıfat olarak kullanmak olasilik olarak
#dusuk oldugu icin nltk.pos_tag() yukarıdaki kullanımı tercih ediyor.
#Bu tercih noktasında belirsizlik oluşuyor.

#Parsing Sentence Structure(Cumle Yapısını Parçalama)
text4 = nltk.word_tokenize('Alice loves Bob')
#Hangisi isim, hangisi fiil ayrımı yapmak istiyoruz. Bunların cümlede 
#nasıl ilişkili olduklarını da merak ediyoruz.

grammar = nltk.CFG.fromstring("""
S -> NP VP
VP -> V NP
NP -> 'Alice' | 'Bob'
V -> 'loves'""")

parser = nltk.ChartParser(grammar)

trees = parser.parse_all(text4)

print("trees : ",trees, "\n")

for tree in trees:
    print(tree)
    
#Cümle dilbilgisi açısından doğru olsa bile belirsizlik olabilir.

text5 = nltk.word_tokenize("I saw the man with a telescope")

grammar1 = nltk.CFG.fromstring("""
S -> NP VP
VP -> V NP | VP PP
PP -> P NP
NP -> DT N | DT N PP | 'I'
DT -> 'a' | 'the'
N -> 'man' | 'telescope'
V -> 'saw'
P -> 'with'""")
#Bu olabilicek 2 alternatif olarak yazilmis bir grammer yapısı
#agac olarak cizilirse 2 farkli kullanilabilecek yapının olduğu gözükür.

parser = nltk.ChartParser(grammar1)
trees = parser.parse_all(text5)

#grammar1 = nltk.data.load('mygrammar.cfg') #kendi grammer dosyanızı yukleyip kullanabilirsiniz.

for tree in trees:
    print(tree)

# treebank kullanımı 
#Wall Street journal ilk cumlesini treebank modulünü kullanarak ekrana bas.
text17 = treebank.parsed_sents('wsj_0001.mrg')[0] 

print("text17 : ",text17, "\n")

### POS tagging and parsing ambiguity

text18 = nltk.word_tokenize('The old man the boat') #kelimelerin yaygın olmayan kullanımları

print(nltk.pos_tag(text18), "\n") #bu gramer olarak dogru degil

#İyi biçimlendirilmiş cümleler anlamsız da olabilir.


#cumleyi okuduğunuzda cumlenin yapısının dogru olduğunu görürsünüz fakat anlamsızdır.Bu şekilde etiketlemeye
#calistigimizda yanlis sonucu verir
text19 = nltk.word_tokenize("Colorless green ideas sleep furiously")

print(nltk.pos_tag(text19), "\n")
