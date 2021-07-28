# -*- coding: utf-8 –*-

"""
一种特殊的单链表节点类描述如下
class Node {
    int value;
    Node next;
    Node rand;
    Node(int val) { value = val; }
}
rand指针是单链表节点结构中新增的指针，rand可能指向链表中的任意一个节点，也可能指向null。
给定一个由Node节点类型组成的无环单链表的头节点 head，请实现一个函数完成这个链表的复制，并返回复制的新链表的头节点。
【要求】
时间复杂度O(N)，额外空间复杂度O(1)
"""


class Node(object):
    """ 单链表节点类
    """
    def __init__(self, value, nexts=None, random=None):
        self.val = value
        self.nexts = nexts
        self.random = random

    def __repr__(self):
        if self.random and self.nexts:
            return "%s(%s)-> %s" % (self.val, self.random.val, self.nexts)
        elif self.nexts:
            return "%s-> %s" % (self.val, self.nexts)
        elif self.random:
            return "%s(%s)" % (self.val, self.random.val)
        else:
            return "%s" % self.val


def copyListWithRand1(head):
    """ 借助字典
        时间复杂度O(N)
        额外空间复杂度 O(N)
    """
    mapping = {}
    cur = head
    while cur:
        mapping[cur] = Node(cur.val)
        cur = cur.nexts
    cur = head
    while cur:
        if cur.nexts:
            mapping[cur].nexts = mapping[cur.nexts]
        if cur.random:
            mapping[cur].random = mapping[cur.random]
        cur = cur.nexts
    return mapping[head]


def copyListWithRand2(head):
    """
        拷贝节点 链接 在 源节点的后面, 源节点.nexts ==> 拷贝节点
        1 -> 2 -> 3
        1 -> 1' -> 2 -> 2' -> 3 -> 3'

        断开连接：
            1 -> 2 -> 3
            1' -> 2' -> 3'
    """
    cur = head
    while cur:                          # 拷贝节点
        nexts = cur.nexts
        cur_copy = Node(cur.val)
        cur.nexts = cur_copy
        cur_copy.nexts = nexts
        cur = nexts
    cur = head
    while cur:                          # 连接 random 节点
        cur_copy = cur.nexts
        if cur.random:
            cur_copy.random = cur.random.nexts
        cur = cur.nexts.nexts

    head_copy = head.nexts
    cur = head
    cur_copy = head.nexts
    while cur_copy.nexts:               # 断开拷贝节点与源节点的链接
        nexts = cur.nexts.nexts
        nexts_copy = nexts.nexts
        cur.nexts = nexts
        cur_copy.nexts = nexts_copy
        cur = nexts
        cur_copy = nexts_copy
    cur.nexts = None                    # 将尾结点与拷贝尾结点断开连接

    return head_copy


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)

    n1.nexts = n2
    n2.nexts = n3
    n3.nexts = n4
    n4.nexts = n5
    n5.nexts = n6
    n6.nexts = n7

    n1.random = n5
    n2.random = n5
    n3.random = n2
    n4.random = n1
    n5.random = n3
    n6.random = n2
    n7.random = n4

    print(n1)
    n11 = copyListWithRand1(n1)
    print(n11)
    n12 = copyListWithRand2(n1)
    print(n1)
    print(n12)