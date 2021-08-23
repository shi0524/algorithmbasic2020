# -*- coding: utf-8 –*-

"""
假设一个固定大小为W的窗口，依次划过arr，
返回每一次滑出状况的最大值
例如，arr = [4,3,5,4,3,3,6,7], W = 3
返回：[5,5,5,4,6,7]
"""

import random
from collections import deque


def right(arr, w):
    """ 对数器
    """
    if not arr or w < 1:
        return []
    n = len(arr)
    ans = []
    L = 0
    R = w - 1
    while R < n:
        ans.append(max(arr[L: R + 1]))
        R += 1
        L += 1
    return ans


def getMaxWindow(arr, w):
    if not arr or w < 1:
        return []
    n = len(arr)
    # 双端队列, 存维护最大值数据索引
    queue = deque()
    ans = []
    for R in range(n):
        # 如果队列不为空 且 最右位置对应值小于R的对应值, 弹出
        while queue and arr[queue[-1]] <= arr[R]:
            queue.pop()
        # 将R加入
        queue.append(R)
        # 如果开始位置过期, 则弹出
        if queue[0] == R - w:
            queue.popleft()
        # 如果R索引超过w-1, 说明每滑动一次, 收集一个答案
        if R >= w - 1:
            ans.append(arr[queue[0]])
    return ans


# for test
def generateRandomArray(maxSize, maxValue):
    """
    :param maxSize:
    :param maxValue:
    :return:
    """
    return [random.randint(0, maxValue) for _ in xrange(maxSize)]


if __name__ == "__main__":
    test_time = 10000
    maxSize = 1000
    maxValue = 100
    maxWindow = 10
    print("test begin !!!")
    for _ in range(test_time):
        arr = generateRandomArray(maxSize, maxValue)
        w = random.randint(1, maxWindow)
        ans1 = right(arr, w)
        ans2 = getMaxWindow(arr, w)
        if ans1 != ans2:
            print(ans1, ans2)
            print("test break because of error !!!")
            break
    print("test end !!!")




