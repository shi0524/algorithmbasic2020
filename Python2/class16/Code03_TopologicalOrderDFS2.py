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
        # write your code here
        indegrees = {node: 0 for node in graph}
        for node in graph:
            for n in node.neighbors:
                indegrees[n] += 1
        return [node for node, _ in sorted(indegrees.iteritems())]

    def topSort2(self, graph):
        """ 傻缓存 统计最大调度
        """
        times_cache = {}
        for cur in graph:
            self.process(cur, times_cache)
        return [node for node, _ in sorted(times_cache.iteritems(), key=lambda x: -x[1])]

    def process(self, cur, times_cache):
        """
        当前来到cur点，请返回cur点所到之处，所有的点次！
        times_cache 缓存  key : 某一个点的点次，之前算过了, value : 点次是多少
        """
        if cur in times_cache:
            return times_cache[cur]
        times = 1
        for n in cur.neighbors:
            times += self.process(n, times_cache)
        times_cache[cur] = times
        return times


