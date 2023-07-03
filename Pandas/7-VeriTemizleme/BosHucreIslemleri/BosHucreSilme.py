import pandas as pd

if __name__  == "__main__":
    # 1-Boş satırları kaldırma
    # 1 - Boş satırları kaldırma
    # dropna() fonksiyonu boş hücrenin olduğu satırı siler, orjinal veri setini değiştirmez
    # dropna(veri_seti, inplace=True) ile orjinal veri seti değiştirilebilir
    dosya = pd.read_csv('../YanlisVeriTipi/dirtydata.csv')
    yeni_dosya = dosya.dropna()
    print(yeni_dosya.to_string())