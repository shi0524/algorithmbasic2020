# -*- coding: utf-8 –*-

"""
Dijkstra算法

1）Dijkstra算法必须指定一个源点
2）生成一个源点到各个点的最小距离表，一开始只有一条记录，即原点到自己的最小距离为0，源点到其他所有点的最小距离都为正无穷大
3）从距离表中拿出没拿过记录里的最小记录，通过这个点发出的边，更新源点到各个点的最小距离表，不断重复这一步
4）源点到所有的点记录如果都被拿过一遍，过程停止，最小距离表得到了
"""


def dijkstra1(start):
    distance = {start: 0}
    selected = set()
    min_node = get_min_distance_and_unselected_node(distance, selected)
    while min_node:
        dis = distance[min_node]
        for edge in min_node.edges:
            t_node = edge.t_node
            if t_node not in distance:
                distance[t_node] = dis + edge.weight
            else:
                distance[t_node] = min(distance[t_node], dis + edge.weight)
        selected.add(min_node)
        min_node = get_min_distance_and_unselected_node(distance, selected)
    return distance


def get_min_distance_and_unselected_node(distance, selected):
    min_node = None
    min_dis = float('inf')
    for node, dis in distance.items():
        if node not in selected and dis < min_dis:
            min_dis = dis
            min_node = node
    return min_node
