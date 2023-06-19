# DSA456V1A
# Lab 5
# Student: Chungon Tse
# ID: 154928188
# Date: 8 Mar 2023
# Singly linked list
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):  # -> bool
        return self.head is None

    def prepend(self, data):  # data: any
        self.head = Node(data, self.head)

    def append(self, data):
        if self.is_empty():
            self.head = Node(data)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(data)

    def insert_after(self, target, data):  # looks like insert between
        if target is None:
            return
        new_node = Node(data)
        new_node.next = target.next
        target.next = new_node

    def delete(self, target):  # bool
        if target is None or self.head is None:
            return False
        if self.head == target:
            self.head = self.head.next
            return True
        current = self.head
        while current.next is not None:
            if current.next == target:
                current.next = current.next.next
                return True
            current = current.next
        return False

    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            current = current.next
        return None

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def to_list(self):
        current = self.head
        lista = []
        while current is not None:
            lista.append(current.data)
            current = current.next
        return lista

    def print(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next


# testing below

list1 = SinglyLinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list1.head.next = e2

e2.next = e3

list1.prepend("Sun")
list1.insert_after(e3, "Thu")

list1.insert_after(list1.search("Thu"), "Fri")

print(list1.is_empty())

list1.insert_after(list1.search("Fri"), "Sat")
list1.insert_after(list1.search("Sat"), "sabato")
list1.delete(list1.search("Samstag"))  # no result for non-existent element
list1.delete(list1.search("sabato"))

list1.print()

print(list1.to_list())

print(list1.size())

"""False
Sun
Mon
Tue
Wed
Thu
Fri
Sat
['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
7
"""

"""Part B: big-O analysis
Overall, the singly linked list spends O(n) at worst for operations since it is likely to traverse the entire list of
linked nodes to find a certain element for a certain function. For a small list size, it may be a decent choice
since it is simple by design and the cost concern is minimal. Not so much for a larger size.

__init__() is O(1) for initializing the head. Likewise, is_empty() is O(1) checking for only 1 existing element.

prepend() at the head is essentially O(1) because this is adding the new node as the new head.
append(), at the back, is, by contrast, essentially O(n), placing the node only after n elements. 
insert_after() in other positions tends to be O(n) but still faster than append().

delete() can be from O(1) to O(n) depending on the target's position.
The same is true of search(), accessing an element by index, that can be from O(1) to O(n) depending on the 
element's position.

size(), to_list() and print() are all essentially O(n) since they need to access the entire list to know their
respective target values.

"""