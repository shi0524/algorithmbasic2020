# -*- coding: utf-8 –*-

""" 某个节点的后继节点
"""

class Node(object):
    """ 二叉树基础节点
    """
    def __init__(self, value, left=None, right=None, parent=None):
        self.val = value
        self.left = left
        self.right = right
        self.parent = parent


def getSuccessorNode(node):
    if not node:
        return node
    if node.right:
        return getLeftMost(node.right)
    parent = node.parent
    while parent and parent.right == node:
        node = parent
        parent = node.parent
    return parent


def getLeftMost(node):
    if not node:
        return node
    while node.left:
        node = node.left
    return node


if __name__ == "__main__":
    head = Node(6)
    head.left = Node(3)
    head.left.parent = head
    head.left.left = Node(1)
    head.left.left.parent = head.left
    head.left.left.right = Node(2)
    head.left.left.right.parent = head.left.left
    head.left.right = Node(4)
    head.left.right.parent = head.left
    head.left.right.right = Node(5)
    head.left.right.right.parent = head.left.right
    head.right = Node(9)
    head.right.parent = head
    head.right.left = Node(8)
    head.right.left.parent = head.right
    head.right.left.left = Node(7)
    head.right.left.left.parent = head.right.left
    head.right.right = Node(10)
    head.right.right.parent = head.right

    test = head.left.left
    print(test.val, "next:", getSuccessorNode(test).val)
    test = head.left.left.right
    print(test.val, "next:", getSuccessorNode(test).val)
    test = head.left
    print(test.val, "next:", getSuccessorNode(test).val)
    test = head.left.right
    print(test.val, "next:", getSuccessorNode(test).val)
    test = head.left.right.right
    print(test.val, "next:", getSuccessorNode(test).val)
    test = head
    print(test.val, "next:", getSuccessorNode(test).val)
    test = head.right.left.left
    print(test.val, "next:", getSuccessorNode(test).val)
    test = head.right.left
    print(test.val, "next:", getSuccessorNode(test).val)
    test = head.right
    print(test.val, "next:", getSuccessorNode(test).val)
    test = head.right.right
    print(test.val, "next:", getSuccessorNode(test))