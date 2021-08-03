# -*- coding: utf-8 –*-

"""
贪心算法

一块金条切成两半，是需要花费和长度数值一样的铜板的。
比如长度为20的金条，不管怎么切，都要花费20个铜板。 一群人想整分整块金条，怎么分最省铜板?

例如,给定数组{10,20,30}，代表一共三个人，整块金条长度为60，金条要分成10，20，30三个部分。

如果先把长度60的金条分成10和50，花费60; 再把长度50的金条分成20和30，花费50;一共花费110铜板。
但如果先把长度60的金条分成30和30，花费60;再把长度30金条分成10和20， 花费30;一共花费90铜板。
输入一个数组，返回分割的最小代价。
"""
import heapq
import random


def less_money1(arr):
    """ 纯暴力
    """
    if not arr:
        return 0
    return process(arr, 0)


def process(arr, pre):
    """
    等待合并的数都在arr里，pre之前的合并行为产生了多少总代价
    arr中只剩一个数字的时候，停止合并，返回最小的总代价
    """
    if len(arr) == 1:
        return pre
    ans = float('inf')
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            ans = min(ans, process(copyAndMergeTwo(arr, i, j), pre + arr[i] + arr[j]))
    return ans


def copyAndMergeTwo(arr, i, j):
    """
    复制列表,
    将i和j位置的元素取出并删除，
    将其和加入复制列表中
    """
    ans = arr[::]
    num1 = ans[i]
    num2 = ans[j]
    ans.remove(num1)
    ans.remove(num2)
    ans.append(num1 + num2)
    return ans


def less_money2(arr):
    """ 用小根堆来实现
    将要分割结果放入堆中
    弹出2个小值, 合成1个大值, 放回堆中
    直到堆中只剩1个值, 则为最初始长度,
    整个合并过程为最经济分割过程的逆序
    """
    heapq.heapify(arr)
    money = 0
    while len(arr) > 1:
        cur = heapq.heappop(arr) + heapq.heappop(arr)
        money += cur
        heapq.heappush(arr, cur)
    return money


def generateRandomArray(arrlen, max_value):
    """ 生成会议列表
    """
    alen = random.randint(1, arrlen)
    return [random.randint(1, max_value) for _ in range(alen)]


if __name__ == "__main__":
    arrlen = 10
    max_value = 50
    test_times = 100000
    print('test begin !!!')
    for _ in range(test_times):
        arr = generateRandomArray(arrlen, max_value)
        ans1 = less_money1(arr[::])
        ans2 = less_money2(arr[::])
        if ans1 != ans2:
            print()
            print(ans1, ans2)
            print("test break because of error !!!")
            break
    print("test end !!!")
