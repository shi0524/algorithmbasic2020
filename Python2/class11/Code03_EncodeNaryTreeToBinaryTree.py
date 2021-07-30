# -*- coding: utf-8 –*-

from collections import deque

"""
431. Encode N-ary Tree to Binary Tree
本题测试链接：https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree
"""


class Node(object):
    """ 多叉树节点类
    """
    def __init__(self, value, children=None):
        self.val = value
        self.children = children or []


class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def encode(root):
    if not root:
        return None
    head = TreeNode(root.val)
    head.left = en(root.children)
    return head


def en(children):
    cur = None
    head = None
    for child in children:
        tnode = TreeNode(child.val)
        if not head:
            head = tnode
        else:
            cur.right = tnode
        cur = tnode
        cur.left = en(child.children)
    return head


def decode(root):
    if not root:
        return None
    return Node(root.val, de(root.left))


def de(root):
    children = []
    while root:
        cur = Node(root.val, de(root.left))
        children.append(cur)
        root = root.right
    return children


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
    n1.children = [n2, n3, n4, n5]
    n2.children = [n6, n7, n8]
    n4.children = [n9, n10]
    n5.children = [n11, n12, n13]
    n7.children = [n14, n15]

    n11 = encode(n1)
    level(n11)
    n12 = decode(n11)
    n11 = encode(n12)
    level(n11)

