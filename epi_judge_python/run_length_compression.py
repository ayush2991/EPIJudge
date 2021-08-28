from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s: str) -> str:
    # TODO - you fill in here.
    result = []
    i = 0
    while i < len(s):
        count = ''
        while s[i].isdigit():
            count += s[i]
            i += 1
        letter = s[i]
        i += 1
        count = int(count)
        for _ in range(count):
            result.append(letter)
    return ''.join(result)


def encoding(s: str) -> str:
    # TODO - you fill in here.
    result = []
    i = 0
    while i < len(s):
        letter = s[i]
        count = 0
        while i < len(s) and s[i] == letter:
            count += 1
            i += 1
        result.append(str(count))
        result.append(letter)
    return ''.join(result)


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('run_length_compression.py',
                                       'run_length_compression.tsv',
                                       rle_tester))
