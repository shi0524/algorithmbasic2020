# -*- coding: utf-8 –*-

class Node(object):
    """ 二叉树基础节点
    """
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left=left
        self.right = right


def f(head):
    if not head:
        return
    # 1 此处打印 head 先序遍历
    f(head.left)
    # 2 此处打印 head 中序遍历
    f(head.right)
    # 3 此处打印 head 后序遍历


def pre(head):
    """ 先序
    """
    if not head:
        return
    print(head.val),
    pre(head.left)
    pre(head.right)


def in_order(head):
    if not head:
        return
    in_order(head.left)
    print(head.val),
    in_order(head.right)


def pos(head):
    if not head:
        return
    pos(head.left)
    pos(head.right)
    print(head.val),


def level(root):
    """ 宽度遍历 分层打印
    """
    if not root:
        return []
    ans = []
    cur_level = 0
    queue = [(root, 1)]
    while queue:
        node, level = queue.pop()
        if level != cur_level:
            cur_level = level
            ans.append([])
        ans[-1].append(node.val)
        if node.left:
            queue.insert(0, (node.left, level + 1))
        if node.right:
            queue.insert(0, (node.right, level + 1))
    return ans


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

    pre(n1)
    print("")
    in_order(n1)
    print("")
    pos(n1)

    print("")
    print(level(n1))
