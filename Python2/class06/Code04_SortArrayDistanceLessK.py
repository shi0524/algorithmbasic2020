# -*- coding: utf-8 –*-


import heapq
from Queue import PriorityQueue


def sortedArrDistanceLessK(arr, k):
    if not arr:
        return []
    heap = PriorityQueue(k)
    idx = 0
    while idx < min(k, len(arr)):
        heap._put(arr[idx])
        idx += 1
    for i in range(idx, len(arr)):
        heap._put(arr[i])
        heap._get()
    ans = [0] * k
    while heap._qsize():
        k -= 1
        ans[k] = heap._get()
    return ans


def sortedArrDistanceLessK2(arr, k):
    return heapq.nlargest(k, arr)


if __name__ == "__main__":
    arr = [1, 5, 7, 9, 2, 4, 6, 8, 3]
    ans = sortedArrDistanceLessK(arr, 3)
    print ans
    ans = sortedArrDistanceLessK2(arr, 3)
    print ans

