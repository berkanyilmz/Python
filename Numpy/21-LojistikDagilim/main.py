from numpy import random

#Lojistik, Büyümeyi tanımlamak için kullanılır

if __name__ == '__main__':
    # logistic(loc, scale, size)
    # loc = ortalama, zirvenin olduğu yer
    # scale = standart sapma, dağılımın düzlüğü

    dizi = random.logistic(loc=1, scale=2, size=5)
    print(dizi)