# -*- coding: utf-8 –*-

import random


def mergeSort1(arr):
    """ merge排序递归版
    """
    if not arr or len(arr) < 2:
        return
    process(arr, 0, len(arr) - 1)


def process(arr, L, R):
    """
    请把arr[L..R]排有序
    l...r N
    T(N) = 2 * T(N / 2) + O(N)
    O(N * logN)
    """
    if L == R:
        return
    # python 数字不会溢出  其他语言：mid = L + ((R - L) >> 1)
    mid = (L + R) // 2
    process(arr, L, mid)
    process(arr, mid + 1, R)
    merge(arr, L, mid, R)


def merge(arr, L, M, R):
    help = [0] * (R - L + 1)
    i = 0
    p1 = L
    p2 = M + 1
    while p1 <= M and p2 <= R:
        if arr[p1] <= arr[p2]:
            help[i] = arr[p1]
            p1 += 1
        else:
            help[i] = arr[p2]
            p2 += 1
        i += 1
    # 要么p1 越界了，要么p2越界了
    while p1 <= M:
        help[i] = arr[p1]
        i+=1
        p1 += 1
    while p2 <= R:
        help[i] = arr[p2]
        p2 += 1
        i += 1
    for i in range(len(help)):      # 这步也可以用 enumerate
        arr[L + i] = help[i]


def mergeSort2(arr):
    """ merge 排序迭代版
    """
    if not arr or len(arr) < 2:
        return
    N = len(arr)
    # 步长
    mergeSize = 1
    while mergeSize < N:
        L = 0
        while L < N:
            if mergeSize >= N - L:
                break
            M = L + mergeSize - 1
            R = M + min(mergeSize, N - M - 1)
            merge(arr, L, M, R)
            L = R + 1
        # 防溢出
        if mergeSize > N / 2:
            break
        mergeSize *= 2


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
        arr1 = generateRandomArray(maxSize, maxValue)
        arr2 = arr1[::]
        mergeSort1(arr1)
        mergeSort2(arr2)
        if arr1 != arr2:
            print(arr1)
            print(arr2)
            break
    print("测试结束")