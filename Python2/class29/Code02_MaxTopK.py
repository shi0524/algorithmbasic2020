# -*- coding: utf-8 –*-

"""
给定一个无序数组arr中，长度为N，给定一个正数k，返回top k个最大的数(k < N)

不同时间复杂度三个方法：

1）O(N*logN)
2）O(N + K*logN)
3）O(N + k*logk)
"""
import time
import random
from heapq import *
from tqdm import trange


def time_it(func):
    """ 测时间 ms
    """
    def wrapper(*args, **kwargs):
        a = time.time()
        rc = func(*args, **kwargs)
        b = time.time()
        print("{}: {} ms".format(func.__name__, (b - a) * 1000))
        return rc
    return wrapper


def maxTopK1(arr, k):
    """ 排序 O(N * logN)
    """
    arr.sort()
    return arr[len(arr)-k:][::-1]


def maxTopK2(arr, k):
    """ 堆化 heapify  O(N)
        大根堆 弹出K个 O(k * logN)
    """
    arr1 = map(lambda x: -x, arr)
    heapify(arr1)
    ans = []
    return [abs(heappop(arr1)) for _ in range(k)]


def maxTopK3(arr, k):
    n = len(arr)
    # 求 第 K 大的数下标
    # 求 第 N - k 小的数的下标
    # O(N)
    index = process(arr, 0, n - 1, n - k)
    # K 大的数排序
    # O(k * logK)
    return sorted(arr[index:], reverse=1)


def process(arr, L, R, index):
    if L == R:
        return L
    pivot = arr[random.randint(L, R)]
    ranges = partition(arr, L, R, pivot)
    if ranges[0] <= index <= ranges[1]:
        return index
    elif index < ranges[0]:
        return process(arr, L, ranges[0] - 1, index)
    return process(arr, ranges[1] + 1, R, index)


def partition(arr, L, R, pivot):
    less = L - 1
    more = R + 1
    index = L
    while index < more:
        if arr[index] == pivot:
            index += 1
        elif arr[index] < pivot:
            less += 1
            swap(arr, less, index)
            index += 1
        else:
            more -= 1
            swap(arr, index, more)
    return [less + 1, more - 1]


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]



# for test
def generate_random_array(maxSize, maxValue):
    """
    :param maxSize:
    :param maxValue:
    :return:
    """
    return [random.randint(1, maxValue) for _ in xrange(maxSize)]


if __name__ == "__main__":
    testTime = 10000
    maxSize = 100
    maxValue = 100
    print("测试开始")
    for i in trange(testTime):
        arr = generate_random_array(maxSize, maxValue)
        k = random.randint(1, len(arr))
        ans1 = maxTopK1(arr[:], k)
        ans2 = maxTopK2(arr[:], k)
        ans3 = maxTopK3(arr[:], k)
        if ans1 != ans2 or ans1 != ans3:
            print arr, k
            print(ans1)
            print(ans2)
            print(ans3)
            break
    print("测试结束")

    print("性能测试开始")
    maxTopK1 = time_it(maxTopK1)
    maxTopK2 = time_it(maxTopK2)
    maxTopK3 = time_it(maxTopK3)
    maxSize = 10000
    maxValue = 1000
    arr = generate_random_array(maxSize, maxValue)
    k = len(arr) / 2
    ans1 = maxTopK1(arr, k)
    ans2 = maxTopK2(arr, k)
    ans3 = maxTopK3(arr, k)
    print("性能测试结束")

