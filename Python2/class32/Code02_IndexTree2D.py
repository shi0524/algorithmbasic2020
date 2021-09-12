# -*- coding: utf-8 –*-

"""
IndexTree
特点：
1）支持区间查询
2）没有线段树那么强，但是非常容易改成一维、二维、三维的结构
3）只支持单点更新
"""


class IndexTree2D(object):
    def __init__(self, matrix):
        if not len(matrix) or not len(matrix[0]):
            self.n = 0
            self.m = 0
            return
        self.n = len(matrix)
        self.m = len(matrix[0])
        n = self.n
        m = self.m
        self.tree = [[0] * (m + 1) for _ in range(n + 1)]
        self.nums = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                self.update(i, j, matrix[i][j])

    def sum(self, row, col):
        sums = 0
        tree = self.tree
        r = row + 1
        while r:
            c = col + 1
            while c:
                sums += tree[r][c]
                c -= c & -c
            r -= r & -r
        return sums

    def update(self, row, col, val):
        if not self.n or not self.m:
            return
        n = self.n
        m = self.m
        nums = self.nums
        tree = self.tree
        add = val - nums[row][col]
        nums[row][col] = val
        r = row + 1
        while r <= n:
            c = col + 1
            while c <= m:
                tree[r][c] += add
                c += c & -c
            r += r & -r

    def sum_region(self, row1, col1, row2, col2):
        if not self.n or not self.m:
            return

        return self.sum(row2, col2) - \
               self.sum(row1 - 1, col2) - \
               self.sum(row2, col1 - 1) + \
               self.sum(row1 - 1, col1 - 1)


if __name__ == "__main__":
    matrix = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ]
    stree = IndexTree2D(matrix)
    print(stree.sum_region(1, 1, 3, 3))
    stree.update(1, 1, 4)
    print(stree.sum_region(1, 1, 3, 3))


