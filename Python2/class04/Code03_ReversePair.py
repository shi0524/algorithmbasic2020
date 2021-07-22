# -*- coding: utf-8 –*-

import random

"""
在一个数组中，
任何一个前面的数a，和任何一个后面的数b，
如果(a,b)是降序的，就称为逆序对
返回数组中所有的逆序对
"""


def reverPairNumber(arr):
    if not arr or len(arr) < 2:
        return 0
    return process(arr, 0, len(arr) - 1)


def process(arr, L, R):
    """
    arr[L..R]既要排好序，也要求逆序对数量返回
    所有merge时，产生的逆序对数量，累加，返回
    左 排序 merge并产生逆序对数量
    右 排序 merge并产生逆序对数量
    """
    if L == R:
        return 0
    mid = L + ((R - L) >> 1)
    ans = process(arr, L, mid)
    ans += process(arr, mid + 1, R)
    ans += merge(arr, L, mid, R)
    return ans


def merge(arr, L, M, R):
    help = [0] * (R - L + 1)
    i = len(help) - 1
    l = M
    r = R
    ans = 0
    while l >= L and r > M:
        if arr[l] > arr[r]:
            help[i] = arr[l]
            ans += (r - M)
            l -= 1
            i -= 1
        else:
            help[i] = arr[r]
            r -= 1
            i -= 1
    while l >= L:
        help[i] = arr[l]
        l -= 1
        i -= 1
    while r > M:
        help[i] = arr[r]
        r -= 1
        i -= 1
    for i in range(len(help)):
        arr[L + i] = help[i]

    return ans


# for test
def reverPairNumber2(arr):
    """ 暴力解
    """
    if not arr or len(arr) < 2:
        return 0
    ans = 0
    for i in range(len(arr)):
        for j in range(0, i):
            ans += 1 if arr[j]> arr[i] else 0
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
        ans1 = reverPairNumber(arr1)
        ans2 = reverPairNumber2(arr2)
        if ans1 != ans2:
            print arr
            print(ans1)
            print(ans2)
            break
    print("测试结束")