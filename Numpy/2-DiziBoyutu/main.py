import numpy as np

#ndim -> Dizinin kaç boyutlu olduğunu gösterir

array1 = np.array([1,2,3])
array2 = np.array([[1,2,3], [4,5,6]])

print(array1.ndim)
print(array2.ndim)

#ndmin -> Dizinin boyutunu belirlemek için kullanılır

array3 = np.array([1,2], ndmin=3)

print(array3)
print("Dizinin boyutu : ", array3.ndim)