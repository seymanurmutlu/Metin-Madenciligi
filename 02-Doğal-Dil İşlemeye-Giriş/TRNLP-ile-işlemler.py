from trnlp import *

text1 = "Uluslararası hukuk bir devletin diğer bir devlet veya devletlerle ve yahut bir devletin uluslararası örgütlerle ilişkilerini düzenleyen kamu hukuku dalıdır."
text2 = text1.split(" ")
print("text1 : ", text1,"\n")
print("text1'in uzunluğu : ",len(text1),"\n")

print("text1 kelime sayısı: ",len(text2),"\n")
print("text1 benzersiz kelimelerin sayısı: ",len(set(text2)),"\n")

#benzersiz kelimeler listesindeki ilk 10 kelimeyi bas.
print("text2'deki benzersiz kelimelerin 10'unu bas",list(set(text2))[:10],"\n")

##Kelimenin Kökünü Bulma

#TrnlpWord klasından bir obje türetilir
obj = TrnlpWord()

# .setword(str) fonksiyonu ile yeni kelime analizi yapılır
# cümledeki tüm kelimelerin kök / gövde ve eklerinin bulunması :
for t in text2:
    obj.setword(t)
    print(obj)

print("\n")

#STEMMING
for t in text2:
    obj.setword(t)
    #Kelimenin bulunan muhtemel gövdesini döndürür.
    print(obj.get_stem)

#LEMMATINAZITON

#TOKENIZATION
text3 = """Saçma ve Gereksiz Bir Yazı.
    Bakkaldan 5 TL'lik 2 çikola-
    ta al. 12.02.2018 tarihinde saat tam 15:45'te yap-
    malıyız bu işi. Tamam mı? Benimle esatmahmutbayol@gmail.com 
    adresinden iletişime geçebilirsin. Yarışta 1. oldu. Doç. Dr. 
    Esat Bayol'un(Böyle bir ünvanım yok!) yanından geliyorum.
    12 p.m. mi yoksa 12 a.m. mi? 100 milyon insan gelmiş! www.deneme.com.tr 
    adresinden sitemizi inceleyebilirsin. 24 Eylül 2018 Pazartesi günü ge-
    lecekmiş. 19 Mayıs'ı coşkuyla kutladık."""

#Metni boşluklardan parçalar.
print("Boşluklardan parçala :",whitespace_token(text3),"\n")

#Metni cümlelere parçalar.
obj = TrnlpToken()
obj.settext(text3)
print("Cümlelere ayır :", obj.phrasetoken)


