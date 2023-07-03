import numpy as np

if __name__ == '__main__':

    x = [1,2,17]
    y = [4,7,3]

    # add() : İki diziyi toplar

    z = np.add(x,y)
    print(z)

    # subtract() : İki diziyi çıkarır

    z = np.subtract(x,y)
    print(z)

    # multiply() : İki diziyi çarpar

    z = np.multiply(x,y)
    print(z)

    # divide() : İki diziyi böler

    z = np.divide(x,y)
    print(z)

    # power() : Birinci dizideki değerlerin, ikinci dizideki değerlerine göre kuvvetini alır

    z = np.power(x,y)
    print(z)

    # mod() : İki diziyi böler ve kalanı dönderir

    z = np.mod(x,y)
    print(z)

    # divmod() : İki diziyi böler. Hem bölümü hem kalanı dönderir

    z = np.divmod(x,y)
    print(z)

    # absolute() : Dizideki değerlerin mutlak değerini dönderir

    mutlak = [-1, -4, 2]
    z = np.absolute(mutlak)
    print(z)