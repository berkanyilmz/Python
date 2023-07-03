from numpy import random

# Poisson, Belirli bir zamanda bir olayın kaç kez olacağını tahmin etmeye yarar

if __name__ == '__main__':
    # poisson (lam=Görülme oranı, size=Dönen dizinin şekli)

    dizi = random.poisson(lam=2, size=5)
    print(dizi)