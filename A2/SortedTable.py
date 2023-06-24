class SortedTable:
    # packaging the key-value pair into one object
    class Record:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, cap=32):
        # this initializes a list of of capacity length with None
        self.the_table = [None for i in range(cap)]
        self.cap = cap

    def insert(self, key, value):
        if (self.search(key) != None):
            return False  # 1

        if (len(self) == self.cap):
            # increase the capacity if list is full
            new_table = [None for i in range(self.cap * 2)]  # 1
            for i in range(self.cap):  # n
                new_table[i] = self.the_table[i]  # n
            self.the_table = new_table  # 1
            self.cap *= 2  # 1

        self.the_table[len(self)] = self.Record(key, value)  # 1
        size = len(self)  # 1
        for i in range(0, size - 1):  # n
            for j in range(0, size - 1 - i):  # n^2
                if (self.the_table[j].key > self.the_table[j + 1].key):  # 1
                    tmp = self.the_table[j]  # n
                    self.the_table[j] = self.the_table[j + 1]  # n
                    self.the_table[j + 1] = tmp  # n
        return True  # 1

    # O(n) = 6n + 7 + n^2 = n^2 + 6n + 7

    def modify(self, key, value):
        i = 0  # 1
        while (i < len(self) and self.the_table[i].key != key):  # n
            i += 1  # 1
        if (i == len(self)):  # 1
            return False
        else:
            self.the_table[i].value = value  # 1
            return True  # 1

    # O(n) = 5 + n

    def remove(self, key):
        i = 0  # 1
        size = len(self)  # 1
        while (i < size and self.the_table[i].key != key):  # n
            i += 1  # 1
        if (i == size):  # 1
            return False  # 1
        while (i + 1 < size):
            self.the_table[i] = self.the_table[i + 1]  # n
            i += 1  # 1
        self.the_table[i] = None  # 1
        return True  # 1

    # O(n) = 8 + 2n

    def search(self, key):
        i = 0  # 1
        size = len(self)  # 1
        while i < size and self.the_table[i].key != key:  # n
            i += 1  # 1
        if i == size:  # 1
            return None  # 1
        else:
            return self.the_table[i].value  # 1

    # O(n) = 6 + n

    def capacity(self):
        return self.cap  # 1

    # O(n) = 1

    def __len__(self):
        i = 0  # 1
        count = 0  # 1
        while (i < len(self.the_table)):  # n
            if (self.the_table[i] != None):  # 1
                count += 1  # 1
            i += 1  # 1
        return count  # 1

    # O(n) = 6 + n
