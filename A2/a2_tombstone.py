# Assignment 2
# Student: Chungon Tse
# Date: 26 Mar 2023

class ChainingHash:

    def __init__(self, cap=32):
        self.cap = cap
        self.the_table = [[] for _ in range(self.cap)]
        self.length = 0

    def insert(self, key, value):
        self.length += 1
        idx = hash(key) % self.cap
        for record in self.the_table[idx]:
            if record[0] == key:
                self.length -= 1
                return False
        # load factor lambda = num_items / num_slots
        if self.length / self.cap > 1.0:
            self.grow()
        self.the_table[idx].append((key, value))
        return True

    def modify(self, key, value):
        h = hash(key) % self.cap
        for i in range(len(self.the_table[h])):
            if self.the_table[h][i][0] == key:
                self.the_table[h][i] = (key, value)
                return True
        return False

    def remove(self, key):
        k = hash(key) % self.cap
        for v in range(len(self.the_table[k])):
            if self.the_table[k][v][0] == key:
                del self.the_table[k][v]
                self.length -= 1
                return True
        return False

    def search(self, key):
        idx = hash(key) % self.cap
        for record in self.the_table[idx]:
            if record[0] == key:
                return record[1]
        return None

    def capacity(self):
        return self.cap

    def __len__(self):
        return self.length

    def grow(self):
        self.length = 1
        self.cap *= 2
        old_table = self.the_table
        self.the_table = [[] for _ in range(self.cap)]
        for record in old_table:
            for kv in record:
                self.insert(kv[0], kv[1])


class LinearProbingHash:  # tombstone

    def __init__(self, cap=32):
        self.cap = cap
        self.the_table = [None] * self.cap
        self.length = 0

    def insert(self, key, value):
        idx = hash(key) % self.cap
        self.length += 1
        while self.the_table[idx] is not None:
            if self.the_table[idx][0] == key:
                self.length -= 1
                return False
            idx = (idx + 1) % self.cap
        # load factor lambda = num_items / num_slots
        if self.length / self.cap > 0.7:
            self.grow()
        self.the_table[idx] = (key, value)
        return True

    def modify(self, key, value):
        idx = hash(key) % self.cap
        for i in range(self.cap):
            if self.the_table[idx] is None:
                return False
            elif self.the_table[idx][0] == key:
                self.the_table[idx] = (key, value)
                return True
            else:
                idx = (idx + 1) % self.cap
        return False

    # def remove(self, key):
    #     idx = hash(key) % self.cap
    #     tombstone_indices = []
    #     for i in range(self.cap):
    #         if self.the_table[idx] is None:
    #             for tombstone_idx in tombstone_indices:
    #                 if self.the_table[tombstone_idx][0] == key:
    #                     self.the_table[tombstone_idx] = ('#TOMBSTONE#', None)
    #                     self.length -= 1
    #                     return True
    #             return False
    #         elif self.the_table[idx][0] == key:
    #             self.the_table[idx] = ('#TOMBSTONE#', None)
    #             self.length -= 1
    #             return True
    #         elif self.the_table[idx][0] == '#TOMBSTONE#':
    #             tombstone_indices.append(idx)
    #         idx = (idx + 1) % self.cap
    #     return False
    def remove(self, key):
        idx = hash(key) % self.cap
        for i in range(self.cap):
            if self.the_table[idx] is None:
                return False
            elif self.the_table[idx][0] == key:
                self.the_table[idx] = ('#TOMBSTONE#', None)
                self.length -= 1
                return True
            else:
                idx = (idx + 1) % self.cap
        return False

    def search(self, key):
        for item in self.the_table:
            if item is not None:
                if item[0] == key and item[0] != '#TOMBSTONE#':
                    return item[1]
        return None

    def capacity(self):
        return self.cap

    def __len__(self):
        return self.length

    def grow(self):
        self.length = 1
        self.cap *= 2
        old_table = self.the_table
        self.the_table = [None] * self.cap
        for record in old_table:
            if record is not None and record[0] != '#TOMBSTONE#':
                self.insert(record[0], record[1])
