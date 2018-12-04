from codiceTutor.avlTree import AVLTree
from strutturaDati.LinkedListDictionarySon import LinkedListDictionarySon

'''
This class is a kind of datastructured wich store the data
as a dictionary in a linked list until this list reach the
max number of element allowed, then the datastructure
switch in an AVL tree
'''

class LinkedListAVLDictionaryHybrid:

    def __init__(self, r):
        self.switchingLength = r
        self.data = LinkedListDictionarySon()
    
    def insert(self, key, value):
        self.data.insert(key, value)
        if ((type(data) is LinkedListDictionarySon) and (data.size() >= r)):
            self.data = self.switchToAVL()

    def delete(self, key):
        self.data.delete(key)
        if ((type(data) is AVLTree) and (data.size() < r)):
            self.data = self.switchToLinkedList()

    def search(self, key):
        self.data.search(key)

    def switchToAVL(self):
            avl = AVLTree()
            current = self.data.theList.first
            while current is not None:
                key = current.elem[data.KEY_INDEX]
                value = current.elem[data.VALUE_INDEX]
                avl.insert(key, value)
                current = current.next
            return avl

    def switchToLinkedList(self, alberoAVL, key):
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
