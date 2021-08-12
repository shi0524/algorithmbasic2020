# -*- coding: utf-8 –*-


"""
516. 最长回文子序列
给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。
"""


def lpsl1(s):
    if not s:
        return 0
    return process(s, 0, len(s) - 1)


def process(s, L, R):
    if L == R:
        return 1
    if L == R - 1:
        return 2 if s[L] == s[R] else 1
    p1 = process(s, L + 1, R - 1)
    p2 = process(s, L + 1, R)
    p3 = process(s, L, R - 1)
    p4 = process(s, L + 1, R - 1) + 2 if s[L] == s[R] else 0
    return max(p1, p2, p3, p4)


def lpsl2(s):
    if not s:
        return 0
    N = len(s)
    dp = [[0] * N for _ in range(N)]
    # 先把对角线的base case 填好
    dp[N - 1][N - 1] = 1
    for L in range(N - 1):
        dp[L][L] = 1
        dp[L][L + 1] = 2 if s[L] == s[L + 1] else 1
    # 可以斜对角线填dp表
    # 也可以从下往上 从左往右填
    for L in range(N - 3, -1, -1):
        for R in range(L + 2, N):
            # p1 = dp[L + 1][R - 1]
            # p2 = dp[L + 1][R]
            # p3 = dp[L][R - 1]
            # p4 = dp[L + 1][R - 1] + 2 if s[L] == s[R] else 0
            # dp[L][R] = max(p1, p2, p3, p4)

            # 根据位置依赖关系, 可得知, p2 >= p1  p3 >= p1, 故p1情况可不考虑
            p2 = dp[L + 1][R]
            p3 = dp[L][R - 1]
            p4 = dp[L + 1][R - 1] + 2 if s[L] == s[R] else 0
            dp[L][R] = max(p2, p3, p4)
    return dp[0][N - 1]


"""
其它思路：

可将 s 反转得 s' 求, s 与 s' 的最长公共子序列
求最长公共子序列方法详见 class19/Code04_LongestCommonSubsequence.py
"""


if __name__ == "__main__":
    s = "abcba"
    ans1 = lpsl1(s)
    ans2 = lpsl2(s)
    print(ans1, ans2)
