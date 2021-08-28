from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    def helper(tree, min_value, max_value):
        if not tree:
            return True
        if tree.data < min_value or tree.data > max_value:
            return False
        return helper(tree.left, min_value, max_value=tree.data) and \
            helper(tree.right, min_value=tree.data, max_value=max_value)
    return helper(tree, float('-inf'), float('inf'))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
