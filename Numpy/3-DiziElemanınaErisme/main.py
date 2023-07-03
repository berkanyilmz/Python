import numpy as np

# [](Köşeli parantez) ile dizi öğelerine erişilir
# Dizinin ilk indisi 0'dan başlar

dizi = np.array([1, 2, 3])
print(dizi[0]) #ilk eleman
print(dizi[1]) #ikinci eleman
print(dizi[2]) #üçüncü eleman

print("-"*10)

#Çok boyutlu dizilerde [ , ] şeklinde erişilir
dizi2 = np.array([[1,2,3], [4,5,6]])
print(dizi2[0, 1]) # 0. indisin 1. elemanı

#dizi3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
dizi3 = np.array(
    [
        [[1, 2], [3, 4]], #0. indis
        [[5, 6], [7, 8]] # 1. indis
    ]
)
print(dizi3[1,1,0]) #->7