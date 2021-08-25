# -*- coding: utf-8 –*-


"""
arr是货币数组，其中的值都是正数。再给定一个正数aim。
每个值都认为是一张货币，
返回组成aim的最少货币数
注意：
因为是求最少货币数，所以每一张货币认为是相同或者不同就不重要了
"""

import time
import random
from tqdm import trange
from collections import Counter, deque


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


@time_it
def min_coins(arr, aim):
    """ 暴力解
    """
    return process(arr, 0, aim)


def process(arr, index, rest):
    if rest < 0:
        return float('inf')
    if index == len(arr):
        return 0 if rest == 0 else float('inf')
    no = process(arr, index + 1, rest)
    yes = 1 + process(arr, index + 1, rest - arr[index])
    return min(no, yes)


@time_it
def min_coins_dp1(arr, aim):
    if not aim:
        return 0
    max_num = float('inf')
    n = len(arr)
    dp = [[0] * (aim + 1) for _ in range(n + 1)]
    # dp[n][0] = 0
    for rest in range(1, aim + 1):
        dp[n][rest] = max_num
    for index in range(n - 1, -1, -1):
        for rest in range(aim + 1):
            no = dp[index + 1][rest]
            yes = max_num
            if rest >= arr[index]:
                yes = 1 + dp[index + 1][rest - arr[index]]
            dp[index][rest] = min(no, yes)
    return dp[0][aim]


def coins_zhangs(arr):
    counts = Counter(arr)
    coins = counts.keys()
    zhangs = [counts[k] for k in coins]
    return coins, zhangs


@time_it
def min_coins_dp2(arr, aim):
    if not aim:
        return 0
    coins, zhangs = coins_zhangs(arr)
    max_num = float('inf')
    n = len(coins)
    dp = [[0] * (aim + 1) for _ in range(n + 1)]
    # dp[n][0] = 0
    for rest in range(1, aim + 1):
        dp[n][rest] = max_num
    for index in range(n - 1, -1, -1):
        for rest in range(aim + 1):
            dp[index][rest] = dp[index + 1][rest]
            for zhang in range(1, zhangs[index] + 1):
                if rest >= zhang * coins[index]:
                    dp[index][rest] = min(dp[index][rest], zhang + dp[index + 1][rest - zhang * coins[index]])
    # print "*" * 100
    # for d in dp:
    #     for p in d:
    #         print "{}".format(p).center(3),
    #     print
    # print "*" * 100

    return dp[0][aim]


@time_it
def min_coins_dp3(arr, aim):
    if not aim:
        return 0
    coins, zhangs = coins_zhangs(arr)
    max_num = float('inf')
    n = len(coins)
    dp = [[0] * (aim + 1) for _ in range(n + 1)]
    # dp[n][0] = 0
    for rest in range(1, aim + 1):
        dp[n][rest] = max_num

    # 虽然是嵌套了很多循环，但是时间复杂度为O(货币种数 * aim)
    # 因为用了窗口内最小值的更新结构
    for index in range(n - 1, -1, -1):
        for mod in range(min(aim + 1, coins[index])):

            # 当前面值 X
            # mod   mod + x   mod + 2*x   mod + 3 * x
            w = deque()
            w.append(mod)
            dp[index][mod] = dp[index + 1][mod]
            for rest in range(mod + coins[index], aim + 1, coins[index]):
                while w and (dp[index + 1][w[-1]] == max_num or
                             dp[index + 1][w[-1]] + compensate(w[-1], rest, coins[index]) >= dp[index + 1][rest]):
                    w.pop()
                w.append(rest)
                overdue = rest - coins[index] * (zhangs[index] + 1)
                if w[0] == overdue:
                    w.popleft()
                dp[index][rest] = dp[index + 1][w[0]] + compensate(w[0], rest, coins[index])
    # for d in dp:
    #     for p in d:
    #         print "{}".format(p).center(3),
    #     print
    return dp[0][aim]


def compensate(pre, cur, coin):
    return (cur - pre) / coin


# for test
def generateRandomArray(maxSize, maxValue):
    """
    :param maxSize:
    :param maxValue:
    :return:
    """
    return [random.randint(1, maxValue) for _ in xrange(maxSize)]


if __name__ == "__main__":

    """ 功能测试开始 """
    # testTime = 1000
    # maxSize = 100000
    # maxValue = 100
    # maxAim = 1000
    # print("测试开始")
    # for i in trange(testTime):
    #     arr = generateRandomArray(maxSize, maxValue)
    #     aim = random.randint(5, maxAim)
    #     ans1 = min_coins(arr, aim)
    #     ans2 = min_coins_dp1(arr, aim)
    #     ans3 = min_coins_dp2(arr, aim)
    #     ans4 = min_coins_dp3(arr, aim)
    #     if ans1 != ans2 or ans1 != ans3 or ans3 != ans4:
    #         print arr
    #         print aim
    #         print(ans1, ans2, ans3, ans4)
    #         break
    # print("测试结束")
    """ 功能测试结束 """

    """ 性能测试开始 """

    print("*" * 10 + "少量货币" + "*" * 10)
    maxSize = 30
    maxValue = 20
    aim = 60
    print("test size {} start".format(maxSize))
    arr = generateRandomArray(maxSize, maxValue)
    ans1 = min_coins(arr, aim)
    ans2 = min_coins_dp1(arr, aim)
    ans3 = min_coins_dp2(arr, aim)
    ans4 = min_coins_dp3(arr, aim)
    print(ans1, ans2, ans3, ans4)
    print("test size {} end".format(maxSize))

    print("*" * 10 + "大量货币出现" + "*" * 10)

    maxSize = 3000
    maxValue = 20
    aim = 6000
    arr = generateRandomArray(maxSize, maxValue)
    print("test size {} start".format(maxSize))
    ans2 = min_coins_dp1(arr, aim)
    ans3 = min_coins_dp2(arr, aim)
    ans4 = min_coins_dp3(arr, aim)
    print(ans2, ans3, ans4)

    print("*" * 10 + "大量重复货币出现" + "*" * 10)

    maxSize = 100000
    maxValue = 100
    aim = 200000
    arr = generateRandomArray(maxSize, maxValue)
    print("test size {} start".format(maxSize))
    ans3 = min_coins_dp2(arr, aim)
    ans4 = min_coins_dp3(arr, aim)
    print(ans3, ans4)
    print("test size {} end".format(maxSize))

    """ 性能测试结束 """



