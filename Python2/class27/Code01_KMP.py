# -*- coding: utf-8 –*-

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


def get_index_of(s1, s2):
    if s1 and not s2:
        return 0
    if not s1 or len(s1) < len(s2):
        return -1

    x = 0
    y = 0
    n1 = len(s1)
    n2 = len(s2)
    str1 = list(s1)
    str2 = list(s2)

    nexts = get_next_array(str2)

    while x < n1 and y < n2:
        if str1[x] == str2[y]:
            x += 1
            y += 1
        elif nexts[y] == -1:
            x += 1
        else:
            y = nexts[y]
    return x - y if y == n2 else -1



def get_next_array(str2):
    if len(str2) == 1:
        return [-1]
    n = len(str2)
    nexts = [0] * n
    nexts[0] = -1
    nexts[1] = 0

    i = 2       # 目前在哪个位置上求 nexts 数组的值
    cn = 0      # 当前是哪个位置的值在和 i-1 位置的字符比较
    while i < n:
        if str2[i - 1] == str2[cn]:
            cn += 1
            nexts[i] = cn
            i += 1
        elif cn > 0:
            cn = nexts[cn]
        else:
            nexts[i] = 0
            i += 1

    return nexts


def get_index_of2(s1, s2):
    try:
        index = s1.index(s2)
    except Exception:
        index = -1
    return index


def get_index_of3(s1, s2):
    if not s1 or not s2 or len(s1) < len(s2):
        return -1
    str1 = list(s1)
    match = list(s2)
    n1 = len(str1)
    n2 = len(match)
    x = 0       # str1 中比对到的位置
    y = 0       # match 中比对到的位置
    nexts = get_next_array3(match)   # nexts[i] match 中i之前的字符串 match[0, i - 1]最长前缀和后缀相等的长度
    while x < n1 and y < n2:
        if str1[x] == match[y]:
            x += 1
            y += 1
        elif nexts[y] != -1:
            y = nexts[y]
        else:
            x += 1
    return x - y if y == n2 else -1


def get_next_array3(match):
    if len(match) == 1:
        return [-1]
    n = len(match)
    nexts = [0] * n
    nexts[0] = -1
    nexts[1] = 0
    cn = 0
    i = 2
    while i < n:
        if match[i - 1] == match[cn]:
            cn += 1
            nexts[i] = cn
            i += 1
        elif cn > 0:
            cn = nexts[cn]
        else:
            nexts[i] = 0
            i += 1
    return nexts



# for test
def generateRandomString(maxSize):
    """
    :param maxSize:
    :param maxValue:
    :return:
    """
    return "".join([random.choice("abcdef") for _ in range(maxSize)])


if __name__ == "__main__":
    maxSize1 = 10
    maxSize2 = 5
    testTime = 10000
    print("功能测试开始")
    for i in trange(testTime):
        s1 = generateRandomString(maxSize1)
        # s2 = generateRandomString(maxSize2)
        start = random.randint(1, maxSize1)
        s2 = s1[start:start + maxSize2]
        ans1 = get_index_of(s1, s2)
        ans2 = get_index_of2(s1, s2)
        if ans1 != ans2:
            print(s1)
            print(s2)
            print(ans1)
            print(ans2)
            print("test1 break because of error !!!")
            break
    print("功能测试结束")

    print("性能测试开始")
    get_index_of = time_it(get_index_of)
    get_index_of2 = time_it(get_index_of2)
    get_index_of3 = time_it(get_index_of3)
    maxSize1 = 1000000
    maxSize2 = 100
    s1 = generateRandomString(maxSize1)
    s2 = generateRandomString(maxSize2)
    start = random.randint(1, maxSize1)
    s2 = s1[start:start + maxSize2]
    ans1 = get_index_of(s1, s2)
    ans2 = get_index_of2(s1, s2)
    ans3 = get_index_of3(s1, s2)
    print(ans1, ans2, ans3)
    print("性能测试结束")
