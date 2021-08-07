# -*- coding: utf-8 –*-

"""
假设有排成一行的 N 个位置，记为1~N，N 一定大于或等于 2
开始时机器人在其中的 M 位置上(M 一定是 1~N 中的一个)
如果机器人来到1位置，那么下一步只能往右来到2位置；
如果机器人来到N位置，那么下一步只能往左来到 N-1 位置；
如果机器人来到中间位置，那么下一步可以往左走或者往右走；
规定机器人必须走 K 步，最终能来到 P 位置(P也是1~N中的一个)的方法有多少种
给定四个参数 N、M、K、P，返回方法数。
"""


def ways1(N, start, aim, k):
    """ 纯暴力递归
    """
    if N < 2 or start < 1 or start > N or aim < 1 or aim > N or k < 0:
        return -1
    return process1(start, k, aim, N)


def process1(cur, rest, aim, N):
    """
    机器人当前来到的位置是cur，
    机器人还有rest步需要去走，
    最终的目标是aim，
    有哪些位置？1~N
    返回：机器人从cur出发，走过rest步之后，最终停在aim的方法数，是多少？
    """
    if rest == 0:
        return 1 if cur == aim else 0
    if cur == 1:
        return process1(cur + 1, rest - 1, aim, N)
    elif cur == N:
        return process1(cur - 1, rest - 1, aim, N)
    return process1(cur + 1, rest - 1, aim, N) + process1(cur - 1, rest - 1, aim, N)


def ways2(N, start, aim, k):
    """ 傻缓存
    """
    if N < 2 or start < 1 or start > N or aim < 1 or aim > N or k < 0:
        return -1
    dp = [[-1] * (k + 1) for _ in range(N + 1)]
    return process2(start, k, aim, N, dp)


def process2(cur, rest, aim, N, dp):
    """
    机器人当前来到的位置是cur，
    机器人还有rest步需要去走，
    最终的目标是aim，
    有哪些位置？1~N
    返回：机器人从cur出发，走过rest步之后，最终停在aim的方法数，是多少？
    """
    if dp[cur][rest] != -1:
        return dp[cur][rest]
    if rest == 0:
        ans = 1 if cur == aim else 0
    elif cur == 1:
        ans = process1(cur + 1, rest - 1, aim, N)
    elif cur == N:
        ans = process1(cur - 1, rest - 1, aim, N)
    else:
        ans = process1(cur + 1, rest - 1, aim, N) + process1(cur - 1, rest - 1, aim, N)
    dp[cur][rest] = ans
    return ans


def ways3(N, start, aim, k):
    dp = [[0] * (k + 1) for _ in range(N + 1)]
    dp[start][0] = 1
    for j in range(1, k + 1):
        dp[1][j] = dp[2][j - 1]
        for i in range(2, N):
            dp[i][j] = dp[i - 1][j - 1] + dp[i + 1][j - 1]
        dp[N][j] = dp[N - 1][j - 1]
    return dp[aim][k]


if __name__ == "__main__":
    N = 10  # 格子总数
    M = 1  # 初始位置
    K = 10  # 走K步
    P = 5  # 目标位置
    ans1 = ways1(N, M, P, K)
    ans2 = ways2(N, M, P, K)
    ans3 = ways3(N, M, P, K)
    print(ans1, ans2, ans3)
