from test_framework import generic_test


def square_root(k: int) -> int:
    # TODO - you fill in here.
    if k <= 1:
        return k
    L, U = 1, k
    root = 1
    while L <= U:
        M = (L+U)//2
        if M**2 > k:
            U = M - 1
        elif M**2 < k:
            root = M
            L = M + 1
        else:
            root = M
            break
    return root


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
