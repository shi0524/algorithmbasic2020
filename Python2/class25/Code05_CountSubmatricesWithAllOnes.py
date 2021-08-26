# -*- coding: utf-8 –*-

"""
给定一个二维数组matrix，其中的值不是0就是1，
返回全部由1组成的子矩形数量
"""
"""
1504. 统计全 1 子矩形
给你一个只包含 0 和 1 的 rows * columns 矩阵 mat ，
请你返回有多少个 子矩形 的元素全部都是 1 。

思路：
    矩阵压缩
    以 第1行做底的矩阵数量
    以 第2行做底的矩阵数量
    ...
    以 第n行做底的矩阵数量
    
    单调栈
    计算矩阵数量
"""


def numSubmat(mat):
    if not mat or not len(mat):
        return 0
    nums = 0
    N = len(mat)
    M = len(mat[0])
    heights = [0] * M
    for i in range(N):
        for j in range(M):
            heights[j] = heights[j] + 1 if mat[i][j] == '1' else 0
        nums += countFromBottom(heights)
    return nums


def countFromBottom(heights):
    n = len(heights)
    stack = []
    ans = 0
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] >= h:
            pos = stack.pop()
            left = stack[-1] if stack else -1
            lh = 0 if left == -1 else heights[left]
            max_h = max(lh, h)
            max_w = i - left - 1
            ans += (heights[pos] - max_h) * num(max_w)
        stack.append(i)
    while stack:
        pos = stack.pop()
        left = stack[-1] if stack else -1
        lh = 0 if left == -1 else heights[left]
        max_h = max(lh, 0)
        max_w = n - 1 - left - 1
        ans += (heights[pos] - max_h) * num(max_w)
    return ans


def num(n):
    return (n * (n + 1)) >> 1


if __name__ == "__main__":

    matrix = [["1", "0", "1"],
              ["1", "1", "0"]]
    print numSubmat(matrix)

    matrix = [["1", "0", "1", "1", "1"],
              ["0", "1", "0", "1", "0"],
              ["1", "1", "0", "1", "1"],
              ["1", "1", "0", "1", "1"],
              ["0", "1", "1", "1", "1"]]

    print numSubmat(matrix)