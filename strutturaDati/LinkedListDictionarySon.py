from codiceTutor.linkedListDictionary import LinkedListDictionary


class LinkedListDictionarySon(LinkedListDictionary):

        def __init__(self):
            super().__init__()

        def size(self):
            length = 0
            current = self.theList.first
            while current is not None:
                length += 1
                current = current.next
            else:
                return length