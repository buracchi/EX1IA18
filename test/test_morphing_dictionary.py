import unittest

from cloneable_dict_utils import CloneableLinkedListDictionary, CloneableAVLTree
from morphing_dictionary import MorphingDictionary


class TestMorphingDictionary(unittest.TestCase):
    def test_insert(self):
        d = MorphingDictionary(5, CloneableLinkedListDictionary, CloneableAVLTree)
        d.insert("a", 1)
        d.insert("b", 2)
        d.insert("c", 3)
        d.insert("d", 4)
        d.insert("e", 5)
        d.insert("f", 6)
        self.assertEqual(d.status, d.MorphingDictionaryStatus.FINAL)
        self.assertEqual(d.search("f"), 6)

    def test_delete(self):
        d = MorphingDictionary(5, CloneableLinkedListDictionary, CloneableAVLTree)
        d.insert("a", 1)
        d.insert("b", 2)
        d.insert("c", 3)
        d.insert("d", 4)
        d.insert("e", 5)
        d.delete("e")
        d.delete("d")
        d.delete("c")
        d.delete("b")
        d.delete("a")
        self.assertEqual(d.status, d.MorphingDictionaryStatus.INITIAL)

    def test_search(self):
        d = MorphingDictionary(5, CloneableLinkedListDictionary, CloneableAVLTree)
        d.insert("a", 1)
        d.insert("b", 2)
        d.insert("c", 3)
        d.insert("d", 4)
        d.insert("e", 5)
        self.assertEqual(d.search("a"), 1)
        self.assertEqual(d.search("e"), 5)
        self.assertEqual(d.search("f"), None)


if __name__ == '__main__':
    unittest.main()
