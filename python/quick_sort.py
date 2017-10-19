'''This is an implementation of Quicksort inspired by the Udacity technical interview course'''
from random import shuffle

def quicksort(array):
    if (len(array) < 2): return array
    if (len(array) == 2): return swap(array)
    return partition(array)


def partition(array):
    start, end = 0, len(array) - 1
    pivot = array[end]
    while start <= end:
        while array[start] >= pivot:
            array[end] = array[start]
            array[start] = array[end - 1]
            array[end - 1] = pivot
            end -= 1
        start += 1
    return quicksort(array[0:start]) + quicksort(array[start:len(array)])


def swap(array):
    if array[0] > array[1]:
        array[0], array[1] = array[1], array[0]
    return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print
quicksort(test)