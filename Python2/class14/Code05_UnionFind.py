# -*- coding: utf-8 –*-

"""
并查集
"""


class Node(object):
    def __init__(self, v):
        self.v = v


class UnionFind(object):
    def __init__(self, values):
        self.nodes = {}
        self.parents = {}
        self.size_map = {}
        for val in values:
            node = Node(val)
            self.nodes[val] = node
            self.parents[val] = node
            self.size_map[node] = 1

    def find_father(self, cur):
        path = []
        parents = self.parents
        while cur != parents.get(cur):
            path.append(cur)
            cur = parents.get(cur)
        while path:
            parents[path.pop()] = cur
        return cur

    def is_same_set(self, a, b):
        return self.find_father(self.nodes[a]) == self.find_father(self.nodes[b])

    def union(self, a, b):
        nodes = self.nodes
        ahead = self.find_father(nodes.get(a))
        bhead = self.find_father(nodes.get(b))
        if ahead != bhead:
            a_size = self.size_map[ahead]
            b_size = self.size_map[bhead]
            big = ahead if a_size >= b_size else bhead
            small = bhead if big == ahead else ahead
            self.parents[small] = big
            self.size_map[big] = a_size + b_size
            self.size_map.pop(small)

    def sets(self):
        return len(self.size_map)

