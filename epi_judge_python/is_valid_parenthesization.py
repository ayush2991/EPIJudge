from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    # TODO - you fill in here.
    mapping = {')' : '(', ']' : '[', '}' : '{'}
    stack = []
    for c in s:
        if not c in mapping.keys():
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            elif stack[-1] != mapping[c]:
                return False
            stack.pop()
    return len(stack) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
