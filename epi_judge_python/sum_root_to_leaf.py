from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    # TODO - you fill in here.
    def helper(tree, s):
        if not tree: 
            return 0
        value = 2 * s + tree.data
        if not tree.left and not tree.right:
            return value
        return helper(tree.left, value) + helper(tree.right, value)
    return helper(tree, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
