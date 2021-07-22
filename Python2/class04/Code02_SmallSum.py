# -*- coding: utf-8 –*-

import random

"""
在一个数组中，一个数左边比它小的数的总和，叫数的小和，所有数的小和累加起来，叫数组小和。求数组小和。
例子： [1,3,4,2,5]
1左边比1小的数：没有
3左边比3小的数：1
4左边比4小的数：1、3
2左边比2小的数：1
5左边比5小的数：1、3、4、 2
所以数组的小和为1+1+3+1+1+3+4+2=16
"""


def smallSum(arr):
    if not arr or len(arr) < 2:
        return 0
    return process(arr, 0, len(arr) - 1)


def process(arr, L, R):
    """
    arr[L..R]既要排好序，也要求小和返回
    所有merge时，产生的小和，累加
    左 排序   merge
    右 排序  merge
    merge
    """
    if L == R:
        return 0
    mid = L + ((R - L) >> 2)
    ans = process(arr, L, mid)
    ans += process(arr, mid + 1, R)
    ans += merge(arr, L, mid, R)
    return ans


def merge(arr, L, M, R):
    help = [0] * (R - L + 1)
    i = 0
    l = L
    r = M + 1
    ans = 0
    while l <= M and r <= R:
        if arr[l] < arr[r]:
            help[i] = arr[l]
            ans += arr[l] * (R - r + 1)
            l += 1
            i += 1
        else:
            help[i] = arr[r]
            r += 1
            i += 1
    while l <= M:
        help[i] = arr[l]
        l += 1
        i += 1
    while r <= R:
        help[i] = arr[r]
        r += 1
        i += 1
    for i in range(len(help)):
        arr[L + i] = help[i]

    return ans


# for test
def smallSum2(arr):
    """ 暴力解
    """
    ans = 0
    for i in range(len(arr)):
        for j in range(0, i):
           ans += arr[j] if arr[j] < arr[i] else 0
    return ans


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
        ans1 = smallSum(arr1)
        ans2 = smallSum2(arr2)
        if ans1 != ans2:
            print arr
            print(ans1)
            print(ans2)
            break
    print("测试结束")