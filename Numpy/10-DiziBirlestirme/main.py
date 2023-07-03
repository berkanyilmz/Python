import numpy as np

if __name__ == '__main__':
    dizi1 = np.array([1,2,3])
    dizi2 = np.array([4,5,6])

    #concatenate() => dizi birleştirmeye yarar.
    # Tek boyutlu dizileri sırlaı olarak birleştiri

    yeni_dizi = np.concatenate((dizi1, dizi2))
    print(yeni_dizi) # [1 2 3 4 5 6]

    #axis -> Satır veya sütun bazında işlem yapmaya yarar
    # 0 olur ise satır bazında işlem yapar
    # 1 olur ise sütun bazında işlem yapar
    arr1 = np.array([[1, 2, 3], [4, 5, 6]])
    arr2 = np.array([[7, 8, 9], [10, 11, 12]])
    new_arr = np.concatenate((arr1, arr2), axis=1)
    print(new_arr)

    #stack() -> Birleştirme ile aynıdır. Farkı, yeni bir eksen boyunca yapılır
    array = np.array([1, 2, 3])
    array2 = np.array([4, 5, 6])
    newArray = np.stack((array, array2), axis=1)
    print(newArray)

    # hstack() -> Satır boyunca yığın yapar
    dizi1 = np.array([1, 2, 3])
    dizi2 = np.array([4, 5, 6])
    yeniDizi = np.hstack((dizi1, dizi2))
    print(yeniDizi)

    # vstack() -> Sütun boyunca yığın yapar
    dizi1 = np.array([1, 2, 3])
    dizi2 = np.array([4, 5, 6])
    yeniDizi = np.vstack((dizi1, dizi2))
    print(yeniDizi)

    #dstack() -> Yükseklik boyunca yığın yapar
    dizi1 = np.array([1, 2, 3])
    dizi2 = np.array([4, 5, 6])
    yeniDizi = np.dstack((dizi1, dizi2))
    print(yeniDizi)