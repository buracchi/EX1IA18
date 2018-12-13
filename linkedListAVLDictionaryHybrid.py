'''
    File name: linkedListAVLDictionaryHybrid.py
    Authors: Fabio Buracchi, Danilo D'Amico
    Date created: 04/12/2018
    Date last modified: 08/12/2018
    Python Version: 3.7

    Questo modulo contiene l'implementazione
    di un dizionario con una lista collegata
    che viene sostituita da un albero AVL se
    supera un numero di elementi dato come
    parametro
'''

from Librerie.avlTree import AVLTree
from Librerie.linkedListDictionary import LinkedListDictionary

class LinkedListAVLDictionaryHybrid:

    def __init__(self, len):
        self.switchingLength = len
        self.dataStructure = LinkedListDictionary()

    """
    I tre metodi insert, delete e search del customDictionary sono presenti
    sia in AvlTree che in LinkedListDictionary, ma hanno implementazioni
    diverse.
    """
    
    def insert(self, key, value):
        """
        AvlTree: O(logn)
        LinkedListDictionary O(1)
        il costo sale a O(nlogn) nel caso si entri nella condizione descritta dall'if

        :param key, value:
        """
        self.dataStructure.insert(key, value)
        if (type(self.dataStructure) is LinkedListDictionary) and (self.dataStructure.size() >= self.switchingLength):
            self.dataStructure = self.switchToAVL()

    def delete(self, key):
        """
        AvlTree: O(logn)
        LinkedListDictionary O(n)
        il costo diventa O(n) nel caso si entri nella condizione descritta dall'if

        :param key:
        """

        self.dataStructure.delete(key)
        if (type(self.dataStructure) is AVLTree) and (self.dataStructure.size() < self.switchingLength):
            self.dataStructure = self.switchToLinkedList()

    def search(self, key):
        """
        AvlTree: O(logn)
        LinkedListDictionary O(n)
        """
        return self.dataStructure.search(key)


    def switchToAVL(self):
        """
        O(nlogn)

        :return AvlTree:
        """
        AVL = AVLTree()
        current = self.dataStructure.theList.first
        while current is not None:
            key = current.elem[self.dataStructure.KEY_INDEX]
            value = current.elem[self.dataStructure.VALUE_INDEX]
            AVL.insert(key, value)
            current = current.next
        return AVL

    def switchToLinkedList(self):
        """
        O(n)

        :return LinkedListDictionary:
        """
        linkedList = LinkedListDictionary()
        current = self.dataStructure.tree.root
        self.fillLinkedList(linkedList, current, self.dataStructure)
        return linkedList


    def fillLinkedList(self, linkedList, current, alberoAVL):
        """
        O(n)

        :param linkedList:
        :param current:
        :param alberoAVL:
        :return:
        """
        if current is None:
            return
        key = current.info[alberoAVL.KEY_INDEX]
        value = current.info[alberoAVL.VALUE_INDEX]
        linkedList.insert(key, value)
        self.fillLinkedList(linkedList, current.leftSon, alberoAVL)
        self.fillLinkedList(linkedList, current.rightSon, alberoAVL)
