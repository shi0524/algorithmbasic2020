# -*- coding: utf-8 –*-

class Node(object):
    def __init__(self, value):
        self.value = value      # 点的值
        self.in_num = 0         # 本节点的入度(有多少个边是指向本节点的)
        self.out_num = 0        # 本节点的出度(有多少个边由本节点指向其他节点)
        self.nexts = []         # 有哪些直接邻居(从本节点出发, 能找到的点)
        self.edges = []         # 从本节点出发, 有哪些边

    def __repr__(self):
        return "Node({})".format(self.value)


class Edge(object):
    def __init__(self, _from, to, weight):
        self.f_node = _from     # 起点
        self.t_node = to        # 终点
        self.weight = weight    # 边的权重


class Graph(object):
    def __init__(self):
        self.nodes = {}         # 图的点集
        self.edges = set()      # 图的边集


def createGraph(matrix):
    """
    matrix 所有的边
    N * 3 的矩阵
    [weight, from节点上面的值, to节点上面的值]
    [5, 0, 7],
    [3, 0, 1],
    """
    graph = Graph()
    for w, f, t in matrix:
        if f not in graph.nodes:
            graph.nodes[f] = Node(f)
        if t not in graph.nodes:
            graph.nodes[t] = Node(t)
        # from 点
        f_node = graph.nodes[f]
        # to 点
        t_node = graph.nodes[t]
        # 根据 from to weight 生成一条边
        new_edge = Edge(f_node, t_node, weight=w)

        # 从from出发的直接邻居包含to, 将to加到from的直接邻居里去
        f_node.nexts.append(t_node)
        # from 的出度 +1, to 的入度+1
        f_node.out_num += 1
        t_node.in_num += 1
        # 新边从from出发, 将新边加入到from的边集中
        f_node.edges.append(new_edge)
        # 将新边加入到图的边集中
        graph.edges.add(new_edge)
    return graph

