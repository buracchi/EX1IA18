import time
import random
from customDictionary import CustomDictionary
from fillCSV import FillCSV

'''
Caricare una lista di elementi casuali e testarla per ogni tipo
di struttura dictionary presa in esame.
Ripetere per n volte e confrontare le miedie dei tempi al
variare degli algoritmi e dei parametri
'''

x = 100         # numero di esecuzioni di ciascun test su cui fare la media

def input(s, n, z = 1):
    """
    :param s: seme che assicura che strutture di memoria differenti vengano testate con elementi identici
    :param n: numero di elemetni da generare
    :param z: indice di dispersione >=1
    :return:

    la probabilità che esistano due elementi identici nella lista è dello 0.001%
    I valori generati sono compresi nell'intervallo (- n * z * 500, n * z * 500)
    """
    random.seed(s)
    l = []
    for i in range (0, n):
        l.append(int(random.random() * z * n * 1000) - n * z * 500)
    return l

def testSwag(n, z, b, vM, vm):

    """
    :param n: numero di operazioni da effettuare
    :param z: indice di dispersione >=1
    :param b:
    :param vM: parametro per calcolare il massimo
    :param vm: parametro per calcolare il minimo
    :return:
    """
    M = b + b * int(vM / b)     # max
    m = b * int(vm / b)         # min
    elapsed = 0
    for i in range(0, x):           #   numero di test
        v = input(i, n, z)
        start = time.time()
        d = CustomDictionary(M, m, b)
        for j in range(0, n):
            d.insert(v[j], v[j])
        for j in range(0, n):
            d.search(v[j])
        for j in range(0, n):
            d.delete(v[j])
        elapsed += time.time() - start
    FillCSV(str(n), str(elapsed / x), str (b)+"./Data/customDictionaryUtilizzo")
    elapsed = 0
    d = CustomDictionary(M, m, b)
    for i in range(0, x):           #   numero di test
        v = input(i, n, z)
        start = time.time()
        for j in range(0, n):
            d.insert(v[j], v[j])
        for j in range(0, n):
            d.search(v[j])
        for j in range(0, n):
            d.delete(v[j])
        elapsed += time.time() - start
    FillCSV(str(n), str(elapsed / x), str (b)+"./Data/customDictionaryInsert")
    for i in range(0, x):           #   numero di test
        v = input(i, n, z)
        M = b + b * int(vM / b)     # max
        m = b * int(vm / b)         # min
        elapsed = 0
        start = time.time()
        d = CustomDictionary(M, m, b)
        for j in range(0, n):
            d.insert(v[j], v[j])
        for j in range(0, n):
            d.search(v[j])
        for j in range(0, n):
            d.delete(v[j])
        elapsed = elapsed + (time.time() - start)
    FillCSV(str(n), str(elapsed / x), str (b)+"./Data/customDictionarySearch")
    for i in range(0, x):           #   numero di test
        v = input(i, n, z)
        M = b + b * int(vM / b)     # max
        m = b * int(vm / b)         # min
        elapsed = 0
        start = time.time()
        d = CustomDictionary(M, m, b)
        for j in range(0, n):
            d.insert(v[j], v[j])
        for j in range(0, n):
            d.search(v[j])
        for j in range(0, n):
            d.delete(v[j])
        elapsed = elapsed + (time.time() - start)
    FillCSV(str(n), str(elapsed / x), str (b)+"./Data/customDictionaryDeleate")

def testDictionary(n):
    """
    :param n: numero di operazioni da effettuare
    :return:
    """
    elapsed = 0
    for i in range(0, x):
        v = input(i, n)
        start = time.time()
        d = {}
        for j in range(0, n):
            d[v[j]] = v[j]
        for j in range(0, n):
            d.get(v[j])
        for j in range(0, n):
            try:
                d.pop(v[j])
            except:
                None
        elapsed += time.time() - start
    FillCSV(str(n), str(elapsed / x), "./Data/pyDictionaryUtilizzo")
    elapsed = 0
    d = {}
    for i in range(0, x):
        v = input(i, n)
        start = time.time()
        for j in range(0, n):
            d[v[j]] = v[j]
        elapsed += time.time() - start
    FillCSV(str(n), str(elapsed / x), "./Data/pyDictionaryInsert")
    elapsed = 0
    for i in range(0, x):
        v = input(i, n)
        d = {}
        start = time.time()
        for j in range(0, n):
            d.get(v[j])
        elapsed += time.time() - start
    FillCSV(str(n), str(elapsed / x), "./Data/pyDictionarySearch")
    elapsed = 0
    for i in range(0, x):
        v = input(i, n)
        d = {}
        start = time.time()
        for j in range(0, n):
            try:
                d.pop(v[j])
            except:
                None
        elapsed += time.time() - start
    FillCSV(str(n), str(elapsed / x), "./Data/pyDictionaryDeleate")

if __name__ == "__main__":
    for i in range(2,5):
        testDictionary(10**i)
    '''
    print("primo test: range di max e min comprendono i valori delle key testate\n")
    z = 1
    for i in range(1,4):
        y = 10 * (10**i)
        print("test con\t" + str(y) + "\telementi\n")
        testSwag(6 + 2**i, 500 * y, -500 * y)

    print("secondo test: range di max e min comprendono i valori delle key testate\n")
    z = 100
    for i in range(1,4):
        print("test con\t" + str(y) + "\telementi\n")
        testSwag(6 + 2**i, 500 * y, -500 * y)
    '''
