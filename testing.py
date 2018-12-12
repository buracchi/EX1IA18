import time
import random
from customDictionary import CustomDictionary
from fillCSV import FillCSV

#Gli imput non possono essere identici!

'''
Caricare una lista di elementi casuali e testarla per ogni tipo
di struttura dictionary presa in esame.
Ripetere per n volte e confrontare le miedie dei tempi al
variare degli algoritmi e dei parametri
'''

def input(s):                               #la probabilità che esistano due elementi identici nella lista è dello 0.001%
    random.seed(s)
    l = []
    for i in range (0, y):
        l.append(int(random.random() * z * y * 1000) - y * z * 500)     # per y=100 ci sono circa 100000 elementi
    return l

def testSwag(v1, v2, v3):   # b è v1, M = b + b * int(v2 / b), m = b * int(v3 / b)
    t = 0
    for i in range(0, x):
        print("sto iniziando a scrivere")
        print(str(z) + "\n")
        v = input(i)
        b = v1
        M = b + b * int(v2 / b)
        m = b * int(v3 / b)
        print("caricamento\n")
        d = CustomDictionary(M, m, b)
        print("sto inziando a cacolare\n")
        start = time.time()
        for j in range(0, y):
            d.insert(v[j], v[j])
        for j in range(0, y):
            d.search(v[j])
        for j in range(0, y):
            d.delete(v[j])

        t = t + (time.time() - start)
    FillCSV(str (b), str(t), "customDictionary")
    print ("CustomDictionary\t" + "(b : " + str(b) + "\tmax : " + str(M) + "\tmin : " + str(m) + ")\t:\t" +str(t / x))

def testDictionary():
    t = 0
    for i in range(0, x):
        v = input(i)
        d = {}
        start = time.time()
        for j in range(0, y):
            d[v[j]] = v[j]
        for j in range(0, y):
            try:
                d.pop(v[j])
            except:
                None
        for j in range(0, y):
            d.get(v[j])
        t = t + (time.time() - start)
    print ("PyDictionary\t :\t\t\t" +str(t / x))

x = 1      #numero di test da fare
y = 100      #numero di elementi su cui opera l'array
z = 0.001

if __name__ == "__main__":

    print("media di " + str(x) +" prove sostenute con " + str(y) + " valori random identici tra test differenti.\n")
    print("valori utilizzati compresi tra: " + str(y * z * -500) + ", " + str(y * z * 500)+ "\n")
    testDictionary()
    for j in range(1, 4) :
        y = 100
        for i in range(8, 14):   # b è v1, M = b + b * int(v2 / b), m = b * int(v3 / b)
            y = 100*10**j
            z = 0.01
            testSwag(2 ** i, 500 * y*z, - 500 * y*z)  # molto vicino
            z = 0.10   # maggiore o uguale di 1!
            testSwag(2 **i, 50 * y*z, - 50 * y*z)   # molto lontano
