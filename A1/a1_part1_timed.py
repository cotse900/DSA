# Assignment 1 part 1
# Student: Chungon Tse
# Date: 1 Mar 2023
# Step 1
# I am borrowing the DSA456 course website's sorting algorithms but added lines for counting operations.
import random
import time


def bubble_sort(my_list):
    n = len(my_list)
    count = 0
    for x in range(n):
        for y in range(n - x - 1):
            if my_list[y] > my_list[y + 1]:
                my_list[y], my_list[y + 1] = my_list[y + 1], my_list[y]
                count += 4  # 3 swap 1 comparison
    # return my_list
    return count


def selection_sort(my_list):
    n = len(my_list)
    count = 0
    for x in range(n - 1):
        min_idx = x
        for y in range(x + 1, n):
            count += 1
            if my_list[y] < my_list[min_idx]:
                min_idx = y
        if min_idx != x:
            my_list[min_idx], my_list[x] = my_list[x], my_list[min_idx]
            count += 1
    return count


def insertion_sort(my_list):
    n = len(my_list)
    count = 0
    for i in range(1, n):
        curr = my_list[i]  # store the first number in the unsorted part of
        # of array into curr
        j = i
        while j > 0 and my_list[j - 1] > curr:  # this loop shifts value within sorted part of array
            my_list[j] = my_list[j - 1]  # to open a spot for curr
            j -= 1
            count += 1
        my_list[j] = curr
        count += 1
    return count


# quick sort has 4 components including insertion sort with 3 args below


def quick_sort(mylist):
    recursive_quick_sort(mylist, 0, len(mylist) - 1)  # call recursive quicksort


def recursive_quick_sort(mylist, left, right, THRESHOLD=1000):
    count = 0
    if right - left <= THRESHOLD:
        count += insertion_sort_sublist(mylist, left, right)
    else:
        pivot_position = partition(mylist, left, right)
        count += recursive_quick_sort(mylist, left, pivot_position - 1)
        count += recursive_quick_sort(mylist, pivot_position + 1, right)

    return count


def partition(mylist, left, right):
    # choose a random index between left and right inclusive
    pivot_location = random.randint(left, right)

    # get the pivot
    pivot = mylist[pivot_location]

    # move the pivot out of the way by swapping with
    # last value of partition.  This step is crucial as pivot will
    # end up "moving" if we don't get it out of the way which will
    # lead to inconsistent results.
    mylist[pivot_location] = mylist[right]
    mylist[right] = pivot

    end_of_smaller = left - 1
    # count = 0  #
    # note the loop below does not look at pivot which is in mylist[right]
    for j in range(left, right):
        if mylist[j] <= pivot:
            end_of_smaller += 1
            mylist[end_of_smaller], mylist[j] = mylist[j], mylist[end_of_smaller]
            # count += 1  #

    # restore the pivot
    mylist[end_of_smaller + 1], mylist[right] = mylist[right], mylist[end_of_smaller + 1]

    # and return its location
    return end_of_smaller + 1


# insertion sort sublist is also counted separately from quick sort
def insertion_sort_sublist(mylist, left, right):
    n = right - left + 1
    count = 0
    for i in range(left + 1, right + 1):
        curr = mylist[i]  # store the first number in the unsorted part of
        # of array into curr
        j = i
        # this loop shifts value within sorted part of array to open a spot for curr
        while j > left and mylist[j - 1] > curr:
            mylist[j] = mylist[j - 1]
            j = j - 1
            count += 1
        mylist[j] = curr
        count += 1
    return count


def time_sort_algorithm(sort_algorithm, array):
    start_time = time.time()
    sort_algorithm(array)
    end_time = time.time()
    return end_time - start_time


def main():
    # variable = 100
    # my_list = [random.randint(1, variable) for _ in range(variable)]
    # instead of random, I just use a reversed list 10 to 1, 100 to 1... for the worst cases
    variable = 1000000
    mylist = list(range(variable, 0, -1))

    print("List size: " + str(variable))

    start_time = time.time()
    bubble_count = bubble_sort(mylist.copy())
    end_time = time.time()
    print(f"Operations by bubble sort: {bubble_count}")
    print(f"Time taken by bubble sort: {end_time - start_time:.6f} seconds")

    start_time = time.time()
    selection_count = selection_sort(mylist.copy())
    end_time = time.time()
    print(f"Operations by selection sort: {selection_count}")
    print(f"Time taken by selection sort: {end_time - start_time:.6f} seconds")

    start_time = time.time()
    insertion_count = insertion_sort(mylist.copy())
    end_time = time.time()
    print(f"Operations by insertion sort: {insertion_count}")
    print(f"Time taken by insertion sort: {end_time - start_time:.6f} seconds")

    start_time = time.time()
    insertion_sublist_count = insertion_sort_sublist(mylist.copy(), 0, len(mylist) - 1)
    end_time = time.time()
    print(f"Operations by insertion sublist sort: {insertion_sublist_count}")
    print(f"Time taken by insertion sublist sort: {end_time - start_time:.6f} seconds")

    # return count from the recursive quick sort
    start_time = time.time()
    quick_sort_count = recursive_quick_sort(mylist.copy(), 0, len(mylist) - 1)
    end_time = time.time()
    print(f"Operations by quick sort: {quick_sort_count}")
    print(f"Time taken by quick sort: {end_time - start_time:.6f} seconds")


if __name__ == "__main__":
    main()
