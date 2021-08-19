# -*- coding: utf-8 –*-

"""
arr是货币数组，其中的值都是正数。
每个值都认为是一张货币，
认为值相同的货币没有任何不同，
再给定一个正数aim。
返回组成aim的方法数
例如：arr = {1,2,1,1,2,1,2}，aim = 4
方法：1+1+1+1、1+1+2、2+2
一共就3种方法，所以返回3
"""
import random
from tqdm import trange
from collections import defaultdict


def coins_count(arr):
    """ 统计钱币张数
    """
    count = defaultdict(int)
    for num in arr:
        count[num] += 1
    return count


def coins_way(arr, aim):
    count = coins_count(arr)
    coins = count.keys()
    zhangs = [count[c] for c in coins]
    return process(coins, zhangs, 0, aim)


def process(coins, zhangs, index, rest):
    if index == len(coins):
        return 0 if rest else 1
    ways = 0
    zhang = 0
    while rest - coins[index] * zhang >= 0 and zhang <= zhangs[index]:
        ways += process(coins, zhangs, index + 1, rest - coins[index] * zhang)
        zhang += 1
    return ways


def dp1(arr, aim):
    count = coins_count(arr)
    coins = count.keys()
    zhangs = [count[c] for c in coins]
    N = len(coins)
    dp = [[0] * (aim + 1) for _ in range(N + 1)]
    dp[N][0] = 1

    for index in range(N - 1, -1, -1):
        for rest in range(aim + 1):
            zhang = 0
            while rest - coins[index] * zhang >= 0 and zhang <= zhangs[index]:
                dp[index][rest] += dp[index + 1][rest - coins[index] * zhang]
                zhang += 1
    return dp[0][aim]


def dp2(arr, aim):
    count = coins_count(arr)
    coins = count.keys()
    zhangs = [count[c] for c in coins]
    N = len(coins)
    dp = [[0] * (aim + 1) for _ in range(N + 1)]
    dp[N][0] = 1

    for index in range(N - 1, -1, -1):
        for rest in range(aim + 1):
            dp[index][rest] = dp[index + 1][rest]
            if rest - coins[index] >= 0:
                dp[index][rest] += dp[index][rest - coins[index]]

            """ 这段代码可以不要 """
            if rest - coins[index] * (zhangs[index] + 1) >= 0:
                dp[index][rest] -= dp[index][rest - coins[index] * (zhangs[index] + 1)]
            """ 这段代码可以不要 """

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
    testTime = 100000
    maxSize = 1000
    maxValue = 100
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
