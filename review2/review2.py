"""
# Q1
Reference: Binary Heaps, course notes
In a balanced binary search tree, each level of the tree contains around half the number of nodes of the level
below it. The tree is about log n where n is the number of nodes, as each step of the search custs the remaining
search space in half. The complexity therefore tends to be O(log n).

# Q2
Heap sort works by extracting the maximal element from a heap and placing it at the end of a given array.
For this reason, max_heap is useful for always storing the largest element at the root, and it sorts the array
in ascending order.

# Q3
A hash table. Each element is stored in an array like structure accessible by a hash function. This function
maps each phone number and allow lookups at O(1). We can use the phone nos as keys and store other info like names.
To search for someone by phone number, just access the table to find the name by computing hash.

# Q4
Yes, but not very efficient. We need to examine each element all along, and the linear search would be O(n log n)
where n is the list length.

## notes
- Depth first
- Preorder (node first)
- Inorder (node in the middle)
- Postorder (node last)
"""
