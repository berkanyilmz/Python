from numpy import random


if __name__ == '__main__':
    # normal(loc, scale, size)
    # loc : Ortalama, zirve değerin bulunduğu yer
    # scale : Standart Sapma : Grafik dağılımının ne kadar düz olduğudur
    # size : Döndürülen dizinin şekli

    dizi = random.normal(size=(3, 3))
    print(dizi)

    dizi2 = random.normal(loc=1, scale=2, size=(3,4))
    print(dizi2)