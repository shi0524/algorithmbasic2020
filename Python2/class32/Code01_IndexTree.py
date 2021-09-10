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


class IndexTree(object):

    def __init__(self, size):
        self.tree = [0] * (size + 1)   # 0 弃而不用, 下标从 1 开始
        self.size = size

    def sum(self, index):
        """ 1 ~ index 的累加和是多少
        """
        tree = self.tree
        ret = 0
        while index > 0:
            ret += tree[index]
            # 抹掉下标最右边的1
            index -= index & - index
        return ret

    def add(self, index, num):
        """ 在 index 位置加一个num
        """
        tree = self.tree
        size = self.size
        while index <= size:
            tree[index] += num
            index += index & -index


class Right(object):

    def __init__(self, size):
        self.nums = [0] * (size + 1)

    def sum(self, index):
        nums = self.nums
        return sum(nums[:index + 1])

    def add(self, index, num):
        self.nums[index] += num


if __name__ == "__main__":
    maxValue = 10
    maxSize = 200
    testTimes = 10000
    roundTimes = 1000

    print("功能测试开始 !!!")
    break_flag = 0
    for _ in trange(testTimes):
        if break_flag:
            break
        size = random.randint(1, maxSize)
        tree = IndexTree(size)
        right = Right(size)
        for _ in range(roundTimes):
            index = random.randint(1, size)
            # 2/3 的概率 加
            if random.randint(0, 2):
                num = random.randint(-maxValue, maxValue)
                tree.add(index, num)
                right.add(index, num)
            # 1/3 的概率 求和
            else:
                sum1 = tree.sum(index)
                sum2 = right.sum(index)
                if sum1 != sum2:
                    print index
                    print right.nums
                    print tree.tree
                    print(sum1, sum2)
                    break_flag = 1
                    print("test break because of error !!!")
                    break
    print("功能测试结束 !!!")

    print("性能测试开始 ！！！")
    size = 10000
    maxValue = 1000
    roundTimes = 100000
    tree = IndexTree(size)
    right = Right(size)
    tree.sum = time_it(tree.sum)
    right.sum = time_it(right.sum)

    for _ in range(roundTimes):
        index = random.randint(1, size)
        num = random.randint(-maxValue, maxValue)
        tree.add(index, num)
        right.add(index, num)
    for _ in range(10):
        index = random.randint(1, size)
        sum1 = tree.sum(index)
        sum2 = right.sum(index)
        print("index: {} ans: {} {}".format(index, sum1, sum2))
        print("*" * 50)
    print("性能测试结束 ！！！")
