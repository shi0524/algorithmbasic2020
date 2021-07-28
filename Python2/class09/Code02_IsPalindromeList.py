# -*- coding: utf-8 –*-

"""
给定一个单链表的头节点head，请判断该链表是否为回文结构。

1）哈希表方法特别简单（笔试用）

2）改原链表的方法就需要注意边界了（面试用）
"""


class Node(object):
    """ 单链表节点类
    """
    def __init__(self, value, nexts=None):
        self.val = value
        self.nexts = nexts

    def __repr__(self):
        return "%s -> %s" % (self.val, self.nexts) if self.nexts else "%s" % self.val


def is_palindrome1(head):
    """ 用其他容器  额外空间 N
    """
    stack = []
    cur = head
    while cur:
        stack.append(cur)
        cur = cur.nexts
    while head:
        if head.val != stack.pop().val:
            return False
        head = head.nexts
    return True


def is_palindrome2(head):
    """ 其他容器 额外空间 N/2
    """
    if not head or not head.nexts:
        return True

    cur = head
    right = head.nexts
    while cur.nexts and cur.nexts.nexts:
        right = right.nexts
        cur = cur.nexts.nexts
    stack = []
    while right:
        stack.append(right)
        right = right.nexts
    while stack:
        if head.val != stack.pop().val:
            return False
        head = head.nexts
    return True


def is_palindrome3(head):
    """ 不借助容器
        反转后半部分链表 --> 判断是否是回文 --> 还原链表  --> 返回判断结果
    """
    if not head or not head.nexts:
        return True
    n1 = head
    n2 = head
    while n2.nexts and n2.nexts.nexts:
        n1 = n1.nexts
        n2 = n2.nexts.nexts
    # n1 中点
    n2 = n1.nexts
    n1.nexts = None                     # 反转后半部分链表
    while n2:
        n3 = n2.nexts
        n2.nexts = n1
        n1 = n2
        n2 = n3
    n3 = n1                             # 链表尾部
    n2 = head                           # 链表头部

    is_palindrome = True
    while n1 and n2:                    # 检测是否是回文
        if n1.val != n2.val:
            is_palindrome = False       # 注意这里，不能反悔，需要还原链表
            break
        n1 = n1.nexts                   # 从尾部向中间移动
        n2 = n2.nexts                   # 从头部向中间移动

    n1 = n3.nexts                       # 将链表后半部分反转回来
    n3.nexts = None
    while n1:
        n2 = n1.nexts
        n1.nexts = n3
        n3 = n1
        n1 = n2

    return is_palindrome


if __name__ == "__main__":
    head = None
    print(head),
    print(is_palindrome1(head)),
    print(is_palindrome2(head)),
    print(is_palindrome3(head))
    print("*" * 40)

    head = Node(1)
    print(head),
    print(is_palindrome1(head)),
    print(is_palindrome2(head)),
    print(is_palindrome3(head))
    print("*" * 40)

    head = Node(1)
    head.nexts = Node(2)
    print(head),
    print(is_palindrome1(head)),
    print(is_palindrome2(head)),
    print(is_palindrome3(head))
    print("*" * 40)

    head = Node(1)
    head.nexts = Node(1)
    print(head),
    print(is_palindrome1(head)),
    print(is_palindrome2(head)),
    print(is_palindrome3(head))
    print("*" * 40)

    head = Node(1)
    head.nexts = Node(2)
    head.nexts.nexts = Node(3)
    print(head),
    print(is_palindrome1(head)),
    print(is_palindrome2(head)),
    print(is_palindrome3(head))
    print("*" * 40)

    head = Node(1)
    head.nexts = Node(2)
    head.nexts.nexts = Node(1)
    print(head),
    print(is_palindrome1(head)),
    print(is_palindrome2(head)),
    print(is_palindrome3(head))
    print("*" * 40)

    head = Node(1)
    head.nexts = Node(2)
    head.nexts.nexts = Node(3)
    head.nexts.nexts.nexts = Node(1)
    print(head),
    print(is_palindrome1(head)),
    print(is_palindrome2(head)),
    print(is_palindrome3(head))
    print("*" * 40)

    head = Node(1)
    head.nexts = Node(2)
    head.nexts.nexts = Node(2)
    head.nexts.nexts.nexts = Node(1)
    print(head),
    print(is_palindrome1(head)),
    print(is_palindrome2(head)),
    print(is_palindrome3(head))
    print("*" * 40)

    head = Node(1)
    head.nexts = Node(2)
    head.nexts.nexts = Node(3)
    head.nexts.nexts.nexts = Node(2)
    head.nexts.nexts.nexts.nexts = Node(1)
    print(head),
    print(is_palindrome1(head)),
    print(is_palindrome2(head)),
    print(is_palindrome3(head))
    print("*" * 40)

