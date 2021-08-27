# -*- coding: utf-8 –*-

"""
斐波那契数列问题
  +
快速幂
  +
递推式
"""

import time
import random
from tqdm import trange


def time_it(func):
    """ 测时间 ms
    """
    def wrapper(*args, **kwargs):
        a = time.time()
        rc = func(*args, **kwargs)
        b = time.time()
        print("{}: {} ms".format(func.__name__, (b - a) * 1000))
        return rc
    return wrapper


"""
斐波那契数列矩阵乘法方式的实现
"""


def fib1(n):
    return process(n)


def process(n):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1
    return process(n - 1) + process(n - 2)


def fib2(n):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1
    res = 1
    pre = 1
    for i in range(3, n + 1):
        pre, res = res, res + pre
    return res


def fib3(n):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1

    base = [
        [1, 1],
        [1, 0],
    ]
    res = matrix_power(base, n - 2)
    return res[0][0] + res[1][0]


"""
一个人可以一次往上迈1个台阶，也可以迈2个台阶

返回这个人迈上N级台阶的方法数
"""


def p1(n):
    if n < 0:
        return 0
    if n == 1 or n == 2:
        return n
    # return p(n - 1) + p(n - 2)
    pre = 1
    res = 2
    for _ in range(n - 2):
        res, pre = pre + res, res
    return res


def p2(n):
    if n < 0:
        return 0
    if n == 1 or n == 2:
        return n
    base = [
        [1, 1],
        [1, 0],
    ]
    res = matrix_power(base, n - 2)
    return res[0][0] * 2 + res[1][0]


"""
第一年农场有1只成熟的母牛A，往后的每年：

1）每一只成熟的母牛都会生一只母牛
2）每一只新出生的母牛都在出生的第三年成熟
3）每一只母牛永远不会死

1, 2, 3, 4, 6, 9, 13, 19...

f(n) = f(n - 1) + f(n - 3)
返回N年后牛的数量
"""


def cow1(n):
    if n < 0:
        return 0
    if n < 5:
        return n
    pre2, pre1, res = 1, 2, 3
    for _ in range(n - 3):
        res, pre1, pre2 = res + pre2, res, pre1
    return res


def cow2(n):
    if n < 0:
        return 0
    if n < 5:
        return n
    base = [
        [1, 1, 0],
        [0, 0, 1],
        [1, 0, 0],
    ]
    res = matrix_power(base, n - 3)
    return 3 * res[0][0] + 2 * res[1][0] + res[2][0]


def matrix_power(m, p):
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
        ans1 = fib1(n)
        ans2 = fib2(n)
        ans3 = fib3(n)
        if ans1 != ans2 or ans1 != ans3:
            print(n)
            print(ans1)
            print(ans2)
            print(ans3)
            print("test1 break because of error !!!")
            break
        ans1 = p1(n)
        ans2 = p2(n)
        if ans1 != ans2:
            print(n)
            print(ans1)
            print(ans2)
            print(ans3)
            print("test1 break because of error !!!")
            break
        ans1 = cow1(n)
        ans2 = cow2(n)
        if ans1 != ans2:
            print(n)
            print(ans1)
            print(ans2)
            print(ans3)
            print("test1 break because of error !!!")
            break
    print("功能测试结束")

    print("性能测试开始")
    fib1 = time_it(fib1)
    fib2 = time_it(fib2)
    fib3 = time_it(fib3)

    n = 30
    print("test {}:".format(n))
    ans1 = fib1(n)
    ans2 = fib2(n)
    ans3 = fib3(n)

    MOD = 10**9 + 7

    n = 10000
    print("test {}:".format(n))
    ans12 = fib2(n)
    ans13 = fib3(n)
    print(ans12 % MOD, ans13 % MOD)

    n = 100000
    print("test {}:".format(n))
    ans22 = fib2(n)
    ans23 = fib3(n)
    print(ans22 % MOD, ans23 % MOD)
    print("性能测试结束")

