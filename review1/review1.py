# midterm sample Q1
# Write a python function that gets a list as an input and returns the number of unique elements in the list.
# def unique_count(mylist)

def unique_count(mylist):
    unique_set = set(mylist)
    return len(unique_set)


# test

mylist = [1, 2, 3, 3, 4, 4, 5]
print(unique_count(mylist))


# Q2
# Write a recursive implementation of bubble sort. To do this, you can run 1 pass of the bubble sort first and
# then send the remaining elements of the list to be sorted. Base case is when there is only 1 element in the list

def bubble_sort(my_list):
    bubble_sort_recursive(my_list, len(my_list))


def bubble_sort_recursive(my_list, n):
    if n == 1:
        return
    for p in range(n - 1):
        if my_list[p] > my_list[p + 1]:
            my_list[p], my_list[p + 1] = my_list[p + 1], my_list[p]
    bubble_sort_recursive(my_list, n - 1)


my_list = [5, 3, 8, 6, 7, 2]
bubble_sort(my_list)
print(my_list)

"""
Q3
bubble_sort(): O(1)
bubble_sort_recursive(): O(1)
with the range, bubble_sort_recursive() performs sorting for n-1 elements and it takes O(n)
In the if statement, bubble_sort_recursive() calls itself recursively with n-1 as the new size of the list.
This happens n times and the size reduces incrementally. It takes O(n^2) time.
Considered together, the entire algorithm takes O(n^3) time for this reason.
It is not better than non-recursive bubble sort which just takes O(n^2) normally for the worst case.
"""

"""
Q4
The outer loop runs n times. For each outer loop run, the inner loop runs up to the square root of num times.
Say, if num is 36, the square root is 6, and the inner loop runs from 2 to 6.
That is, T(n) = O(sqrt(n)).
Overall, the time complexity is O(n * sqrt(n)).

In general, sorting a list of size n can result in O(n log n) with algorithms like quicksort, mergesort, and heapsort.
Moreover, once n grows linearly, like by 2 times, then the printing time complexity will also grow at least linearly,
whereas with the sorting, growing of size logarithmically is of a slower rate.
That explains sorting a list of size n is generally faster than printing all prime numbers up to n.
"""

"""
Q5
T(n) = 1 + T(n/3) + 1 + T(n/3)
T(n) = 2 + 2T(n/3)
= 2*(2T(n/9) + 2)
= 2*2*T(n/9) + 2*2
= 2*2*2*T(n/27) + 2*2*2
= 2*2*2*2*T(n/81) + 2*2*2*2
= 2*2*2…*2T(1)+ 2*2*2*2…*2
= (A+1) * 2^ Log3(n)
As such, the time complexity is O(n^(2/3)) (linear)

Another proof would yield the result O(n^(log_3(2))) (logarithmic) which is not exactly the same but very close 
in value.

In the expansion you provided, you can see that the pattern is 2^k * T(n/3^k) + 2^(k+1), and the last term 
is 2^(log3(n)+1). Then, we can simplify this using the formula for the sum of a geometric series:

2^0 * T(n/3^0) + 2^1 + 2^2 + ... + 2^k = 2^(k+1) - 1

Solving for k, we get k = log3(n), and plugging this back into the equation gives us:

T(n) = 2^log3(n) * T(1) + 2^(log3(n)+1) - 1
= n^(log3(2)) * T(1) + 2 * n^(log3(2)) - 1

Since T(1) is a constant, we can drop it and obtain the big O notation O(n^(log3(2))).
"""

"""
Q6
Advantages of linked lists over arrays: Linked lists can easily grow or shrink as needed. Arrays must be allocated
ahead of time.
Insertion and deletion of elements in a linked list can be done in constant time. Arrays require such operations
by shifting elements for the sake of contiguous memory.
Linked lists use memory more efficiently since they only use memory for elements they do contain.
Linked lists are more flexible and may be used for different data structures. Arrays are one-dimensional sequences.

Disadvantages of linked lists over arrays: while arrays access elements faster at O(1) in contiguous memory while
linked lists require O(n) and memory is not contiguous.
Linked lists use more pointers than arrays.
Reversals take more time for linked lists than arrays.
"""


class LList:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.front = None
        self.back = None

    def insert(self, data):
        if self.front is None:
            self.front = self.back = LList.Node(data)
        else:
            self.back.next = LList.Node(data)
            self.back = self.back.next

    def clone_init(self, myLList):
        if myLList.front is None:
            self.front = None
            self.back = None
            return
        node = myLList.front
        while node is not None:
            self.insert(node.data)
            node = node.next

# create a new linked list instance
my_list = LList()

# add some nodes to the list
my_list.insert("I am elem1")
my_list.insert("I am elem2")
my_list.insert("I am elem3")

# clone the list
cloned_list = LList()
cloned_list.clone_init(my_list)

# print the original list
node = my_list.front
while node is not None:
    print(node.data)
    node = node.next

# print the cloned list
node = cloned_list.front
while node is not None:
    print(node.data)
    node = node.next
