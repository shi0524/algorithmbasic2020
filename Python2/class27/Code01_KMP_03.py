# -*- coding: utf-8 –*-

import random
from tqdm import trange


def get_index_of(s1, s2):
    if not s2:
        return 0
    if len(s1) < len(s2):
        return -1
    n1 = len(s1)
    n2 = len(s2)
    nexts = get_next_array(s2)
    x = 0
    y = 0
    while x < n1 and y < n2:
        if s1[x] == s2[y]:
            x += 1
            y += 1
        elif nexts[y] == -1:
            x += 1
        else:
            y = nexts[y]
    return x - y if y == n2 else -1


def get_next_array(s2):
    if len(s2) == 1:
        return [-1]
    n = len(s2)
    nexts = [0] * n
    nexts[0] = -1
    cn = 0
    i = 2
    while i < n:
        if s2[i - 1] == s2[cn]:
            nexts[i] = cn + 1
            cn += 1
            i += 1
        elif cn > 0:
            cn = nexts[cn]
        else:
            i += 1
    return nexts


def get_index_of2(s1, s2):
    try:
        index = s1.index(s2)
    except Exception:
        index = -1
    return index


# for test
def generateRandomString(maxSize):
    """
    :param maxSize:
    :param maxValue:
    :return:
    """
    return "".join([random.choice("abcdef") for _ in range(maxSize)])


if __name__ == "__main__":
    maxSize1 = 100
    maxSize2 = 10
    testTime = 10000
    print("功能测试开始")
    for i in trange(testTime):
        s1 = generateRandomString(maxSize1)
        start = random.randint(1, maxSize1)
        s2 = s1[start:start + maxSize2]
        # s1 = 'aacaacaab'
        # s2 = 'aacaab'
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


