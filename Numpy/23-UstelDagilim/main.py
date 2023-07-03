from numpy import random

#Ustel Dağılım, bir sonraki olaya kadar geçen süreyi tanımlamak için kullanılır

if __name__ == '__main__':

    # exponential(scale, size)
    # scale=Oranın tersi
    
    dizi = random.exponential(scale=2, size=(3))
    print(dizi)