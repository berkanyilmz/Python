import pandas as pd

if __name__ == '__main__':
    sayilar = [1, 4, 6]

    # Seriler, herhanig bir türden veriyi tutan tek boyutlu bir dizidir
    seri = pd.Series(sayilar)
    print(seri)

    print('indeks numarası ile erişme')
    # indeks numarasıyla erişilebilir
    print(seri[2])

    print('etiket oluşturma')
    # Etiket oluşturulabilir
    seri2 = pd.Series(sayilar, index=['a', 'b', 'c'])
    print(seri2)
    print(seri2['b'])

    print('sözlük ile oluşturma')
    # Sözlük ile oluşturulabilir
    gunler = {'1' : "pazartesi",
              '2' : 'sali',
              '3' : 'carsamba',
              '4' : 'persembe'}
    gunSerisi = pd.Series(gunler)
    print(gunSerisi)