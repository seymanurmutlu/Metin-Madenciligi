# -*- coding: utf-8 -*-

##Metin uzunluğu bulmak
text1 = "Yurt dışında yaşayan vatandaşlarımız, daha önce zahmetli ve uzun süren apostil işlemlerini internet üzerinden çok kısa sürede yapabiliyor."
print("text1 :" , text1)
print("text1 karakter sayısı: " , len(text1))

##Metindeki kelime sayısını bulmak
text2 = text1.split(' ')
print("text1 kelime sayısı: " , len(text2))

print("text2 :", text2)
##Belirli kelimeleri bulma

#text2'de 3 harften uzun kelimeleri bulmak 
print("text2'de 3 harften uzun kelimeler :",[w for w in text2 if len(w) > 3] )

# text2'de büyük harfle başlayan kelimeleri bulmak 
print("text2'de büyük harfle başlayan kelimeler :",[w for w in text2 if w.istitle()])

# text2'de e ile biten kelimeleri bulmak 
print("text2'de e ile biten kelimeler :" , [w for w in text2 if w.endswith('e')])

# Benzersiz kelimeleri 'set()' kullanarak bulmak 
text3 = "Dal sarkar kartal kalkar, kartal kalkar dal sarkar"
print("text3 :" , text3)
text4 = text3.split(' ')
print("text3 kelime sayısı :",len(text4))
print("text3 tekrar etmeyen kelime sayısı :",len(set(text4)))
print("text3 tekrar etmeyen kelimeler :",set(text4))

print("text4'de tüm stringleri küçük harfe çevir" ,len(set([w.lower() for w in text4])) ) # .lower tüm stringleri küçük harfe çevirir
print("tüm stringleri küçük harfe çevir, tekrar etmen kelimeler :" ,set([w.lower() for w in text4]) )


##Serbest metin işleme
text5 = 'İdari Yargının Etkinliğinin Artırılması ve Danıştay’ın Kurumsal Kapasitesinin Güçlendirilmesi Projesi’nin 3. Yürütme Kurulu toplantısı Sn. Hakan Öztatar’ın başkanlığında 19/06/2020 tarihinde video konferans yoluyla gerçekleştirilmiştir #ABProjeleri #OrtakGelecegimiz @ABBaskanligi https://twitter.com/higm_adalet'
print("text5 :",text5)
text6 = text5.split(' ')
print("text6 :",text6)

#Hashtag bulmak
print("Hashtagleri bul:", [w for w in text6 if w.startswith('#')])

# Bahsetmeleri(callout) bulmak 
print("Calloutları bul:", [w for w in text6 if w.startswith('@')])