# -*- coding: utf-8 –*-

"""
岛问题（扩展）

给你一个充满'0'（水）的 m * n 的二维网格，现在给你一个长度为k的坐标数组，
数组内每个坐标可将网格中的'0'(水)转换成'1'(陆地), 请计算每个坐标转换成陆地时当前岛屿数量
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。

测试链接：https://leetcode.com/problems/number-of-islands-ii/
"""
import random
from tqdm import tqdm


def num_islands21(m, n, positions):
    uf = UnionFind1(m, n)
    ans = []
    for pos in positions:
        ans.append(uf.connect(pos[0], pos[1]))
    return ans


class UnionFind1(object):
    def __init__(self, m, n):
        self.col = n
        self.row = m
        self.size = 0
        N = m * n
        self.sizes = [0] * N
        self.parents = [0] * N

    def index(self, r, c):
        return r * self.col + c

    def find(self, i):
        path = []
        while i != self.parents[i]:
            path.append(i)
            i = self.parents[i]
        while path:
            self.parents[path.pop()] = i
        return i

    def union(self, r1, c1, r2, c2):
        # 判断 坐标1 越不越界(本题自己调用, 坐标1 肯定不越界)
        # if r1 < 0 or r1 == self.row or c1 < 0 or c1 == self.col:
        #     return
        # 判断 坐标2 越不越界
        if r2 < 0 or r2 == self.row or c2 < 0 or c2 == self.col:
            return
        i1 = self.index(r1, c1)
        i2 = self.index(r2, c2)
        f1 = self.find(i1)
        f2 = self.find(i2)
        if self.sizes[f1] and self.sizes[f2]:
            if self.sizes[f1] >= self.sizes[f2]:
                self.sizes[f1] += self.sizes[f2]
                self.parents[f2] = f1
            else:
                self.sizes[f2] += self.sizes[f1]
                self.parents[f1] = f2
            self.size -= 1

    def connect(self, r, c):
        i = self.index(r, c)
        if not self.sizes[i]:
            self.parents[i] = i
            self.sizes[i] = 1
            self.size += 1
            self.union(r, c, r - 1, c)
            self.union(r, c, r + 1, c)
            self.union(r, c, r, c - 1)
            self.union(r, c, r, c + 1)
        return self.size


# 如果列表 m * n 比较大, 而k比较小，用map替代数组
def num_islands22(m, n, positions):
    uf = UnionFind2(m, n)
    ans = []
    for pos in positions:
        ans.append(uf.connect(pos[0], pos[1]))
    return ans


class UnionFind2(object):
    def __init__(self, m, n):
        self.col = n
        self.row = m
        self.size = 0
        self.sizes = {}
        self.parents = {}

    def index(self, r, c):
        """ 数字需要防止溢出的语言,可以拼接字符串
            类似: "{}_{}".format(r, c)
            python 有长整型, 无溢出风险
        """
        return r * self.col + c

    def find(self, i):
        path = []
        while i != self.parents[i]:
            path.append(i)
            i = self.parents[i]
        while path:
            self.parents[path.pop()] = i
        return i

    def union(self, r1, c1, r2, c2):
        # 判断 坐标1 越不越界(本题自己调用, 坐标1 肯定不越界)
        # if r1 < 0 or r1 == self.row or c1 < 0 or c1 == self.col:
        #     return
        # 判断 坐标2 越不越界
        if r2 < 0 or r2 == self.row or c2 < 0 or c2 == self.col:
            return
        i1 = self.index(r1, c1)
        i2 = self.index(r2, c2)
        if not self.sizes.get(i2):
            return
        f1 = self.find(i1)
        f2 = self.find(i2)
        if self.sizes.get(f1) and self.sizes.get(f2):
            if self.sizes[f1] >= self.sizes[f2]:
                self.sizes[f1] += self.sizes[f2]
                self.parents[f2] = f1
            else:
                self.sizes[f2] += self.sizes[f1]
                self.parents[f1] = f2
            self.size -= 1

    def connect(self, r, c):
        i = self.index(r, c)
        # 判断，没有初始化过的才进行初始化
        if not self.sizes.get(i):
            self.parents[i] = i
            self.sizes[i] = 1
            self.size += 1
            self.union(r, c, r - 1, c)
            self.union(r, c, r + 1, c)
            self.union(r, c, r, c - 1)
            self.union(r, c, r, c + 1)
        return self.size


def generateRandomPositionsArray(max_row, max_col, max_len):
    """ 生成坐标数字
    """
    arr_len = random.randint(1, max_len)
    return [[random.randint(1, max_row - 1), random.randint(1, max_col-1)] for _ in range(arr_len)]


if __name__ == "__main__":
    arrlen = 1000
    max_row = 1000
    max_col = 1000
    test_times = 1000
    print('test begin !!!')
    for _ in tqdm(range(test_times)):
        positions = generateRandomPositionsArray(max_row, max_col, arrlen)
        ans1 = num_islands21(max_row, max_col, positions)
        ans2 = num_islands22(max_row, max_col, positions)
        if ans1 != ans2:
            print()
            print(ans1, ans2)
            print("test break because of error !!!")
            break
    print("test end !!!")

