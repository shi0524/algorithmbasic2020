# -*- coding: utf-8 –*-

"""
左旋 (cur的左指针接管 左孩子的右子树, 左孩子的右指针指向cur)
右旋

LL: 只做一次 右旋 (即LL 又LR 按 LL处理总对, 但有情况 按LR处理不对)
LR: 对左子树做一次左旋，对当前节点做一次右旋
RR: 只做一次 左旋
RL: 对右子树做一次右旋, 对当前节点做一次左旋
"""


class AVLNode(object):
    def __init__(self, k, v):
        self.k = k      # k 必须可比较
        self.v = v
        self.h = 1
        self.l = None
        self.r = None

    def __repr__(self):
        return " {}: {} ".format(self.k, self.v)


class AVLTreeMap(object):
    """ AVL 树
    """
    def __init__(self):
        self.root = None
        self._size = 0

    def _right_rotate(self, cur):
        """ 右旋
        """
        left = cur.l
        cur.l = left.r
        left.r = cur
        cur.h = max(cur.l.h if cur.l else 0, cur.r.h if cur.r else 0) + 1
        left.h = max(left.l.h if left.l else 0, left.r.h if left.r else 0) + 1
        return left

    def _left_rotate(self, cur):
        """ 左旋
        """
        right = cur.r
        cur.r = right.l
        right.l = cur
        cur.h = max(cur.l.h if cur.l else 0, cur.r.h if cur.r else 0) + 1
        right.h = max(right.l.h if right.l else 0, right.r.h if right.r else 0) + 1
        return right

    def _maintain(self, cur):
        """ 平衡树的高度
            判断LL、LR、RR、RL 四种类型
        """
        if cur is None:
            return None
        left_height = cur.l.h if cur.l else 0
        right_height = cur.r.h if cur.h else 0
        if abs(left_height - right_height) > 1:
            if left_height > right_height:
                left_left_height = cur.l.l.h if cur.l and cur.l.l else 0
                left_right_height = cur.l.r.h if cur.l and cur.l.r else 0
                # LL型 或者 LL型+LR型
                if left_left_height >= left_right_height:
                    cur = self._right_rotate(cur)
                # 单独 LR型
                else:
                    cur.l = self._left_rotate(cur.l)
                    cur = self._right_rotate(cur)
            else:
                right_left_height = cur.r.l.h if cur.r and cur.r.l else 0
                right_right_height = cur.r.r.h if cur.r and cur.r.r else 0
                # RR型 或者 RR型+RL型
                if right_right_height >= right_left_height:
                    cur = self._left_rotate(cur)
                # 单独的 RL型
                else:
                    cur.r = self._right_rotate(cur.r)
                    cur = self._left_rotate(cur)
        return cur

    def _find_last_index(self, key):
        """ 查找小于等于自己的key
        """
        pre = self.root
        cur = self.root
        while cur:
            pre = cur
            if key == cur.k:
                break
            elif key < cur.k:
                cur = cur.l
            else:
                cur = cur.r
        return pre

    def _find_last_no_small_index(self, key):
        """ 查找下一个不小于自己的key
        """
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
        """ 查找下一个不大于自己的key
        """
        ans = None
        cur = self.root
        while cur:
            if key == cur.k:
                ans = cur
                break
            elif key < cur.k:
                cur = cur.k
            else:
                ans = cur
                cur = cur.r
        return ans

    def _add(self, cur, key, value):
        """ 添加一个节点
        """
        if cur is None:
            return AVLNode(key, value)
        if key < cur.k:
            cur.l = self._add(cur.l, key, value)
        else:
            cur.r = self._add(cur.r, key, value)
        cur.h = max(cur.l.h if cur.l else 0, cur.r.h if cur.r else 0) + 1
        return self._maintain(cur)

    def _delete(self, cur, key):
        """ 在cur这棵树上, 删掉key所代表的节点
            返回cur这棵树的新头部
        """
        if key < cur.k:
            cur.l = self._delete(cur.l, key)
        elif key > cur.k:
            cur.r = self._delete(cur.r, key)
        else:
            # 左右孩子都没有
            if cur.l is None and cur.r is None:
                cur = None
            # 只有右孩子
            elif cur.l is None and cur.r:
                cur = cur.r
            # 只有左孩子
            elif cur.l and cur.r is None:
                cur = cur.l
            # 左右孩子都有, 拿右孩子的最左节点替换
            else:
                des = cur.r
                while des.l:
                    des = des.l
                cur.r = self._delete(cur.r, des.key)
                des.l = cur.l
                des.r = cur.r
                cur = des
        if cur:
            cur.h = max(cur.l.h if cur.l else 0, cur.r.h if cur.r else 0) + 1
        return self._maintain(cur)

    """ 公有方法 """
    def size(self):
        return self._size

    def contains_key(self, key):
        if key is None:
            return False
        last_node = self._find_last_index(key)
        return True if last_node and key == last_node.k else False

    def put(self, key, value):
        """ 添加 或 更新 一组 key, value 数据
        """
        if key is None:
            return
        last_node = self._find_last_index(key)
        if last_node and last_node.k == key:
            last_node.v = value
        else:
            self._size += 1
            self.root = self._add(self.root, key, value)

    def remove(self, key):
        if self.contains_key(key):
            self._size -= 1
            self.root = self._delete(self.root, key)

    def get(self, key):
        if key is None:
            return None
        last_node = self._find_last_index(key)
        if last_node and last_node.k == key:
            return last_node.v
        return None

    def first_key(self):
        if self.root is None:
            return None
        cur = self.root
        while cur.l:
            cur = cur.l
        return cur.k

    def last_key(self):
        if self.root is None:
            return None
        cur = self.root
        while cur.r:
            cur = cur.r
        return cur.k

    def floor_key(self, key):
        if key is None:
            return None
        last_no_big_node = self._find_last_no_big_index(key)
        return None if last_no_big_node else last_no_big_node.k

    def ceiling_key(self, key):
        if key is None:
            return None
        last_no_small_node = self._find_last_no_small_index(key)
        return None if last_no_small_node else last_no_small_node.k


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

    head = AVLTreeMap()
    head.put(1, 1)
    head.put(2, 2)
    head.put(3, 3)
    head.put(4, 4)
    head.put(5, 5)
    head.put(6, 6)
    head.put(7, 7)
    head.put(8, 8)
    print_tree(head.root)
    head.remove(5)
    print_tree(head.root)
