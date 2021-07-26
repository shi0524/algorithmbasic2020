# -*- coding: utf-8 –*-
import random


class HeapGreater(object):
    def __init__(self, limit, cmpFunc=cmp):
        self.size = 0
        self.cmp = cmpFunc
        self.limit = limit
        self.heap = [0] * limit
        self.map = {}

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.limit

    def containts(self, obj):
        return obj in self.map

    def peek(self):
        return self.heap[0]

    def push(self, value):
        if self.isFull():
            raise RuntimeError("heap is full !!!")
        if self.containts(value):
            return
        self.heap[self.size] = value
        self.map[value] = self.size
        self.heap_insert(self.size)
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise RuntimeError("heap is empty !!!")
        self.size -= 1
        self.swap(0, self.size)
        self.heapify(0)
        ans = self.heap[self.size]
        self.map.pop(ans)
        return ans

    def remove(self, value):
        if value not in self.map:
            raise RuntimeError('{} not in heap'.format(value))
        self.size -= 1
        replace = self.heap[self.size]
        pos = self.map.pop(value)
        if value != replace:
            self.heap[pos] = replace
            self.map[replace] = pos
            self.resign(replace)

    def heap_insert(self, idx):
        arr = self.heap
        while idx and self.cmp(arr[idx], arr[(idx - 1) / 2]) < 0:
            self.swap(idx, (idx - 1) / 2)
            idx = (idx - 1) / 2

    def heapify(self, idx):
        arr = self.heap
        size = self.size
        left = idx * 2 + 1
        while left < size:
            bester = left + 1 if left + 1 < size and self.cmp(arr[left + 1], arr[left]) < 0 else left
            bester = bester if self.cmp(arr[bester], arr[idx]) < 0 else idx
            if idx == bester:
                break
            self.swap(idx, bester)
            idx = bester
            left = idx * 2 + 1

    def resign(self, value):
        self.heapify(self.map[value])
        self.heap_insert(self.map[value])

    def swap(self, i, j):
        arr = self.heap
        indxe_map = self.map
        arr[i], arr[j] = arr[j], arr[i]
        indxe_map[arr[i]], indxe_map[arr[j]] = indxe_map[arr[j]], indxe_map[arr[i]]


if __name__ == "__main__":
    lst = [13, 4, 10, 11, 2, 7, 3, 1, 8, 5, 9, 6, 12, 14, 15]
    h = HeapGreater(15)
    for i in lst:
        h.push(i)
    while h.size:
        h.pop()
    print(h.heap)


