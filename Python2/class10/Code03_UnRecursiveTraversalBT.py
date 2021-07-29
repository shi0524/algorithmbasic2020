# -*- coding: utf-8 –*-

"""
二叉树的分递归遍历
"""


class Node(object):
    """ 二叉树基础节点
    """
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left=left
        self.right = right


def pre_order(head):
    print("pre-order:"),
    if not head:
        return
    stack = []
    stack.append(head)
    while stack:
        node = stack.pop()
        print(node.val),
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    print("")


def in_order(head):
    print("in-order:"),
    if not head:
        return
    stack = []
    cur = head
    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            print(cur.val),
            cur = cur.right
    print("")


def pos_order1(head):
    print("pos-order:"),
    if not head:
        return
    stack1 = [head]
    stack2 = []
    while stack1:
        node = stack1.pop()             # 头、右、左
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while stack2:                       # 左、右、头
        print(stack2.pop().val),
    print("")


def pos_order2(head):
    print("pos-order:"),
    if not head:
        return
    h = head
    stack = [head]
    while stack:
        cur = stack[-1]
        if cur.left and h != cur.left and h != cur.right:
            stack.append(cur.left)
        elif cur.right and h != cur.right:
            stack.append(cur.right)
        else:
            print(stack.pop().val),
            h = cur
    print("")


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    n10 = Node(10)
    n11 = Node(11)
    n12 = Node(12)
    n13 = Node(13)
    n14 = Node(14)
    n15 = Node(15)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n4.left = n8
    n4.right = n9
    n5.left = n10
    n5.right = n11
    n6.left = n12
    n6.right = n13
    n7.left = n14
    n7.right = n15

    pre_order(n1)
    in_order(n1)
    pos_order1(n1)
    pos_order2(n1)

