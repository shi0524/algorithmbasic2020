# -*- coding: utf-8 –*-

import random
from tqdm import trange


class SegmentTree(object):

    def __init__(self, origin):
        self.MAXN = len(origin) + 1
        MAXN = self.MAXN * 4
        self.arr = [0] + origin         # arr[0] 弃而不用  从1开始
        self.sum = [0] * MAXN           # 用来支持脑补概念中，某一个范围的累加和信息
        self.lazy = [0] * MAXN          # 用来支持脑补概念总，某一个范围没有向下传到的叠加任务
        self.change = [0] * MAXN        # 用来支持脑补概念中，某一个范围更新人任务更新成了什么(为更新的值)
        self.update = [False] * MAXN    # 用来支持脑补概念中，某一个范围有没有更新操作的任务(为更新慵懒标记)

    def push_up(self, rt):
        """ 某一个位置的累加和是它子节点向上汇报得到
        """
        self.sum[rt] = self.sum[rt * 2] + self.sum[rt * 2 + 1]

    def push_down(self, rt, ln, rn):
        """
            之前的, 所有的懒增加、懒更新, 从父范围, 发给两个子范围
            分发策略
            ln 表示左子树元素节点个数, rn 表示右子树节点个数
        """
        if self.update[rt]:
            # 下发左边
            self.update[rt * 2] = True
            self.change[rt * 2] = self.change[rt]
            self.lazy[rt * 2] = 0
            self.sum[rt * 2] = self.change[rt] * ln

            # 下发右边
            self.update[rt * 2 + 1] = True
            self.change[rt * 2 + 1] = self.change[rt]
            self.lazy[rt * 2 + 1] = 0
            self.sum[rt * 2 + 1] = self.change[rt] * rn

            # 当前节点 update 标记至为 False
            self.update[rt] = False

        if self.lazy[rt] != 0:
            # 下发左边
            self.lazy[rt * 2] += self.lazy[rt]
            self.sum[rt * 2] += self.lazy[rt] * ln
            # 下发右边
            self.lazy[rt * 2 + 1] += self.lazy[rt]
            self.sum[rt * 2 + 1] += self.lazy[rt] * rn
            # rt 懒信息清空
            self.lazy[rt] = 0

    def build(self, l, r, rt):
        """
            在初始化阶, 先把sum数组填好
            在 arr[l~r] 范围上, 去build, 1~N
            rt: 这个范围在 sum 中的下标
        """
        if l == r:
            self.sum[rt] = self.arr[l]
            return
        mid = (l + r) // 2
        self.build(l, mid, rt * 2)
        self.build(mid + 1, r, rt * 2 + 1)
        self.push_up(rt)

    def add_operate(self, L, R, C, l, r, rt):
        """
            L, R, C 当前接到的任务(从 L ~ R 范围上, 每个值都加一个C)
            当前来到的格子是 rt
            rt 表示的位置是 l ~ r
        """
        # 任务把当前范围全包, 直接懒住
        if L <= l and r <= R:
            self.sum[rt] += C * (r - l + 1)
            self.lazy[rt] += C
            return
        # 如果没有全包
        mid = (l + r) // 2
        # 先把之前的 任务 往下发
        self.push_down(rt, mid - l + 1, r - mid)

        # 如果任务左边小于等于 mid, 说明左半部分也有任务
        if L <= mid:
            self.add_operate(L, R, C, l, mid, rt * 2)
        # 如果任务大于 mid, 说明右半部分也有任务
        if R > mid:
            self.add_operate(L, R, C, mid + 1, r, rt * 2 + 1)
        # 汇总
        self.push_up(rt)

    def update_operate(self, L, R, C, l, r, rt):
        """
            L, R, C 当前接到的任务(从 L ~ R 范围上, 每个值都变成C)
            当前来到的格子是 rt
            rt 表示的位置是 l ~ r
        """
        # 任务把此时的范围全包
        if L <= l and r <= R:
            self.change[rt] = C
            self.sum[rt] = C * (r - l + 1)
            self.update[rt] = True
            self.lazy[rt] = 0
            return
        if L <= l and r <= R:
            self.update[rt] = True
            self.change[rt] = C
            self.sum[rt] = C * (r - l + 1)
            self.lazy[rt] = 0
            return

        # 没有全包
        mid = (l + r) // 2
        self.push_down(rt, mid - l + 1, r - mid)

        if L <= mid:
            self.update_operate(L, R, C, l, mid, rt * 2)
        if R > mid:
            self.update_operate(L, R, C, mid + 1, r, rt * 2 + 1)

        self.push_up(rt)

    def query(self, L,  R, l, r, rt):
        if L <= l and r <= R:
            return self.sum[rt]
        mid = (l + r) // 2
        self.push_down(rt, mid - l + 1, r - mid)
        ans = 0
        if L <= mid:
            ans += self.query(L, R, l, mid, rt * 2)
        if R > mid:
            ans += self.query(L, R, mid + 1, r, rt * 2 + 1)
        return ans


class Right(object):
    def __init__(self, origin):
        self.arr = [0] * (len(origin) + 1)
        for i, num in enumerate(origin, start=1):
            self.arr[i] = num

    def update_operate(self, L, R, C):
        for i in range(L, R + 1):
            self.arr[i] = C

    def add_operate(self, L, R, C):
        for i in range(L, R + 1):
            self.arr[i] += C

    def query(self, L, R):
        ans = 0
        for i in range(L, R + 1):
            ans += self.arr[i]
        return ans


# for test
def generateRandomArray(maxSize, maxValue):
    """
    :param maxSize:
    :param maxValue:
    :return:
    """
    return [random.randint(1, maxValue) for _ in xrange(maxSize)]


# for test
def test():
    length = 30
    max_value = 100
    test_times = 1000
    add_or_update_times = 100
    query_times = 50

    for _ in trange(test_times):
        origin = generateRandomArray(length, max_value)
        seg = SegmentTree(origin)
        S = 1
        N = len(origin)
        root = 1
        seg.build(S, N, root)
        right = Right(origin)
        for j in range(add_or_update_times):
            num1 = random.randint(1, N)
            num2 = random.randint(1, N)
            L = min(num1, num2)
            R = max(num1, num2)
            C = random.randint(1, max_value)

            if random.randint(0, 1):
                seg.add_operate(L, R, C, S, N, root)
                right.add_operate(L, R, C)
            else:
                seg.update_operate(L, R, C, S, N, root)
                right.update_operate(L, R, C)

            for k in range(query_times):
                num1 = random.randint(1, N)
                num2 = random.randint(1, N)
                L = min(num1, num2)
                R = max(num1, num2)
                ans1 = seg.query(L, R, S, N, root)
                ans2 = right.query(L, R)
                if ans1 != ans2:
                    print origin
                    print seg.arr
                    print seg.sum
                    print(ans1, ans2)
                    print("test break because of error !!!")
                    break


if __name__ == "__main__":
    test()



