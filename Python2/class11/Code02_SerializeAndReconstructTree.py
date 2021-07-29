# -*- coding: utf-8 –*-


"""
    /*
     * 二叉树可以通过先序、后序或者按层遍历的方式序列化和反序列化，
     * 以下代码全部实现了。
     * 但是，二叉树无法通过中序遍历的方式实现序列化和反序列化
     * 因为不同的两棵树，可能得到同样的中序序列，即便补了空位置也可能一样。
     * 比如如下两棵树
     *         __2
     *        /
     *       1
     *       和
     *       1__
     *          \
     *           2
     * 补足空位置的中序遍历结果都是{ null, 1, null, 2, null}
     *
     * */
"""


class Node(object):
    """ 二叉树基础节点
    """
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def pre_serial(head):
    """ 先序序列化
    """
    queue = []
    pres(head, queue)
    return queue


def pres(head, queue):
    if head:
        queue.append(str(head.val))
        pres(head.left, queue)
        pres(head.right, queue)
    else:
        queue.append(None)


def buildByPreQueue(pre_queue):
    if not pre_queue:
        return None
    return pre_build(pre_queue)


def pre_build(pre_queue):
    val = pre_queue.pop(0)
    if val is None:
        return None
    head = Node(int(val))
    head.left = pre_build(pre_queue)
    head.right = pre_build(pre_queue)
    return head


def pos_serial(head):
    queue = []
    pos_s(head, queue)
    return queue


def pos_s(head, queue):
    if head:
        pos_s(head.left, queue)
        pos_s(head.right, queue)
        queue.append(str(head.val))
    else:
        queue.append(None)


def buildByPosQueue(pos_queue):
    if not pos_queue:
        return None
    # pos_queue 存入的是 左 右 头
    # 将 队列 倒入 栈中反序 （因为 pos_queue 为 列表模拟, 故无需转换）
    # 从 栈中倒出顺序为 头、右、左
    return pos_build(pos_queue)


def pos_build(stack):
    val = stack.pop()
    if val:
        head = Node(int(val))
        head.right = pos_build(stack)
        head.left = pos_build(stack)
        return head
    else:
        return None


def level_serial(head):
    ans = []
    if not head:
        ans.append(None)
        return ans
    ans.append(str(head.val))
    queue = [head]
    while queue:
        node = queue.pop(0)
        if node.left:
            ans.append(str(node.left.val))
            queue.append(node.left)
        else:
            ans.append(None)
        if node.right:
            ans.append(str(node.right.val))
            queue.append(node.right)
        else:
            ans.append(None)
    return ans


def buildByLevelQueue(level_queue):
    if not level_queue:
        return None
    head = generateNode(level_queue.pop(0))
    queue = []
    if head:
        queue.append(head)
    while queue:
        node = queue.pop(0)
        node.left = generateNode(level_queue.pop(0))
        node.right = generateNode(level_queue.pop(0))
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return head


def generateNode(val):
    if not val:
        return None
    return Node(int(val))




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

    pre_queue = pre_serial(n1)
    print(pre_queue)
    nn_pre = buildByPreQueue(pre_queue)
    pre_queue = pre_serial(nn_pre)
    print(pre_queue)

    print("*" * 180)
    pos_queue = pos_serial(n1)
    print(pos_queue)
    nn_pos = buildByPosQueue(pos_queue)
    pos_queue = pos_serial(nn_pos)
    print(pos_queue)

    print("*" * 180)
    level_queue = level_serial(n1)
    print(level_queue)
    nn_level = buildByLevelQueue(level_queue)
    level_queue = level_serial(nn_level)
    print (level_queue)





