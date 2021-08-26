# -*- coding: utf-8 –*-

"""
给定一个只包含正数的数组arr，arr中任何一个子数组sub，
一定都可以算出(sub累加和 )* (sub中的最小值)是什么，
那么所有子数组中，这个值最大是多少？
"""

import random
from tqdm import trange


def sub_max(arr):
    """ 前缀和数组 求sum
        单调栈
    """

    # 前缀和数组
    pre_sum = [arr[0]]
    for num in arr[1:]:
        pre_sum.append(pre_sum[-1] + num)

    # 求每个元素左右两边比自己大的元素左边位置
    ans = 0
    n = len(arr)
    stack = []
    stackk = []
    for i, num in enumerate(arr):
        while stack and arr[stack[-1]] >= num:
            pos = stack.pop()
            stackk.pop()
            right = i - 1
            left = stack[-1] + 1 if stack else 0
            sub_sum = pre_sum[right] - pre_sum[left - 1] if left else pre_sum[right]
            ans = max(ans, sub_sum * arr[pos])
        stack.append(i)
        stackk.append(arr[i])
    while stack:
        pos = stack.pop()
        stackk.pop()
        right = n - 1
        left = stack[-1] + 1 if stack else 0
        sub_sum = pre_sum[right] - pre_sum[left - 1] if left else pre_sum[right]
        ans = max(ans, sub_sum * arr[pos])

    return ans


def right(arr):
    n = len(arr)
    ans = 0
    for i in range(n):
        for j in range(i, n):
            sub_sum = sum(arr[i: j + 1])
            sub_min = min(arr[i: j + 1])
            ans = max(ans, sub_min * sub_sum)
    return ans


# for test
def generateNoReapteRandomArray(maxSize, maxValue):
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
    print("测试开始")
    for i in trange(testTime):
        arr = generateNoReapteRandomArray(maxSize, maxValue)
        ans1 = right(arr)
        ans2 = sub_max(arr)
        if ans1 != ans2:
            print(arr)
            print(ans1)
            print(ans2)
            print("test1 break because of error !!!")
            break
    print("测试结束")