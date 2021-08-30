from test_framework import generic_test


def evaluate(expression: str) -> int:
    # TODO - you fill in here.
    def is_operator(op):
        return op == '+' or op == '-' or op == '*' or op == '/'

    def apply(a, b, op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        else:
            return a // b

    ops = expression.split(',')
    stack = []
    for op in ops:
        if not is_operator(op):
            stack.append(int(op))
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(apply(a, b, op))
    return stack[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
