from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    # TODO - you fill in here.
    h = {}
    for c in magazine_text:
        h[c] = h.get(c, 0) + 1
    for c in letter_text:
        h[c] = h.get(c, 0) - 1
        if h[c] < 0:
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
