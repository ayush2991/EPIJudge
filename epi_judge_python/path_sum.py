from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:
    # TODO - you fill in here.
    if not tree:
        return False
    balance = remaining_weight - tree.data
    if not tree.left and not tree.right:
        return True if balance == 0 else False
    return has_path_sum(tree.left, balance) \
            or has_path_sum(tree.right, balance)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('path_sum.py', 'path_sum.tsv',
                                       has_path_sum))
