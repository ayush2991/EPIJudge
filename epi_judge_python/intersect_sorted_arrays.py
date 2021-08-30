import inspect
from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    # TODO - you fill in here.
    i = 0
    j = 0
    intersect = []
    while i < len(A) and j < len(B):
        if A[i] > B[j]:
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            if intersect == [] or A[i] != intersect[-1]:
                intersect.append(A[i])
            i += 1
            j += 1
    return intersect


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
