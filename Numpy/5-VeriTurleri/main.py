import numpy as np

# i -> Tam sayı
# c -> Complex float
# b -> Boole
# m -> Time delta
# u -> İşaretsiz tam sayı
# M ->Tarih-zaman
# f -> Float
# O -> Nesne
# S -> String
# V ->Diğer tür için sabit bellek yığını
# U -> Unicode string

# dtype -> Dizinin veri türünü dönderir

dizi = np.array([1,2,3])
print(dizi.dtype) #int32

string = np.array(['a', 'b', 'c'])
print(string.dtype) #U1

#dtype ile dizi türü tanımlayabiliriz
liste = np.array([1, 2, 3], dtype='S')
print(liste.dtype) #S1

sayilar = np.array([1, 2, 3], dtype='i4')
print(sayilar)
print(sayilar.dtype)

# astype(param) -> Dizinin kopyasını oluşturur ve veri türünü değiştirir. Veri türü, parametre olarak metoda geçirilebilir
Dizi = np.array([1.2, 3.4, 5.6])
print("Dizinin veri tipi : ", Dizi.dtype)
yeniDizi = Dizi.astype('i')
print("Dizinin yeni veri tipi : ", yeniDizi.dtype)
print("Eski dizinin veri tipi : ", Dizi.dtype)

