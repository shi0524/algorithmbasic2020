# -*- coding: utf-8 –*-

"""
给定一个正数数组arr，
请把arr中所有的数分成两个集合，尽量让两个集合的累加和接近
返回：
最接近的情况下，较小集合的累加和
"""
import random
from tqdm import trange


def right(arr):
    if len(arr) < 2:
        return 0
    sum_arr = 0
    for num in arr:
        sum_arr += num
    return process(arr, 0, sum_arr/2)


def process(arr, index, rest):
    if index == len(arr):
        return 0
    # 不使用arr[index]
    p1 = process(arr, index + 1, rest)
    # 使用arr[index]
    p2 = 0
    if rest >= arr[index]:
        p2 = arr[index] + process(arr, index + 1, rest - arr[index])
    return max(p1, p2)


def dp(arr):
    if len(arr) < 2:
        return 0
    n = len(arr)
    sum_arr = 0
    for num in arr:
        sum_arr += num

    dp = [[0] * (sum_arr/2 + 1) for _ in range(n + 1)]
    for index in range(n - 1, -1, -1):
        for rest in range(sum_arr/2 + 1):
            p1 = dp[index + 1][rest]
            p2 = 0
            if rest >= arr[index]:
                p2 = arr[index] + dp[index + 1][rest - arr[index]]
            dp[index][rest] = max(p1, p2)
    return dp[0][sum_arr/2]


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
    testTime = 1000
    print("测试开始")
    for i in trange(testTime):
        arr = generateRandomArray(maxSize, maxValue)
        ans1 = right(arr)
        ans2 = dp(arr)
        if ans1 != ans2:
            print arr
            print(ans1, ans2)
            print("test break because of error !!!")
            break
    print("测试结束")
