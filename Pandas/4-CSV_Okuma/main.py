import pandas as pd

# CSV(comma separated files) yani vigülle ayrılmış dosyalar

if __name__ == "__main__":
    dosya = pd.read_csv('data.csv')
    print(dosya.to_string())