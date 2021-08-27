# -*- coding: utf-8 –*-

"""
给定一个数N，想象只由0和1两种字符，组成的所有长度为N的字符串
如果某个字符串,任何0字符的左边都有1紧挨着,认为这个字符串达标
返回有多少达标的字符串
"""
import random
from tqdm import trange


def get_num1(n):
    if n < 1:
        return 0
    return process(1, n)


def process(i, n):
    if i == n - 1:
        return 2
    if i == n:
        return 1
    return process(i + 1, n) + process(i + 2, n)


def get_num2(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    pre, cur = 1, 1
    for _ in range(n - 1):
        cur, pre = pre + cur, cur
    return cur


def get_num3(n):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return n
    base = [
        [1, 1],
        [1, 0],
    ]
    res = matrix_power(base, n - 2)
    return 2 * res[0][0] + res[1][0]


"""
用1*2的瓷砖，把N*2的区域填满
返回铺瓷砖的方法数

类似斐波那锲数列递推式 f(n) = f(n - 1) + f(n - 2)
"""


def matrix_power(m, p):
    """ 矩阵快次幂
    :param m: 矩阵
    :param p: 幂次
    :return:
    """
    N = len(m)
    # 单位矩阵
    res = [[0] * N for _ in range(N)]
    for i in range(N):
        res[i][i] = 1

    # 矩阵1次方
    t = m
    while p:
        if p & 1:
            res = muli_matrix(res, t)
        p >>= 1
        t = muli_matrix(t, t)
    return res


def muli_matrix(m1, m2):
    """ 两个矩阵相乘
    """
    row = len(m1)
    col = len(m2[0])
    N2 = len(m2)
    res = [[0] * col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            for k in range(N2):
                res[i][j] += m1[i][k] * m2[k][j]
    return res


if __name__ == "__main__":

    maxValue = 20
    testTime = 10000
    print("功能测试开始")
    for i in trange(testTime):
        n = random.randint(1, maxValue)
        ans1 = get_num1(n)
        ans2 = get_num2(n)
        ans3 = get_num3(n)
        if ans1 != ans2 or ans1 != ans3:
            print(n)
            print(ans1)
            print(ans2)
            print(ans3)
            print("test1 break because of error !!!")
            break
    print("功能测试结束")