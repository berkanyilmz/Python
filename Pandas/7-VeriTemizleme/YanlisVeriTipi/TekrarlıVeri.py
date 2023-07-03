import pandas as pd

if __name__ == '__main__':
    # duplicated() : Tekrar eden verileri bulur
    # drop_duplicated() : Tekrar eden veriyi kaldırmak için kullanılır

    dosya = pd.read_csv('dirtydata.csv')
    yeni_dosya = dosya.drop_duplicates()
    print(yeni_dosya.to_string())