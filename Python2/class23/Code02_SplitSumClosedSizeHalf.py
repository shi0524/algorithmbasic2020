# -*- coding: utf-8 –*-

"""
给定一个正数数组arr，请把arr中所有的数分成两个集合
如果arr长度为偶数，两个集合包含数的个数要一样多
如果arr长度为奇数，两个集合包含数的个数必须只差一个
请尽量让两个集合的累加和接近
返回：
最接近的情况下，较小集合的累加和
"""
import random
from tqdm import trange


def right(arr):
    n = len(arr)
    if n < 2:
        return 0
    arr_sum = 0
    for num in arr:
        arr_sum += num
    if n & 1:
        p1 = process(arr, 0, n / 2, arr_sum / 2)
        p2 = process(arr, 0, n / 2 + 1, arr_sum / 2)
        return max(p1, p2)
    return process(arr, 0, n / 2, arr_sum / 2)


def process(arr, index, pick, rest):
    if len(arr) == index:
        return 0 if not pick else -1
    no = process(arr, index + 1, pick, rest)
    yes = -1
    if rest >= arr[index] and pick:
        nexts = process(arr, index + 1, pick - 1, rest - arr[index])
        if nexts != -1:
            yes = arr[index] + nexts
    return max(yes, no)


def dp(arr):
    n = len(arr)
    if n < 2:
        return 0
    arr_sum = 0
    for num in arr:
        arr_sum += num
    half_sum = arr_sum / 2
    half_num = (n + 1) / 2

    dp = [[[-1] * (half_sum + 1) for _ in range(half_num + 1)] for _ in range(n + 1)]
    for rest in range(half_sum + 1):
        dp[n][0][rest] = 0
    for index in range(n - 1, -1, -1):
        for pick in range(half_num + 1):
            for rest in range(half_sum + 1):
                no = dp[index + 1][pick][rest]
                yes = -1
                if pick and arr[index] <= rest:
                    nexts = dp[index + 1][pick - 1][rest - arr[index]]
                    if nexts != -1:
                        yes = arr[index] + nexts
                dp[index][pick][rest] = max(no, yes)
    if n & 1:
        return max(dp[0][half_num][half_sum], dp[0][half_num - 1][half_sum])
    return dp[0][half_num][half_sum]


# for test
def generateRandomArray(maxSize, maxValue):
    """
    :param maxSize:
    :param maxValue:
    :return:
    """
    return [random.randint(1, maxValue) for _ in xrange(maxSize)]


if __name__ == "__main__":
    maxSize = 10
    maxValue = 50
    testTime = 10000
    print("测试开始")
    for i in trange(testTime):
        arr = generateRandomArray(maxSize, maxValue)
        ans1 = right(arr)
        ans2 = dp(arr)
        if ans1 != ans2:
            print arr
            print(ans1, ans2)
            print("test break because of error !!!")
            break
    print("测试结束")


