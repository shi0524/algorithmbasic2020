# -*- coding: utf-8 –*-


import random
from tqdm import trange


class SegmentTree(object):
    def __init__(self, origin):
        self.arr = [0] + origin
        MAXN = len(self.arr) * 4
        self.sums = [0] * MAXN
        self.lazy = [0] * MAXN
        self.change = [0] * MAXN
        self.update = [0] * MAXN

    def push_up(self, rt):
        self.sums[rt] = self.sums[rt * 2] + self.sums[rt * 2 + 1]

    def push_down(self, rt, ln, rn):
        if self.update[rt]:
            C = self.change[rt]
            self.update[rt * 2] = True
            self.change[rt * 2] = C
            self.sums[rt * 2] = C * ln
            self.lazy[rt * 2] = 0

            self.update[rt * 2 + 1] = True
            self.change[rt * 2 + 1] = C
            self.sums[rt * 2 + 1] = C * rn
            self.lazy[rt * 2 + 1] = 0

            self.update[rt] = False

        if self.lazy[rt]:
            self.lazy[rt * 2] += self.lazy[rt]
            self.sums[rt * 2] += self.lazy[rt] * ln

            self.lazy[rt * 2 + 1] += self.lazy[rt]
            self.sums[rt * 2 + 1] += self.lazy[rt] * rn

            self.lazy[rt] = 0

    def build(self, l, r, rt):
        if l == r:
            self.sums[rt] = self.arr[l]
            return
        mid = (l + r) // 2
        self.build(l, mid, rt * 2)
        self.build(mid + 1, r, rt * 2 + 1)

        self.push_up(rt)

    def add_operate(self, L, R, C, l, r, rt):
        if L <= l and r <= R:
            self.sums[rt] += C * (r - l + 1)
            self.lazy[rt] += C
            return

        mid = (l + r) // 2
        self.push_down(rt, mid - l + 1, r - mid)
        if L <= mid:
            self.add_operate(L, R, C, l, mid, rt * 2)
        if R > mid:
            self.add_operate(L, R, C, mid + 1, r, rt * 2 + 1)

        self.push_up(rt)

    def update_operate(self, L, R, C, l, r, rt):
        if L <= l and r <= R:
            self.update[rt] = True
            self.change[rt] = C
            self.sums[rt] = C * (r - l + 1)
            self.lazy[rt] = 0
            return
        mid = (l + r) // 2
        self.push_down(rt, mid - l + 1, r - mid)

        if L <= mid:
            self.update_operate(L, R, C, l, mid, rt * 2)
        if R > mid:
            self.update_operate(L, R, C, mid + 1, r, rt * 2 + 1)
        self.push_up(rt)

    def query(self, L, R, l, r, rt):
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
    length = 100
    max_value = 10
    test_times = 10000
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





