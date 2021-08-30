import collections
import copy
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze: List[List[int]], s: Coordinate,
                e: Coordinate) -> List[Coordinate]:
    # TODO - you fill in here.
    def helper(maze, s, e):
        if s.x<0 or s.y<0 or s.x>=len(maze) or s.y>=len(maze[0]) or maze[s.x][s.y] != WHITE:
            return False
        maze [s.x][s.y] = BLACK
        if s.x == e.x and s.y == e.y:
            result.append(e)
            return True
        for n in [(s.x-1, s.y), (s.x, s.y-1), (s.x+1, s.y), (s.x, s.y+1)]:
            if helper(maze, Coordinate(n[0], n[1]), e):
                result.append(Coordinate(s.x, s.y))
                return True
        return False
    result = []
    helper(maze, s, e)
    return result[::-1]
                


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure('Path doesn\'t lay between start and end points')

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure('Path contains invalid segments')

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_maze.py', 'search_maze.tsv',
                                       search_maze_wrapper))
