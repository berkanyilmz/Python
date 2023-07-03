import numpy as np

arr = np.array([1, 2, 3, 4, 5])

for i in arr:
    print(i)

print("* "*10)
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

for i in arr2d:
    for j in i:
        print(j)


# nditer -> Temelden çok ileri iterasyonlara kadar kullanılabilecek yardım fonksiyondur
print("- " * 10)
for i in np.nditer(arr2d):
    print(i)

print("+" * 10)
for i in np.nditer(arr2d[:, ::2]):
    print(i)

print(">" * 10)

#ndenumarete -> Dizinin elemanlarının satır ve sütun değerlerini gösterir

for i in np.ndenumerate(arr2d):
    print(i)