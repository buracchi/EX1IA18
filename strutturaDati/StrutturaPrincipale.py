"""
    Ingegneria degli Algoritmi, Progetto 1

    File name: StrutturaPrincipale.py
    Date created: 30/11/2018
    Date last modified:
    Python Version: 3.7

    Autori: Fabio Buracchi, Danilo D'Amico
"""

from codiceTutor.avlTree import AVLTree
from strutturaDati.LinkedListDictionarySon import LinkedListDictionarySon



class StrutturaPrincipale:

    def __init__(self, max, min, b):
        self.max = max
        self.min = min
        self.b = b
        self.d = int(abs((max - min) / b))
        self.v = self.creaArray()
        self.r = 6

    def creaArray(self):
        array = []
        for i in range(0, self.d + 2):
            array.append(LinkedListDictionarySon())
        return array

    def indiceArray(self, n):
        if n > self.max:
            indice = self.d + 1
        elif n < self.min:
            indice = self.d
        else:
            indice = int((n - self.min)/self.b)
        return indice

    def selectElementoArray(self, n):
        return self.v[self.indiceArray(n)]


    def insert(self, key, value):
        elementoArray = self.selectElementoArray(key)       # cella che indirizza la struttura relativa a key
        elementoArray.insert(key, value)

        if type(elementoArray) is LinkedListDictionarySon and elementoArray.size() == 6:
            indice = self.indiceArray(key)
            self.v[indice] = self.makeAVL(elementoArray)        # perchè non gli piace?

    def delete(self, key):
        elementoArray = self.selectElementoArray(key)   # errore: elementoArray = None
        elementoArray.delete(key)

        if type(elementoArray) is AVLTree and elementoArray.size() == 5:
            indice = self.indiceArray(key)
            self.makeLinkedList(elementoArray, key)  # neanche questo gli piace

    def search(self, key):
        elementoArray = self.selectElementoArray(key)
        elementoArray.search(key)

    def makeAVL(self, linkedList):
            avl = AVLTree()
            current = linkedList.theList.first
            while current is not None:
                currkey = current.elem[linkedList.KEY_INDEX]
                currvalue = current.elem[linkedList.VALUE_INDEX]
                avl.insert(currkey, currvalue)
                current = current.next
            return avl

    def makeLinkedList(self, alberoAVL, key):

        # creo una Linked List a partire da un albero AVL

        linkedList = LinkedListDictionarySon()
        curr = alberoAVL.tree.root
        self.makeLinkedListLoop(linkedList, curr, alberoAVL)
        indice = self.indiceArray(key)
        self.v[indice] = linkedList


    def makeLinkedListLoop(self, linkedList, curr, alberoAVL):

        # fuga
        if curr is None:
            return None

        # corpo
        key = curr.info[alberoAVL.KEY_INDEX]                      # key = alberoAVL.__key(curr)
        value = curr.info[alberoAVL.VALUE_INDEX]                          # value = alberoAVL.__value(curr)
        linkedList.insert(key, value)

        self.makeLinkedListLoop(linkedList, curr.leftSon, alberoAVL)
        self.makeLinkedListLoop(linkedList, curr.rightSon, alberoAVL)

"""
a = StrutturaPrincipale(102, 2, 25)
print(a.v)
a.insert(12, "prova")
a.insert(13, "provolone")
a.insert(14, "provoletto")
a.insert(15, "prada")
a.insert(16, "pronto")
a.insert(17, "prova costume")
print("ora stampo")
print(a.v)
a.v[0].print()
a.delete(12)
print("ora stampo")
print(a.v)
a.v[0].print()
a.ciao()
a.delete(13)
a.delete(14)
a.delete(15)
a.delete(16)
a.delete(17)
"""