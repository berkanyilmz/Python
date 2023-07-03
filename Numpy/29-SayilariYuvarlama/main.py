from builtins import print

import numpy as np


if __name__ == '__main__':

    # trunc(), fix() : Ondalık kısımları kaldırır ve sıfıra en yakın noktalı sayısını dönderir
    x = [4.354, 5.7676, 1.768]
    y = [-3.467, -2.684]

    z = np.trunc(x)
    print(z)

    z = np.fix(y)
    print(z)

    # around() : Basamaktan veta ondalık sayıdan önce birer artış yapar
    sayi = np.around(2.678)
    print(sayi)

    # floor() : Ondalık sayıyıı en yakın alt tam sayıya yuvarlar
    z = np.floor(x)
    print(z)

    # ceil() : Ondalık sayıyı en yakın üst tam sayıya yuvarlar
    z = np.ceil(x)
    print(z)