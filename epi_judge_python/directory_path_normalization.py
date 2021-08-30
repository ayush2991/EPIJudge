from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    # TODO - you fill in here.
    if not path:
        return path
    result = []
    parts = path.split('/')
    for part in parts:
        if part == '..':
            if len(result) > 0 and result[-1] != '..':
                result.pop()
            else:
                result.append(part)
        elif part != '.' and part != "":
            result.append(part)
    final = '/' if path[0] == '/' else ''
    final += '/'.join(result)
    return final


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
