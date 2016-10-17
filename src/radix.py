# -*- coding: utf-8 -*-
"""File implements a radix sort method."""
from __future__ import unicode_literals
from collections import OrderedDict
from collections import deque
import random
import timeit


def radix_sort(sort_list):
    """Sorts input based on the least significant digits of the data first
    and cascades upward until the input has been sorted by it's most
    signifiant digit.

    Worked with Steven and Victor writing this function."""
    if not isinstance(sort_list, list):
        raise TypeError("Radix sort only accepts inputs inside a Python list.")
    if not sort_list:
        return sort_list
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


if __name__ == '__main__':
    print("")
    print("Radix Sort")
    print("")
    print("The following code demonstrates the performance of Radix Sort")
    print("in a variety of use conditions executed 500 times.")
    print("")
    print("Input: 20 random ints under 100")
    result = timeit.timeit(
        'radix_sort(random.sample(range(100), 20))',
        setup="""from __main__ import radix_sort, random""",
        number=500)
    print("Total elapsed time: ", result)
    print ("Average time per cycle: ", result / 500)
    print("")
    print("Input: 100 random ints under 1000")
    result = timeit.timeit(
        'radix_sort(random.sample(range(1000), 100))',
        setup="""from __main__ import radix_sort, random""",
        number=500)
    print("Total elapsed time: ", result)
    print ("Average time per cycle: ", result / 500)
    print("")
    print("Input: 1000 random ints under 10000")
    result = timeit.timeit(
        'radix_sort(random.sample(range(10000), 1000))',
        setup="""from __main__ import radix_sort, random""",
        number=500)
    print("Total elapsed time: ", result)
    print ("Average time per cycle: ", result / 500)
