# -*- coding: utf-8 –*-
import random


def heap_sort(arr):
    """ 堆排序
    """
    if not arr or len(arr) < 2:
        return
    size = len(arr)

    # O(Nlog(N))
    # for i in range(size):
    #     heap_insert(arr, i)

    # O(N)
    for i in range(size - 1, -1, -1):
        heapify(arr, i, size)

    # O(Nlog(N))
    while size:
        swap(arr, 0, size - 1)
        heapify(arr, 0, size - 1)
        size -= 1


def heap_insert(arr, idx):
    while idx and arr[idx] > arr[(idx-1)/2]:
        swap(arr, idx, (idx-1)/2)
        idx = (idx - 1) / 2


def heapify(arr, idx, size):
    left = idx * 2 + 1
    while left < size:
        largest = left + 1 if left + 1 < size and arr[left + 1] > arr[left] else left
        largest = largest if arr[largest] > arr[idx] else idx
        if idx == largest:
            break
        swap(arr, idx, largest)
        idx = largest
        left = idx * 2 + 1


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]



# for test
def generateRandomArray(maxSize, maxValue):
    """
    :param maxSize:
    :param maxValue:
    :return:
    """
    return [random.randint(-maxValue, maxValue) for _ in xrange(maxSize)]


if __name__ == "__main__":
    testTime = 50000
    maxSize = 100
    maxValue = 100
    print("测试开始")
    for i in xrange(testTime):
        arr1 = generateRandomArray(maxSize, maxValue)
        arr2 = arr1[::]
        heap_sort(arr1)
        arr2.sort()
        if arr1 != arr2:
            print(arr1)
            print(arr2)
            break
    print("测试结束")