# -*- coding: utf-8 –*-

"""
给定3个参数，N，M，K
怪兽有N滴血，等着英雄来砍自己
英雄每一次打击，都会让怪兽流失[0~M]的血量
到底流失多少？每一次在[0~M]上等概率的获得一个值
求K次打击之后，英雄把怪兽砍死的概率
"""
import math
import random
from tqdm import trange


def right1(N, M, K):
    if N < 1 or M < 1 or K < 1:
        return 0
    posibility = process(N, M, K)
    all_posibility = math.pow(M + 1, K)
    return float(posibility) / all_posibility


def process(hp, M, rest):
    if rest == 0:
        return 1 if hp <= 0 else 0
    ways = 0
    for atk in range(M + 1):
        ways += process(hp - atk, M, rest - 1)
    return ways


def right2(N, M, K):
    if N < 1 or M < 1 or K < 1:
        return 0
    posibility = process2(N, M, K)
    all_posibility = math.pow(M + 1, K)
    return float(posibility) / all_posibility


def process2(hp, M, rest):
    if rest == 0:
        return 1 if hp <= 0 else 0
    if hp <= 0:
        return (M + 1)**rest
    ways = 0
    for atk in range(M + 1):
        ways += process2(hp - atk, M, rest - 1)
    return ways


def dp1(N, M, K):
    if N < 1 or M < 1 or K < 1:
        return 0
    all_posibility = math.pow(M + 1, K)
    dp = [[0] * (N + 1) for _ in range(K + 1)]
    dp[0][0] = 1
    for rest in range(1, K + 1):
        dp[rest][0] = math.pow(M + 1, rest)
        for hp in range(1, N + 1):
            ways = 0
            for atk in range(M + 1):
                if hp - atk >= 0:
                    ways += dp[rest - 1][hp - atk]
                else:
                    ways += math.pow(M + 1, rest -1)
            dp[rest][hp] = ways
    return dp[K][N] / all_posibility


def dp2(N, M, K):
    if N < 1 or M < 1 or K < 1:
        return 0
    all_posibility = math.pow(M + 1, K)
    dp = [[0] * (N + 1) for _ in range(K + 1)]
    dp[0][0] = 1
    for rest in range(1, K + 1):
        dp[rest][0] = math.pow(M + 1, rest)
        for hp in range(1, N + 1):
            # ways = 0
            # for atk in range(M + 1):
            #     if hp - atk >= 0:
            #         ways += dp[rest - 1][hp - atk]
            #     else:
            #         ways += math.pow(M + 1, rest -1)
            # dp[rest][hp] = ways
            dp[rest][hp] = dp[rest][hp - 1] + dp[rest - 1][hp]
            if hp - 1 - M >= 0:
                dp[rest][hp] -= dp[rest - 1][hp - 1 - M]
            else:
                dp[rest][hp] -= math.pow(M + 1, rest -1)
    return dp[K][N] / all_posibility


def dp3(N, M, K):
    """ 计算怪兽存活情况, all - 存活 = 死亡
    """
    if N < 1 or M < 1 or K < 1:
        return 0
    all_posibility = math.pow(M + 1, K)
    dp = [[0] * (N + 1) for _ in range(K + 1)]
    for hp in range(1, N + 1):
        dp[0][hp] = 1
    for rest in range(1, K + 1):
        for hp in range(1, N + 1):
            ways = 0
            for atk in range(M + 1):
                if hp > atk:
                    ways += dp[rest - 1][hp - atk]
            dp[rest][hp] = ways

    return (all_posibility - dp[K][N]) / all_posibility


def dp4(N, M, K):
    """ 计算怪兽存活情况, all - 存活 = 死亡
    """
    if N < 1 or M < 1 or K < 1:
        return 0
    all_posibility = math.pow(M + 1, K)
    dp = [[0] * (N + 1) for _ in range(K + 1)]
    for hp in range(1, N + 1):
        dp[0][hp] = 1
    for rest in range(1, K + 1):
        for hp in range(1, N + 1):

            # 枚举优化

            # ways = 0
            # for atk in range(M + 1):
            #     if hp > atk:
            #         ways += dp[rest - 1][hp - atk]
            # dp[rest][hp] = ways

            dp[rest][hp] = dp[rest][hp - 1] + dp[rest - 1][hp] - (dp[rest - 1][hp - 1 - M] if hp - 1 - M > 0 else 0)

    return (all_posibility - dp[K][N]) / all_posibility


if __name__ == "__main__":

    testTime = 10000
    maxM = 5
    maxN = 10
    maxK = 5
    print("测试开始")
    for i in trange(testTime):
        M = random.randint(1, maxM)
        N = random.randint(1, maxN)
        K = random.randint(1, maxK)
        ans1 = right1(N, M, K)
        ans2 = right1(N, M, K)
        ans11 = dp1(N, M, K)
        ans12 = dp2(N, M, K)
        ans13 = dp1(N, M, K)
        ans14 = dp2(N, M, K)
        if ans1 != ans2 or ans1 != ans11 or ans1 != ans12 or ans1 != ans13 or ans1 != ans14:
            print(N, M, K)
            print(ans1)
            print(ans2)
            print(ans11)
            print(ans12)
            print(ans13)
            print(ans14)
            print("test break because of error !!!")
            break
    print("测试结束")





