from numpy import random

# Uniform, Her olayın eşit gerçekleşme oranına sahip olduğu olasılığı tanımlamak için kullanılır

if __name__ == '__main__':

    #uniform(a,b,size)
    # a = Alt sınır - Varsayılan değer = 0.0
    # b = Üst sınır - Varsayılan değer = 1.0

    dizi = random.uniform(size=5)
    print(dizi)