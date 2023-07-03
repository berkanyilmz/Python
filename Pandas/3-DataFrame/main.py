import pandas as pd

if __name__ == '__main__':

    veri = {
        'kisi' : ['batuhan', 'burcin', 'deniz'],
        'yas' : [20, 26, 23]
    }

    # DataFrame() : Veriyi DataFrame nesnesine yükler
    df = pd.DataFrame(veri)
    print(df)

    print("\n Satır bulma")
    # loc, bir veya daha fazla satır dönderir
    print(df.loc[0])
    print(df.loc[[1,2]])

    # Etiket oluşturulabilir
    print("\n Etiket oluşturma : ")
    etiketli_veri = pd.DataFrame(veri, index=['1.kisi', '2.kisi', '3.kisi'])
    print(etiketli_veri)
    print("etiketli_veri.loc['2.kisi'] : ", etiketli_veri.loc['2.kisi'])