from codiceTutor.avlTree import AVLTree
from strutturaDati.LinkedListDictionarySon import LinkedListDictionarySon

class DataStructure:

    def __init__(self, r):
        self.r = r
    
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
