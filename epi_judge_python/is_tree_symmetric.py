from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    def helper(s, t):
        if not s and not t:
            return True
        if not (s and t):
            return False
        return s.data == t.data and helper(s.left, t.right) and helper(s.right, t.left)
    return helper(tree, tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
