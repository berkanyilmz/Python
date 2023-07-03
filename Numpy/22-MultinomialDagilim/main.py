from numpy import random

# Multinomial dağılım, çok terimli senaryoların sonuçlarını tahmin etmede kullanılır. Örneğin zar atma

if __name__ == '__main__':
    # multinomial(n, pvals, size)
    # n = Deneme sayısı
    # pvals = Her bir denemenin olasılık sonucu

    dizi = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
    print(dizi)