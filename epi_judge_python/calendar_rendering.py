import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A: List[Event]) -> int:
    # TODO - you fill in here.
    L = []
    for a in A:
        # in case of same timestamp, start should appear first so as to count more concurrent events
        L.append((a.start, '1_start'))
        L.append((a.finish, '2_finish'))
    L.sort()
    events = 0
    max_events = 0
    for l in L:
        if l[1] == '1_start':
            events += 1
            max_events = max(max_events, events)
        else:
            events -= 1
    return max_events


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
