from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    def helper(tree):
        if not tree:
            return 0
        left_height = helper(tree.left)
        right_height = helper(tree.right)
        if abs(left_height - right_height) > 1 or left_height == -1 or right_height == -1:
            return -1
        return max(left_height, right_height) + 1
    return True if helper(tree) != -1 else False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
