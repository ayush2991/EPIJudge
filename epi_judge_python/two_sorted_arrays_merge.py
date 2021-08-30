from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    # TODO - you fill in here.
    index = m + n - 1
    while index >= 0:
        if m<=0:
            A[index] = B[n-1]
            n -= 1
        elif n<=0:
            A[index] = A[m-1]
            m -= 1
        elif A[m-1] < B[n-1]:
            A[index] = B[n-1]
            n -= 1
        else:
            A[index] = A[m-1]
            m -= 1
        index -= 1
    return


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
