from numpy import random

# Pareto Dagilim, küçük bir nesnenin bir büyük nesneye dağılımında kararlılık
# elde edildiği hallerde kullanılan bir sürekli olasılık dağılımıdır

if __name__ == '__main__':

    #pareto(a, size)
    # a : Şekil parametresi

    dizi = random.pareto(a=3, size=(3,3))
    print(dizi)