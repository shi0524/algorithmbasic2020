# -*- coding: utf-8 –*-

"""
最小生成树算法之Kruskal
1）总是从权值最小的边开始考虑，依次考察权值依次变大的边
2）当前的边要么进入最小生成树的集合，要么丢弃
3）如果当前的边进入最小生成树的集合中不会形成环，就要当前边
4）如果当前的边进入最小生成树的集合中会形成环，就不要当前边
5）考察完所有边之后，最小生成树的集合也得到了
"""


class UnionFind(object):

    def __init__(self):
        self.parents = {}
        self.sizes = {}

    def make_sets(self, nodes):
        self.parents = {node: node for node in nodes}
        self.sizes = {node: 1 for node in nodes}

    def find(self, node):
        path = []
        while node != self.parents[node]:
            path.append(self.parents[node])
            node = self.parents[node]
        while path:
            self.parents[path.pop()] = node
        return node

    def is_same(self, nodeA, nodeB):
        return self.find(nodeA) == self.find(nodeB)

    def union(self, nodeA, nodeB):
        if not nodeA or not nodeB:
            return
        pA = self.find(nodeA)
        pB = self.find(nodeB)
        if pA != pB:
            sizeA = self.sizes[pA]
            sizeB = self.sizes[pB]
            if sizeA >= sizeB:
                self.parents[sizeA] += sizeB
                self.parents[sizeB] = sizeA
                self.sizes.pop(sizeB)
            else:
                self.parents[sizeB] += sizeA
                self.parents[sizeA] = sizeB
                self.sizes.pop(sizeA)


def kruskalMST(graph):
    uf = UnionFind()
    uf.make_sets(graph.nodes)
    sorted_edges = sorted(graph.edges, key=lambda x: x.weight)
    ans = []
    for edge in sorted_edges:
        if uf.is_same(edge.f_node, edge.t_node):
            continue
        ans.append(edge)
        uf.union(edge.f_node, edge.t_node)
    return ans

