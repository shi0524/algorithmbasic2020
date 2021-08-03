# -*- coding: utf-8 –*-

"""
贪心算法

输入: 正数数组costs、正数数组profits、正数K、正数M
costs[i]表示i号项目的花费
profits[i]表示i号项目在扣除花费之后还能挣到的钱(利润)
K表示你只能串行的最多做k个项目
M表示你初始的资金
说明: 每做完一个项目，马上获得的收益，可以支持你去做下一个项目。不能并行的做项目。
输出：你最后获得的最大钱数。
"""

from Queue import PriorityQueue


def findMaximizedCapital(K, W, profits, costs):
    minCostQ = PriorityQueue()      # 花费小根堆
    maxProfitQ = PriorityQueue()    # 利润大根堆(PriorityQueue 是小根堆, 转换成负值, 当大根堆使用)
    for i in range(len(profits)):
        minCostQ._put((costs[i], profits[i]))

    i = 0
    while i < K:
        while minCostQ.queue and minCostQ.queue[0][0] < W:
            item = minCostQ._get()
            maxProfitQ._put(-item[1])
        if not maxProfitQ.queue:
            return W
        # W += -maxProfitQ._get()   # 加一个 负的 负值  相当于 减一个 负值
        W -= maxProfitQ._get()
    return W

