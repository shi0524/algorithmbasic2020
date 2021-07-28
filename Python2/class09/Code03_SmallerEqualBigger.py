# -*- coding: utf-8 –*-

"""
将单向链表按某值划分成左边小、中间相等、右边大的形式

1）把链表放入数组里，在数组上做partition（笔试用）

2）分成小、中、大三部分，再把各个部分之间串起来（面试用）
"""


class Node(object):
    """ 单链表节点类
    """
    def __init__(self, value, nexts=None):
        self.val = value
        self.nexts = nexts

    def __repr__(self):
        return "%s -> %s" % (self.val, self.nexts) if self.nexts else "%s" % self.val


def listPartition1(head, pivot):
    if not head or not head.nexts:
        return head
    cur = head
    node_arr = []
    while cur:
        node_arr.append(cur)
        cur = cur.nexts
    arr_partition(node_arr, pivot)
    for i in range(1, len(node_arr)):
        node_arr[i-1].nexts = node_arr[i]
    node_arr[len(node_arr) - 1].nexts = None
    return node_arr[0]


def arr_partition(arr, pivot):
    small = -1
    big = len(arr)
    idx = 0
    while idx != big:
        if arr[idx].val < pivot:
            small += 1
            swap(arr, small, idx)
            idx += 1
        elif arr[idx].val == pivot:
            idx += 1
        else:
            big -= 1
            swap(arr, idx, big)     # 在这里交换, 大于区域排序是倒着的, 这里排序是不稳定的


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def listPartition2(head, pivot):
    if not head or not head.nexts:
        return head
    small_head = None
    small_tail = None
    equal_head = None
    equal_tail = None
    big_head = None
    big_tail = None
    cur = head
    while cur:
        nexts = cur.nexts
        cur.nexts = None
        if cur.val < pivot:
            if not small_head:
                small_head = cur
                small_tail = cur
            else:
                small_tail.nexts = cur
                small_tail = small_tail.nexts
        elif cur.val == pivot:
            if not equal_head:
                equal_head = cur
                equal_tail = cur
            else:
                equal_tail.nexts = cur
                equal_tail = equal_tail.nexts
        else:
            if not big_head:
                big_head = cur
                big_tail = cur
            else:
                big_tail.nexts = cur
                big_tail = big_tail.nexts
        cur = nexts

    # 链接 三个区域
    # new_head = small_head
    # new_tail = small_tail
    # if not new_head:
    #     new_head = equal_head
    #     new_tail = equal_tail
    # else:
    #     new_tail.nexts = equal_head
    #     new_tail = equal_tail
    # if not new_head:
    #     new_head = big_head
    #     new_tail = big_tail
    # else:
    #     new_tail.nexts = big_head
    #     new_tail = big_tail
    # return new_head

    # 链接 三个区域 精简版
    # 小于区域的尾巴，连等于区域的头，等于区域的尾巴连大于区域的头
    if small_tail:  # 如果有小于区域
        small_tail.nexts = equal_head
        equal_tail = equal_tail or small_tail   # 下一步，谁去连大于区的头，谁变成 equal_tail
    # 下一步，一定是需要用eT去接大于区域的头
    # 有等于区域，equal_tail -> 等于区域的尾结点
    # 无等于区域，equal_tail -> 小于区域的尾结点

    # equal_tail 尽量不为空的尾巴节点
    if equal_tail:  # 如果小于区域和等于区域，不是都没有
        equal_tail.nexts = big_head
    return small_head if small_head else (equal_head if equal_head else big_head)


if __name__ == "__main__":
    n1 = Node(1)
    n1.nexts = Node(2)
    n1.nexts.nexts = Node(3)
    n1.nexts.nexts.nexts = Node(4)
    n1.nexts.nexts.nexts.nexts = Node(3)
    n1.nexts.nexts.nexts.nexts.nexts = Node(5)
    n1.nexts.nexts.nexts.nexts.nexts.nexts = Node(3)

    head = listPartition1(n1, 3)
    print(head)

    n1 = Node(1)
    n1.nexts = Node(2)
    n1.nexts.nexts = Node(3)
    n1.nexts.nexts.nexts = Node(4)
    n1.nexts.nexts.nexts.nexts = Node(3)
    n1.nexts.nexts.nexts.nexts.nexts = Node(5)
    n1.nexts.nexts.nexts.nexts.nexts.nexts = Node(3)

    head = listPartition2(n1, 3)
    print(head)