# -*- coding: utf-8 –*-

"""
给定一个由字符串组成的数组strs，
必须把所有的字符串拼接起来，
返回所有可能的拼接结果中，字典序最小的结果
"""
import random


def lowestString1(strs):
    if not strs:
        return ""
    all_str = process(strs)
    all_str.sort()
    return all_str[0]


def process(strs):
    if not strs:
        return [""]
    all_strs = []
    for i in range(len(strs)):
        first = strs[i]
        nexts = strs[::]
        nexts.pop(i)
        next_strs = process(nexts)
        for cur in next_strs:
            all_strs.append(first + cur)
    return all_strs


class String(object):
    def __init__(self, str):
        self.str = str

    def __lt__(self, other):
        return self.str + other.str < other.str + self.str


def lowestString2(strs):
    if not strs:
        return ""
    return "".join(sorted(strs, key=lambda x: String(x)))


# for test
def generateRandomString(strlen):
    """ 生成字符串
    """
    slen = random.randint(1, strlen)
    return "".join([chr(random.randint(97, 122)) for _ in range(slen)])


def generateRandomStringArray(arrlen, strlen):
    """ 生成字符串列表
    """
    alen = random.randint(1, arrlen)
    return [generateRandomString(strlen) for _ in range(alen)]


if __name__ == "__main__":
    arrlen = 100
    strlen = 20
    test_times = 100000
    print('test begin !!!')
    for _ in range(test_times):
        strs = generateRandomStringArray(arrlen, strlen)
        ans1 = lowestString1(strs)
        ans2 = lowestString2(strs)
        if ans1 != ans2:
            print(ans1, ans2)
            print("test break because of error !!!")
            break
    print("test end !!!")

