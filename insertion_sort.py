#! python3
# Implementation of the insertion sort algorithm.

def insertion_sort(A):
    for i in range(1, len(A)):
        # current value under examination held in a temporary variable
        temp = A[i]
        j = i - 1
        # move all values smaller than temp value and to the left of current
        # index one to the right
        while j >= 0 and A[j] > temp:
            A[j + 1] = A[j]
            j -= 1
        # assign temp value to the correct index determined in the last loop
        A[j + 1] = temp
    return A