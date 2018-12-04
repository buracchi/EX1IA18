'''
This class is a kind of datastructured wich store the data
as a dictionary in a linked list until this list reach the
max number of element allowed, then the datastructure
switch in an AVL tree
'''

from codiceTutor.avlTree import AVLTree
from strutturaDati.LinkedListDictionarySon import LinkedListDictionarySon

class LinkedListAVLDictionaryHybrid:

    def __init__(self, maxLen):
        self.switchingLength = maxLen
        self.dataStructure = LinkedListDictionarySon()
    
    def insert(self, key, value):
        self.dataStructure.insert(key, value)
        if ((type(dataStructure) is LinkedListDictionarySon) and (dataStructure.size() >= switchingLength)):
            self.dataStructure = self.switchToAVL()

    def delete(self, key):
        self.dataStructure.delete(key)
        if ((type(dataStructure) is AVLTree) and (dataStructure.size() < switchingLength)):
            self.dataStructure = self.switchToLinkedList()

    def search(self, key):
        self.dataStructure.search(key)

    def switchToAVL(self):
            avl = AVLTree()
            #start of the shit
            current = self.dataStructure.theList.first
            while current is not None:
                key = current.elem[data.KEY_INDEX]
                value = current.elem[data.VALUE_INDEX]
                avl.insert(key, value)
                current = current.next
            #end of the shit
            return avl

    def switchToLinkedList(self, alberoAVL, key):
        linkedList = LinkedListDictionarySon()
        curr = alberoAVL.tree.root
        self.makeLinkedListLoop(linkedList, curr, alberoAVL)
        return linkedList


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
