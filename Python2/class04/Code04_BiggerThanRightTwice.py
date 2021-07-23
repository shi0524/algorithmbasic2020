# -*- coding: utf-8 –*-
import random

"""
在一个数组中，
对于每个数num，求有多少个后面的数 * 2 依然<num，求总个数
比如：[3,1,7,0,2]
3的后面有：1，0
1的后面有：0
7的后面有：0，2
0的后面没有
2的后面没有
所以总共有5个
"""


def biggerTwice(arr):
    if not arr or len(arr) < 2:
        return 0
    return process(arr, 0, len(arr) - 1)


def process(arr, L, R):
    if L == R:
        return 0
    mid = L + ((R - L) >> 1)
    ans = process(arr, L, mid)
    ans += process(arr, mid + 1, R)
    ans += merge(arr, L, mid, R)
    return ans


def merge(arr, L, M, R):
    """
        [L....M]   [M+1....R]
        [M + 1, windowR)
    """
    ans = 0
    # 目前囊括进来的数，是从[M + 1, windowR)
    windowR = M + 1
    for i in range(L, M + 1):
        while windowR <= R and arr[i] > arr[windowR] * 2:
            windowR += 1
        ans += windowR - M - 1

    help = [0] * (R - L + 1)
    i = 0
    l = L
    r = M + 1
    while l <= M and r <= R:
        if arr[l] <= arr[r]:
            help[i] = arr[l]
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
def biggerTwice2(arr):
    if not arr or len(arr) < 2:
        return 0
    ans = 0
    N = len(arr)
    for i in range(N):
        for j in range(i, N):
            if arr[i] > arr[j] * 2:
                ans += 1
    return ans


# for test
def generateRandomArray(maxSize, maxValue):
    """
    :param maxSize:
    :param maxValue:
    :return:
    """
    return [random.randint(0, maxValue) for _ in xrange(maxSize)]


if __name__ == "__main__":
    testTime = 50000
    maxSize = 100
    maxValue = 100
    print("测试开始")
    for i in xrange(testTime):
        arr = generateRandomArray(maxSize, maxValue)
        arr1 = arr[::]
        arr2 = arr[::]
        ans1 = biggerTwice(arr1)
        ans2 = biggerTwice2(arr2)
        if ans1 != ans2:
            print arr
            print(ans1)
            print arr1
            print(ans2)
            break
    print("测试结束")