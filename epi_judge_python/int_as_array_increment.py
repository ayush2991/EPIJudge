from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    # TODO - you fill in here.
    j = len(A) - 1
    while j>=0 and A[j] == 9:
        A[j] = 0
        j -= 1
    if j == -1:
        return [1] + A
    A[j] += 1
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
