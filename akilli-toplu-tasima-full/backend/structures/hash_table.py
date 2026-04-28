class HashTable:
    def __init__(self, size=101):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        total = 0
        for char in str(key):
            total += ord(char)

        return total % self.size

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for stored_key, value in bucket:
            if stored_key == key:
                return value

        return None