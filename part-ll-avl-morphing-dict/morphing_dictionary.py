from enum import Enum
from typing import Type, TypeVar, Any

from cloneable_dict_utils import CloneableDictionary
from ext.ia18.dictionary.Dictionary import Dictionary


class MorphingDictionary(Dictionary):
    """
    A dictionary that morphs between two different dictionary types
    when a certain capacity threshold is reached.
    """
    InitialDictType = TypeVar('InitialDictType', bound=CloneableDictionary)
    FinalDictType = TypeVar('FinalDictType', bound=CloneableDictionary)

    class MorphingDictionaryStatus(Enum):
        INITIAL = 0
        FINAL = 1

    def __init__(self, threshold: int, initial_dict_type: Type[InitialDictType], final_dict_type: Type[FinalDictType]):
        """
        Initializes a new MorphingDictionary instance.

        :param threshold: The threshold at which the dictionary will morph from the
                          initial dictionary type to the final dictionary type.
        :param initial_dict_type: The type of dictionary to use initially.
        :param final_dict_type: The type of dictionary to use after the threshold is reached.
        """
        self.threshold = threshold
        self.initial_dict_type = initial_dict_type
        self.final_dict_type = final_dict_type
        self.dictionary = self.initial_dict_type()
        self.status = self.MorphingDictionaryStatus.INITIAL

    def insert(self, key: Any, value: Any) -> None:
        """
        Inserts a key-value pair into the dictionary.

        :param key: The key to insert.
        :param value: The value to insert.
        """
        self.dictionary.insert(key, value)
        if self.status is self.MorphingDictionaryStatus.INITIAL and len(self.dictionary) >= self.threshold:
            old_dict = self.dictionary
            self.dictionary = self.final_dict_type()
            self.dictionary.clone(old_dict)
            self.status = self.MorphingDictionaryStatus.FINAL

    def delete(self, key: Any) -> None:
        """
        Deletes a key from the dictionary.

        :param key: The key to delete.
        """
        self.dictionary.delete(key)
        if self.status is self.MorphingDictionaryStatus.FINAL and len(self.dictionary) < self.threshold:
            old_dict = self.dictionary
            self.dictionary = self.initial_dict_type()
            self.dictionary.clone(old_dict)
            self.status = self.MorphingDictionaryStatus.INITIAL

    def search(self, key: Any) -> Any:
        """
        Searches for a key in the dictionary.

        :param key: The key to search for.
        :return: The value associated with the key, or None if the key is not found.
        """
        return self.dictionary.search(key)
