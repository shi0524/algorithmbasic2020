# -*- coding: utf-8 –*-

"""
给定5个参数，N，M，row，col，k
表示在N*M的区域上，醉汉Bob初始在(row,col)位置
Bob一共要迈出k步，且每步都会等概率向上下左右四个方向走一个单位
任何时候Bob只要离开N*M的区域，就直接死亡
返回k步之后，Bob还在N*M的区域的概率
"""
import random
from tqdm import trange


def livePosibility1(row, col, k, N, M):
    return process(row, col, k, N, M)


def process(i, j, rest, N, M):
    if i < 0 or i == N or j < 0 or j == M:
        return 0
    if rest == 0:
        return 1
    ans  = process(i - 1, j, rest - 1, N, M)
    ans += process(i + 1, j, rest - 1, N, M)
    ans += process(i, j - 1, rest - 1, N, M)
    ans += process(i, j + 1, rest - 1, N, M)
    return ans


def livePosibility2(row, col, k, N, M):
    dp = [[[0] * (k + 1) for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            dp[i][j][0] = 1
    for rest in range(1, k + 1):
        for i in range(N):
            for j in range(M):
                dp[i][j][rest] += pick(dp, N, M, i - 1, j, rest - 1)
                dp[i][j][rest] += pick(dp, N, M, i + 1, j, rest - 1)
                dp[i][j][rest] += pick(dp, N, M, i, j - 1, rest - 1)
                dp[i][j][rest] += pick(dp, N, M, i, j + 1, rest - 1)

    return dp[row][col][k]


def pick(dp, N, M, i, j, rest):
    if i < 0 or i == N or j < 0 or j == M:
        return 0
    return dp[i][j][rest]


def livePosibility3(row, col, k, N, M):
    dp = [[[0] * M for _ in range(N)] for _ in range(k + 1)]
    for i in range(N):
        for j in range(M):
            dp[0][i][j] = 1
    for rest in range(1, k + 1):
        for i in range(N):
            for j in range(M):
                for ii, jj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= ii < N and 0 <= jj < M:
                        dp[rest][i][j] += dp[rest - 1][ii][jj]

    return dp[k][row][col]


if __name__ == "__main__":
    testTime = 1000
    maxM = 10
    maxN = 10
    maxK = 10
    print("测试开始")
    for i in trange(testTime):
        M = random.randint(1, maxM)
        N = random.randint(1, maxN)
        k = random.randint(1, maxK)
        row = random.randint(0, N - 1)
        col = random.randint(0, M - 1)
        ans1 = livePosibility1(row, col, k, N, M)
        ans2 = livePosibility2(row, col, k, N, M)
        ans3 = livePosibility3(row, col, k, N, M)
        if ans1 != ans2 or ans1 != ans3:
            print(row, col, k, N, M)
            print(ans1)
            print(ans2)
            print(ans3)
            print("test break because of error !!!")
            break
    print("测试结束")

