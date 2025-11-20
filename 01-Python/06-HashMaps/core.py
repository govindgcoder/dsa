class HashMap:
    def __init__(self):
        self.size = 100
        self.buckets = [[] for _ in range(self.size)]

    def div_hash(self, key) -> int:
        return key % self.size

    def put(self, key, data):
        index = self.div_hash(key)
        curr_bucket = self.buckets[index]
        present = False
        for i in curr_bucket:
            if i[0] == key:
                i[1] = data
                present = True
        if not present:
            curr_bucket.append([key, data])

    def get(self, key):
        index = self.div_hash(key)
        curr_bucket = self.buckets[index]
        present = False
        for i in curr_bucket:
            if i[0] == key:
                return i[1]
                present = True
        if not present:
            print("Not found\n")
            return -1


hm = HashMap()
hm.put(1, 100)
print(hm.get(1))
