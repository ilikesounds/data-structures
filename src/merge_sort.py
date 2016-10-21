""" This module will implement a merge sort on a list"""
# This solution was heavily influenced by the example found on interactive
# python found at the URL below. I've attempted to make the function a class
# with a recursive method:
# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html
import timeit
import random


def merge_sort(merge_list):
    """This function will call the recursive merge sort method and returb a
    sorted list"""

    if len(merge_list) > 1:
        mid_point = len(merge_list) // 2
        left = merge_list[:mid_point]
        right = merge_list[mid_point:]

        merge_sort(left)
        merge_sort(right)

        left_i = 0
        right_i = 0
        ml_i = 0

        while left_i < len(left) and right_i < len(right):
            if left[left_i] < right[right_i]:
                merge_list[ml_i] = left[left_i]
                left_i += 1
            else:
                merge_list[ml_i] = right[right_i]
                right_i += 1
            ml_i += 1

        while left_i < len(left):
            merge_list[ml_i] = left[left_i]
            left_i += 1
            ml_i += 1

        while right_i < len(right):
            merge_list[ml_i] = right[right_i]
            right_i += 1
            ml_i += 1

if __name__ == '__main__':
    print("")
    print("Merge Sort")
    print("")
    print("The following code demonstrates the performance of Merge Sort")
    print("in a variety of use conditions executed 500 times.")
    print("")
    print("Input: 20 random ints under 100")
    result = timeit.timeit(
        'merge_sort(random.sample(range(100), 20))',
        setup="""from __main__ import merge_sort, random""",
        number=500)
    print("Total elapsed time: ", result)
    print ("Average time per cycle: ", result / 500)
    print("")
    print("Input: 100 random ints under 1000")
    result = timeit.timeit(
        'merge_sort(random.sample(range(1000), 100))',
        setup="""from __main__ import merge_sort, random""",
        number=500)
    print("Total elapsed time: ", result)
    print ("Average time per cycle: ", result / 500)
    print("")
    print("Input: 1000 random ints under 10000")
    result = timeit.timeit(
        'merge_sort(random.sample(range(10000), 1000))',
        setup="""from __main__ import merge_sort, random""",
        number=500)
    print("Total elapsed time: ", result)
    print ("Average time per cycle: ", result / 500)
