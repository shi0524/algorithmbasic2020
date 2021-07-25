# -*- coding: utf-8 –*-

"""
最大线段重合问题(用堆实现)
给定很多线段，每个线段都有两个数[start, end]，
表示线段开始位置和结束位置，左右都是闭区间
规定：
1）线段的开始和结束位置一定都是整数值
2）线段重合区域的长度必须>=1
返回线段最多重合区域中，包含了几条线段
"""
import heapq
import random
from Queue import PriorityQueue


def maxCover1(lines):
    """ 循环遍历
        时间复杂度: O(N * K)   K 为线段开始结束位置差
        额外空间复杂度: O(1)
    """
    min_s = lines[0][0]
    max_e = lines[0][1]
    for line in lines:
        min_s = min(min_s, line[0])
        max_e = max(max_e, line[1])

    cover = 0
    for s in range(min_s, max_e):
        ss = s + 0.5
        cur = 0
        for line in lines:
            if line[0] < ss < line[1]:
                cur += 1
        cover = max(cover, cur)
    return cover


def maxCover2(lines):
    """ 小根堆
        时间复杂度: O(N * logN)
        额外空间复杂度: O(N)
    """
    lines.sort()
    heap = PriorityQueue(len(lines))
    cover = 0
    for line in lines:
        s = line[0]
        while heap.queue and heap.queue[0] <= s:
            heap._get()
        heap._put(line[1])
        cover = max(cover, len(heap.queue))
    return cover


def maxCover3(lines):
    """ 差分数组
        时间复杂度: O(N)
        额外空间复杂度: O(K)   K 为线段开始结束位置差
    """
    min_s = lines[0][0]
    max_e = lines[0][1]
    for line in lines:
        min_s = min(min_s, line[0])
        max_e = max(max_e, line[1])
    diff = [0] * (max_e - min_s + 1)
    for line in lines:
        diff[line[0] - min_s] += 1
        diff[line[1] - min_s] -= 1
    pre_sum = 0
    cover = 0
    for i in diff:
        pre_sum += i
        cover = max(cover, pre_sum)
    return cover


# for test
def generateLines(N, L, R):
    size = random.randint(1, N)
    lines = []
    for _ in range(size):
        l = random.randint(L, R)
        r = random.randint(L, R)
        if l == r:
            r += 1
        if l > r:
            l, r = r, l
        lines.append([l, r])
    return lines


if __name__ == "__main__":
    N = 3
    L = 0
    R = 20
    testTimes = 200000
    print("test begin !!!")
    for _ in range(testTimes):
        lines = generateLines(N, L, R)
        ans1 = maxCover1(lines)
        ans2 = maxCover2(lines)
        ans3 = maxCover3(lines)
        if ans1 != ans2 or ans1 != ans3:
            print(ans1, ans2, ans3)
            break
    print("test end !!!")