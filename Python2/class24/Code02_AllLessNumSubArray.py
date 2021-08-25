# -*- coding: utf-8 –*-

"""
给定一个整型数组arr，和一个整数num
某个arr中的子数组sub，如果想达标，必须满足：
sub中最大值 – sub中最小值 <= num，
返回arr中达标子数组的数量
"""
import time
import random
from tqdm import trange
from collections import deque


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


# @time_it
def right(arr, num):
    """ 暴力解, 绝对正确, 做对数器用
    :param arr:
    :param num:
    :return:
    """
    if not arr or num < 0:
        return 0
    n = len(arr)
    ans = 0
    for L in range(n):
        for R in range(L, n):
            min_num = min(arr[L: R + 1])
            max_num = max(arr[L: R + 1])
            if max_num - min_num <= num:
                ans += 1
    return ans


# @time_it
def sub_arr_num(arr, num):
    """
    滑动窗口 + 贪心
    小贪心:
        一个窗口的最大(小)值不会随着窗口的扩大而变小(大), 只可能越来越大(小)
        一个窗口的最大(小)值不会随着窗口的缩小而变大(小), 只可能越来越小(大)
    思路:
        如果一个子数组达标，那么该子数组的子数组也达标
        计算以L开头的数组
        窗口R扩到不能再扩(如果窗口左闭右开)
        则以L开头的数组个数为 R - L
    """
    if not arr or num < 0:
        return 0
    n = len(arr)
    ans = 0
    max_window = deque()
    min_window = deque()

    # 窗口范围左闭右开 [L, R)
    R = 0
    for L in range(n):
        # L ... R(初次不达标了, 停)
        while R < n:
            while max_window and arr[max_window[-1]] <= arr[R]:
                max_window.pop()
            max_window.append(R)
            while min_window and arr[min_window[-1]] >= arr[R]:
                min_window.pop()
            min_window.append(R)
            if arr[max_window[0]] - arr[min_window[0]] > num:
                break
            R += 1
        ans += (R - L)
        # L 马上要 +1 了, 检查窗口最大值最小值是否过期
        if max_window[0] == L:
            max_window.popleft()
        if min_window[0] == L:
            min_window.popleft()
    return ans


# for test
def generateRandomArray(maxSize, maxValue):
    """
    :param maxSize:
    :param maxValue:
    :return:
    """
    return [random.randint(-maxValue, maxValue) for _ in xrange(maxSize)]


if __name__ == "__main__":
    test_time = 1000
    maxSize = 100
    maxValue = 10
    maxNum = 100
    print("test begin !!!")
    for _ in trange(test_time):
        arr = generateRandomArray(maxSize, maxValue)
        num = random.randint(1, maxNum)
        ans1 = right(arr, num)
        ans2 = sub_arr_num(arr, num)
        if ans1 != ans2:
            print(arr)
            print(num)
            print(ans1, ans2)
            print("test break because of error !!!")
            break
    print("test end !!!")



