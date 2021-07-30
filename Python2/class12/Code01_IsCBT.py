# -*- coding: utf-8 –*-

"""
判断二叉树是否是完全二叉树

会在后面的题目中用二叉树的递归套路来解这个题
"""
import random


class Node(object):
    """ 二叉树基础节点
    """
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def isCBT1(head):
    if not head:
        return True
    leaf = False        # 是否遇到过左右两个孩子不双全的节点
    queue = [head]
    while queue:
        node = queue.pop(0)
        l = node.left
        r = node.right
        # 如果有右孩子但是没有子孩子 或者 如果遇到过左右两个孩子不双全的节点之后，又发现当前节点不是叶节点
        if (r and not l) or (leaf and (l or r)):
            return False
        if l:
            queue.append(l)
        if r:
            queue.append(r)

        # 遇到过左右两个孩子不双全的节点, leaf 标记为True
        if not l or not r:
            leaf = True
    return True


def isCBT2(head):
    if not head:
        return True
    return process(head)['isCBT']


def process(node):
    """
    :param node: 树的节点信息
    :return: {
                "is_full": True,        # 子树是否是满二叉树
                "isCBT": True,          # 子树是否是完全二叉树
                "height": 1,            # 子树高度
            }
    """
    if not node:
        return {"is_full": True, 'isCBT': True, "height": 0}
    left_info = process(node.left)
    right_info = process(node.right)

    height = max(left_info['height'], right_info['height']) + 1

    is_full = left_info['is_full'] and right_info['is_full'] and left_info['height'] == right_info['height']

    isCBT = False
    if is_full:
        isCBT = True
    else:
        if left_info['isCBT'] and right_info['isCBT']:
            if left_info['isCBT'] and right_info['is_full'] and left_info['height'] == right_info['height'] + 1:
                isCBT = True
            if left_info['is_full'] and right_info['isCBT'] and left_info['height'] == right_info['height']:
                isCBT = True
            if left_info['is_full'] and right_info['is_full'] and left_info['height'] == right_info['height'] + 1:
                isCBT = True
    return {"is_full": is_full, 'isCBT': isCBT, "height": height}


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
        cbt1 = isCBT1(head)
        cbt2 = isCBT2(head)
        if cbt1 != cbt2:
            print(cbt1, cbt2)
            print("test break because of error !!!")
            break
    print("test end !!!")

