from numpy import random

#Rayleigh Dağılımı, sinyal işlemede kullanılır

if __name__ == '__main__':

    # rayleigh(scale, size)
    # scale = standart sapma
    
    dizi = random.rayleigh(scale=2, size=(3,3))
    print(dizi)