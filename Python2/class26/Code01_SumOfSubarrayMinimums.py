# -*- coding: utf-8 –*-

"""
给定一个数组arr，
返回所有子数组最小值的累加和
"""
"""
907. 子数组的最小值之和
给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。

由于答案可能很大，因此 返回答案模 10^9 + 7


提示：
    1 <= arr.length <= 3 * 104
    1 <= arr[i] <= 3 * 104
测试链接：https://leetcode-cn.com/problems/sum-of-subarray-minimums/
"""

import time
import random
from tqdm import trange
from collections import deque


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


def subArrayMinSum1(arr):
    """ 暴力解 O(N^2)
    """
    MOD = 1000000007
    ans = 0
    n = len(arr)
    for i in range(n):
        min_num = arr[i]
        for num in arr[i:]:
            if num < min_num:
                min_num = num
            ans += min_num
    return ans % MOD


def subArrayMinSum2(arr):
    """ 没有使用单调栈
    """
    MOD = 1000000007
    # left[i] = x : arr[i]左边, 离arr[i]最近, <=arr[i]的数, 位置在x
    left = leftNearLessEqual2(arr)
    # right[i] = y : arr[i]右边, 离arr[i]最近, < arr[i]的数, 位置在y
    right = rightNearLess2(arr)
    ans = 0
    n = len(arr)
    for i in range(n):
        start = i - left[i]
        end = right[i] - i
        ans += start * end * arr[i]
    return ans % MOD


def leftNearLessEqual2(arr):
    """ 获取左边离 i 最近小于等于 i 的数
    """
    n = len(arr)
    left = [0] * n
    for i in range(n):
        ans = -1
        for j in range(i - 1, -1, -1):
            if arr[j] <= arr[i]:
                ans = j
                break
        left[i] = ans
    return left


def rightNearLess2(arr):
    """
    获取右边离 i 最近小于 i 的数
    """
    n = len(arr)
    right = [0] * n
    for i in range(n):
        ans = n
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                ans = j
                break
        right[i] = ans
    return right

def subArrayMinSum3(arr):
    if not arr:
        return 0
    MOD = 1000000007
    # left = leftNearLessEqual3(arr)
    # right = rightNearLess3(arr)
    left, right = nearLessEqualLiftLessRight(arr)
    ans = 0
    n = len(arr)
    for i in range(n):
        start = i - left[i]
        end = right[i] - i
        ans += start * end * arr[i]
    return ans % MOD


def leftNearLessEqual3(arr):
    n = len(arr)
    left = [0] * n
    stack = []
    stackk = []
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            cur = stack.pop()
            left[cur] = stack[-1] if stack else -1
            stackk.pop()
        stack.append(i)
        stackk.append(arr[i])
    while stack:
        cur = stack.pop()
        left[cur] = stack[-1] if stack else -1
        stackk.pop()
    return left


def rightNearLess3(arr):
    n = len(arr)
    right = [0] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            right[stack.pop()] = i
        stack.append(i)
    while stack:
        right[stack.pop()] = n
    return right


def nearLessEqualLiftLessRight(arr):
    n = len(arr)
    left = [-1] * n
    right = [n] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            cur = stack.pop()
            if stack:
                left[cur] = stack[-1]
            right[cur] = i
        stack.append(i)
    while stack:
        cur = stack.pop()
        if stack:
            left[cur] = stack[-1]
    return left, right


# for test
def generateRandomArray(maxSize, maxValue):
    """
    :param maxSize:
    :param maxValue:
    :return:
    """
    return [random.randint(1, maxValue) for _ in xrange(maxSize)]


if __name__ == "__main__":
    maxSize = 100
    maxValue = 50
    testTime = 10000
    print("功能测试开始")
    for i in trange(testTime):
        arr = generateRandomArray(maxSize, maxValue)
        ans1 = subArrayMinSum1(arr)
        ans2 = subArrayMinSum2(arr)
        ans3 = subArrayMinSum3(arr)
        if ans1 != ans2 or ans1 != ans3:
            print(arr)
            print(ans1)
            print(ans2)
            print(ans3)
            print("test1 break because of error !!!")
            break
    print("功能测试结束")

    print("性能测试开始")
    subArrayMinSum1 = time_it(subArrayMinSum1)
    subArrayMinSum2 = time_it(subArrayMinSum2)
    subArrayMinSum3 = time_it(subArrayMinSum3)
    maxSize = 10000
    maxValue = 5000
    arr = generateRandomArray(maxSize, maxValue)
    ans1 = subArrayMinSum1(arr)
    ans2 = subArrayMinSum2(arr)
    ans3 = subArrayMinSum3(arr)
    print("性能测试结束")
