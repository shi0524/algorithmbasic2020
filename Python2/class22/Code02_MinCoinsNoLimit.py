# -*- coding: utf-8 –*-


"""
arr是面值数组，其中的值都是正数且没有重复。再给定一个正数aim。
每个值都认为是一种面值，且认为张数是无限的。
返回组成aim的最少货币数
"""
import random
from tqdm import trange


def min_coins(arr, aim):
    if not aim:
        return 0
    return process(arr, 0, aim)


def process(arr, index, rest):
    if index == len(arr):
        return float('inf') if rest else 0
    ans = float('inf')
    for zhang in range(rest / arr[index] + 1):
        next_need = process(arr, index + 1, rest - (arr[index] * zhang))
        ans = min(ans, next_need + zhang)
    return ans


def min_coins_dp(arr, aim):
    if not aim:
        return 0
    N = len(arr)
    dp = [[float('inf')] * (aim + 1) for _ in range(N + 1)]
    dp[N][0] = 0
    for rest in range(0, aim + 1):
        for index in range(N - 1, -1, -1):
            min_need = float('inf')
            for zhang in range(rest/arr[index] + 1):
                if rest - arr[index] * zhang < 0:
                    continue
                min_need = min(dp[index + 1][rest - arr[index] * zhang] + zhang, min_need)
            dp[index][rest] = min_need
    # for i, d in enumerate(dp):
    #     print ("%s" % arr[i] if i < len(arr) else 0),
    #     for p in d:
    #         print ("%s"%p).center(3),
    #     print
    return dp[0][aim]


def min_coins_dp2(arr, aim):
    if not aim:
        return 0
    N = len(arr)
    dp = [[float('inf')] * (aim + 1) for _ in range(N + 1)]
    dp[N][0] = 0
    for rest in range(0, aim + 1):
        for index in range(N - 1, -1, -1):
            # min_need = float('inf')
            # for zhang in range(rest/arr[index] + 1):
            #     if rest - arr[index] * zhang < 0:
            #         continue
            #     min_need = min(dp[index + 1][rest - arr[index] * zhang] + zhang, min_need)
            dp[index][rest] = min(dp[index + 1][rest], dp[index][rest - arr[index]] + 1)

    return dp[0][aim]


# for test
def generateRandomArray(maxSize, maxValue):
    """
    :param maxSize:
    :param maxValue:
    :return:
    """
    return list({random.randint(1, maxValue) for _ in xrange(maxSize)})


if __name__ == "__main__":
    testTime = 1000
    maxSize = 10
    maxValue = 10
    maxAim = 50
    print("测试开始")
    for i in trange(testTime):
        arr = generateRandomArray(maxSize, maxValue)
        aim = random.randint(10, maxAim)
        ans1 = min_coins(arr, aim)
        ans2 = min_coins_dp(arr, aim)
        ans3 = min_coins_dp2(arr, aim)
        if ans1 != ans2 or ans1 != ans3:
            print arr
            print aim
            print(ans1, ans2, ans3)
            break
    print("测试结束")

