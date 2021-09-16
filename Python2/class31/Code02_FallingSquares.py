# -*- coding: utf-8 –*-

"""
在无限长的数轴（即 x 轴）上，我们根据给定的顺序放置对应的正方形方块。

第 i 个掉落的方块（positions[i] = (left, side_length)）是正方形，
其中left 表示该方块最左边的点位置(positions[i][0])，
side_length 表示该方块的边长(positions[i][1])。

每个方块的底部边缘平行于数轴（即 x 轴），并且从一个比目前所有的落地方块更高的高度掉落而下。
在上一个方块结束掉落，并保持静止后，才开始掉落新方块。

方块的底边具有非常大的粘性，并将保持固定在它们所接触的任何长度表面上（无论是数轴还是其他方块）。
邻接掉落的边不会过早地粘合在一起，因为只有底边才具有粘性。

返回一个堆叠高度列表ans 。
每一个堆叠高度ans[i]表示在通过positions[0], positions[1], ..., positions[i]表示的方块掉落结束后，
目前所有已经落稳的方块堆叠的最高高度。

注意:
    1 <= positions.length <= 1000.
    1 <= positions[i][0] <= 10^8.
    1 <= positions[i][1] <= 10^6.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/falling-squares
"""


class SegmentTree(object):
    def __init__(self, size):
        MAXN = size * 4
        self.maxs = [0] * MAXN
        self.change = [0] * MAXN
        self.update = [False] * MAXN

    def push_up(self, rt):
        self.maxs[rt] = max(self.maxs[rt * 2], self.maxs[rt * 2 + 1])

    def push_down(self, rt, ln, rn):
        # print self.update, rt, len(self.update)
        if self.update[rt]:
            C = self.change[rt]
            self.update[rt * 2] = True
            self.change[rt * 2] = C
            self.maxs[rt * 2] = C

            self.update[rt * 2 + 1] = True
            self.change[rt * 2 + 1] = C
            self.maxs[rt * 2 + 1] = C

            self.update[rt] = False

    def update_operate(self, L, R, C, l, r, rt):
        if L <= l and r <= R:
            self.change[rt] = C
            self.update[rt] = True
            self.maxs[rt] = C
            return
        mid = (l + r) // 2
        self.push_down(rt, mid - l + 1, r - mid)

        if L <= mid:
            # print l, mid, (L, R, C, l, mid, rt * 2)
            self.update_operate(L, R, C, l, mid, rt * 2)

        if R > mid:
            self.update_operate(L, R, C, mid + 1, r, rt * 2 + 1)
        self.push_up(rt)

    def query(self, L, R, l, r, rt):
        if L <= l and r <= R:
            return self.maxs[rt]
        mid = (l + r) // 2
        self.push_down(rt, mid - l + 1, r - mid)
        left = 0
        right = 0
        if L <= mid:
            left = self.query(L, R, l, mid, rt * 2)
        if R > mid:
            right = self.query(L, R, mid + 1, r, rt * 2 + 1)
        return max(left, right)


class Solution(object):
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        """ 由于坐标值会很大, 对坐标做离散化处理 """
        mapping = self.index(positions)
        """ 由于坐标值会很大, 对坐标做离散化处理 """
        N = len(mapping)
        segment_tree = SegmentTree(N)
        ans = []
        max_height = 0
        for position in positions:
            L = mapping[position[0]]
            R = mapping[position[0] + position[1] - 1]
            height = segment_tree.query(L, R, 1, N, 1) + position[1]
            segment_tree.update_operate(L, R, height, 1, N, 1)
            max_height = max(max_height, height)
            ans.append(max_height)
        return ans

    def index(self, positions):
        pos = set()
        for position in positions:
            pos.add(position[0])
            pos.add(position[0] + position[1] - 1)
        pos = sorted(pos)
        return {num: index for index, num in enumerate(pos, start=1)}


if __name__ == "__main__":
    """
    输入: [[1, 2], [2, 3], [6, 1]]
    输出: [2, 5, 5]
    """
    postions = [[1, 2], [2, 3], [6, 1]]
    s = Solution()
    ans = s.fallingSquares(postions)
    print ans




