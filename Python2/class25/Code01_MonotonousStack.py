# -*- coding: utf-8 –*-

"""
单调栈的实现
给定一个无重复元素数组，
返回数组元素左右两边比该元素小的下标
没有返回设为 -1

arr = [ 3, 1, 2, 3]
        0  1  2  3
    0 : [-1,  1]
    1 : [-1, -1]
    2 : [ 1, -1]
    3 : [ 2, -1]
"""

import random
from tqdm import trange


def getNearLessNoRepeat(arr):
    """ 没有重复值
    """
    ans = {}
    stack = []
    for i, num in enumerate(arr):
        while stack and arr[stack[-1]] > num:
            pos = stack.pop()
            left_less = stack[-1] if stack else -1
            ans[pos] = [left_less, i]
        stack.append(i)
    while stack:
        pos = stack.pop()
        left_less = stack[-1] if stack else -1
        ans[pos] = [left_less, -1]
    return ans


def getNearLess(arr):
    """ 有重复值
    """
    ans = {}
    stack = []
    for i, num in enumerate(arr):
        while stack and arr[stack[-1][-1]] > num:
            pos_indexs = stack.pop()
            left_less = stack[-1][-1] if stack else -1
            for pos in pos_indexs:
                ans[pos] = [left_less, i]

        if stack and arr[stack[-1][-1]] == num:
            stack[-1].append(i)
        else:
            stack.append([i])
    while stack:
        pos_indexs = stack.pop()
        left_less = stack[-1][-1] if stack else -1
        for pos in pos_indexs:
            ans[pos] = [left_less, -1]
    return ans


def right(arr):
    ans = {}
    n = len(arr)
    for i, num in enumerate(arr):
        left_less = -1
        right_less = -1
        for L in range(i, -1, -1):
            if arr[L] < num:
                left_less = L
                break
        for R in range(i, n):
            if arr[R] < num:
                right_less = R
                break
        ans[i] = [left_less, right_less]
    return ans


# for test
def generateNoReapteRandomArray(maxSize, maxValue):
    """
    :param maxSize:
    :param maxValue:
    :return:
    """
    return list({random.randint(1, maxValue) for _ in xrange(maxSize)})


# for test
def generateRandomArray(maxSize, maxValue):
    """
    :param maxSize:
    :param maxValue:
    :return:
    """
    return [random.randint(1, maxValue) for _ in xrange(maxSize)]


if __name__ == "__main__":
    maxSize = 10
    maxValue = 50
    testTime = 10000
    print("测试开始")
    for i in trange(testTime):
        arr1 = generateNoReapteRandomArray(maxSize, maxValue)
        ans11 = right(arr1)
        ans12 = getNearLessNoRepeat(arr1)
        if ans11 != ans12:
            print(arr1)
            print(ans11)
            print(ans12)
            print("test1 break because of error !!!")
            break
        arr2 = generateRandomArray(maxSize, maxValue)
        ans21 = right(arr2)
        ans22 = getNearLess(arr2)
        if ans21 != ans22:
            print(arr2)
            print(ans21)
            print(ans22)
            print("test2 break because of error !!!")
            break
    print("测试结束")