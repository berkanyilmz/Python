import numpy as np

# where() : Aratıland değerin indis değerlerini dönderir

if __name__ == '__main__':
    dizi = np.array([1, 2, 5, 6, 4, 8, 0, 1, 6, 4, 3, 2, 8])
    index = np.where(dizi == 2)
    print(index)
    
    x = np.where(dizi%2 == 0) # 2 ile bölümünden kalan 0 olan değerlerin indisini dönderir
    print(x)

    # searchsorted() : Dizide ikili arama yapar, eklenecek değerin dizinin sırasını
    # bozmadan hangi indise ekleneceğini dönderir

    dizi2 = np.array([2, 4, 6, 8])
    indis = np.searchsorted(dizi2, 5)
    print(indis) #2, yani dizinin sırası bozulmadna eklenmek isteniyorsa 2. indise eklenmeli
