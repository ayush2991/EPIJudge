from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    # TODO - you fill in here.
    L, U = 0, len(A) - 1
    index = -1
    while L<=U:
        M = (L+U)//2
        if A[M] > k:
            U = M - 1
        elif A[M] < k:
            L = M + 1
        else:
            index = M
            U = M - 1
    return index


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
