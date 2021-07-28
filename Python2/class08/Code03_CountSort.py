# -*- coding: utf-8 –*-

import random

"""
不基于比较的排序

计数排序 (数据范围有限制)
公司员工按年龄排序
"""


def countSort(arr):
    if not arr or len(arr) < 2:
        return 0
    max_age = max(arr)
    bucket = [0] * (max_age + 1)
    for age in arr:
        bucket[age] += 1
    i = 0
    for age, num in enumerate(bucket):
        if not num:
            continue
        while num:
            arr[i] = age
            i += 1
            num -= 1
    return arr


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
    maxValue = 150
    print("test begin !!!")
    for _ in range(testTime):
        arr = generateRandomArray(maxSize, maxValue)
        arr1 = arr[::]
        arr2 = arr[::]
        countSort(arr1)
        arr2.sort()
        if arr1 != arr2:
            print('test fail !!!')
            print arr1
            print arr2
            break

    print("test end !!!")