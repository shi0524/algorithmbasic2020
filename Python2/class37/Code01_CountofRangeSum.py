# -*- coding: utf-8 –*-

"""
给定一个数组arr，和两个整数a和b（a<=b）
求arr中有多少个子数组，累加和在[a,b]这个范围上
返回达标的子数组数量

纯暴力: O(N^3)
暴力 + 前缀和数组: O(N^2)
merge 排序改写: O(N*logN)
有序表改写: O(N*logN)
"""


import random
from tqdm import trange


def countRangeSum1(nums, lower, upper):
    n = len(nums)
    sums = [0] * (n + 1)
    for i, num in enumerate(nums, start=1):
        sums[i] = num + sums[i - 1]
    return count_while_merge_sort(sums, 0, n + 1, lower, upper)


def count_while_merge_sort(sums, start, end, lower, upper):
    if end - start <= 1:
        return 0
    mid = (start + end) // 2
    count = count_while_merge_sort(sums, start, mid, lower, upper) + \
        count_while_merge_sort(sums, mid, end, lower, upper)
    j = k = t = mid
    cache = [0] * (end - start)
    r = 0
    for i in range(start, mid):
        while k < end and sums[k] - sums[i] < lower:
            k += 1
        while j < end and sums[j] - sums[i] <= upper:
            j += 1
        while t < end and sums[t] < sums[i]:
            cache[r] = sums[t]
            r += 1
            t += 1
        cache[r] = sums[i]
        count += j - k
        r += 1
    sums[start: t] = cache[:t - start]
    # for ii in range(t - start):
    #     sums[start + ii] = cache[ii]
    return count


def countRangeSum2(nums, lower, upper):
    if not nums:
        return 0
    preSum = [0] * len(nums)
    preSum[0] = nums[0]
    for i in range(1, len(nums)):
        preSum[i] = nums[i] + preSum[i - 1]
    return process(preSum, 0, len(nums) - 1, lower, upper)


def process(preSum, L, R, lower, upper):
    if L == R:
        return 1 if lower <= preSum[L] <= upper else 0
    mid = L + ((R - L) >> 1)
    ans = process(preSum, L, mid, lower, upper)
    ans += process(preSum, mid + 1, R, lower, upper)
    ans += merge(preSum, L, mid, R, lower, upper)
    return ans

#
def merge(preSum, L, M, R, lower, upper):
    ans = 0
    windowL = L
    windowR = L
    # [windowL, windowR)
    for i in range(M + 1, R + 1):
        min_ = preSum[i] - upper
        max_ = preSum[i] - lower
        while windowR <= M and preSum[windowR] <= max_:
            windowR += 1
        while windowL <= M and preSum[windowL] < min_:
            windowL += 1
        ans += windowR - windowL

    help = [0] * (R - L + 1)
    i = 0
    l = L
    r = M + 1
    while l <= M and r <= R:
        if preSum[l] <= preSum[r]:
            help[i] = preSum[l]
            l += 1
            i += 1
        else:
            help[i] = preSum[r]
            r += 1
            i += 1
    while l <= M:
        help[i] = preSum[l]
        l += 1
        i += 1
    while r <= R:
        help[i] = preSum[r]
        r += 1
        i += 1
    for i in range(len(help)):
        preSum[L + i] = help[i]

    return ans


def merge2(preSum, L, M, R, lower, upper):
    ans = 0
    windowL = L
    windowR = L
    for i in preSum[M + 1: R + 1]:
        low = i - upper
        up = i - lower
        while windowL <= M and preSum[windowL] < low:
            windowL += 1
        while windowR <= M and preSum[windowR] <= up:
            windowR += 1
        ans += windowR - windowL

    p1 = L
    p2 = M + 1
    help = []
    while p1 <= M and p2 <= R:
        if preSum[p1] <= preSum[p2]:
            help.append(preSum[p1])
            p1 += 1
        else:
            help.append(preSum[p2])
            p2 += 1

    if p1 <= M:
        help.extend(preSum[p1:M + 1])
    if p2 <= R:
        help.extend(preSum[p2:R + 1])

    for i, num in enumerate(help):
        preSum[L + i] = num

    return ans


class SBTNode(object):
    def __init__(self, k):
        self.key = k
        self.size = 1
        self.all = 1
        self.l = None
        self.r = None

    def __repr__(self):
        return """[{}]<- ({}, {}, {}) -> [{}]""".format(self.l, self.key, self.size, self.all, self.r)


