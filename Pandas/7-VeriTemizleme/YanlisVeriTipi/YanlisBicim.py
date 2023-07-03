import pandas as pd

if __name__ == '__main__':
    # Veri setinde 'Date' kısmında 27. satırdaki veri yanlış yazılmış
    # to_date() fonksiyonu, hücredeki veriyi tarih biçimine dönüştürür
    dosya = pd.read_csv('dirtydata.csv')
    yeni_dosya = pd.to_datetime(dosya['Date'])
    print(yeni_dosya.to_string())