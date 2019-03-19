#! python3
# Implementation of quicksort algorithm

# Function to partition a given array A into three, possibly empty, sets of the form
# {values <= x}{x}{values >= x} and returning the index of the pivot point x which
# starts out to be the last value in the given array
def partition_idx(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

# Recursive definition of quicksort algorithm
def quicksort_idx(A, p, r):
    if p < r:
        q = partition_idx(A, p, r)
        quicksort_idx(A, p, q - 1)
        quicksort_idx(A, q + 1, r)

# Quicksort wrapper function
def quicksort(A):
    quicksort_idx(A, 0, len(A) - 1)
    return A