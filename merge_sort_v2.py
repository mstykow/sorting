#! python3
# Another go at merge-sort

from math import inf

# Function to merge two already sorted arrays into one sorted array
def merge(A, B):
    C = A + B
    # Add sentinel value to the end of A and B
    A.append(inf)
    B.append(inf)
    i = j = 0
    for k in range(len(C)):
        if A[i] >= B[j]:
            C[k] = B[j]
            j += 1
        else:
            C[k] = A[i]
            i += 1
    return C

# Recursive implementation of merge-sort algorithm
def sort(A):
    if len(A) > 1:
        q = len(A) // 2
        B = sort(A[:q])
        C = sort(A[q:])
        return merge(B, C)
    else:
        return A