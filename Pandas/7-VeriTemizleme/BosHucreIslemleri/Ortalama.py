import pandas as pd

if __name__ == '__main__':
    # 3-Ortalama, ortanca değer ve mod
    # Ortalama : Tüm değerlerin toplamının, toplam değer sayısına bölümü
    # Ortanca, tüm değerler küçükten büyüğe sıralanır, boş hücreye ortanca değer yazılır
    # Mod, en sık görülen değer
    dosya = pd.read_csv('../YanlisVeriTipi/dirtydata.csv')
    ortalama = dosya['Calories'].mean()
    yeni_dosya = dosya['Calories'].fillna(ortalama)
    print("Ortalama : {}\n".format(ortalama), yeni_dosya.to_string())


    # Ortanca
    ortanca = dosya['Calories'].median()
    yeni_dosya = dosya['Calories'].fillna(ortanca)
    print("Ortanca : {}\n".format(ortanca), yeni_dosya.to_string())

    #Mod
    mod = dosya['Calories'].mode()[0]
    yeni_dosya = dosya['Calories'].fillna(mod)
    print("Mod : {}\n".format(mod), yeni_dosya.to_string())