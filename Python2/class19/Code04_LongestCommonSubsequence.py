# -*- coding: utf-8 –*-

"""
给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-subsequence
"""


def longestCommonSubsequence1(s1, s2):
    if not s1 or not s2:
        return 0
    return process1(s1, s2, len(s1) - 1, len(s2) - 1)


def process1(s1, s2, i, j):
    if i == 0 and j == 0:
        return 1 if s1[0] == s2[0] else 0
    elif i == 0:
        if s1[0] == s2[j]:
            return 1
        return process1(s1, s2, i, j - 1)
    elif j == 0:
        if s1[i] == s2[j]:
            return 1
        return process1(s1, s2, i - 1, j)
    else:
        p1 = process1(s1, s2, i - 1, j)
        p2 = process1(s1, s2, i, j - 1)
        p3 = process1(s1, s2, i - 1, j - 1) + 1 if s1[i] == s2[j] else 0
    return max(p1, p2, p3)


def longestCommonSubsequence2(s1, s2):
    if not s1 or not s2:
        return 0
    N = len(s1)
    M = len(s2)
    dp = [[0] * M for _ in range(N)]
    if s1[0] == s2[0]:
        dp[0][0] = 1
    for i in range(1, N):
        dp[i][0] = 1 if s1[i] == s2[0] else dp[i - 1][0]
    for j in range(1, M):
        dp[0][j] = 1 if s1[0] == s2[j] else dp[0][j - 1]
    for i in range(1, N):
        for j in range(1, M):
            p1 = dp[i - 1][j]
            p2 = dp[i][j - 1]
            p3 = dp[i - 1][j - 1] + 1 if s1[i] == s2[j] else 0
            dp[i][j] = max(p1, p2, p3)
    return dp[N - 1][M - 1]


if __name__ == "__main__":
    s1 = "abcde"
    s2 = "ace"
    ans1 = longestCommonSubsequence1(s1, s2)
    ans2 = longestCommonSubsequence2(s1, s2)
    print(ans1, ans2)
