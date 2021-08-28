from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    # TODO - you fill in here.
    dest = len(A) - 1
    can_reach = 0
    for i, a in enumerate(A):
        if can_reach < i:
            return False
        can_reach = max(can_reach, i+a)
        if can_reach >= dest:
            return True
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
