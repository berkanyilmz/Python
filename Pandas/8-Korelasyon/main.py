import pandas as pd

if __name__ == '__main__':
    # corr() : sütunlar arasındaki ilişkiyi bulur
    dosya = pd.read_csv('data.csv')
    korelasyon = dosya.corr()
    print("Korelasyon : \n", korelasyon)

    # Sonuç 1 ise, 1'e 1 ilişki olduğu anlamına gelir. Aralarında mükemmel bir ilişki vardır