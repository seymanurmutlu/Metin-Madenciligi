#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 18:51:44 2020

@author: seyma
"""

import pandas as pd

time_sentences = ["Pazartesi:  14:45'te doktor ile randevu.", 
                  "Salı: 11:30'da diş hekimi ile randevu.",
                  "Çarşamba: 19:00 basketbol maçı!",
                  "Perşembe: En geç 23:15'te eve dön.",
                  "Cuma: 08:10'da trene bin, 09:00'da in."]

df = pd.DataFrame(time_sentences, columns=['text'])
print(df,"\n")

# df['text'] her satırın uzunluğunu bul
print( df['text'].str.len() ,"\n")

# df['text'] her satırdaki kelime sayısını bul
print( df['text'].str.split().str.len() ,"\n")

# hangi satırlarda 'randevu' geçtiğini bul
print( df['text'].str.contains('randevu') ,"\n")

#her satırda kaç sayı karakteri geçtiğini bul
print( df['text'].str.count(r'\d') ,"\n")

#her satırdaki sayı karakterlerini bul ve yazdır.
print( df['text'].str.findall(r'\d') ,"\n")

#her satırdaki saat ve dakikaları bulup grupla
print( df['text'].str.findall(r'(\d?\d):(\d\d)') ,"\n")

#türkçe günler için uyarla
#her satırdaki saat ve dakikaları bulup grupla
#print( df['text'].str.replace(r'\w+day\b', '???') ,"\n")

#her satırdaki saat ve dakikaları bulup grupla
#print( df['text'].str.replace(r'(\w+day\b)', lambda x: x.groups()[0][:3]) ,"\n")

#Çıkarılan grupların ilk eşleşmesinden yeni sütunlar oluştur
print( df['text'].str.extract(r'(\d?\d):(\d\d)') ,"\n")
