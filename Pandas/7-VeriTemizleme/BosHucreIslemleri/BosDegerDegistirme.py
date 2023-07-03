import pandas as pd

if __name__ == '__main__':
    # 2 - Boş değerleri değiştirme
    # fillna() fonksiyonu boş hücrelerin içine belirlediğimiz değerleri yazar
    # Bütün boş değerleri değiştirmek için dosya.fillna(değer, inplace=True). inplace true olursa orjinal veri seti değişir
    # Bir sütundaki boş değerleri değiştirmek için dosya['sütun_ismi'].fillna(değer, inplace)
    dosya = pd.read_csv('../YanlisVeriTipi/dirtydata.csv')
    yeni_dosya = dosya['Calories'].fillna(200)
    print(yeni_dosya.to_string())