# -*- coding: utf-8 –*-

import random

"""
基数排序 (only for no-negative value)
"""


def radix_sort(arr):
    if not arr or len(arr) < 2:
        return
    radix_sort_process(arr, 0, len(arr) - 1, maxbits(arr))


def maxbits(arr):
    maxbit = 0
    maxnum = max(arr)
    while maxnum:
        maxbit += 1
        maxnum /= 10
    return maxbit


def radix_sort_process(arr, L, R, digit):
    """ arr 在[L, R]上排序
    :param arr:
    :param L:
    :param R:
    :param digit: 最大值的十进位数 digit
    :return:
    """
    # 十进位
    radix = 10
    help = [0] * (R - L + 1)
    for d in range(1, digit + 1):
        # 10个空间
        # count[0] 当前位(d位)是0的数字有多少
        # count[1] 当前位(d位)是0 ~ 1的数字有多少
        # count[i] 当前位(d位)是0 ~ i的数字有多少
        count = [0] * radix

        # 先求词频
        for num in arr:
            j = get_digit(num, d)
            count[j] += 1
        # 再求前缀和
        for i in range(1, radix):
            count[i] = count[i] + count[i-1]

        # 将数字有序倒入help数组
        for i in range(R, L - 1, -1):
            j = get_digit(arr[i], d)
            help[count[j] - 1] = arr[i]
            count[j] -= 1
        # 将help数组数字拷贝回原数组
        for i, num in enumerate(help, start=L):
            arr[i] = num


def get_digit(num, digit):
    """ 从后往前，num 第 digit 位数字
    :param num: 数字
    :param d: 第 d 位
    :return:
    """
    return num / pow(10, digit - 1) % 10


# for test
def generateRandomArray(maxSize, maxValue):
    """
    :param maxSize:
    :param maxValue:
    :return:
    """
    return [random.randint(1, maxValue) for _ in xrange(maxSize)]


if __name__ == "__main__":
    testTime = 500000
    maxSize = 100
    maxValue = 100000
    print("test begin !!!")
    for _ in range(testTime):
        arr = generateRandomArray(maxSize, maxValue)
        arr1 = arr[::]
        arr2 = arr[::]
        radix_sort(arr1)
        arr2.sort()
        if arr1 != arr2:
            print('test fail !!!')
            print arr
            print arr1
            print arr2
            break

    print("test end !!!")
