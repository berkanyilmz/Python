import numpy as np

# DİZİ KOPYALAMA
# Kopyalamada, orijinal dizide yapılan değişiklikler kopya diziyi etkilemez
# Aynı şekilde kopya dizide yapılan değişikler orjinal diziyi etkilemez
# copy() -> Dizi kopyalama fonksiyonu

dizi = np.array([1, 2, 3])
x = dizi.copy()
x[0] = 5

print(dizi)
print(x)

# Görüntülemede, orjinal dizide yapılan değişiklikler görüntülenen diziyi etkiler,
# görüntülenen dizide yapılan değişiklikler de orjinal diziyi etkiler
# view() -> Dizi görüntüleme fonksiyonu

array = np.array([1, 2, 3])
y = array.view()
array[1] = 10
print(array)
print(y)

# base ->Dizi kopya mı görünüm mü kontrol eder.
# Dizi kopya ise 'None' dönderir değil ise orjinal diziyi ifade eder

print(x.base) # None
print(y.base) # [1 10 3]