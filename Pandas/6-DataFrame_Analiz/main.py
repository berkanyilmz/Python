import pandas as pd

if __name__ == "__main__":
     dosya = pd.read_csv('data.csv')

     # head(), üst taraftan başlayarak belirli sayıda satırı dönderir
     print("head() fonksiyonu : ")
     print(dosya.head(15))

     # tail(), alt taraftan başlayarak belirli sayıda satırı dönderir
     print('tail() fonksiyonu : ')
     print(dosya.tail(7))

     # info(), veri seti hakkında bilgileri gösterir
     print('info() fonksiyonu : ')
     print(dosya.info())