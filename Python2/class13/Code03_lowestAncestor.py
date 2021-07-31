# -*- coding: utf-8 –*-

"""
二叉树递归套路
给定一棵二叉树的头节点head，和另外两个节点a和b。
返回a和b的最低公共祖先
"""

import random


class Node(object):
    """ 二叉树基础节点
    """
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def lowestAncestor1(head, nodeA, nodeB):
    if not head:
        return None
    parents = {}
    nodes = [head]
    while nodes:
        node = nodes.pop()
        if node.left:
            parents[node.left] = node
            nodes.append(node.left)
        if node.right:
            parents[node.right] = node
            nodes.append(node.right)
    parentA = {nodeA}
    pa = parents.get(nodeA)
    while pa:
        parentA.add(pa)
        pa = parents.get(pa)
    pb = nodeB
    while pb:
        if pb in parentA:
            return pb
        pb = parents.get(pb)
    return None


def lowestAncestor2(head, nodeA, nodeB):
    if not head:
        return None
    info = process(head, nodeA, nodeB)
    return info['ans']


def process(node, nodeA, nodeB):
    if not node:
        return {'ans': None, 'findA': False, 'findB': False}
    left_info = process(node.left, nodeA, nodeB)
    right_info = process(node.right, nodeA, nodeB)
    if left_info['ans']:
        return left_info
    if right_info['ans']:
        return right_info
    findA = left_info['findA'] or right_info['findA'] or node == nodeA
    findB = left_info['findB'] or right_info['findB'] or node == nodeB
    ans = node if findA and findB else None
    return {'ans': ans, 'findA': findA, 'findB': findB}


def get_all_nodes(head):
    nodes = []
    in_order(head, nodes)
    return nodes


def in_order(head, nodes):
    if not head:
        return
    in_order(head.left, nodes)
    nodes.append(head.val)
    in_order(head.right, nodes)


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


if __name__ == "__main__":
    maxLevel = 5
    maxValue = 100
    testTimes = 1000000
    print("test begin !!!")
    for _ in range(testTimes):
        head = generate_random_BST(maxLevel, maxValue)
        nodes = set(get_all_nodes(head))
        nodeA = nodes.pop() if nodes else None
        nodeB = nodes.pop() if nodes else None

        ans1 = lowestAncestor1(head, nodeA, nodeB)
        ans2 = lowestAncestor2(head, nodeA, nodeB)
        if ans1 != ans2:
            print(ans1, ans2)
            print("test break because of error !!!")
            break
    print("test end !!!")