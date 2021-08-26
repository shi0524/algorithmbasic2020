# -*- coding: utf-8 –*-

"""
给定一个非负数组arr，代表直方图
返回直方图的最大长方形面积
"""
"""
84. 柱状图中最大的矩形
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。
"""


import random
from tqdm import trange


def largestRectangleArea1(height):
    """ 单调栈
        必须以height[i] 做高, 矩形最大面积
                    ↓
        求 height[i] 往两边最远扩多少
    """
    if not height:
        return 0
    area = 0
    stack = []
    for i, h in enumerate(height):
        while stack and stack[-1] >= h:
            pos = stack.pop()
            right = i - 1
            left = stack[-1] + 1 if stack else 0
            bottom = right - left + 1
            area = max(area, bottom * height[pos])
    n = len(height)
    while stack:
        pos = stack.pop()
        right = n - 1
        left = stack[-1] + 1 if stack else 0
        bottom = right - left + 1
        area = max(area, bottom * height[pos])
    return area


def largestRectangleArea2(height):
    if not height:
        return 0
    n = len(height)
    stack = [0] * n
    si = -1
    max_area = 0
    for i in range(n):
        while si != -1 and height[i] <= height[stack[si]]:
            j = stack[si]
            si -= 1
            k = -1 if si == -1 else stack[si]
            cur_area = (i - k - 1) * height[j]
            max_area = max(max_area, cur_area)
        si += 1
        stack[si] = i
    while si != -1:
        j = stack[si]
        si -= 1
        k = -1 if si == -1 else stack[si]
        cur_area = (n - 1 - k) * height[j]
        max_area = max(max_area, cur_area)
    return max_area


# for test
def generateNoReapteRandomArray(maxSize, maxValue):
    """
    :param maxSize:
    :param maxValue:
    :return:
    """
    return [random.randint(1, maxValue) for _ in xrange(maxSize)]


if __name__ == "__main__":
    maxSize = 100
    maxValue = 50
    testTime = 10000
    print("测试开始")
    for i in trange(testTime):
        arr = generateNoReapteRandomArray(maxSize, maxValue)
        ans1 = largestRectangleArea1(arr)
        ans2 = largestRectangleArea1(arr)
        if ans1 != ans2:
            print(arr)
            print(ans1)
            print(ans2)
            print("test1 break because of error !!!")
            break
    print("测试结束")
