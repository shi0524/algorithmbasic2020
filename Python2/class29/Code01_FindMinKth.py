# -*- coding: utf-8 –*-

"""
在无序数组中求第K小的数

1）改写快排的方法
2）bfprt算法(每次最少排除 3/10规模, 常数时间比改写随机快排大)
    1. 5个数分一组
    2. 小组内排序
    3. 取各中位数, 组成M数组
    4. 用 bfprt 选出中位数 p
    5. 用 p 做patition    小于区 等于区 大于区
    6. 看是否命中, 没命中, 走左边或右边
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


def minKth1(arr, k):
    """ 大根堆
        时间复杂度 O(N * k)
    """
    topk = []
    for i in range(k):
        heappush(topk, -arr[i])
    for i in range(k, len(arr)):
        if arr[i] < -topk[0]:
            heappushpop(topk, -arr[i])
    return -topk[0]


def minKth2(arr, k):
    """ 改写快排
        时间复杂度 O(N)
        k >= 1
    """
    if k < 1 or k > len(arr):
        return None
    arr = arr[:]
    return process2(arr, 0, len(arr) - 1, k -1)


def minKth3(arr, k):
    """ minkth2 迭代版
    """
    if k < 1 or k > len(arr):
        return None
    arr = arr[:]
    L = 0
    R = len(arr) - 1
    index = k - 1
    while L < R:
        pivot = arr[random.randint(L, R)]
        ranges = partition(arr, L, R, pivot)
        if ranges[0] <= index <= ranges[1]:
            return arr[index]
        elif index < ranges[0]:
            R = ranges[0] - 1
        else:
            L = ranges[1] + 1
    return arr[L]


def process2(arr, L, R, index):
    """ arr 中第k小的数
        在arr[L, R] 范围上, 如果排序的话(不是真的去排序)找位于index的数(index 一定在 L~R 范围内)
    """
    # 只有一个数
    if L == R:
        return arr[L]
    # 不止一个数
    pivot = arr[random.randint(L, R)]   # 在 L~R 范围内随机一个数
    ranges = partition(arr, L, R, pivot)
    if ranges[0] <= index <= ranges[1]:
        return arr[index]
    elif index < ranges[0]:
        return process2(arr, L, ranges[0] - 1, index)
    return process2(arr, ranges[1] + 1, R, index)


def partition(arr, L, R, pivot):
    less = L - 1
    more = R + 1
    cur = L
    while cur < more:
        if arr[cur] == pivot:
            cur += 1
        elif arr[cur] < pivot:
            less += 1
            swap(arr, less, cur)
            cur += 1
        else:
            more -= 1
            swap(arr, more, cur)
    return [less + 1, more - 1]


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def minKth4(arr, k):
    """ bfprt
    """
    if k < 1 or k > len(arr):
        return None
    arr = arr[:]
    return bfprt(arr, 0, len(arr) - 1, k -1)


def bfprt(arr, L, R, index):
    if L == R:
        return arr[L]
    pivot = median_of_medians(arr, L, R)
    # pivot = arr[random.randint(L, R)]
    ranges = partition(arr, L, R, pivot)
    if ranges[0] <= index <= ranges[1]:
        return arr[index]
    elif index < ranges[0]:
        return bfprt(arr, L, ranges[0] - 1, index)
    else:
        return bfprt(arr, ranges[1] + 1, R, index)


def median_of_medians(arr, L, R):
    """ 5个数1组
        每个小组内部排序
        选出每个小组内部中位数，组成mArr
        返回 marr 的中位数
    """
    size = R - L + 1
    offset = 1 if size % 5 else 0
    mArr = [0] * (size / 5 + offset)
    for team in range(len(mArr)):
        teamL = L + team * 5
        teamR = min(teamL + 4, R)
        mArr[team] = get_median(arr, teamL, teamR)
    return bfprt(mArr, 0, len(mArr) - 1, len(mArr)/2 - 1)


def get_median(arr, L, R):
    insert_sort(arr, L, R)
    return arr[(R + L) / 2]


def insert_sort(arr, L, R):
    for i in range(L + 1, R + 1):
        for j in range(i, L, -1):
            if arr[j] > arr[j - 1]:
                break
            swap(arr, j, j - 1)


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
        ans1 = minKth1(arr, k)
        ans2 = minKth2(arr, k)
        ans3 = minKth3(arr, k)
        ans4 = minKth4(arr, k)
        if ans1 != ans2 or ans1 != ans3 or ans1 != ans4:
            print arr, k
            print(ans1)
            print(ans2)
            print(ans3)
            break
    print("测试结束")

    print("性能测试开始")
    minKth1 = time_it(minKth1)
    minKth2 = time_it(minKth2)
    minKth3 = time_it(minKth3)
    minKth4 = time_it(minKth4)
    maxSize = 1000000
    maxValue = 1000
    arr = generate_random_array(maxSize, maxValue)
    k = len(arr) / 2
    ans1 = minKth1(arr, k)
    ans2 = minKth2(arr, k)
    ans3 = minKth3(arr, k)
    ans4 = minKth4(arr, k)
    print(ans1, ans2, ans3, ans4)
    print("性能测试结束")



