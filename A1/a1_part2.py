# Assignment 1 part 2
# Student: Chungon Tse
# Date: 1 Mar 2023
# I copied assignment 1 starter.py and then added code below. --Chungon
class SortedList:
    class Node:

        # Node is internal.  Feel free to add
        # to the argument list for its init function if you want
        # you can add additonal data members if you like
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

        # Sorted list is external, do not change its prototype.

    # you can add additional data members if you like
    def __init__(self):
        self.front = None
        self.back = None
        self.length = 0

    def insert(self, data):
        new_node = self.Node(data)
        # when empty
        if self.front is None:
            self.front = self.back = new_node
        # if data is less than front data, insert it to the front and make front as new node
        elif data <= self.front.data:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        # if data is greater than back data, insert it to the back and make back as new code
        elif data >= self.back.data:
            new_node.prev = self.back
            self.back.next = new_node
            self.back = new_node
        else:
            current = self.front.next
            while current.data < new_node.data:
                current = current.next
            current.prev.next = new_node
            new_node.prev = current.prev
            current.prev = new_node
            new_node.next = current
        self.length += 1

    def remove(self, data):
        current = self.front
        while current is not None and current.data != data:
            current = current.next
        if current is None:
            return False
        elif current.data is None:
            self.front = current.next
        else:
            current.prev.next = current.next
        if current.next is None:
            self.back = current.prev
        else:
            current.next.prev = current.prev
        return True

    def is_present(self, data):
        current = self.front
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def __len__(self):
        return self.length

    # The functions below called __iter__ and __reversed__
    # allows an external function to
    # iterate through your list.
    #
    # myll = SortedList()
    #
    # for i in myll:
    #     print(i)
    #
    # for i in reversed(myll):
    # 	  print(i)
    #
    # with each iteration, curr goes through only one step of the while loop
    # (ie you don't run it all at once..)
    # there are two versions of these function as sentinels nodes do
    # make a difference in terms of where you start and end
    # keep only the version you are using and erase the version you are
    # not using (or comment it out...)

    # NOTE: if you change the names of your data members, you need
    # to change them in the functions below or your tests won't pass.

    # This is the version you need if you do not use sentinels:
    def __iter__(self):
        curr = self.front
        while curr:
            yield curr.data
            curr = curr.next

    def __reversed__(self):
        curr = self.back
        while curr:
            yield curr.data
            curr = curr.prev

    # This is the version you need if you used sentinels:
    # def __iter__(self):
    #     curr = self.front.next
    #     while curr != self.back:
    #         yield curr.data
    #         curr=curr.next
    #
    # def __reversed__(self):
    #     curr = self.back.prev
    #     while curr != self.front:
    #         yield curr.data
    #         curr=curr.prev


