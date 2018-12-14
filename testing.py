import time
import random
from customDictionary import CustomDictionary

'''
Caricare una lista di elementi casuali e testarla per ogni tipo
di struttura dictionary presa in esame.
Ripetere per n volte e confrontare le miedie dei tempi al
variare degli algoritmi e dei parametri
'''

x = 100         # numero di esecuzioni di ciascun test su cui fare la media

def FillCSV(ascissa, ordinata, filename):
    file = open(filename + ".csv", "a")
    file.write(ascissa + ",\t" + ordinata + "\n")
    file.close()

def input(n, z = 1):
    """
    :param s: seme che assicura che strutture di memoria differenti vengano testate con elementi identici
    :param n: numero di elemetni da generare
    :param z: indice di dispersione >=1
    :return:

    la probabilità che esistano due elementi identici nella lista è dello 0.001%
    I valori generati sono compresi nell'intervallo (- n * z * 500, n * z * 500)
    """
    #random.seed(s)
    #l = []
    #for i in range (0, n):
        #l.append(int(random.random() * z * n * 1000) - n * z * 500)
    return int(random.random() * z * n * 1000) - n * z * 500

def testSwag(n, z, b, vM, vm):
    """
    :param n: numero di operazioni da effettuare
    :param z: indice di dispersione >=1
    :param b:
    :param vM: parametro per calcolare il massimo
    :param vm: parametro per calcolare il minimo
    :return:
    """
    elapsed = 0
    for i in range(0, x):
        random.seed = i
        start = time.time()
        d = CustomDictionary(b + b * int(vM / b), b * int(vm / b), b)
        for j in range(0, n):
            d.insert(input(n, z), input(n, z))
        for j in range(0, n):
            d.search(input(n, z))
        for j in range(0, n):
            d.delete(input(n, z))
        elapsed += time.time() - start
    FillCSV(str(n), str(elapsed / x), "./Data/Utilizzo"+str(z == 1)+"CustomDictionary")
    d = CustomDictionary(b + b * int(vM / b), b * int(vm / b), b)
    elapsed = 0
    for i in range(0, x):
        random.seed = i
        start = time.time()
        for j in range(0, n):
            d.insert(input(n, z), input(n, z))
        elapsed += time.time() - start
    FillCSV(str(n), str(elapsed / x), "./Data/Insert"+str(z == 1)+"customDictionary")
    elapsed = 0
    for i in range(0, x):
        random.seed = i
        start = time.time()
        for j in range(0, n):
            d.search(input(n, z))
        elapsed += time.time() - start
    FillCSV(str(n), str(elapsed / x), "./Data/Search"+str(z == 1)+"customDictionary")
    elapsed = 0
    for i in range(0, x):
        random.seed = i
        start = time.time()
        for j in range(0, n):
            d.delete(input(n, z))
        elapsed += time.time() - start
    FillCSV(str(n), str(elapsed / x), "./Data/Deleate"+str(z == 1)+"customDictionary")

def testYolo(n, z, b, vM, vm):
    """
    :param n: numero di operazioni da effettuare
    :param z: indice di dispersione >=1
    :param b:
    :param vM: parametro per calcolare il massimo
    :param vm: parametro per calcolare il minimo
    :return:
    """
    elapsed = 0
    for i in range(0, x):
        random.seed(i)
        start = time.time()
        d = CustomDictionary(b + b * int(vM / b), b * int(vm / b), b)
        for j in range(0, n):
            d.insert(input(n, z), input(n, z))
        for j in range(0, n):
            d.search(input(n, z))
        for j in range(0, n):
            d.delete(input(n, z))
        elapsed += time.time() - start
    FillCSV(str(b), str(elapsed / x), "./Data/Range ("+str(vm)+","+str(vM)+")-UtilizzoCustomDictionary")

def testDictionary(n):
    """
    :param n: numero di operazioni da effettuare
    :return:
    """
    elapsed = 0
    for i in range(0, x):
        random.seed = i
        start = time.time()
        d = {}
        for j in range(0, n):
            d[input(n)] = input(n)
        for j in range(0, n):
            d.get(input(n))
        for j in range(0, n):
            try:
                d.pop(input(n))
            except:
                None
        elapsed += time.time() - start
    FillCSV(str(n), str(elapsed / x), "./Data/UtilizzoPyDictionary")
    elapsed = 0
    d = {}
    for i in range(0, x):
        random.seed = i
        start = time.time()
        for j in range(0, n):
            d[input(n)] = input(n)
        elapsed += time.time() - start
    FillCSV(str(n), str(elapsed / x), "./Data/InsertPyDictionary")
    elapsed = 0
    for i in range(0, x):
        random.seed = i
        d = {}
        start = time.time()
        for j in range(0, n):
            d.get(input(n))
        elapsed += time.time() - start
    FillCSV(str(n), str(elapsed / x), "./Data/SearchPyDictionary")
    elapsed = 0
    for i in range(0, x):
        random.seed = i
        d = {}
        start = time.time()
        for j in range(0, n):
            try:
                d.pop(input(n))
            except:
                None
        elapsed += time.time() - start
    FillCSV(str(n), str(elapsed / x), "./Data/DeleatePyDictionary")

if __name__ == "__main__":
    print("primo test: PyDictionary\n")
    for i in range(2,5):
        testDictionary(10**i)
    print("secondo test: Custom dictionary, range di max e min comprendono i valori delle key testate\n")
    for j in range(2,5):
        testSwag(10**j, 1, 1024, 500 * 10**j, -500 * 10**j)
    print("terzo test: Custom dictionary, range di max e min comprendono i valori delle key testate\n")
    for j in range(2,5):
        testSwag(10**j, 1000, 1024, 500 * 10**j, -500 * 10**j)
    #print("quarto test: Custom dictionary, b ottimale\n")
    '''
    Test che misura l'efficienza della struttura dati per 1000 inserimenti tra vari range
    con b che varia tra le potenze di 2
    '''
    '''
    for i in range(2,5):
        for j in range(7,19):
            testYolo(1000, 1, 2**j, 500 * 10**i, -500 * 10**i)
        print(str(i)-1+"/3")
    '''
