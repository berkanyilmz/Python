from numpy import random

if __name__ == '__main__':

    # choice() bir değer için olasılık belirlememizi sağlar
    dizi = random.choice([3,5,1,7], p=[0.2, 0.1, 0.3, 0.4], size=(50))
    # 3'nin gelme olasığı : 0.1
    # 5'in gelme olasılığı : 0.1
    # 1'in gelme olasılığı : 0.3
    # 7'nin gelme olasılığı : 0.4
    # !!!! Bütün olasılık değerlerinin toplamının 1 olması lazım
    
    print(dizi)
    
    dizi2 = random.choice([2,9,4,8], p=[0.2, 0.1, 0.7, 0.0], size=(20))
    # 0 = imkansız, 1 = kesin
    # Olasılık değeri 0 olan değer asla dizide olmaz
    # Olasılık değer 1 olan değer kesin dizide olur
    # 8 değeri dizi2'de asla olmaz
    print(dizi2)