class SizeBalancedTreeSet(object):
    def __init__(self):
        self.root = None
        self.set = set()

    def right_rotate(self, cur):
        same = cur.all - (cur.l.all if cur.l else 0) - (cur.r.all if cur.r else 0)
        left_node = cur.l
        cur.l = left_node.r
        left_node.r = cur
        left_node.size = cur.size
        cur.size = (cur.l.size if cur.l else 0) + (cur.r.size if cur.r else 0) + 1

        # all modify
        left_node.all = cur.all
        cur.all = (cur.l.all if cur.l else 0) + (cur.r.all if cur.r else 0) + same
        return left_node

    def left_rotate(self, cur):
        same = cur.all - (cur.l.all if cur.l else 0) - (cur.r.all if cur.r else 0)
        right_node = cur.r
        cur.r = right_node.l
        right_node.l = cur
        right_node.size = cur.size
        cur.size = (cur.l.size if cur.l else 0) + (cur.r.size if cur.r else 0) + 1

        # all modify
        right_node.all = cur.all
        cur.all = (cur.l.all if cur.l else 0) + (cur.r.all if cur.r else 0) + same
        return right_node

    def maintain(self, cur):
        if cur is None:
            return None
        left_size = cur.l.size if cur.l else 0
        left_left_size = cur.l.l.size if cur.l and cur.l.l else 0
        left_right_size = cur.l.r.size if cur.l and cur.l.r else 0

        right_size = cur.r.size if cur.r else 0
        right_left_size = cur.r.l.size if cur.r and cur.r.l else 0
        right_right_size = cur.r.r.size if cur.r and cur.r.r else 0

        if left_left_size > right_size:
            cur = self.right_rotate(cur)
            cur.r = self.maintain(cur.r)
            cur = self.maintain(cur)
        elif left_right_size > right_size:
            cur.l = self.left_rotate(cur.r)
            cur = self.right_rotate(cur)
            cur.l = self.maintain(cur.l)
            cur.r = self.maintain(cur.r)
            cur = self.maintain(cur)
        elif right_right_size > left_size:
            cur = self.left_rotate(cur)
            cur.l = self.maintain(cur.l)
            cur = self.maintain(cur)
        elif right_left_size > left_size:
            cur.r = self.right_rotate(cur.r)
            cur = self.left_rotate(cur)
            cur.r = self.maintain(cur.r)
            cur.l = self.maintain(cur.l)
            cur = self.maintain(cur)
        return cur

    def _add(self, cur, key, contains):
        if cur is None:
            return SBTNode(key)

        cur.all += 1
        if key == cur.key:
            return cur

        if not contains:
            cur.size += 1
        if key < cur.key:
            cur.l = self._add(cur.l, key, contains)
        else:
            cur.r = self._add(cur.r, key, contains)
        return cur

    def add(self, sum):
        contains = sum in self.set
        self.root = self._add(self.root, sum, contains)
        self.set.add(sum)

    def less_key_size(self, key):
        cur = self.root
        ans = 0
        while cur:
            if key == cur.key:
                return ans + (cur.l.all if cur.l else 0)
            elif key < cur.key:
                cur = cur.l
            else:
                ans += cur.all - (cur.r.all if cur.r else 0)
                cur = cur.r
        return ans

    def more_key_size(self, key):
        return self.root.all - self.less_key_size(key + 1) if self.root else 0


def countRangeSum3(nums, lower, upper):
    tree_set = SizeBalancedTreeSet()
    sums = 0
    ans = 0
    tree_set.add(0)
    for num in nums:
        sums += num
        a = tree_set.less_key_size(sums - lower + 1)
        b = tree_set.less_key_size(sums - upper)
        ans += a - b
        tree_set.add(sums)
    return ans


""" for test """

def print_tree(head):
    print("Binary Tree:")
    printInOrder(head, 0, "H", 17)
    print("")


def printInOrder(head, height, to, length):
    if not head:
        return
    printInOrder(head.r, height + 1, "v", length)
    val = to + str(head.key) + to
    lenM = len(val)
    lenL = (length - lenM)
    lenR = (length - lenM - lenL)
    val = get_space(lenL) + val + get_space(lenR)
    print(get_space(height * length) + val)
    printInOrder(head.l, height + 1, "^", length)


def get_space(length):
    return " " * length


def generateRandomArray(maxSize, maxValue):
    """
    :param maxSize:
    :param maxValue:
    :return:
    """
    return [random.randint(-maxValue, maxValue) for _ in xrange(maxSize)]


""" for test """


if __name__ == "__main__":

    testTime = 10000
    maxSize = 100
    maxValue = 100
    print("测试开始")
    for i in trange(testTime):
        nums = generateRandomArray(maxSize, maxValue)
        lower = random.randint(-maxValue, maxValue)
        upper = lower + random.randint(0, maxValue)
        ans1 = countRangeSum1(nums[:], lower, upper)
        ans2 = countRangeSum2(nums[:], lower, upper)
        ans3 = countRangeSum2(nums[:], lower, upper)
        if ans1 != ans2 or ans1 != ans3:
            print nums
            print(ans1)
            print(ans2)
            print(ans3)
            break
    print("测试结束")
