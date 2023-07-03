import pandas as pd

if __name__ == "__main__":
    jsonDosya = pd.read_json('data.js')
    print(jsonDosya.to_string())