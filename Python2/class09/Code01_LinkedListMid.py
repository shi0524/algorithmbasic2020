# -*- coding: utf-8 –*-

"""
1）输入链表头节点，奇数长度返回中点，偶数长度返回上中点

2）输入链表头节点，奇数长度返回中点，偶数长度返回下中点

3）输入链表头节点，奇数长度返回中点前一个，偶数长度返回上中点前一个

4）输入链表头节点，奇数长度返回中点前一个，偶数长度返回下中点前一个
"""


class Node(object):
    """ 单链表节点类
    """
    def __init__(self, value, nexts=None):
        self.val = value
        self.nexts = nexts


def mid_or_upmid_node(head):
    """ 中点或上中点
    """
    if not head or not head.nexts or not head.nexts.nexts:
        return head

    # 链表上至少有3个节点
    slow = head.nexts
    fast = head.nexts.nexts
    while fast.nexts and fast.nexts.nexts:
        slow = slow.nexts
        fast = fast.nexts.nexts
    return slow


def mid_or_downmid_node(head):
    """ 中点或下中点
    """
    if not head or not head.nexts:
        return head
    slow = head.nexts
    fast = head.nexts
    while fast.nexts and fast.nexts.nexts:
        slow = slow.nexts
        fast = fast.nexts.nexts
    return slow


def mid_or_upmid_pre_node(head):
    """ 中点或上中点的前一个节点
    """
    if not head or not head.nexts or not head.nexts.nexts:
        return None
    slow = head
    fast = head.nexts.nexts
    while fast.nexts and fast.nexts.nexts:
        slow = slow.nexts
        fast = fast.nexts.nexts
    return slow


def mid_or_downmid_pre_node(head):
    """ 中点或下中点的前一个节点
    """
    if not head or not head.nexts:
        return None
    if not head.nexts.nexts:
        return head

    slow = head
    fast = head.nexts
    while fast.nexts and fast.nexts.nexts:
        slow = slow.nexts
        fast = fast.nexts.nexts
    return slow


def right1(head):
    if not head:
        return None
    arr = []
    cur = head
    while cur:
        arr.append(cur)
        cur = cur.nexts
    return arr[(len(arr) - 1)/2]


def right2(head):
    if not head:
        return None
    arr = []
    cur = head
    while cur:
        arr.append(cur)
        cur = cur.nexts
    return arr[len(arr)/2]


def right3(head):
    if not head or not head.nexts or not head.nexts.nexts:
        return None
    arr = []
    cur = head
    while cur:
        arr.append(cur)
        cur = cur.nexts
    return arr[(len(arr) - 3)/2]


def right4(head):
    if not head or not head.nexts:
        return None
    arr = []
    cur = head
    while cur:
        arr.append(cur)
        cur = cur.nexts
    return arr[(len(arr) - 2)/2]


if __name__ == "__main__":
    test = Node(0)
    test.nexts = Node(1)
    test.nexts.nexts = Node(2)
    test.nexts.nexts.nexts = Node(3)
    test.nexts.nexts.nexts.nexts = Node(4)
    test.nexts.nexts.nexts.nexts.nexts = Node(5)
    test.nexts.nexts.nexts.nexts.nexts.nexts = Node(6)
    test.nexts.nexts.nexts.nexts.nexts.nexts.nexts = Node(7)
    test.nexts.nexts.nexts.nexts.nexts.nexts.nexts.nexts = Node(8)

    ans1 = mid_or_upmid_node(test)
    ans2 = right1(test)
    print(ans1.val if ans1 else "无")
    print(ans2.val if ans2 else "无")

    ans1 = mid_or_downmid_node(test)
    ans2 = right2(test)
    print(ans1.val if ans1 else "无")
    print(ans2.val if ans2 else "无")

    ans1 = mid_or_upmid_pre_node(test)
    ans2 = right3(test)
    print(ans1.val if ans1 else "无")
    print(ans2.val if ans2 else "无")

    ans1 = mid_or_downmid_pre_node(test)
    ans2 = right4(test)
    print(ans1.val if ans1 else "无")
    print(ans2.val if ans2 else "无")