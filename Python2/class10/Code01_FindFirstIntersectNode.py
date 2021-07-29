# -*- coding: utf-8 –*-

"""
给定两个可能有环也可能无环的单链表，头节点head1和head2。
请实现一个函数，
    如果两个链表相交，请返回相交的 第一个节点。
    如果不相交，返回null
【要求】
    如果两个链表长度之和为N，时间复杂度请达到O(N)，额外空间复杂度 请达到O(1)。
"""


class Node(object):
    """ 单链表节点类
    """
    def __init__(self, value, nexts=None):
        self.val = value
        self.nexts = nexts

    def __repr__(self, deep=10):
        return "%s -> %s" % (self.val, self.nexts.__repr__(deep-1)) if self.nexts else "%s" % self.val


def getIntersectNode(head1, head2):
    if not head1 or not head2:
        return None
    loop1 = getLoopNode(head1)
    loop2 = getLoopNode(head2)

    # 都没有环
    if not loop1 and not loop2:
        return noLoop(head1, head2)
    if loop1 and loop2:
        return bothLoop(head1, loop1, head2, loop2)
    return None


def getLoopNode(head):
    """ 如果一个链表有环, 返回入环位置
        如果无环, 返回None
    """
    if not head or not head.nexts or not head.nexts.nexts:
        return None

    # 定义快慢指针
    slow = head.nexts
    fast = head.nexts.nexts

    # 如果不是快慢指针相遇, 则说明无环
    while slow != fast:
        if not fast or not fast.nexts:  # fast 走到链表尾部, 说明无环
            return None
        slow = slow.nexts
        fast = fast.nexts.nexts

    # 有环, fast 从头走, 每次1步, 与 slow 再次相遇，则为入环位置
    fast = head
    while slow != fast:
        slow = slow.nexts
        fast = fast.nexts
    return slow


def noLoop(head1, head2):
    if not head1 or not head2:
        return None

    cur1 = head1
    cur2 = head2
    n = 0
    while cur1.nexts:
        n += 1
        cur1 = cur1.nexts

    while cur2.nexts:
        n -= 1
        cur2 = cur2.nexts

    # 最后一个链表不相等, 肯定不相交
    if cur1 != cur2:
        return None

    cur1 = head1 if n >= 0 else head2
    cur2 = head2 if cur1 == head1 else head2
    n = abs(n)
    while n:
        n -= 1
        cur1 = cur1.nexts
    while cur1 != cur2:
        cur1 = cur1.nexts
        cur2 = cur2.nexts
    return cur1


def bothLoop(head1, loop1, head2, loop2):
    """ 两个以loop1、loop2 结尾的有环链表相交问题
    :param head1: 链表1
    :param loop1: 链表1入环点
    :param head2: 链表2
    :param loop2: 链表2入环点
    :return:
    """
    # loop1 = loop2  在入环点或环外相交
    # 转换成以loop1为结尾的两条无环链表相交问题
    if loop1 == loop2:
        cur1 = head1
        cur2 = head2
        n = 0
        while cur1.nexts != loop1:
            n += 1
            cur1 = cur1.nexts
        while cur2.nexts != loop1:
            n -= 1
            cur2 = cur2.nexts
        cur1 = head1 if n >= 0 else cur2
        cur2 = head2 if cur1 == head1 else head1
        n = abs(n)
        while n:
            n -= 1
            cur1 = cur1.nexts
        while cur1 != cur2:
            cur1 = cur1.nexts
            cur2 = cur2.nexts
        return cur1
    else:
        # 循环一个环一周, 期间遇见loop2则相交, 否则不相交
        cur1 = loop1.nexts
        while cur1 != loop1:
            if cur1 == loop2:
                return loop1
            cur1 = cur1.nexts
        return None


def print_link_list(head):
    loop = getLoopNode(head)
    if loop:
        while head != loop.nexts.nexts:
            print head.val, "->",
            head = head.nexts
        while head != loop.nexts:
            print head.val, "->",
            head = head.nexts
        print head.val, "..."
    else:
        print(head)


if __name__ == "__main__":

    # 1->2->3->4->5->6->7->null
    head1 = Node(1)
    head1.nexts = Node(2)
    head1.nexts.nexts = Node(3)
    head1.nexts.nexts.nexts = Node(4)
    head1.nexts.nexts.nexts.nexts = Node(5)
    head1.nexts.nexts.nexts.nexts.nexts = Node(6)
    head1.nexts.nexts.nexts.nexts.nexts.nexts = Node(7)

    # 0->9->8->6->7->null
    head2 = Node(0)
    head2.nexts = Node(9)
    head2.nexts.nexts = Node(8)
    head2.nexts.nexts.nexts = head1.nexts.nexts.nexts.nexts.nexts

    print(head1)
    print(head2)
    print(getIntersectNode(head1, head2))
    print("*" * 50)

    # 1->2->3->4->5->6->7->4...
    head1 = Node(1)
    head1.nexts = Node(2)
    head1.nexts.nexts = Node(3)
    head1.nexts.nexts.nexts = Node(4)
    head1.nexts.nexts.nexts.nexts = Node(5)
    head1.nexts.nexts.nexts.nexts.nexts = Node(6)
    head1.nexts.nexts.nexts.nexts.nexts.nexts = Node(7)
    head1.nexts.nexts.nexts.nexts.nexts.nexts.nexts = head1.nexts.nexts.nexts

    # 0->9->8->2...
    head2 = Node(0)
    head2.nexts = Node(9)
    head2.nexts.nexts = Node(8)
    head2.nexts.nexts.nexts = head1.nexts

    print_link_list(head1)
    print_link_list(head2)
    print_link_list(getIntersectNode(head1, head2))
    print("*" * 50)

    # 0->9->8->7->4->5->6...
    head2 = Node(0)
    head2.nexts = Node(9)
    head2.nexts.nexts = Node(8)
    head2.nexts.nexts.nexts = head1.nexts.nexts.nexts.nexts.nexts.nexts

    print_link_list(head1)
    print_link_list(head2)
    print_link_list(getIntersectNode(head1, head2))


