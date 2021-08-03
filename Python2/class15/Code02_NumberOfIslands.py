# -*- coding: utf-8 –*-

"""
给你一个由'1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
"""
import copy
import random
import time


def time_it(func):
    """ 测时间 ms
    """
    def wrapper(*args, **kwargs):
        a = time.time()
        rc = func(*args, **kwargs)
        b = time.time()
        print (b - a) * 1000
        return rc
    return wrapper


@time_it
def numIslands3(board):
    """ 感染（深度优先）
    """
    islands = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '1':
                islands += 1
                infect(board, i, j)
    return islands


def infect(board, i, j):
    """
    从(i, j)位置出发, 向四周感染
    将遇到的'1'全部变成'2'
    """
    if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or board[i][j] != '1':
        return
    board[i][j] = '0'
    infect(board, i + 1, j)
    infect(board, i - 1, j)
    infect(board, i, j + 1)
    infect(board, i, j - 1)


class Dot(object):
    __slots__ = ()


class UnionFind1(object):
    def __init__(self, values):
        self.nodes = {}
        self.parents = {}
        self.size_map = {}
        for cur in values:
            node = Dot()
            self.nodes[cur] = node
            self.parents[node] = node
            self.size_map[node] = 1

    def find_father(self, cur):
        path = []
        while cur != self.parents[cur]:
            path.append(cur)
            cur = self.parents[cur]
        while path:
            self.parents[path.pop()] = cur
        return cur

    def union(self, a, b):
        fa = self.find_father(self.nodes[a])
        fb = self.find_father(self.nodes[b])
        if fa != fb:
            a_size = self.size_map[fa]
            b_size = self.size_map[fb]
            big = fa if a_size >= b_size else fb
            small = fb if big == fa else fa
            self.parents[small] = big
            self.size_map[big] += self.size_map.pop(small)

    def sets(self):
        return len(self.size_map)


@time_it
def numIslands1(board):
    row = len(board)
    col = len(board[0])
    dots = [[None] * col for _ in range(row)]
    dot_list = []
    for i in range(row):
        for j in range(col):
            if board[i][j] == '1':
                dots[i][j] = Dot()
                dot_list.append(dots[i][j])
    uf = UnionFind1(dot_list)
    for j in range(1, col):
        if board[0][j - 1] == '1' and board[0][j] == '1':
            uf.union(dots[0][j - 1], dots[0][j])
    for i in range(1, row):
        if board[i - 1][0] == '1' and board[i][0] == '1':
            uf.union(dots[i-1][0], dots[i][0])
    for i in range(1, row):
        for j in range(1, col):
            if board[i][j] != '1':
                continue
            if board[i - 1][j] == '1':
                uf.union(dots[i][j], dots[i - 1][j])
            if board[i][j-1] == '1':
                uf.union(dots[i][j], dots[i][j-1])
    return uf.sets()


class UnionFind2(object):
    def __init__(self, board):
        n = len(board)
        self.col = len(board[0])
        N = n * self.col
        self.parents = range(N)
        self.sizes = [1] * N
        self.size = 0
        for i in range(n):
            for j in range(self.col):
                if board[i][j] == '1':
                    self.size += 1

    def find(self, i):
        path = []
        len(self.parents)
        while i != self.parents[i]:
            path.append(i)
            i = self.parents[i]
        while path:
            self.parents[path.pop()] = i
        return i

    def union(self, r1, c1, r2, c2):
        i1 = r1 * self.col + c1
        i2 = r2 * self.col + c2
        f1 = self.find(i1)
        f2 = self.find(i2)
        if f1 != f2:
            if self.sizes[f1] >= self.sizes[f2]:
                self.sizes[f1] += self.sizes[f2]
                self.parents[f2] = f1
            else:
                self.sizes[f2] += self.sizes[f1]
                self.parents[f1] = self.parents[f2]
            self.size -= 1

    def sets(self):
        return self.size

@time_it
def numIslands2(board):
    row = len(board)
    col = len(board[0])
    uf = UnionFind2(board)
    for j in range(1, col):
        if board[0][j - 1] == '1' and board[0][j] == '1':
            uf.union(0, j - 1, 0, j)
    for i in range(1, row):
        if board[i - 1][0] == '1' and board[i][0] == '1':
            uf.union(i-1, 0, i, 0)
    for i in range(1, row):
        for j in range(1, col):
            if board[i][j] != '1':
                continue
            if board[i - 1][j] == '1':
                uf.union(i, j, i - 1, j)
            if board[i][j-1] == '1':
                uf.union(i, j, i, j-1)
    return uf.sets()


def generateRandomMatrix(row, col):
    """ 生成矩阵
    """
    return [['1' if random.randint(0, 1) else 0 for _ in range(col)] for _ in range(row)]


if __name__ == "__main__":
    row = 1000
    col = 1000
    print('test begin !!!')
    matrix = generateRandomMatrix(row, col)
    ans1 = numIslands1(copy.deepcopy(matrix))
    ans2 = numIslands2(copy.deepcopy(matrix))
    ans3 = numIslands3(copy.deepcopy(matrix))
    print ans1, ans2, ans3
    print("test end !!!")
