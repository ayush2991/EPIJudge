from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    # TODO - you fill in here.
    def is_opening(c):
        return c == '(' or c == '[' or c == '{'

    def match(c):
        if c == '}':
            return '{'
        elif c == ']':
            return '['
        else:
            return '('

    stack = []
    for c in s:
        if is_opening(c):
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            elif stack[-1] != match(c):
                return False
            stack.pop()
    return len(stack) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
