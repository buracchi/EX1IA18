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

x = 100         # numero di test da eseguire
y = 100         # numero di elementi su cui opera l'array
z = 1           # indice di dispersione

def input(s, n, z = 1):
    """
    :param s: seme che assicura che strutture di memoria differenti vengano testate con elementi identici
    :param n: numero di elemetni da generare
    :return:

    la probabilità che esistano due elementi identici nella lista è dello 0.001%
    I valori generati sono compresi nell'intervallo (- n * z * 500, n * z * 500)
    """
    random.seed(s)
    l = []
    for i in range (0, n):
        l.append(int(random.random() * z * n * 1000) - n * z * 500)
    return l

def testSwag(b, v2, v3):

    """

    :param b:
    :param v2: parametro per calcolare il massimo
    :param v3: parametro per calcolare il minimo
    :return:
    """
    elapsed = 0

    for i in range(0, x):           #   numero di test
        v = input(i)
        M = b + b * int(v2 / b)     # max
        m = b * int(v3 / b)         # min
        elapsed = 0
        start = time.time()
        d = CustomDictionary(M, m, b)
        for j in range(0, y):
            d.insert(v[j], v[j])
        for j in range(0, y):
            d.search(v[j])
        for j in range(0, y):
            d.delete(v[j])
        elapsed = elapsed + (time.time() - start)
    FillCSV(str(y), str(elapsed / x), str (b)+"../Data/customDictionaryUtilizzo")
    #print ("CustomDictionary\t" + "(b : " + str(b) + "\tmax : " + str(M) + "\tmin : " + str(m) + ")\t:\t" +str(tempoMedio))

def testDictionary(n):
    """
    :param n: numero di operazioni da effettuare
    :return:
    """
    t = 0
    elapsed = 0
    for i in range(0, x):
        v = input(i)
        start = time.time()
        d = {}
        for j in range(0, y):
            d[v[j]] = v[j]
        for j in range(0, y):
            d.get(v[j])
        for j in range(0, y):
            try:
                d.pop(v[j])
            except:
                None
        elapsed = elapsed + (time.time() - start)
    FillCSV(str(n), str(elapsed / x), "../Data/pyDictionaryUtilizzo")
    elapsed = 0
    d = {}
    for i in range(0, x):
        v = input(i)
        start = time.time()
        for j in range(0, y):
            d[v[j]] = v[j]
        elapsed = elapsed + (time.time() - start)
    FillCSV(str(n), str(elapsed / x), "../Data/pyDictionaryInsert")
    elapsed = 0
    for i in range(0, x):
        v = input(i)
        d = {}
        start = time.time()
        for j in range(0, y):
            d.get(v[j])
        elapsed = elapsed + (time.time() - start)
    FillCSV(str(n), str(elapsed / x), "../Data/pyDictionarySearch")
    elapsed = 0
    for i in range(0, x):
        v = input(i)
        d = {}
        start = time.time()
        for j in range(0, y):
            try:
                d.pop(v[j])
            except:
                None
        elapsed = elapsed + (time.time() - start)
    FillCSV(str(n), str(elapsed / x), "../Data/pyDictionaryDeleate")



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
