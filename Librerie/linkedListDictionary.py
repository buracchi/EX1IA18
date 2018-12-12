"""
    File name: linkedListDictionary.py
    Author: Ovidiu Daniel Barba
    Date created: 14/11/2018
    Date last modified: 14/11/2018
    Python Version: 3.7

    Questo modulo contiene l'implementazione
    di un dizionario con una lista collegata
"""


from Librerie.LinkedList import ListaCollegata
from Librerie.Dictionary import Dictionary


class LinkedListDictionary(Dictionary):
    """
    Dizionario che mantiene una lista disordinata di coppie chiave valore.
    Ha le seguenti caratteristiche:
    - Inserimento degli elementi in O(1)
    - Ricerca di un elemento in O(n)
    - Cancellazione di un elemento in O(n)
    """
    KEY_INDEX = 0
    VALUE_INDEX = 1

    def __init__(self):
        self.theList = ListaCollegata()

    def print(self):
        self.theList.printOrdered()
    """
        METODI DEL DIZIONARIO
    """
    def search(self, k):
        """
        O(n)
        :param k:
        """
        current = self.theList.first
        while current is not None:
            currkey = current.elem[self.KEY_INDEX]
            if currkey == k:
                break  # trovata
            current = current.next
        else:
            return None  # non esiste
        
        return current.elem[self.VALUE_INDEX]

    def insert(self, key, value):
        """
        O(1)
        :param key:
        :param value:
        """
        pair = [key, value]
        self.theList.addAsLast(pair)
    
    def delete(self, key):
        """
        O(n)
        :param key:
        """
        current = self.theList.first
        pred = None
        while current is not None:
            currkey = current.elem[self.KEY_INDEX]
            if currkey == key:
                break
            pred = current
            current = current.next
        else:
            return None  # non esiste
        
        if pred is None:
            self.theList.popFirst()
        else:
            pred.next = current.next

    """
    Metodo aggiuntivo
    """

    def size(self):

        """
        O(n)
        """

        if self.theList.isEmpty():
            return 0
        else:
            length = 0
            current = self.theList.first
            while current is not None:
                length += 1
                current = current.next
            return length

