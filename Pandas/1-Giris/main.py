import pandas as pd

if __name__ == '__main__':
     veriler = {
          'urun' : ['kalem', 'silgi', 'canta'],
          'fiyat' : [3,7,1]
     }

     # Dataframe, çok boyutlu tablolardır
     veriSeti = pd.DataFrame(veriler)
     print(veriSeti)

