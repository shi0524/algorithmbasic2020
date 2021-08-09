# -*- coding: utf-8 –*-

"""
给定两个长度都为N的数组weights和values，
weights[i]和values[i]分别代表 i号物品的重量和价值。
给定一个正数bag，表示一个载重bag的袋子，
你装的物品不能超过这个重量。
返回你能装下最多的价值是多少?
为了方便，其中没有负数
"""


def max_value(w, v, bag):
    if not w or not v or len(w) != len(v):
        return 0
    return process(w, v, 0, bag)


def process(w, v, index, rest):
    if rest < 0:
        return -1
    if index == len(w):
        return 0
    p1 = process(w, v, index + 1, rest)
    p2 = 0
    nexts = process(w, v, index + 1, rest - w[index])
    if nexts != -1:
        p2 = v[index] + nexts
    return max(p1, p2)


def max_value_dp(w, v, bag):
    if not w or not v or len(w) != len(v):
        return 0
    n = len(w)
    dp = [[0] * (bag + 1) for _ in range(n + 1)]
    for index in range(n - 1, -1, -1):
        for rest in range(0, bag + 1):
            p1 = dp[index + 1][rest]
            p2 = dp[index + 1][rest - w[index]] + v[index] if rest - w[index] >= 0 else -1
            dp[index][rest] = max(p1, p2) if p2 != -1 else p1
    return dp[0][bag]


if __name__ == "__main__":
    weights = [3, 2, 4, 7, 3, 1, 7]
    values = [5, 6, 3, 19, 12, 4, 2]
    bag = 15
    ans1 = max_value(weights, values, bag)
    ans2 = max_value_dp(weights, values, bag)
    print(ans1, ans2)

