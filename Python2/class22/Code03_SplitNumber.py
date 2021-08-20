# -*- coding: utf-8 –*-


"""
给定一个正数n，求n的裂开方法数，
规定：后面的数不能比前面的数小
比如4的裂开方法有：
1+1+1+1、1+1+2、1+3、2+2、4
5种，所以返回5
"""
import random
from tqdm import trange


def ways(n):
    return process(1, n)


def process(pre, rest):
    if rest == 0:
        return 1
    if pre > rest:
        return 0
    ans = 0
    for i in range(pre, rest + 1):
        ans += process(i, rest - i)
    return ans


def ways_dp(n):
    if n < 0:
        return 0
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for pre in range(1, n + 1):
        dp[pre][0] = 1
        dp[pre][pre] = 1
    for pre in range(n - 1, 0, -1):
        for rest in range(pre + 1, n + 1):
            for i in range(pre, rest + 1):
                dp[pre][rest] += dp[i][rest - i]
    return dp[1][n]


def ways_dp2(n):
    if n < 0:
        return 0
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for pre in range(1, n + 1):
        dp[pre][0] = 1
        dp[pre][pre] = 1
    for pre in range(n - 1, 0, -1):
        for rest in range(pre + 1, n + 1):
            # for i in range(pre, rest + 1):
            #     dp[pre][rest] += dp[i][rest - i]
            dp[pre][rest] = dp[pre + 1][rest] + dp[pre][rest - pre]
    return dp[1][n]


if __name__ == "__main__":
    testTime = 1000
    maxAim = 50
    print("测试开始")
    for i in trange(testTime):
        aim = random.randint(1, maxAim)
        ans1 = ways(aim)
        ans2 = ways_dp(aim)
        ans3 = ways_dp2(aim)
        if ans1 != ans2 or ans1 != ans3:
            print aim
            print(ans1, ans2, ans3)
            break
    print("测试结束")