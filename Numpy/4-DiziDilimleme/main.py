import numpy as np

# [başlangıç: bitiş: kademe] -> Dizinin belirli bir kısmını seçer. Bitiş indeksi seçilmez

dizi = np.array([1,2,3,4,5,6])
print(dizi[1:5]) # 2, 3, 4, 5
print(dizi[0:5:2]) # Dizinin 0. indisi ile 5. indisi arasındaki elemanları ikişer aralıklarla seçer -> 1, 3, 5
print(dizi[2:]) # 2. indis ve sonrasını seçer

            # -----> NEGATİF DİLİMLEME <----- #

print("Negatif dilimleme", dizi[-4: -1]) # Sondan 4. eleman ile son elemana kadar seçer

# [::kademe] -> Dizinin bütün elemanlarını belirtilen kademede böler
print(dizi[::2]) # Bütün diziyi ikişer ikişer böler => 1,3,5

            # 2-B DİZİLERİ DİLİMLEME
# [indis, başlangıç:bitiş] -> indis, dizinin kaçıncı indisi olduğunu belirtir
dizi2b = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(dizi2b[1, 0:2]) # 1. indisdeki diziyi, 0-2 arasında böler
