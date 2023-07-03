import pandas as pd

if __name__ == '__main__':
    # 'Duration' sütununda 7. satırdaki süre yanlış yazılmış
    dosya = pd.read_csv('dirtydata.csv')

    # bu döngü 'Duration' sütununda 60'dan büyük değer var ise bu değeri 60 yapacaktır
    for i in dosya.index:
        if dosya.loc[i, "Duration"] > 60:
            dosya.loc[i, "Duration"] = 60

    print(dosya.to_string())