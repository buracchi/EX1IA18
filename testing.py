import time
import random
from swagDictionary import SwagDictionary

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
        l.append(int(random.random() * y * 1000) - y * 500)
    return l

def testSwag(v1, v2, v3):
    t = 0
    for i in range(0, x):
        v = input(i)
        b = v1
        M = b + b * int(v2 / b)
        m = b * int(v3 / b)
        d = SwagDictionary(M,m,b)
        start = time.time()
        for j in range(0, y):
            d.insert(v[j], v[j])
        for j in range(0, y):
            d.delete(v[j])
        for j in range(0, y):
            d.search(v[j])
        t = t + (time.time() - start)
    print ("SwagDictionary\t" + "(b : " + str(b) + "\tmax : " + str(M) + "\tmin : " + str(m) + ")\t:\t" +str(t / x))

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

x = 10  #numero di test da fare
y = 10000 #numero di elementi su cui opera l'array

print("media di " + str(x) +" prove sostenute con " + str(y) + " valori random identici tra test differenti.\n")
print("valori utilizzati compresi tra: " + str(y * -500) + ", " + str(y * 500)+ "\n")
testDictionary()
for i in range(0, 6):
    for j in range(2, 8):
        testSwag(2**(i+3), 10**j, 0)
        testSwag(2**(i+3), 0, -10**j)
        testSwag(2**(i+3), 10**j, -10**j)
