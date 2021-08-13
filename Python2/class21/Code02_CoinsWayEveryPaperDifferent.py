# -*- coding: utf-8 –*-

"""
arr是货币数组，其中的值都是正数。再给定一个正数aim。
每个值都认为是一张货币，
即便是值相同的货币也认为每一张都是不同的，
返回组成aim的方法数
例如：arr = {1,1,1}，aim = 2
第0个和第1个能组成2，第1个和第2个能组成2，第0个和第2个能组成2
一共就3种方法，所以返回3
"""
import random
from tqdm import trange


def coinWays(arr, aim):
    return process(0, aim, arr)


def process(index, rest, arr):
    if rest < 0:
        return 0
    if index == len(arr):
        return 1 if rest == 0 else 0
    return process(index + 1, rest, arr) + process(index + 1, rest - arr[index], arr)


def coin_ways_dp(arr, aim):
    if aim == 0:
        return 1
    N = len(arr)
    dp = [[0] * (aim + 1) for _ in range(N + 1)]
    dp[N][0] = 1
    for index in range(N - 1, -1, -1):
        for rest in range(aim + 1):
            dp[index][rest] = dp[index + 1][rest]
            if rest - arr[index] >= 0:
                dp[index][rest] += dp[index + 1][rest - arr[index]]
    return dp[0][aim]


# for test
def generateRandomArray(maxSize, maxValue):
    """
    :param maxSize:
    :param maxValue:
    :return:
    """
    return [random.randint(0, maxValue) for _ in xrange(maxSize)]


if __name__ == "__main__":
    testTime = 1000
    maxSize = 20
    maxValue = 100
    maxAim = 500
    print("测试开始")
    for i in trange(testTime):
        arr = generateRandomArray(maxSize, maxValue)
        aim = random.randint(100, maxAim)
        ans1 = coinWays(arr, aim)
        ans2 = coin_ways_dp(arr, aim)
        if ans1 != ans2:
            print arr
            print aim
            print(ans1, ans2)
            break
    print("测试结束")
