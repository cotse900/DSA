# DSA456V1A
# Lab 2
# Student: Chungon Tse
# ID: 154928188
# Date: 8 Feb 2023

def function1(number):
    total = 0  # 1

    for i in range(0, number):  # n+1
        x = (i + 1)  # 2n
        total += (x * x)  # 2n

    return total  # 1


'''function1 receives a certain number and computes a total as a return value. Assume n is the number of operations
required for things including iterations. To consider a general function T, we consider time complexity T(n).

In line 2, total = 0 counts as 1 time.
In line 4, i changes in every iteration of loop from index 0 to (n-1). i changes n times and the count is n.
range() is called once per loop execution for the loop to go through.
In line 5, every time in the loop, = and + operators run n times each.
In line 6, every time in the loop, += and * operators run n times each.
In line 8, total is returned at least once.
From the above, T(n) = 5n + 3
This is a linear function. As time progresses, the constant 3 will be insignificant, and generally we can also ignore 5,
leaving the general T(n) = O(n) for linear search. In addition, the upper bound would be Omega(1).
'''


def function2(number):
    return ((number) * (number + 1) * (2 * number + 1)) / 6  # 6+1


'''function2 also receives a number for returning a result of the above operations. *, +, *, *, +, and / are 6
operations. The return itself is 1 operation. T(n) = 7 and it is also O(1) with constant growth.'''


def function3(list):
    for i in range(0, len(list) - 1):  # (n - 1) + 1 + 1, i.e. n+1
        for j in range(0, len(list) - 1 - i):  # q + (n - 1) + 1 + 1 + (n - 1)
            if (list[j] > list[j + 1]):  # 2q
                tmp = list[j]  # q
                list[j] = list[j + 1]  # 2q
                list[j + 1] = tmp  # 2q


'''function3 is a bubble sort algorithm.
In line 2, the outer range for loop works through
index 0 to (length - 1). Assume n = len(list), and we count (n - 1) for this loop. Both range and len count once each.
Therefore, the count is (n + 1).
In line 3, the inner loop iterations are as follows:
(n - 1) - 0 + (n - 1) - 1 + ... (n - 1) - (n - 2)
= n(n - 1)/2 = q
In short, let this count be q.
In line 4, the comparison yields 2q operations for all [j] and [j + 1].
In line 5, the assignment yields q operations.
In line 6, the assignment yields q operations.
T(n) = n + 1 + q + n + 1 + n - 1 + 7q
= 3n + 8q + 1
= 3n + 8(n(n - 1)/2) + 1
= 3n + 4n^2 - 4n + 1
= 4n^2 - n + 1
Disregard 1, then we have 4n^2 - n. In the long run, then T(n) tends to be O(n^2). It is exponential growth.
'''


def function4(number):
    total = 1  # 1
    for i in range(1, number):  # (n - 1) + 1
        total *= (i + 1)  # (n - 1) * 3
    return total  # 1


'''function4 is a linear function.
In line 2, there is 1 operation.
In line 3, with a range for loop, there is (n - 1) iterations plus 1 operation of range().
In line 4, there are 3 operators for (n - 1) iterations.
In line 5, the return is 1 operation.
T(n) = 1 + (n - 1) + 1 + (n - 1)*3 + 1
= n + 1 + 3n - 3 + 1
= 4n - 1
So, T(n) tends to be O(n) with linear growth.
'''
