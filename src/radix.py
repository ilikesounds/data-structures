# -*- coding: utf-8 -*-
"""File implements a radix sort method."""
from __future__ import unicode_literals
from collections import OrderedDict
from collections import deque


def radix_sort(sort_list):
    """Sorts input based on the least significant digits of the data first
    and cascades upward until the input has been sorted by it's most
    signifiant digit.

    Worked with Steven and Victor writing this function."""
    if not isinstance(sort_list, list):
        raise TypeError("Radix sort only accepts inputs inside a Python list.")
    for item in sort_list:
        if not isinstance(item, int):
            raise TypeError("All the items in your list must be integers.")
    biggest = max(sort_list)
    num_sorts = len(str(biggest))
    sort_list = [str(item).zfill(num_sorts) for item in sort_list]
    counter = -1
    bucket = OrderedDict()
    for i in range(10):
        bucket[str(i)] = deque()
    while abs(counter) < (num_sorts + 1):
        for num in sort_list:
            bucket[num[counter]].append(num)
        # import pdb; pdb.set_trace()
        sort_list = []
        for key in bucket:
            while len(bucket[key]):
                sort_list.append(bucket[key].popleft())
        counter -= 1
    return [int(item) for item in sort_list]


# bucket = ordered dict
# lesser_buckets = dequs
# {
#     0:[],
#     1:[],
#     2:[],
# }
    # for item in the list:
    #     dict[item % (num_sorts)].append(item)

    # to get 1's digit, % 10
    # to get 10's digit, % 100
    # to get 100's digit, % 1000
