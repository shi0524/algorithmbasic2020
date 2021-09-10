# -*- coding: utf-8 –*-

"""
morris 遍历

假设来到当前节点cur，开始时cur来到头节点位置
1）如果cur没有左孩子，cur向右移动(cur = cur.right)
2）如果cur有左孩子，找到左子树上最右的节点mostRight:
    a.如果mostRight的右指针指向空，让其指向cur, 然后cur向左移动(cur = cur.left)
    b.如果mostRight的右指针指向cur，让其指向null, 然后cur向右移动(cur = cur.right)
3）cur为空时遍历停止

特点：
    有左孩子的遍历 2 次
    没有左孩子的只 1 次
"""


class Node(object):

    __slots__ = ("val", "left", "right")

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "{}".format(self.val)


def morris(root):
    """ morris 遍历
    """
    cur = root
    # 如果当前节点不为空
    while cur:
        print(cur),
        # most_right 当前节点的最后节点
        most_right = cur.left
        # 如果当前节点有左孩子
        if most_right:
            # 去找左孩子的最右节点
            # 如果最右节点的右指针指向空 或者 指向 当前节点 找到最右孩子
            while most_right.right and most_right.right != cur:
                most_right = most_right.right
            # 如果最右孩子右节点指向空, 将右节点指向当前节点, 当前节点来到左孩子
            if most_right.right is None:
                most_right.right = cur
                cur = cur.left
                continue
            # 如果最右孩子右指针指向当前节点, 将右孩子右指针指向空
            else:
                most_right.right = None
        # 当前节点往右移, 来到右孩子节点
        cur = cur.right
    print("")


def morris_pre(root):
    """ morris 先序遍历
        有左树(会来到2次), 第一次来到时打印
        无左树(会来到1次), 第一次来到时打印
    """
    cur = root
    # 如果当前节点不为空
    while cur:
        # most_right 当前节点的最后节点
        most_right = cur.left
        # 如果当前节点有左孩子
        if most_right:
            # 去找左孩子的最右节点
            # 如果最右节点的右指针指向空 或者 指向 当前节点 找到最右孩子
            while most_right.right and most_right.right != cur:
                most_right = most_right.right
            # 如果最右孩子右节点指向空, 将右节点指向当前节点, 当前节点来到左孩子
            if most_right.right is None:
                print(cur),
                most_right.right = cur
                cur = cur.left
                continue
            # 如果最右孩子右指针指向当前节点, 将右孩子右指针指向空
            else:
                most_right.right = None
        else:
            print(cur),
        # 当前节点往右移, 来到右孩子节点
        cur = cur.right
    print(" ")


def morris_in(root):
    """ morris 中序遍历
        有左树(会来到2次), 第 2 次来到时打印
        无左树(会来到1次), 第 1 次来到时打印
    """
    cur = root
    # 如果当前节点不为空
    while cur:
        # most_right 当前节点的最后节点
        most_right = cur.left
        # 如果当前节点有左孩子
        if most_right:
            # 去找左孩子的最右节点
            # 如果最右节点的右指针指向空 或者 指向 当前节点 找到最右孩子
            while most_right.right and most_right.right != cur:
                most_right = most_right.right
            # 如果最右孩子右节点指向空, 将右节点指向当前节点, 当前节点来到左孩子
            if most_right.right is None:
                most_right.right = cur
                cur = cur.left
                continue
            # 如果最右孩子右指针指向当前节点, 将右孩子右指针指向空
            else:
                most_right.right = None
        print(cur),
        # 当前节点往右移, 来到右孩子节点
        cur = cur.right
    print(" ")


def morris_pos(root):
    """ morris 后续遍历
        有左树(会来到2次), 第 2 次来到时 逆序打印左树的右边界
        无左树(会来到1次)
        遍历结束, 逆序打印头结点的右边界
    """
    cur = root
    # 如果当前节点不为空
    while cur:
        # most_right 当前节点的最后节点
        most_right = cur.left
        # 如果当前节点有左孩子
        if most_right:
            # 去找左孩子的最右节点
            # 如果最右节点的右指针指向空 或者 指向 当前节点 找到最右孩子
            while most_right.right and most_right.right != cur:
                most_right = most_right.right
            # 如果最右孩子右节点指向空, 将右节点指向当前节点, 当前节点来到左孩子
            if most_right.right is None:
                most_right.right = cur
                cur = cur.left
                continue
            # 如果最右孩子右指针指向当前节点, 将右孩子右指针指向空
            else:
                most_right.right = None
                print_edge(cur.left)
        # 当前节点往右移, 来到右孩子节点
        cur = cur.right
    print_edge(root)
    print(" ")


def print_edge(head):
    """ 逆序打印树的有边界
        1、逆序右边界
        2、打印
        3、逆序回来
    """
    tail = reverse_edge(head)
    cur = tail
    while cur:
        print(cur),
        cur = cur.right
    reverse_edge(tail)


def reverse_edge(head):
    """ 树节点反转
    """
    pre = None
    cur = head
    while cur:
        right = cur.right
        cur.right = pre
        pre = cur
        cur = right
    return pre


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

    morris(n1)
    print("*" * 50)

    morris_pre(n1)
    print("*" * 50)

    morris_in(n1)
    print("*" * 50)

    morris_pos(n1)
    print("*" * 50)