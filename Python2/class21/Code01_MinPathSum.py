# -*- coding: utf-8 –*-

"""
给定一个二维数组matrix，一个人必须从左上角出发，最后到达右下角
沿途只可以向下或者向右走，沿途的数字都累加就是距离累加和
返回最小距离累加和
"""
import random


def min_path_sum1(m):
    if not m or not len(m[0]):
        return 0

    row = len(m)
    col = len(m[0])
    dp = [[0] * col for _ in range(row)]
    dp[0][0] = m[0][0]
    for r in range(1, row):
        dp[r][0] = dp[r - 1][0] + m[r][0]
    for c in range(1, col):
        dp[0][c] = dp[0][c - 1] + m[0][c]
    for r in range(1, row):
        for c in range(1, col):
            dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + m[r][c]
    return dp[row - 1][col - 1]


def min_path_sum2(m):
    """ 将 m * n 矩阵压缩成 n 长度数组
    """
    if not m or not len(m[0]):
        return 0

    row = len(m)
    col = len(m[0])
    arr = [0] * col
    arr[0] = m[0][0]
    for c in range(1, col):
        arr[c] = arr[c - 1] + m[0][c]
    for r in range(1, row):
        arr[0] += m[r][0]
        for c in range(1, col):
            arr[c] = min(arr[c - 1], arr[c]) + m[r][c]
    return arr[col - 1]


def generateRandomMatrix(row_size, col_size):
    if not row_size or not col_size:
        return []
    return [[random.randint(1, 100) for _ in range(col_size)] for _ in range(row_size)]


if __name__ == "__main__":
    test_time = 1000
    row_size = 100
    col_size = 100
    print("test begin !!!")
    for _ in range(test_time):
        m = generateRandomMatrix(row_size, col_size)
        ans1 = min_path_sum1(m)
        ans2 = min_path_sum2(m)
        if ans1 != ans2:
            print(ans1, ans2)
            print("test break because of error !!!")
            break
    print("test end !!!")

