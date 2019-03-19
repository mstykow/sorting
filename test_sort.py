#! python3

import random
from insertion_sort import insertion_sort
from shell_sort import shell_sort
from merge_sort import merge_sort
from quicksort import quicksort

array1 = [5,4,3,2]
array2 = [0]
array3 = [3, 0, -1, 1000]

array4 = random.sample(range(1, 1000), 400)
array5 = random.sample(range(1, 1000), 400)

array6 = [2,8,7,1,3,5,6,4]

def test_insertion_sort():
    assert insertion_sort(array1) == [2, 3, 4, 5], 'array1 did not sort correctly'
    assert insertion_sort(array2) == [0], 'array2 did not sort correctly'
    assert insertion_sort(array3) == [-1, 0, 3, 1000], 'array3 did not sort correctly'

def test_shell_sort():
    assert shell_sort(array4) == sorted(array4), 'array4 did not sort correctly'

def test_merge_sort():
    assert merge_sort(array5) == sorted(array5), 'array5 did not sort correctly'

def test_quicksort():
    assert quicksort(array6) == sorted(array6), 'array6 did not sort correctly'