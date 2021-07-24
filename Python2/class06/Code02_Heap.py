# -*- coding: utf-8 –*-

"""
大根堆
"""
import random


class MyMaxHeap(object):
    def __init__(self, limit):
        self.limit = limit
        self.size = 0
        self.heap = [0] * limit

    def isEmpty(self):
        return not self.size

    def isFull(self):
        return self.size == self.limit

    def push(self, num):
        if self.isFull():
            raise RuntimeError('堆已满')
        self.heap[self.size] = num
        self.heapInsert(self.heap, self.size)
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise RuntimeError('堆为空')
        self.size -= 1
        self.swap(self.heap, 0, self.size)
        self.heapify(self.heap, 0, self.size)
        return self.heap[self.size]

    @classmethod
    def heapInsert(cls, arr, idx):
        while idx > 0 and arr[idx] > arr[(idx - 1)/2]:
            cls.swap(arr, idx, (idx - 1) / 2)
            idx = (idx - 1) / 2

    def heapify(self, arr, idx, heap_size):
        left = idx * 2 + 1
        while left < heap_size:
            largest = left + 1 if left + 1 < heap_size and arr[left + 1] > arr[left] else left
            largest = largest if arr[largest] > arr[idx] else idx
            if idx == largest:
                break
            self.swap(arr, idx, largest)
            idx = largest
            left = idx * 2 + 1

    @classmethod
    def swap(cls, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]


# for test
class RightMaxHeap(object):
    def __init__(self, limit):
        self.heap = []
        self.limit = limit

    def isEmpty(self):
        return not self.heap

    def isFull(self):
        return len(self.heap) == self.limit

    def push(self, num):
        if self.isFull():
            raise RuntimeError("堆已满")
        self.heap.append(num)

    def pop(self):
        if self.isEmpty():
            raise RuntimeError("堆为空")
        _max = max(self.heap)
        self.heap.remove(_max)
        return _max


if __name__ == "__main__":
    # lst = [-1, 3, 6, -9, 8, 7, 5, 4, 2, 0]
    # heap = MyMaxHeap(10)
    # for i in lst:
    #     heap.push(i)
    # print(heap.heap)
    # while not heap.isEmpty():
    #     heap.pop()
    # print(heap.heap)

    value = 1000
    limit = 100
    testTimes = 1000000

    print("test begin!!!")

    for _ in range(testTimes):
        cur_limit = random.randint(1, limit)
        curOpTimes = random.randint(1, limit)
        my = MyMaxHeap(cur_limit)
        right = RightMaxHeap(cur_limit)
        for _ in range(curOpTimes):
            if my.isEmpty() != right.isEmpty():
                print("ERROR isEmpty")
                break
            if my.isFull() != right.isFull():
                print("ERROR isFull")
                break
            if my.isEmpty():
                cur_value = random.randint(0, value)
                my.push(cur_value)
                right.push(cur_value)
            elif my.isFull():
                if my.pop() != right.pop():
                    print("ERROR pop")
            else:
                if random.randint(0, 1):
                    cur_value = random.randint(0, value)
                    my.push(cur_value)
                    right.push(cur_value)
                else:
                    if my.pop() != right.pop():
                        print("ERROR pop")

    print("test end!!!")