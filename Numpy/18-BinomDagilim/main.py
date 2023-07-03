from numpy import random

# Binom, ikili olayların sonucunu belirlemeye yarar

if __name__ == '__main__':

    # binomial(n=Deneme Sayısı,
    #          p=Her bir denemenin olma olasılığı,
    #          size=Dönen dizinin şekli)

    dizi = random.binomial(n=4, p=0.5, size=4)
    print(dizi)