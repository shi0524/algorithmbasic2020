# -*- coding: utf-8 –*-

"""
蓄水池算法

解决的问题：
假设有一个源源吐出不同球的机器，
只有装下10个球的袋子，每一个吐出的球，要么放入袋子，要么永远扔掉
如何做到机器吐出每一个球之后，所有吐出的球都等概率被放进袋子里
"""
import random
from tqdm import trange


class RandomBox(object):
    """
    """
    def __init__(self, capacity):
        self.count = 0
        self.capacity = capacity
        self.pool = [0] * self.capacity

    def rand(self, max_val):
        return random.randint(1, max_val)

    def add(self, num):
        self.count += 1
        if self.count <= self.capacity:
            self.pool[self.count - 1] = num
        else:
            # capacity / count 的概率决定，要不要进入池子
            if self.rand(self.count) <= self.capacity:
                # 如果进池子, 池子里面的球 1/capacity 的概率被扔掉
                # 则 球进池子的概率为 1/capacity * capacity / count = 1/count
                self.pool[self.rand(self.capacity) - 1] = num

    def choices(self):
        return self.pool[:]


if __name__ == "__main__":

    print("测试开始")
    test_num = 173
    testTime = 100000
    count = [0] * (test_num + 1)
    for _ in trange(testTime):
        box = RandomBox(10)
        for num in range(1, test_num + 1):
            box.add(num)
        for i in box.choices():
            count[i] += 1
    for i, num in enumerate(count):
        print(i, num / (10.0 * testTime))
    print("测试结束")


