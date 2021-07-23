# -*- coding: utf-8 –*-

"""
这道题直接在leetcode测评：
https://leetcode.com/problems/count-of-range-sum/
"""


def countRangeSum(nums, lower, upper):
    if not nums:
        return 0
    preSum = [0] * len(nums)
    preSum[0] = nums[0]
    for i in range(1, len(nums)):
        preSum[i] = nums[i] + preSum[i - 1]
    return process(preSum, 0, len(nums) - 1, lower, upper)


def process(preSum, L, R, lower, upper):
    if L == R:
        return 1 if lower <= preSum[L] <= upper else 0
    mid = L + ((R - L) >> 1)
    ans = process(preSum, L, mid, lower, upper)
    ans += process(preSum, mid + 1, R, lower, upper)
    ans += merge(preSum, L, mid, R, lower, upper)
    return ans

#
def merge(preSum, L, M, R, lower, upper):
    ans = 0
    windowL = L
    windowR = L
    # [windowL, windowR)
    for i in range(M + 1, R + 1):
        min_ = preSum[i] - upper
        max_ = preSum[i] - lower
        while windowR <= M and preSum[windowR] <= max_:
            windowR += 1
        while windowL <= M and preSum[windowL] < min_:
            windowL += 1
        ans += windowR - windowL

    help = [0] * (R - L + 1)
    i = 0
    l = L
    r = M + 1
    while l <= M and r <= R:
        if preSum[l] <= preSum[r]:
            help[i] = preSum[l]
            l += 1
            i += 1
        else:
            help[i] = preSum[r]
            r += 1
            i += 1
    while l <= M:
        help[i] = preSum[l]
        l += 1
        i += 1
    while r <= R:
        help[i] = preSum[r]
        r += 1
        i += 1
    for i in range(len(help)):
        preSum[L + i] = help[i]

    return ans


def merge2(preSum, L, M, R, lower, upper):
    ans = 0
    windowL = L
    windowR = L
    for i in preSum[M + 1: R + 1]:
        low = i - upper
        up = i - lower
        while windowL <= M and preSum[windowL] < low:
            windowL += 1
        while windowR <= M and preSum[windowR] <= up:
            windowR += 1
        ans += windowR - windowL

    p1 = L
    p2 = M + 1
    help = []
    while p1 <= M and p2 <= R:
        if preSum[p1] <= preSum[p2]:
            help.append(preSum[p1])
            p1 += 1
        else:
            help.append(preSum[p2])
            p2 += 1

    if p1 <= M:
        help.extend(preSum[p1:M + 1])
    if p2 <= R:
        help.extend(preSum[p2:R + 1])

    for i, num in enumerate(help):
        preSum[L + i] = num

    return ans


if __name__ == "__main__":
    nums = [-2, 5, -1]
    lower = -2
    upper = 2
    ans = countRangeSum(nums, lower, upper)
    print(ans)