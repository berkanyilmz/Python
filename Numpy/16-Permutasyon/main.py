from numpy import random
import numpy as np

if __name__ == '__main__':

    # Permütasyon, değerlerin kendi arasında yer değiştirmesidir
    # İki yöntem vardır, shuffle(dizi) ve permutation(dizi)
    # shuffle(dizi) : Orjinal diziyi değiştirir
    # permutation(dizi) : Orjinal diziyi değiştirmez yeni dizi oluşturur
    
    dizi = np.array([1,2,3,4,5,6])

    print("Permutation metodu : ", random.permutation(dizi))
    random.shuffle(dizi)
    print("Shuffle metodu : ", dizi)