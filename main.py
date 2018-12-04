import time
import random
from swagDictionary import SwagDictionary

n = 100000000000

for i in range(7,100):
    b = i
    M = b * int((100000 / b) - 1)
    m = b * int(-100000 / b)
    d = SwagDictionary(M,m,b)
    t = 0
    for t in range(0, 15):
        random.seed(t)
        start = time.time()
        for j in range(0,1000):
            d.insert(n / 2 - random.random()%n, n / 2 - random.random()%n)
        t = t + time.time() - start
    t = t / 15
    print (str(b) + "\t:\t" +str(t))
