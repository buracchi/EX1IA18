from strutturaDati.linkedListAVLDictionaryHybrid import LinkedListAVLDictionaryHybrid

class SwagDictionary:

    def __init__(self, max, min, b):
        self.r = 6
        assert max > min, "il parametro max dev'essere maggiore del parametro min"
        assert b > self.r, "il parametro b dev'essere maggiore di " + str(self.r)
        assert not (max-min)%b, "max - min dev'essere un multiplo di b"
        self.max = max
        self.min = min
        self.b = b
        self.d = int(abs((max - min) / b))
        self.v = []
        for i in range(0, self.d+2):
            self.v.append(LinkedListAVLDictionaryHybrid(self.r))

    def getIndexFromKey(self, key):
        if key > self.max:
            i = self.d + 1
        elif key < self.min:
            i = self.d
        else:
            i = int((key - self.min) / self.b)
        return i

    def insert(self, key, value):
        i = self.getIndexFromKey(key)
        self.v[i].insert(key,value)

    def delete(self, key):
        i = self.getIndexFromKey(key)
        self.v[i].delete(key)

    def search(self, key):
        i = self.getIndexFromKey(key)
        return self.v[i].search(key)
