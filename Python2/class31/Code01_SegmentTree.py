# -*- coding: utf-8 –*-

import random
from tqdm import trange


class SegmentTree(object):
    """ 线段树
        其它语言, 乘2、除2 使用位运算速度会快一下
        基于python底层的实现
            在值 x<=2^30 时，乘法比直接位运算要快
            在值 x>2^32 时，乘法显著慢于位运算
    """
    def __init__(self, origin):
        MAXN = len(origin) + 1
        self.arr = [0] * MAXN                   # origin信息从0开始, arr从1开始, 元素值相等
        for i, num in enumerate(origin, start=1):
            self.arr[i] = num
        self.sums = [0] * (MAXN * 4)            # 用来支持脑补概念中, 某一个范围的累加和信息
        self.lazy = [0] * (MAXN * 4)            # 用来支持脑补概念中, 某一个范围没有网线传递的累加任务
        self.change = [0] * (MAXN * 4)          # 用来支持脑补概念中, 某一个范围更新人任务更新成了什么(为更新的值)
        self.update = [False] * (MAXN * 4)      # 用来支持脑补概念中, 某一个范围有没有更新操作的任务(为更新慵懒标记)

    def push_up(self, rt):
        """ 计算区间和
        """
        # self.sums[rt] = self.sums[rt << 1] + self.sums[rt << 1 | 1]
        self.sums[rt] = self.sums[rt * 2] + self.sums[rt * 2 + 1]

    def push_down(self, rt, ln, rn):
        """
        之前的，所有懒增加，和懒更新，从父范围，发给左右两个子范围
        分发策略是什么
        :param rt: 父节点位置
        :param ln: 左子树元素结点个数
        :param rn: 右子树结点个数
        :return:
        """

        # 先判断有没有缓存的更新任务
        if self.update[rt]:
            # 分发给左子树
            self.update[rt * 2] = True                  # 更新的标记
            self.change[rt * 2] = self.change[rt]       # 更新的值
            self.lazy[rt * 2] = 0                       # 原先的缓存住的懒更新全部失效, 重置为0
            self.sums[rt * 2] = self.change[rt] * ln    # 重新计算左子树区间和

            # 分发给右子树
            self.update[rt * 2 + 1] = True
            self.change[rt * 2 + 1] = self.change[rt]
            self.lazy[rt * 2 + 1] = 0
            self.sums[rt * 2 + 1] = self.change[rt] * rn
            self.update[rt] = False

        # 再做加减操作
        if self.lazy[rt]:
            self.lazy[rt * 2] += self.lazy[rt]
            self.sums[rt * 2] += self.lazy[rt] * ln

            self.lazy[rt * 2 + 1] += self.lazy[rt]
            self.sums[rt * 2 + 1] += self.lazy[rt] * rn
            self.lazy[rt] = 0

    def build(self, l, r, rt):
        """ 初始化阶段, 将 sums 数组填好
            在 arr[l ~ r] 范围上, 去build, 1 ~ N
            rt 这个范围在sum中的下标
        """
        if l == r:
            self.sums[rt] = self.arr[l]
            return
        mid = (l + r) // 2
        self.build(l, mid, rt * 2)
        self.build(mid + 1, r, rt * 2 + 1)

        # 去计算区间和
        self.push_up(rt)

    def update_operate(self, L, R, C, l, r, rt):
        """ L, R, C: 更新区间 L ~ R 更新成 C
            l, r: 当前要更新的范围
            rt: 位置
        """

        # 能懒住
        if L <= l and r <= R:
            self.update[rt] = True
            self.change[rt] = C
            self.sums[rt] = C * (r - l + 1)
            self.lazy[rt] = 0
            return
        # 当前任务躲不掉, 无法懒更新, 要往下发
        mid = (l + r) // 2
        # 处理之前懒更新的任务
        self.push_down(rt, mid - l + 1, r - mid)

        if L <= mid:    # l ~ mid
            self.update_operate(L, R, C, l, mid, rt * 2)
        if R > mid:     # mid + 1 ~ r
            self.update_operate(L, R, C, mid + 1, r, rt * 2 + 1)
        self.push_up(rt)

    def add_operate(self, L, R, C, l, r, rt):
        """ 加操作
        """
        # 任务如果把此时的范围全包了！
        if L <= l and r <= R:
            self.sums[rt] += C * (r - l + 1)
            self.lazy[rt] += C
            return

        # 任务没有把此时的范围全包
        mid = (l + r) // 2
        self.push_down(rt, mid - l + 1, r - mid)

        # L ~ R
        if L <= mid:
            self.add_operate(L, R, C, l, mid, rt * 2)
        if R > mid:
            self.add_operate(L, R, C, mid + 1, r, rt * 2 + 1)

        # 更新区间和
        self.push_up(rt)

    def query(self, L,  R, l, r, rt):
        if L <= l and r <= R:
            return self.sums[rt]

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
    length = 10
    max_value = 10
    test_times = 5000
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
                    print(ans1, ans2)
                    print("test break because of error !!!")
                    break


if __name__ == "__main__":
    test()

