from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    # TODO - you fill in here.
    m = [[0]*(len(B)+1) for _ in range(len(A) + 1)]
    for i in range(len(B) + 1):
        m[0][i] = i
    for i in range(len(A) + 1):
        m[i][0] = i
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            m[i][j] = min(m[i][j-1] + 1, m[i-1][j] + 1, m[i-1][j-1] + (0 if A[i-1] == B[j-1] else 1))
    return m[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
