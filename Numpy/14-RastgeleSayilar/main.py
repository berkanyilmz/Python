from numpy import random
import numpy

if __name__ == '__main__':

    # rand() : 0-1 arasında float sayı oluşturur
    x = random.rand()
    print("Random float : ", x)

    float_dizi = random.rand(5) # Random float sayılardan oluşan, 5 elemanlı dizi oluşturur
    print("Float dizi : ", float_dizi)

    # randint(tavan_sayı) : 0-tavan sayı arasında tam sayı oluşturur
    i = random.randint(100)
    print("Random int : ", i)
    
    # Random sayılarla dizi oluşturulabilir
    dizi = random.randint(20, size=(5)) # 0-100 arasında rastgele tamsayılar ile 5 elemanlı dizi oluşturur
    print("Tek boyutlu dizi : ", dizi)

    dizi2b = random.randint(50, size=(4, 4)) # 4 satır, 4 sütundan oluşan random tamsayılarla oluşmuş bir dizi oluşturur
    print("2 boyutlu dizi : \n", dizi2b)

    # choice(dizi) : Dizi içerisinden rastgele bir değer seçer
    rastgele = random.choice([1,2,3,4,5,6,7])
    print("Rastgele sayı : ", rastgele)
    # size parametresi olur ise dizi içerisinden seçtiği değerler ile size boyutunda başka bir dizi oluşturur
    rastgele_dizi = random.choice([1,2,3,5,7,4], size=(4))
    print("Rastgele Dizi : ", rastgele_dizi)

