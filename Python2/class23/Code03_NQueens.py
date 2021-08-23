# -*- coding: utf-8 –*-

import time


def time_it(func):
    """ 测时间 ms
    """
    def wrapper(*args, **kwargs):
        a = time.time()
        rc = func(*args, **kwargs)
        b = time.time()
        print("{} ms".format((b - a) * 1000))
        return rc
    return wrapper


@time_it
def num1(n):
    record = [0] * n
    return process1(0, record, n)


def process1(i, record, n):
    """
    当前来到i行, 一共是 0 ~ n-1 行
    在 i 行上上皇后, 所有列都尝试
    必须要保证跟之前所有的皇后都不打架
    record[i] = j 第i行的皇后放在了j列上
    返回不管 i 以上发生了什么, i... n-1有多少合法的方法数
    """
    if i == n:
        return 1
    ans = 0
    for j in range(n):
        if is_valid(record, i, j):
            record[i] = j
            ans += process1(i + 1, record, n)
    return ans


def is_valid(record, i, j):
    for k in range(i):
        if j == record[k] or abs(record[k] - j) == abs(k - i):
            return False
    return True


@time_it
def num2(n):
    """ 不超过32位
    """
    if n < 1 or n > 32:
        return 0

    limit = (1 << n) - 1 if n < 32 else -1
    return process2(limit, 0, 0, 0)


def process2(limit, col_lim, left_dia_lim, right_dia_lim):

    # n个位置全部使用完，表示放完了
    if col_lim == limit:
        return 1

    # col_lim | left_dia_lim | right_dia_lim  所有不可使用的位置
    # ~(col_lim | left_dia_lim | right_dia_lim) 除去边界左边的1, 所有可以使用的位置
    # limit & (~(col_lim | left_dia_lim | right_dia_lim)) 将边界左边的1全部除去, 只剩余可以使用的位置
    pos = limit & (~(col_lim | left_dia_lim | right_dia_lim))
    ans = 0
    while pos:
        # 取 pos 最右的1
        most_right_one = pos & (~pos + 1)
        pos -= most_right_one
        ans += process2(
            limit,
            col_lim | most_right_one,
            (left_dia_lim | most_right_one) << 1,
            (right_dia_lim | most_right_one) >> 1
        )
    return ans


if __name__ == "__main__":
    n = 10
    ans2 = num2(n)
    ans1 = num1(n)
    print(ans1, ans2)



