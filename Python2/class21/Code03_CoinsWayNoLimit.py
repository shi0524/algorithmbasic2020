# -*- coding: utf-8 –*-

"""
arr是面值数组，其中的值都是正数且没有重复。再给定一个正数aim。
每个值都认为是一种面值，且认为张数是无限的。
返回组成aim的方法数
例如：arr = {1,2}，aim = 4
方法如下：1+1+1+1、1+1+2、2+2
一共就3种方法，所以返回3
"""
import random
from tqdm import trange


def coins_way(arr, aim):
    if not arr or aim < 0:
        return 0
    return process(arr, 0, aim)


def process(arr, index, rest):
    if index == len(arr):
        return 1 if rest == 0 else 0
    ways = 0
    zhang = 0
    while zhang * arr[index] <= rest:
        ways += process(arr, index + 1, rest - arr[index] * zhang)
        zhang += 1
    return ways


def dp1(arr, aim):
    if not arr or aim < 0:
        return 0
    N = len(arr)
    dp = [[0] * (aim + 1) for _ in range(N + 1)]
    dp[N][0] = 1
    for index in range(N - 1, -1, -1):
        for rest in range(aim + 1):
            ways = 0
            zhang = 0
            while zhang * arr[index] <= rest:
                ways += dp[index + 1][rest - arr[index] * zhang]
                zhang += 1
            dp[index][rest] = ways
    return dp[0][aim]


def dp2(arr, aim):
    if not arr or aim < 0:
        return 0
    N = len(arr)
    dp = [[0] * (aim + 1) for _ in range(N + 1)]
    dp[N][0] = 1
    for index in range(N - 1, -1, -1):
        for rest in range(aim + 1):
            dp[index][rest] = dp[index + 1][rest]
            if (rest - arr[index] >= 0):
                dp[index][rest] += dp[index][rest - arr[index]]
    return dp[0][aim]


# for test
def generateRandomArray(maxSize, maxValue):
    """
    :param maxSize:
    :param maxValue:
    :return:
    """
    return [random.randint(maxValue, maxValue) for _ in xrange(maxSize)]


if __name__ == "__main__":
    testTime = 1000
    maxSize = 10
    maxValue = 10
    maxAim = 100
    print("测试开始")
    for i in trange(testTime):
        arr = generateRandomArray(maxSize, maxValue)
        aim = random.randint(1, maxAim)
        ans1 = coins_way(arr, aim)
        ans2 = dp1(arr, aim)
        ans3 = dp2(arr, aim)
        if ans1 != ans2 or ans1 != ans3:
            print(arr)
            print(aim)
            print(ans1)
            print(ans2)
            print(ans3)
            print("test break because of error !!!")
            break
    print("测试结束")

