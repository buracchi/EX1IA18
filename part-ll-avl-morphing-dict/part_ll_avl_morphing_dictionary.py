"""
    Authors: Fabio Buracchi, Danilo D'Amico
    Date of creation: 04/12/2018

    This module contains an implementation of a dictionary that
    handles key-value pairs where the keys are integers partitioned
    into a fixed number of blocks, each associated with a
    linked list or AVL tree depending on its size.
"""
from typing import Any

from cloneable_dict_utils import CloneableLinkedListDictionary, CloneableAVLTree
from ext.ia18.dictionary.Dictionary import Dictionary
from morphing_dictionary import MorphingDictionary


class PartitionedLinkedListAVLMorphingDictionary(Dictionary):

    def __init__(self, max: int, min: int, b: int):
        self.r: int = 6
        self.v: list[MorphingDictionary] = []
        assert max > min, "il parametro max dev'essere maggiore del parametro min"
        assert b > self.r, "il parametro b dev'essere maggiore di " + str(self.r)
        assert not (max - min) % b, "max - min dev'essere un multiplo di b"
        self.max = max
        self.min = min
        self.b = b
        self.d = int(abs((max - min) / b))
        for _ in range(0, self.d + 2):
            self.v.append(MorphingDictionary(self.r, CloneableLinkedListDictionary, CloneableAVLTree))

    def insert(self, key: int, value: Any) -> None:
        """
        AvlTree: O(log(n)), O(1) nel caso i appartenga ai primi d elementi dell'array
        LinkedListDictionary: O(1)

        :param key, value:
        """

        i = self._get_block_index_from_key(key)
        self.v[i].insert(key, value)

    def delete(self, key: int) -> None:
        """
        AvlTree: O(log(n)), O(1) nel caso i appartenga ai primi d elementi dell'array
        LinkedListDictionary: O(1)

        :param key:
        """
        i = self._get_block_index_from_key(key)
        self.v[i].delete(key)

    def search(self, key: int) -> Any:
        """
        AvlTree: O(log(n)), O(1) nel caso i appartenga ai primi d elementi dell'array
        LinkedListDictionary: O(1)
        """
        i = self._get_block_index_from_key(key)
        return self.v[i].search(key)

    def _get_block_index_from_key(self, key: int) -> int:
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
