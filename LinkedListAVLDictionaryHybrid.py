'''
    File name: linkedListAVLDictionaryHybrid.py
    Authors: Fabio Buracchi, Danilo D'Amico (in ordine di importanza, non alfabetico)
    Date created: 04/12/2018
    Date last modified: 04/12/2018
    Python Version: 3.7

    Questo modulo contiene l'implementazione
    di un dizionario con una lista collegata
    che viene sostituita da un albero AVL se
    super un numero di elementi dato come
    parametro
'''

from Librerie.avlTree import AVLTree
from Librerie.linkedListDictionary import LinkedListDictionary

class LinkedListAVLDictionaryHybrid:

    def __init__(self, len):
        self.switchingLength = len
        self.dataStructure = LinkedListDictionary()
    
    def insert(self, key, value):
        self.dataStructure.insert(key, value)
        if (type(self.dataStructure) is LinkedListDictionary) and (self.dataStructure.size() >= self.switchingLength):
            self.dataStructure = self.switchToAVL()

    def delete(self, key):
        self.dataStructure.delete(key)
        if (type(self.dataStructure) is AVLTree) and (self.dataStructure.size() < self.switchingLength):
            self.dataStructure = self.switchToLinkedList()

    def search(self, key):
        return self.dataStructure.search(key)

    '''
    METODI BRUTTI CHE UN GIORNO CAMBIERO'
    '''

    def switchToAVL(self):
            AVL = AVLTree()
            current = self.dataStructure.theList.first
            while current is not None:
                key = current.elem[self.dataStructure.KEY_INDEX]
                value = current.elem[self.dataStructure.VALUE_INDEX]
                AVL.insert(key, value)
                current = current.next
            return AVL

    def switchToLinkedList(self):
        linkedList = LinkedListDictionary()
        current = self.dataStructure.tree.root
        self.fillLinkedList(linkedList, current, self.dataStructure)
        return linkedList


    def fillLinkedList(self, linkedList, current, alberoAVL):
        if current is None:
            return
        key = current.info[alberoAVL.KEY_INDEX]
        value = current.info[alberoAVL.VALUE_INDEX]
        linkedList.insert(key, value)
        self.fillLinkedList(linkedList, current.leftSon, alberoAVL)
        self.fillLinkedList(linkedList, current.rightSon, alberoAVL)
