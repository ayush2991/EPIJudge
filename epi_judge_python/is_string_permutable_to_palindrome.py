from test_framework import generic_test


def can_form_palindrome(s: str) -> bool:
    # TODO - you fill in here.
    h = set()
    for c in s:
        if c in h:
            h.remove(c)
        else:
            h.add(c)
    return len(h) <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
