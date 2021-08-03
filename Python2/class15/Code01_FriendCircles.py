# -*- coding: utf-8 –*-

"""

有 n 个城市，其中一些彼此相连，另一些没有相连。
如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。

省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。

给你一个 n x n 的矩阵 isConnected，
其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。

返回矩阵中 省份 的数量。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-provinces
"""


class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        N = len(isConnected)
        ufind = UnionFind(N)
        for i in range(N):
            for j in range(i + 1, N):
                if isConnected[i][j]:
                    ufind.union(i, j)
        return ufind.get_size()


class UnionFind(object):
    def __init__(self, N):
        self.parent = range(N)
        self.sizes = [1] * N
        self.size = 0

    def find(self, i):
        path = []
        while i != self.parent[i]:
            path.append(i)
            i = self.parent[i]
        while path:
            self.parent[path.pop()] = i
        return i

    def union(self, i, j):
        fi = self.find(i)
        fj = self.find(j)
        if fi != fj:
            if self.sizes[fi] >= self.sizes[fj]:
                self.parent[fj] = fi
                self.sizes[fi] += self.sizes[fj]
            else:
                self.parent[fi] = fj
                self.sizes[fj] += self.sizes[fi]
            self.size -= 1

    def get_size(self):
        return self.size
