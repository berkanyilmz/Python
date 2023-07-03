import numpy as np

# Bir dizinin şekli, her boyuttaki eleman sayısıdır
# shape -> dizinin boyutunu demet şeklinde döndürür
# Geri dönen değerde, ilk değer satır sayısını, ikinci değer sütun sayısını gösterir
# Başka bir tanımda dizinin boyut sayısını ve eleman sayısını dönderir.
# Son değer eleman sayısını gösterirken önceki değerler, dizinin boyutunu gösterir

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)


arr2 = np.array([1,2,3,4], ndmin=5)
print(arr2.shape)