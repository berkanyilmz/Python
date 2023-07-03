from numpy import random
import numpy as np

#Zipf dağılım, verileri zipf yasasına göre örneklemek için kullanılır

# Zipf yasası, Bir koleksiyonda n. ortak terim, en yaygın terimin 1/n katıdır

if __name__ == '__main__':

    # zipf(a, size)
    # a : Dağıtım parametresi

    dizi = random.zipf(a=2, size=(3,3))
    print(dizi)