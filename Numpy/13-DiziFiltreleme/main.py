import numpy as np

if __name__ == '__main__':
    dizi = np.array([1, 2, 3, 4])
    boolean = [True, False, False, True]

    #dizi, True değerlerine denk gelen değerleri dönerir
    print(dizi[boolean])

    filtre = dizi > 2 # --> Filtreleme dizisidir
    yeni_dizi = dizi[filtre]
    print(yeni_dizi)
