# -*- coding: utf-8 –*-

"""
SB树（size-balance-tree）
  1）让每一个叔叔节点为头的数，节点个数都不少于其任何一个侄子节点
  2）也是从底层被影响节点开始向上做路径每个节点检查
  3）与AVL树非常像，也是四种违规类型:(当前节点不违规, 查子节点是否违规)
    LL: 当前节点左儿子的左子树的节点个数大于当前节点的右儿子
    RR: 当前节点右儿子的右子树的节点个数大于当前节点的左儿子
    LR: 当前节点左儿子的右子树的节点个数大于当前节点的右儿子
    RL: 当前节点右儿子的左子树的节点个数大于当前节点的左儿子
  4）与AVL树非常像，核心点是：
    LL（做一次右旋）、RR（做一次左旋）
    LR和RL（利用旋转让底层那个上到顶部）
  5）与AVL树不同的是，每轮经过调整后，谁的孩子发生变化了，谁就再查
"""

class SBTNode(object):
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.size = 1
        self.l = None
        self.r = None


class SizeBalancedTreeMap():
    def __init__(self):
        self.root = None

    def _right_rotate(self, cur):
        """ 右旋
        """
        left_node = cur.l
        cur.l = left_node.r
        left_node.r = cur
        left_node.size = cur.size
        cur.size = (cur.l.size if cur.l else 0) + (cur.r.size if cur.r else 0) + 1
        return left_node

    def _left_rotate(self, cur):
        """ 左旋
        """
        right_node = cur.r
        cur.r = right_node.l
        right_node.l = cur
        right_node.size = cur.size
        cur.size = (cur.l.size if cur.l else 0) + (cur.r.size if cur.r else 0) + 1
        return right_node

    def _maintain(self, cur):
        if cur is None:
            return None
        left_size = cur.l.size if cur.l else 0
        left_left_size = cur.l.l.size if cur.l and cur.l.l else 0
        left_right_size = cur.l.r.size if cur.l and cur.l.r else 0

        right_size = cur.r.size if cur.r else 0
        right_left_size = cur.r.l.size if cur.r and cur.r.l else 0
        right_right_size = cur.r.r.size if cur.r and cur.r.r else 0

        if left_left_size > right_size:
            cur = self._left_rotate(cur)
            cur.r = self._maintain(cur.r)
            cur = self._maintain(cur)
        elif left_right_size > right_size:
            cur.l = self._left_rotate(cur.l)
            cur = self._right_rotate(cur)
            cur.l = self._maintain(cur.l)
            cur.r = self._maintain(cur.r)
            cur = self._maintain(cur)
        elif right_right_size > left_size:
            cur = self._left_rotate(cur)
            cur.l = self._maintain(cur.l)
            cur = self._maintain(cur)
        elif right_left_size > left_size:
            cur.r = self._right_rotate(cur.r)
            cur = self._left_rotate(cur)
            cur.l = self._maintain(cur.l)
            cur.r = self._maintain(cur.r)
            cur = self._maintain(cur)

        return cur

    def _finde_last_index(self, key):
        pre = self.root
        cur = self.root
        while cur:
            pre = cur
            if cur.k == key:
                break
            elif key < cur.k:
                cur = cur.l
            else:
                cur = cur.r
        return pre

    def _find_last_no_small_index(self, key):
        ans = None
        cur = self.root
        while cur:
            if key == cur.k:
                ans = cur
                break
            elif key < cur.k:
                ans = cur
                cur = cur.l
            else:
                cur = cur.r
        return ans

    def _find_last_no_big_index(self, key):
        ans = None
        cur = self.root
        while cur:
            if key == cur.k:
                ans = cur
                break
            elif key < cur.k:
                cur = cur.l
            else:
                ans = cur
                cur = cur.r
        return ans

    def _add(self, cur, key, value):
        if cur is None:
            return SBTNode(key, value)
        else:
            cur.size += 1
            if key < cur.k:
                cur.l = self._add(cur.l, key, value)
            else:
                cur.r = self._add(cur.r, key, value)
            return self._maintain(cur)

    def _delete(self, cur, key):
        cur.size -= 1
        if key < cur.k:
            cur.l = self._delete(cur.l, key)
        elif key > cur.k:
            cur.r = self._delete(cur.r, key)
        else:
            if cur.l is None and cur.r is None:
                cur = None
            elif cur.l == None and cur.r:
                cur = cur.r
            elif cur.l and cur.r is None:
                cur = cur.l
            else:
                pre = None
                des = cur.r
                des.size -= 1
                while des.l:
                    pre = des
                    des = des.l
                    des.size -= 1
                if pre is not None:
                    pre.l = des.r
                    des.r = cur.r
                des.l = cur.l
                des.size = des.l.size + (des.r.size if des.r else 0) + 1
                cur = des
        # cur = self._maintain(cur)
        return cur

    def _get_index(self, cur, kth):
        """ 获取第K小
        """
        if kth == (cur.l.size if cur.l else 0) + 1:
            return cur
        elif kth <= (cur.l.size if cur.l else 0):
            return self._get_index(cur.l, kth)
        else:
            return self._get_index(cur.r, kth - (cur.l.size if cur.l else 0) - 1)

    def size(self):
        return self.root.size if self.root else 0

    def contains_key(self, key):
        if key is None:
            raise RuntimeError("invalid parameter.")
        lastNode = self._finde_last_index(key)
        return True if lastNode != None and lastNode.k == key else False

    def put(self, key, value):
        if key is None:
            raise RuntimeError("invalid parameter.")
        last_node = self._finde_last_index(key)
        if last_node and key == last_node.k:
            last_node.v = value
        else:
            self.root = self._add(self.root, key, value)

    def remove(self, key):
        if key is None:
            raise RuntimeError("invalid parameter.")
        if self.contains_key(key):
            self.root = self._delete(self.root, key)

    def get_index_key(self, index):
        if index < 0 or index >= self.root.size:
            raise RuntimeError("invalid parameter.")
        return self._get_index(self.root, index + 1).k

    def get_index_value(self, index):
        if index < 0 or index >= self.root.size:
            raise RuntimeError("invalid parameter.")
        return self._get_index(self.root, index + 1).v

    def get(self, key):
        if key is None:
            raise RuntimeError("invalid parameter.")
        last_node = self._finde_last_index(key)
        if last_node and last_node.k == key:
            return last_node
        return None

    def first_key(self):
        if self.root is None:
            return None
        cur = self.root
        while cur.l:
            cur = cur.l
        return cur.key

    def last_key(self):
        if self.root is None:
            return None
        cur = self.root
        while cur.r:
            cur = cur.r
        return cur.key

    def floor_key(self, key):
        if key is None:
            raise RuntimeError("invalid parameter.")
        last_no_big_node = self._find_last_no_big_index(key)
        return last_no_big_node.k if last_no_big_node else None

    def ceiling_key(self, key):
        if key is None:
            raise RuntimeError("invalid parameter.")
        last_no_small_node = self._find_last_no_small_index(key)
        return last_no_small_node.k if last_no_small_node else None


""" for test """


def print_tree(head):
    print("Binary Tree:")
    printInOrder(head, 0, "H", 17)
    print("")


def printInOrder(head, height, to, length):
    if not head:
        return
    printInOrder(head.r, height + 1, "v", length)
    val = to + str(head.v) + to
    lenM = len(val)
    lenL = (length - lenM)
    lenR = (length - lenM - lenL)
    val = get_space(lenL) + val + get_space(lenR)
    print(get_space(height * length) + val)
    printInOrder(head.l, height + 1, "^", length)


def get_space(length):
    return " " * length


""" for test """


if __name__ == "__main__":

    head = SizeBalancedTreeMap()
    head.put(1, 1)
    head.put(2, 2)
    head.put(3, 3)
    head.put(4, 4)
    head.put(5, 5)
    head.put(6, 6)
    head.put(7, 7)
    head.put(8, 8)
    head.put(9, 9)
    head.put(10, 10)
    print_tree(head.root)
    head.remove(5)
    print_tree(head.root)

    print(head.floor_key(0.1), head.floor_key(1.1))


