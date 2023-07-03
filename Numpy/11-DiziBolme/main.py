import numpy as np

# array_split(dizi, bölünme sayısı) : Parametre olarak aldığı diziyi, bölünme sayısına göre böler

if __name__ == '__main__':
    dizi = np.array([1, 2, 3, 4, 5, 6])
    yeniDizi = np.array_split(dizi, 3)
    print("Yeni Dizi : ", yeniDizi)
    print("yeniDizi[0] : ", yeniDizi[0])
    print("yeniDizi[1] : ", yeniDizi[1])
    print("yeniDizi[2] : ", yeniDizi[2])

    dizi1, dizi2, dizi3 = np.array_split(dizi, 3)
    print("Dizi 1 : ", dizi1)
    print("Dizi 2 : ", dizi2)
    print("Dizi 3 : ", dizi3)

    # 2B DİZİLERİ DİLİMLEME

    dizi2b = np.array([
        [1, 2], [3, 4], [5, 6],
        [7, 8], [9, 10], [11, 12]
    ])

    yeniDizi2b = np.array_split(dizi2b, 3)
    print(yeniDizi2b)

    yeniDizi2b = np.array_split(dizi2b, 2, axis=1) # Diziyi sütun sütun böler
    print(yeniDizi2b)

    # hsplit(dizi, bölünme sayısı) : Diziyi sütun boyunca böler
    dizi_hsplit = np.hsplit(dizi2b, 2)
    print(dizi_hsplit)