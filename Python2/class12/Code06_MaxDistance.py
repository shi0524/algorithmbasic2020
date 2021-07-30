# -*- coding: utf-8 –*-

"""
1）假设以X节点为头，假设可以向X左树和X右树要任何信息
2）在上一步的假设下，讨论以X为头节点的树，得到答案的可能性（最重要）
3）列出所有可能性后，确定到底需要向左树和右树要什么样的信息
4）把左树信息和右树信息求全集，就是任何一棵子树都需要返回的信息S
5）递归函数都返回S，每一棵子树都这么要求
6）写代码，在代码中考虑如何把左树的信息和右树信息整合出整棵树的信息
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


# 暴力方法
def max_distance1(head):
    """ 暴力方法
        获取到所有节点列表
        获取到所有节点父节点映射
        算出每个节点之间的距离
        取最大距离
    """
    if not head:
        return 0
    nodes = []
    parents = {}
    get_pre_list(head, nodes)
    get_parent_map(head, parents)
    max_dis = 1
    for i in range(0, len(nodes)):
        for j in range(i, len(nodes)):
            distance = two_node_distance(nodes[i], nodes[j], parents)
            max_dis = max(max_dis, distance)
    return max_dis


def get_pre_list(head, nodes):
    if not head:
        return
    pre_order(head, nodes)


def pre_order(head, nodes):
    if not head:
        return
    nodes.append(head)
    pre_order(head.left, nodes)
    pre_order(head.right, nodes)


def get_parent_map(head, parents):
    if not head:
        return
    calc_parent(head, parents)


def calc_parent(head, parents):
    if head.left:
        parents[head.left] = head
        calc_parent(head.left, parents)
    if head.right:
        parents[head.right] = head
        calc_parent(head.right, parents)


def two_node_distance(node1, node2, parents):
    """ 深度优先，计算二叉树两个节点之间的距离
    :param node1: 起始节点
    :param node2: 终止节点
    :param parents: 子节点与父节点的映射关系
    :return:
    """
    if node1 == node2:
        return 1
    visited = {node1}
    path = [[node1, 1]]
    while path:
        node, dis = path.pop()
        if node.left and node.left not in visited:
            if node.left == node2:
                return dis + 1
            visited.add(node.left)
            path.append([node.left, dis + 1])
        if node.right and node.right not in visited:
            if node.right == node2:
                return dis + 1
            visited.add(node.right)
            path.append([node.right, dis + 1])
        parent = parents.get(node)
        if parent and parent not in visited:
            if parent == node2:
                return dis + 1
            visited.add(parent)
            path.append([parent, dis + 1])
    return 0




"""
两种大情况：
    过 X 节点
        X左树离X最远距离 + 1 + X右树离X最远距离
    不过 X 节点：
        X 左树的最大距离
        X 右树的最大距离
"""


def max_distance2(head):
    if not head:
        return 0
    info = distance(head)
    return info['distance']


def distance(node):
    if not node:
        return {'distance': 0, 'hight': 0}
    left_info = distance(node.left)
    right_info = distance(node.right)
    height = max(left_info['hight'], right_info['hight']) + 1
    max_dis = max(left_info['distance'], right_info['distance'], left_info['hight'] + right_info['hight'] + 1)
    return {'distance': max_dis, 'hight': height}


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
        dis1 = max_distance1(head)
        dis2 = max_distance2(head)
        if dis1 != dis2:
            print(dis1, dis2)
            print_tree(head)
            print("test break because of error !!!")
            break
    print("test end !!!")