from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    # TODO - you fill in here.
    L, U = 0, len(A) - 1
    while L < U-1:
        M = (L + U)//2
        if A[M] < A[U]:
            U = M
        elif A[L] < A[M]:
            L = M
    return L if A[L] < A[U] else U


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
