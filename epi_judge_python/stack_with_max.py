from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:

    def __init__(self):
        self.s_ = []
        self.maxes_ = []

    def empty(self) -> bool:
        # TODO - you fill in here.
        return len(self.s_) == 0

    def max(self) -> int:
        # TODO - you fill in here.
        if self.empty():
            raise IndexError
        print (self.maxes_)
        return self.maxes_[-1]

    def pop(self) -> int:
        # TODO - you fill in here.
        if self.empty():
            raise IndexError
        e = self.s_.pop()
        if e == self.maxes_[-1]:
            self.maxes_.pop()
        return e

    def push(self, x: int) -> None:
        # TODO - you fill in here.
        self.s_.append(x)
        if len(self.maxes_) == 0 or x > self.maxes_[-1]:
            self.maxes_.append(x)
        return


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
