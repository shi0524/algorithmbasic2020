# -*- coding: utf-8 –*-

"""
跳表
"""

import random


class SkipListNode(object):
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.next_nodes = []

    def is_key_less(self, other_key):
        # otherKey == None -> false
        return other_key is not None and (self.key is None or self.key < other_key)

    def is_key_equal(self, other_key):
        return self.key == other_key


class SkipListMap(object):

    PROBABILITY = 0.5   # < 0.5 继续做，>=0.5 停

    def __init__(self):
        self.head = SkipListNode(None, None)
        self.head.next_nodes.append(None)
        self.size = 0
        self.max_level = 0

    def _most_right_less_node_in_tree(self, key):
        if key is None:
            return None
        level = self.max_level
        cur = self.head
        while level >= 0:   # 从上一层往下跳
            cur = self._most_right_less_node_in_level(key, cur, level - 1)
            level -= 1

        return cur

    def _most_right_less_node_in_level(self, key, cur, level):
        """ 在level 层里, 如何往右移动
            现在来到的节点是cur, 来到了cur的level层, 在level层上, 找到 < key 的最后一个几点并返回
        """
        next= cur.next_nodes[level]
        while next and next.is_key_less(key):
            cur = next
            next = cur.next_nodes[level]
        return cur

    def contains_key(self, key):
        if key is None:
            return False
        less = self._most_right_less_node_in_tree(key)
        next = less.next_nodes[0]
        return next is not None and next.is_key_equal(key)

    def put(self, key, value):
        if key is None:
            return
        less = self._most_right_less_node_in_tree(key)
        find = less.next_nodes[0]
        # 存在 覆盖
        if find is not None and find.is_key_equal(key):
            find.val = value
        # 不存在, 新加节点
        else:
            self.size += 1
            head = self.head
            max_level = self.max_level
            new_node_level = 0
            while random.random() < self.PROBABILITY:
                new_node_level += 1

            while new_node_level > max_level:
                head.next_nodes.append(None)
                max_level += 1
            self.max_level = max_level

            new_node = SkipListNode(key, value)
            new_node.next_nodes = [None] * (max_level + 1)
            level = max_level
            pre = self.head

            # while level >= 0:
            #     pre = self._most_right_less_node_in_level(key, pre, level)
            #     if level <= new_node_level:
            #         new_node.next_nodes[level] = pre.next_nodes[level]
            #         pre.next_nodes[level] = new_node
            #     level -= 1

            for lv in range(level, -1, -1):
                pre = self._most_right_less_node_in_level(key, pre, lv)
                if lv <= new_node_level:
                    new_node.next_nodes[lv] = pre.next_nodes[lv]
                    pre.next_nodes[lv] = new_node

    def get(self, key):
        if key is None:
            return None
        less = self._most_right_less_node_in_tree(key)
        next = less.next_nodes[0]
        return next.value if next is not None and next.is_key_equal(key) else None

    def remove(self, key):
        if self.contains_key(key):
            self.size -= 1
            level = self.max_level
            pre = self.head
            while level >= 0:
                pre = self._most_right_less_node_in_level(key, pre, level)
                next = pre.next_nodes[level]
                # 1) 在这一层中, pre 下一个就是key
                # 2) 在这一层中, pre 的下一个key是 > 要删除的key
                if next is not None and next.is_key_equal(key):
                    pre.next_nodes[level] = next.next_nodes[level]
                # 在 level 层总只有一个节点了, 就是默认的head
                if level != 0 and pre is self.head and pre.next_nodes[level] is None:
                    self.head.next_nodes.pop()
                    self.max_level -= 1
                level -= 1

    def first_key(self):
        first_node = self.head.next_nodes[0]
        return first_node.key if first_node else None

    def last_key(self):
        level = self.max_level
        cur = self.head
        for lv in range(level, -1, -1):
            next = cur.next_nodes[lv]
            while next:
                cur = next
                next = cur.next_nodes[lv]
        return cur.key

    def ceiling_key(self, key):
        if key is None:
            return None
        less = self._most_right_less_node_in_tree(key)
        next = less.next_nodes[0]
        return next.key if next else None

    def floor_key(self, key):
        if key is None:
            return None
        less = self._most_right_less_node_in_tree(key)
        next = less.next_nodes[0]
        return next.key if next and next.is_key_equal(key) else less.key


""" for test """


def print_all(skip):
    for lv in range(skip.max_level, -1, -1):
        print("level {}:".format(lv)),
        cur = skip.head
        while cur.next_nodes[lv]:
            next = cur.next_nodes[lv]
            print((next.key, next.value)),
            cur = next
        print("")


""" for test """


if __name__ == "__main__":
    skip = SkipListMap()
    print_all(skip)
    print("*" * 50)

    skip.put('A', 10)
    print_all(skip)
    print("*" * 50)

    skip.remove('A')
    print_all(skip)
    print("*" * 50)

    skip.put('E', 'E')
    skip.put('B', 'B')
    skip.put('A', 'A')
    skip.put('F', 'F')
    skip.put('C', 'C')
    skip.put('W', 'W')
    skip.put('H', 'H')
    print_all(skip)
    print("*" * 50)

    print(skip.contains_key('B'))
    print(skip.contains_key('Y'))
    print(skip.first_key())
    print(skip.last_key())

    print(skip.floor_key('I'))
    print(skip.ceiling_key('C'))

