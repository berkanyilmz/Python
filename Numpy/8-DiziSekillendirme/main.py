import numpy as np

# reshape(satır, sütun) -> Diziyi yeniden şekillendirir
# !!!!! Matris yeniden şekillendirildiğinde aynı sayıda elemana sahip olmalıdır

arr = np.array([1,2,3,4,5,6,7,8,9,0])
print("Dizinin şekli", arr.shape)
print("Dizi : ", arr)


newarray = arr.reshape(2, 5) # 2 satır 5 sütundan oluşan bir dizi
print("Dizinin yeni şekli : ", newarray.shape)
print("Yeni Dizi : ", newarray)

array3d = arr.reshape(2, 5, 1) #Dizi 2 satır 5 sütundan oluşur ve her boyutta 1 eleman vardır
print("3D dizi : ", array3d)
