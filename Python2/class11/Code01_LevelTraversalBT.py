# -*- coding: utf-8 –*-

from collections import deque


"""
1）其实就是宽度优先遍历，用队列
2）可以通过设置flag变量的方式，来发现某一层的结束（看题目）
"""


class Node(object):
    """ 二叉树基础节点
    """
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def level(head):
    if not head:
        return
    queue = deque()
    queue.appendleft(head)
    while queue:
        node = queue.pop()
        print(node.val),
        if node.left:
            queue.appendleft(node.left)
        if node.right:
            queue.appendleft(node.right)
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

    level(n1)