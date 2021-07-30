# -*- coding: utf-8 –*-

"""
二叉树的递归套路
判断二叉树是否是搜索二叉树
"""
import random


class Node(object):
    """ 二叉树基础节点
    """

    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def isBST1(head):
    """ 判断是否是搜索二叉树
        先中序遍历，获取所有值到一个列表
        然后查看列表值是否是升序
    """
    if not head:
        return True
    all_value = []
    in_order(head, all_value)
    for i in range(1, len(all_value)):
        if all_value[i] <= all_value[i - 1]:
            return False
    return True


def in_order(head, all_value):
    if not head:
        return
    in_order(head.left, all_value)
    all_value.append(head.val)
    in_order(head.right, all_value)


def isBST2(head):
    if not head:
        return True
    info = pos_order(head)
    return info['isBST']


def pos_order(head):
    """
    :param head: 二叉树节点
    :return: {
                "isBST": True,      # 是否是二叉搜索树
                "min_value": 10,    # 最大值
                "max_value": 100,   # 最小值
                }
    """
    if not head:
        return None
    left_info = pos_order(head.left)
    right_info = pos_order(head.right)
    min_value = head.val
    max_value = head.val

    if left_info:
        min_value = min(min_value, left_info['min_value'])
        max_value = max(max_value, left_info['max_value'])
    if right_info:
        min_value = min(min_value, right_info['min_value'])
        max_value = max(max_value, right_info['max_value'])

    isBST = True
    if left_info and not left_info['isBST']:
        isBST = False
    if right_info and not right_info['isBST']:
        isBST = False
    if left_info and left_info['max_value'] >= head.val:
        isBST = False
    if right_info and right_info['min_value'] <= head.val:
        isBST = False
    return {'isBST': isBST, 'min_value': min_value, 'max_value': max_value}


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
        cbt1 = isBST1(head)
        cbt2 = isBST2(head)
        if cbt1 != cbt2:
            print(cbt1, cbt2)
            print_tree(head)
            print("test break because of error !!!")
            break
    print("test end !!!")
