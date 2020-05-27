from abc import ABC
from collections.abc import Iterable, Sized
from typing import TypeVar, Iterator, Any

from dictionary.trees.binaryTree import BinaryNode
from ext.ia18.dictionary.Dictionary import Dictionary
from ext.ia18.dictionary.dictTrees.avlTree import AVLTree
from ext.ia18.dictionary.linkedListDictionary import LinkedListDictionary
from list.LinkedList import Record

Dict = TypeVar('Dict', bound='CloneableDictionary')


class CloneableDictionary(Dictionary, Sized, Iterable, ABC):
    """
    A cloneable dictionary that implements the
    `Dictionary`, `Sized`, and `Iterable` interfaces.
    """
    KEY_INDEX = 0
    VALUE_INDEX = 1

    def clone(self, other: Dict) -> 'CloneableDictionary':
        """
        Clones the dictionary by inserting each item from the `other` dictionary.
        """
        for pair in other:
            self.insert(pair[self.KEY_INDEX], pair[self.VALUE_INDEX])
        return self


class CloneableLinkedListDictionary(LinkedListDictionary, CloneableDictionary):
    """
    A cloneable dictionary that uses a linked list to store the items.
    """

    def __init__(self):
        super().__init__()
        self.size = 0

    def __len__(self) -> int:
        """
        Returns the number of items in the dictionary.
        """
        return self.size

    def __iter__(self) -> Iterator[tuple[Any, Any]]:
        """
        Returns an iterator over the items in the dictionary.
        """
        node: Record = self.theList.first
        while node is not None:
            yield node.elem
            node = node.next

    def insert(self, key: Any, value: Any) -> None:
        """
        Inserts a key-value pair into the dictionary.

        :param key: The key to insert.
        :param value: The value to insert.
        """
        super().insert(key, value)
        self.size += 1

    def delete(self, key: Any) -> None:
        """
        Deletes the item with the given key from the dictionary.
        """
        super().delete(key)
        if self.size > 0:
            self.size -= 1


class CloneableAVLTree(AVLTree, CloneableDictionary):
    """
    A cloneable dictionary that uses an AVL tree to store the items.
    """

    def __len__(self) -> int:
        """
        Returns the number of items in the dictionary.
        """
        return self.size()

    def __iter__(self) -> Iterator[tuple[Any, Any]]:
        """
        Returns an iterator over the items in the dictionary.
        """
        root: BinaryNode = self.tree.root
        if root is not None:
            yield from CloneableAVLTree._binary_node_iterator(root)

    @staticmethod
    def _binary_node_iterator(node: BinaryNode) -> Iterator[tuple[Any, Any]]:
        """
        Returns an iterator over the items in the subtree rooted at `node`.
        """
        if node.leftSon is not None:
            yield from CloneableAVLTree._binary_node_iterator(node.leftSon)
        yield node.info
        if node.rightSon is not None:
            yield from CloneableAVLTree._binary_node_iterator(node.rightSon)
