# -*- coding: utf-8 –*-

"""
二叉树的递归套路深度实践
给定一棵二叉树的头节点head，返回这颗二叉树是不是满二叉树
"""
import random


class Node(object):
    """ 二叉树基础节点
    """

    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def is_full1(head):
    """ 通过对比每层的节点数量，判断是不是满二叉树
    """
    if not head:
        return True
    level = 0
    node_num = 0
    queue = [[head, 0]]
    while queue:
        node, cur_lv = queue.pop(0)
        if cur_lv == level:
            node_num += 1
        else:
            if node_num != 1 << level:
                return False
            node_num = 1
            level = cur_lv
    return node_num == 1 << level


def isFull2(head):
    info = check_full(head)
    return info['is_full']


def check_full(head):
    if not head:
        return {'is_full': True, 'hight': 0}
    left_info = check_full(head.left)
    right_info = check_full(head.right)
    hight = max(left_info['hight'], right_info['hight']) + 1
    is_full = left_info['is_full'] and right_info['is_full'] and left_info['hight'] == right_info['hight']
    return {'is_full': is_full, "hight": hight}


# for test
def generate_random_BST(max_level, max_value):
    return generate(1, max_level, max_value)


def generate(level, max_level, max_value):
    if level > max_level or random.randint(0, 1):
        return None
    head = Node(random.randint(1, max_value))
    head.left = generate(level + 1, max_level, max_value)
    head.right = generate(level + 1, max_level, max_value)
    return head


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
    maxLevel = 5
    maxValue = 100
    testTimes = 1000000
    print("test begin !!!")
    for _ in range(testTimes):
        head = generate_random_BST(maxLevel, maxValue)
        dis1 = is_full1(head)
        dis2 = is_full1(head)
        if dis1 != dis2:
            print(dis1, dis2)
            print_tree(head)
            print("test break because of error !!!")
            break
    print("test end !!!")

