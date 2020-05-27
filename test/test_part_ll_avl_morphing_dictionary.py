import unittest
from part_ll_avl_morphing_dictionary import PartitionedLinkedListAVLMorphingDictionary


class TestPartitionedLinkedListAVLMorphingDictionary(unittest.TestCase):

    def test_insert_and_search(self):
        d = PartitionedLinkedListAVLMorphingDictionary(100, 0, 10)
        d.insert(5, "a")
        d.insert(15, "b")
        d.insert(25, "c")
        d.insert(35, "d")
        d.insert(45, "e")
        self.assertEqual(d.search(5), "a")
        self.assertEqual(d.search(15), "b")
        self.assertEqual(d.search(25), "c")
        self.assertEqual(d.search(35), "d")
        self.assertEqual(d.search(45), "e")
        self.assertIsNone(d.search(55))

    def test_insert_and_delete(self):
        d = PartitionedLinkedListAVLMorphingDictionary(100, 0, 10)
        d.insert(5, "a")
        d.insert(15, "b")
        d.insert(25, "c")
        d.insert(35, "d")
        d.insert(45, "e")
        d.delete(15)
        d.delete(35)
        self.assertEqual(d.search(5), "a")
        self.assertEqual(d.search(25), "c")
        self.assertEqual(d.search(45), "e")
        self.assertIsNone(d.search(15))
        self.assertIsNone(d.search(35))


if __name__ == '__main__':
    unittest.main()
