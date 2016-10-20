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

presorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pre_sorted_rev_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
rand_list = random.sample(range(1000), random.randrange(2, 100))

if __name__ == '__main__':

    print(timeit.timeit("merge_sort(presorted_list)"))
    print(timeit.timeit("merge_sort(presorted_rev_list)"))
    print(timeit.timeit("merge_sort(rand_list)"))
