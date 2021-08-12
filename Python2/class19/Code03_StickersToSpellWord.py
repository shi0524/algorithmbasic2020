# -*- coding: utf-8 –*-

"""
691. 贴纸拼词

我们给出了 N 种不同类型的贴纸。每个贴纸上都有一个小写的英文单词。
你希望从自己的贴纸集合中裁剪单个字母并重新排列它们，从而拼写出给定的目标字符串 target。
如果你愿意的话，你可以不止一次地使用每一张贴纸，而且每一张贴纸的数量都是无限的。
拼出目标 target 所需的最小贴纸数量是多少？如果任务不可能，则返回 -1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/stickers-to-spell-word
"""

from collections import defaultdict


def minStickers1(stickers, target):
    """ 暴力递归
    :param stickers: 贴纸
    :param target: 目标
    :return:
    """
    if not target:
        return 0
    ans = process1(stickers, target)
    return -1 if ans == float('inf') else ans


def process1(stickers, target):
    """ 所有贴纸, 每种都有无穷张, 每种都去试, 最少张数
    """
    if not target:
        return 0
    min_ = float('inf')
    for s in stickers:
        rest = minus(target, s)
        if len(rest) != len(target):
            min_ = min(min_, process1(stickers, rest))
    return min_ + 1


def minus(target, s):
    t_d = defaultdict(int)
    for t in target:
        t_d[t] += 1
    for s_ in s:
        t_d[s_] -= 1
    lst = [k * v for k, v in t_d.iteritems() if v > 0]
    return "".join(lst)


def minStickers2(stickers, target):
    """ 暴力递归 + 剪枝
    :param stickers: 贴纸
    :param target: 目标
    :return:
    """
    if not target:
        return 0
    counts = []
    for sticker in stickers:
        s_count = defaultdict(int)
        for s in sticker:
            s_count[s] += 1
        counts.append(dict(s_count))
    ans = process2(counts, target)
    return -1 if ans == float('inf') else ans


def process2(stickers, target):
    if not target:
        return 0
    t_d = {}
    for t in target:
        if t in t_d:
            t_d[t] += 1
        else:
            t_d[t] = 1
    min_ = float('inf')
    for sticker in stickers:
        # 按目标字符串第一个字符试, 如果不存在, continue (肯定会遇到，只是顺序不一样而已)
        if target[0] not in sticker:
            continue
        lst = []
        for k, v in t_d.iteritems():
            if k in sticker:
                lst.append(k * max(v - sticker[k], 0))
            else:
                lst.append(k * v)
        min_1 = process2(stickers, "".join(lst))
        min_ = min(min_, min_1)
    return min_ + 1


def minStickers3(stickers, target):
    """ 暴力递归 + 剪枝 + 傻缓存
    :param stickers: 贴纸
    :param target: 目标
    :return:
    """
    if not target:
        return 0
    dp = {"": 0}
    counts = []
    for sticker in stickers:
        s_count = defaultdict(int)
        for s in sticker:
            s_count[s] += 1
        counts.append(dict(s_count))
    ans = process3(counts, target, dp)
    return -1 if ans == float('inf') else ans


def process3(stickers, target, dp):
    if target in dp:
        return dp[target]
    t_d = {}
    for t in target:
        if t in t_d:
            t_d[t] += 1
        else:
            t_d[t] = 1
    min_ = float('inf')
    for sticker in stickers:
        if target[0] not in sticker:
            continue
        lst = []
        for k, v in t_d.iteritems():
            if k in sticker:
                lst.append(k * max(v - sticker[k], 0))
            else:
                lst.append(k * v)
        min_1 = process3(stickers, "".join(lst), dp)
        min_ = min(min_, min_1)
    ans = min_ + 1
    dp[target] = ans
    return ans


if __name__ == "__main__":
    target = 'abcdeefg'
    stickers = ['ab', 'cd', 'acd', 'be', 'afg']
    ans1 = minStickers1(stickers, target)
    ans2 = minStickers2(stickers, target)
    ans3 = minStickers3(stickers, target)
    print(ans1, ans2, ans3)


