# -*- coding: utf-8 –*-

import random

"""
快排3.0 迭代版本
"""


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def netherlandFlag(arr, L, R):
    if L > R:
        return [-1, -1]
    if L == R:
        return [L, R]

    less = L - 1
    more = R
    index = L
    while index < more:
        if arr[index] < arr[R]:
            less += 1
            swap(arr, less, index)
            index += 1
        elif arr[index] == arr[R]:
            index += 1
        else:
            more -= 1
            swap(arr, index, more)
    swap(arr, R, more)
    return [less + 1, more]


def quickSort4(arr):
    """ 快排迭代版
    """
    if not arr or len(arr) < 2:
        return
    N = len(arr)
    stack = [[0, N - 1]]
    while stack:
        sort_area = stack.pop()
        swap(arr, sort_area[1], random.randint(*sort_area))
        equal_area = netherlandFlag(arr, *sort_area)
        if equal_area[0] < equal_area[1]:
            stack.append([sort_area[0], equal_area[0] - 1])
            stack.append([equal_area[1] + 1, sort_area[1]])



def quickSort3(arr):
    if not arr or len(arr) < 2:
        return
    process3(arr, 0, len(arr) - 1)


def process3(arr, L, R):
    if L >= R:
        return
    num = random.randint(L, R)
    swap(arr, num, R)
    equal = netherlandFlag(arr, L, R)
    process3(arr, L, equal[0] - 1)
    process3(arr, equal[1] + 1, R)


# for test
def generateRandomArray(maxSize, maxValue):
    """
    :param maxSize:
    :param maxValue:
    :return:
    """
    return [random.randint(-maxValue, maxValue) for _ in xrange(maxSize)]


if __name__ == "__main__":
    testTime = 50000
    maxSize = 100
    maxValue = 100
    print("测试开始")
    for i in xrange(testTime):
        arr = generateRandomArray(maxSize, maxValue)
        arr3 = arr[::]
        arr4 = arr[::]
        quickSort3(arr3)
        quickSort4(arr4)
        if arr3 != arr4:
            print(arr)
            print(arr3)
            print(arr4)
            break
    print("测试结束")