# -*- coding: utf-8 –*-

from collections import defaultdict

"""
打印二叉树
"""

class Node(object):
    """ 二叉树基础节点
    """
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def print_tree(head):
    print("Binary Tree:")
    printInOrder(head, 0, "H", 17)
    print("")


def printInOrder(head, height, to, length):
    if not head:
        return
    printInOrder(head.right, height + 1, "v", length)
    val = to + str(head.val) + to
    lenM = len(val)
    lenL = (length - lenM)
    lenR = (length - lenM - lenL)
    val = get_space(lenL) + val + get_space(lenR)
    print(get_space(height * length) + val)
    printInOrder(head.left, height + 1, "^", length)


def get_space(length):
    return " " * length



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

    print_tree(n1)