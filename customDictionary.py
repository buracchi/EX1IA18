'''
    File name: customDictionary.py
    Authors: Fabio Buracchi, Danilo D'Amico
    Date created: 04/12/2018
    Date last modified: 08/12/2018
    Python Version: 3.7

    Questo modulo contiene l'implementazione
    di un dizionario personalizzato che gestisce
    multipli ibridi lista collegata/albero AVL in
    base a dei parametri max, min, b |
    (max-min)%b == 0.
'''

from LinkedListAVLDictionaryHybrid import LinkedListAVLDictionaryHybrid

class CustomDictionary:

    def __init__(self, max, min, b):
        self.r = 6
        assert max > min, "il parametro max dev'essere maggiore del parametro min"
        assert b > self.r, "il parametro b dev'essere maggiore di " + str(self.r)
        assert not (max-min)%b, "max - min dev'essere un multiplo di b"
        self.max = max
        self.min = min
        self.b = b
        self.d = int(abs((max - min) / b))
        self.v = []
        for i in range(0, self.d+2):
            self.v.append(LinkedListAVLDictionaryHybrid(self.r))

    def getIndexFromKey(self, key):
        """
        O(1)
        :param key:

        questo metodo consente di assegnare key
        all'indirizzo v[i] corrispondente
        """

        if key > self.max:
            i = self.d + 1
        elif key < self.min:
            i = self.d
        else:
            i = int((key - self.min) / self.b)
        return i

    """
    I tre metodi insert, delete e search del customDictionary derivano
    dalla classe LinkedListAVLDictionaryHybrid, pertanto hanno stessi
    costi e parametri nel caso peggiore, mentre nel caso ideale hanno
    costo in funzione di b, costante.
    """

    def insert(self, key, value):
        """
        AvlTree: O(logn), O(1) nel caso i appartenga ai primi d elementi dell'array
        LinkedListDictionary: O(1)

        :param key, value:
        """

        i = self.getIndexFromKey(key)
        self.v[i].insert(key, value)

    def delete(self, key):
        """
        AvlTree: O(logn), O(1) nel caso i appartenga ai primi d elementi dell'array
        LinkedListDictionary: O(1)

        :param key:
        """
        i = self.getIndexFromKey(key)
        self.v[i].delete(key)

    def search(self, key):
        """
        AvlTree: O(logn), O(1) nel caso i appartenga ai primi d elementi dell'array
        LinkedListDictionary: O(1)
        """
        i = self.getIndexFromKey(key)
        return self.v[i].search(key)
