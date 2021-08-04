# -*- coding: utf-8 –*-


"""
给定一个有向图，图节点的拓扑排序定义如下:

对于图中的每一条有向边 A -> B , 在拓扑排序中A一定在B之前.
拓扑排序中的第一个节点可以是图中的任何一个没有其他节点指向它的节点.
针对给定的有向图找到任意一种拓扑排序的顺序.
链接：https://www.lintcode.com/problem/topological-sorting
"""


class DirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        """ 傻缓存最大深度
        """
        follow_cache = {}
        for cur in graph:
            self.process(cur, follow_cache)
        return [node for node, _ in sorted(follow_cache.iteritems(), key=lambda x: -x[1])]

    def process(self, cur, follow_cache):
        """
        当前来到cur点，请返回cur点所到之处，所有的点次！
        follow_cache 缓存  key : 某一个点的点次，之前算过了, value : 最大深度
        """
        if cur in follow_cache:
            return follow_cache[cur]
        follow = 0
        for n in cur.neighbors:
            follow = max(follow, self.process(n, follow_cache))
        follow += 1
        follow_cache[cur] = follow
        return follow


