# -*- coding: utf-8 –*-

"""
求二叉树最宽的层有多少个节点
"""

class Node(object):
    """ 二叉树基础节点
    """
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def maxWidthUseMap(head):
    """ 用 map 记录节点层数
    """
    if not head:
        return 0
    levelMap = {head: 1}
    cur_level = 1
    cur_level_nodes = 0
    max_width = 0
    queue = [head]
    while queue:
        cur =queue.pop(0)
        cur_node_level = levelMap[cur]
        if cur.left:
            queue.append(cur.left)
            levelMap[cur.left] = cur_node_level + 1
        if cur.right:
            queue.append(cur.right)
            levelMap[cur.right] = cur_node_level + 1
        if cur_node_level == cur_level:
            cur_level_nodes += 1
        else:
            max_width = max(max_width, cur_level_nodes)
            cur_level += 1
            cur_level_nodes = 1
    max_width = max(max_width, cur_level_nodes)
    return max_width


def maxWidthNoMap1(head):
    if not head:
        return 0
    cur_level = 0
    cur_level_nodes = 0
    max_width = 0
    queue = [[head, 1]]
    while queue:
        node, level = queue.pop(0)
        if level == cur_level:
            cur_level_nodes += 1
        else:
            max_width = max(max_width, cur_level_nodes)
            cur_level = level
            cur_level_nodes = 1
        if node.left:
            queue.append([node.left, level + 1])
        if node.right:
            queue.append([node.right, level + 1])
    max_width = max(max_width, cur_level_nodes)
    return max_width


def maxWidthNoMap2(head):
    if not head:
        return 0
    curEnd = head
    nextEnd = None
    max_width = 0
    cur_level_nodes = 0
    queue = [head]
    while queue:
        cur = queue.pop(0)
        if cur.left:
            queue.append(cur.left)
            nextEnd = cur.left
        if cur.right:
            queue.append(cur.right)
            nextEnd = cur.right
        cur_level_nodes += 1
        if cur == curEnd:
            max_width = max(max_width, cur_level_nodes)
            curEnd = nextEnd
            cur_level_nodes = 0
    return max_width

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

    print(maxWidthUseMap(n1))
    print(maxWidthNoMap1(n1))
    print(maxWidthNoMap2(n1))
