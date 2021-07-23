# -*- coding: utf-8 –*-

import random

"""
荷兰国旗和快排
"""


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, L, R):
    """
    arr[L..R]上，以arr[R]位置的数做划分值
    <= X 在左边
    > X 的在右边
    """
    if L > R:
        return -1
    if L == R:
        return L
    lessEqual = L - 1
    index = L
    while index < R:
        if arr[index] <= arr[R]:
            lessEqual += 1
            swap(arr, index, lessEqual)
        index += 1
    lessEqual += 1
    swap(arr, lessEqual, R)
    return lessEqual


def netherlandsFlag(arr, L, R):
    if L > R:
        return [-1, -1]
    if L == R:
        return [L, R]

    less = L - 1    # 小于区右边界
    more = R        # 大于区左边界
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


def quickSort1(arr):
    """ 快排 1.0
    """
    if not arr or len(arr) < 2:
        return
    process1(arr, 0, len(arr) - 1)


def process1(arr, L, R):
    if L >= R:
        return
    mid = partition(arr, L, R)
    process1(arr, L, mid - 1)
    process1(arr, mid + 1, R)


def quickSort2(arr):
    if not arr or len(arr) < 2:
        return
    process2(arr, 0, len(arr) - 1)


def process2(arr, L, R):
    if L >= R:
        return
    equal = netherlandsFlag(arr, L, R)
    process2(arr, L, equal[0] - 1)
    process2(arr, equal[1] + 1, R)


def quickSort3(arr):
    if not arr or len(arr) < 2:
        return
    process3(arr, 0, len(arr) - 1)


def process3(arr, L, R):
    if L >= R:
        return
    num = random.randint(L, R)
    swap(arr, num, R)
    equal = netherlandsFlag(arr, L, R)
    process2(arr, L, equal[0] - 1)
    process2(arr, equal[1] + 1, R)



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
        arr1 = arr[::]
        arr2 = arr[::]
        arr3 = arr[::]
        quickSort1(arr1)
        quickSort2(arr2)
        quickSort3(arr3)
        if arr1 != arr2 or arr1 != arr3:
            print(arr1)
            print(arr2)
            print(arr3)
            break
    print("测试结束")
