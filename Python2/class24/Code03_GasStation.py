# -*- coding: utf-8 –*-

"""
134. 加油站
在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。
你从其中的一个加油站出发，开始时油箱为空。
如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。

说明:
    如果题目有解，该答案即为唯一答案。
    输入数组均为非空数组，且长度相同。
    输入数组中的元素均为非负数。

本题可以求出所有出发点 可以或不可以环绕一周

01:27:36
"""

from collections import deque


def canCompleteCircuit(gas, cost):
    goods = goodArray(gas, cost)
    for i, good in enumerate(goods):
        if good:
            return i
    return -1


def goodArray(gas, cost):
    N = len(gas)
    M = N << 1
    arr = [0] * M

    for i in range(N):
        arr[i] = gas[i] - cost[i]
        arr[i + N] = gas[i] - cost[i]

    # 两倍长度的 复合型前缀和数组
    for i in range(1, M):
        arr[i] += arr[i - 1]

    w = deque()
    for i in range(N):
        while w and arr[w[-1]] >= arr[i]:
            w.pop()
        w.append(i)

    ans = [False] * N
    for j in range(N, M):
        i = j - N
        offset = arr[i - 1] if i else 0
        if arr[w[0]] - offset >= 0:
            ans[i] = True
        if w[0] == i:
            w.popleft()
        while w and arr[w[-1]] >= arr[j]:
            w.pop()
        w.append(j)
    return ans


if __name__ == "__main__":
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    ans = canCompleteCircuit(gas, cost)
    print ans