from numpy import random

# Ki Kare Testi, değerleri ölçülemeyen ve karşılaştırılamayan iki
# değişken arasındaki ilişkiyi ölçmeye yarayan istatiksel bir test

if __name__ == '__main__':      
    
    # chisquare(df, size)
    # df : Serbestlik derecesi
    
    dizi = random.chisquare(df=2, size=(3,4))
    print(dizi)