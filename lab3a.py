# DSA456V1A
# Lab 3
# Student: Chungon Tse
# ID: 154928188
# Date: 15 Feb 2023
# Part A
# function 1
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


# function 2
def linear_search(lst, key, index):
    if len(lst) == 0:
        return -1
    elif lst[0] == key:
        return index
    else:
        return linear_search(lst, key, index + 1)


# function 3
def binary_search(lst, key, start, end):
    if end is None:
        end = len(lst) - 1  # to cater for array index = 0 or 1
    if start > end:
        return -1
    mid = (start + end) // 2  # floor division
    if lst(mid) == key:
        return mid
    elif lst(mid) > key:
        return binary_search(lst, key, start, mid - 1)  # key in the lower end of array
    else:
        return binary_search(list, key, mid + 1, end)  # key in the upper end of array


# function 4
def tower_of_hanoi(num_disks, tower_1, tower_3, tower_2):
    if num_disks == 1:
        print(f"{tower_1} to {tower_3}")
    else:
        tower_of_hanoi(num_disks - 1, tower_1, tower_2, tower_3)
        print(f"{tower_1} to {tower_3}")
        tower_of_hanoi(num_disks - 1, tower_2, tower_3, tower_1)

