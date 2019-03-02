#! python3
# Recursive implementation of the merge-sort algorithm. Following divide-and-conquer,
# we assume smaller parts of the overall problem have been solved and begin by
# writing a function to merge the smaller parts back into the larger whole.

from math import inf

# Given is an array A indexed from 0 to len(A) - 1 with two sub-arrays indexed from
# p to q and the other from q + 1 to r. Assuming the two sub-arrays have been sorted,
# the following function merges them back into A.
def merge_by_indices(A, p, q, r):
    # Create copies of each subarray.
    L = A[p:q + 1]
    R = A[q + 1:r + 1]
    # Adding a sentinel value to the end of each array to avoid needing to check for
    # when the end of a stack is reached.
    L.append(inf)
    R.append(inf)
    i = j = 0
    for k in range(p, r + 1):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

# Given an array A indexed from 0 to len(A) - 1, we are now ready to implement the
# algorithm for sorting a subarray of A indexed from p to r.
def merge_sort_by_indices(A, p, r):
    if p < r:
        # Divide subarray into two roughly equal pieces.
        q = (p + r) // 2
        merge_sort_by_indices(A, p, q)
        merge_sort_by_indices(A, q + 1, r)
        merge_by_indices(A, p, q, r)

def merge_sort(A):
    merge_sort_by_indices(A, 0, len(A) - 1)
    return A