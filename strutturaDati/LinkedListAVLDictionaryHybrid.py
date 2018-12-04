'''
This class is a kind of datastructured wich store the data
as a dictionary in a linked list until this list reach the
max number of element allowed, then the datastructure
switch in an AVL tree
'''

from Librerie.avlTree import AVLTree
from Librerie.linkedListDictionary import LinkedListDictionary

class LinkedListAVLDictionaryHybrid:

    def __init__(self, maxLen):
        self.switchingLength = maxLen
        self.dataStructure = LinkedListDictionary()
    
    def insert(self, key, value):
        self.dataStructure.insert(key, value)
        if ((type(self.dataStructure) is LinkedListDictionary) and (self.dataStructure.size() >= self.switchingLength)):
            self.dataStructure = self.switchToAVL()

    def delete(self, key):
        self.dataStructure.delete(key)
        if ((type(self.dataStructure) is AVLTree) and (self.dataStructure.size() < self.switchingLength)):
            self.dataStructure = self.switchToLinkedList()

    def search(self, key):
        return self.dataStructure.search(key)

    '''
    METODI BRUTTI CHE UN GIORNO CAMBIERO'
    '''

    def switchToAVL(self):
            avl = AVLTree()
            current = self.dataStructure.theList.first
            while current is not None:
                key = current.elem[self.dataStructure.KEY_INDEX]
                value = current.elem[self.dataStructure.VALUE_INDEX]
                avl.insert(key, value)
                current = current.next
            return avl

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
