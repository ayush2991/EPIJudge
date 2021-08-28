from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    # TODO - you fill in here.
    def helper(tree, result):
        if not tree or len(result) >= k:
            return
        helper(tree.right, result)
        result.append(tree.data)
        helper(tree.left, result)

    result = []
    helper(tree, result)
    return result[:k]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
