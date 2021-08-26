# -*- coding: utf-8 –*-

"""
给定一个二维数组matrix，其中的值不是0就是1，
返回全部由1组成的最大子矩形，内部有多少个1
"""

"""
85. 最大矩形
给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
"""


def maximalRectangle(matrix):
    if not matrix or not len(matrix[0]):
        return 0
    N = len(matrix)
    M = len(matrix[0])
    heights = [0] * M
    max_area = 0
    for i in range(N):
        for j in range(M):
            heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
        max_area = max(max_area, largestRectangleArea(heights))
    return max_area


def largestRectangleArea(heights):
    """ 单调栈
        必须以heights[i] 做高, 矩形最大面积
                    ↓
        求 heights[i] 往两边最远扩多少
    """
    if not heights:
        return 0
    max_area = 0
    stack = []
    stackk = []
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] >= h:
            pos = stack.pop()
            stackk.pop()
            left = stack[-1] + 1 if stack else 0
            # right = i - 1
            # cur_area = (right - left + 1) * heights[pos]
            # max_area = max(max_area, cur_area)
            max_area = max(max_area, (i - left) * heights[pos])
        stack.append(i)
        stackk.append(heights[i])
    n = len(heights)
    while stack:
        pos = stack.pop()
        stackk.pop()
        left = stack[-1] + 1 if stack else 0
        # right = n - 1
        # cur_area = (right - left + 1) * heights[pos]
        # max_area = max(max_area, cur_area)
        max_area = max(max_area, (n - left) * heights[pos])
    return max_area


if __name__ == "__main__":
    matrix = [["1", "0", "1", "1", "1"],
              ["0", "1", "0", "1", "0"],
              ["1", "1", "0", "1", "1"],
              ["1", "1", "0", "1", "1"],
              ["0", "1", "1", "1", "1"]]
    print maximalRectangle(matrix)
