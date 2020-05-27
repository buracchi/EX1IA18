import unittest
from cloneable_dict_utils import CloneableLinkedListDictionary, CloneableAVLTree


class CloneableLinkedListDictionaryTest(unittest.TestCase):
    def test_clone(self):
        dict1 = CloneableLinkedListDictionary()
        dict1.insert("key1", "value1")
        dict1.insert("key2", "value2")
        dict2 = CloneableLinkedListDictionary()
        dict2.clone(dict1)
        self.assertEqual(dict1.search("key1"), dict2.search("key1"))
        self.assertEqual(dict1.search("key2"), dict2.search("key2"))

    def test_iterator(self):
        d = CloneableLinkedListDictionary()
        d.insert('a', 1)
        d.insert('b', 2)
        d.insert('c', 3)
        d.insert('d', 4)
        iter_list = [(item[0], item[1]) for item in list(d)]
        self.assertEqual(iter_list, [('a', 1), ('b', 2), ('c', 3), ('d', 4)])

    def test_len(self):
        d = CloneableLinkedListDictionary()
        self.assertEqual(len(d), 0)
        d.insert('a', 1)
        self.assertEqual(len(d), 1)
        d.insert('b', 2)
        self.assertEqual(len(d), 2)
        d.delete('a')
        self.assertEqual(len(d), 1)


class CloneableAVLTreeTest(unittest.TestCase):
    def test_clone(self):
        dict1 = CloneableAVLTree()
        dict1.insert("key1", "value1")
        dict1.insert("key2", "value2")
        dict2 = CloneableAVLTree()
        dict2.clone(dict1)
        self.assertEqual(dict1.search("key1"), dict2.search("key1"))
        self.assertEqual(dict1.search("key2"), dict2.search("key2"))

    def test_iterator(self):
        d = CloneableAVLTree()
        d.insert('a', 1)
        d.insert('b', 2)
        d.insert('c', 3)
        d.insert('d', 4)
        iter_list = [(item[0], item[1]) for item in list(d)]
        self.assertEqual(iter_list, [('a', 1), ('b', 2), ('c', 3), ('d', 4)])

    def test_len(self):
        d = CloneableAVLTree()
        self.assertEqual(len(d), 0)
        d.insert('a', 1)
        self.assertEqual(len(d), 1)
        d.insert('b', 2)
        self.assertEqual(len(d), 2)
        d.delete('a')
        self.assertEqual(len(d), 1)


if __name__ == '__main__':
    unittest.main()
