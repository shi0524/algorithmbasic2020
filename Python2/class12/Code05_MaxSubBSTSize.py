# -*- coding: utf-8 –*-

"""
给定一棵二叉树的头节点head，
返回这颗二叉树中最大的二叉搜索子树的大小
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


def getBSTSize(head):
    """ 获取搜索二叉树的大小
    """
    if not head:
        return 0
    nodes = []
    in_order(head, nodes)
    size = len(nodes)
    for i in range(1, size):
        if nodes[i] <= nodes[i - 1]:
            return 0
    return size


def in_order(head, nodes):
    if head.left:
        in_order(head.left, nodes)
    nodes.append(head.val)
    if head.right:
        in_order(head.right, nodes)


def maxSubBSTSize1(head):
    if not head:
        return 0
    size = getBSTSize(head)
    if size:
        return size
    return max(maxSubBSTSize1(head.left), maxSubBSTSize1(head.right))


def maxSubBSTSize2(head):
    if not head:
        return 0
    info = calc_size(head)
    return info['max_size']


def calc_size(head):
    if not head:
        return None
    left_info = calc_size(head.left)
    right_info = calc_size(head.right)
    max_val = head.val
    min_val = head.val
    if left_info:
        max_val = max(max_val, left_info['max_val'])
        min_val = min(min_val, left_info['min_val'])
    if right_info:
        max_val = max(max_val, right_info['max_val'])
        min_val = min(min_val, right_info['min_val'])

    is_BST = True
    if left_info and not left_info['isBST']:
        is_BST = False
    if right_info and not right_info['isBST']:
        is_BST = False
    if left_info and left_info['max_val'] >= head.val:
        is_BST = False
    if right_info and right_info['min_val'] <= head.val:
        is_BST = False
    if is_BST:
        max_size = 1
        if left_info:
            max_size += left_info['max_size']
        if right_info:
            max_size += right_info['max_size']
    else:
        max_size = 0
        if left_info:
            max_size = max(max_size, left_info['max_size'])
        if right_info:
            max_size = max(max_size, right_info['max_size'])

    return {'isBST': is_BST, 'max_val': max_val, 'min_val': min_val, 'max_size': max_size}


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
        cbt1 = maxSubBSTSize1(head)
        cbt2 = maxSubBSTSize2(head)
        if cbt1 != cbt2:
            print(cbt1, cbt2)
            print_tree(head)
            print("test break because of error !!!")
            break
    print("test end !!!")

