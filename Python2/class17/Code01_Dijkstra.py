# -*- coding: utf-8 –*-


"""
Dijkstra算法

1）Dijkstra算法必须指定一个源点
2）生成一个源点到各个点的最小距离表，一开始只有一条记录，即原点到自己的最小距离为0，源点到其他所有点的最小距离都为正无穷大
3）从距离表中拿出没拿过记录里的最小记录，通过这个点发出的边，更新源点到各个点的最小距离表，不断重复这一步
4）源点到所有的点记录如果都被拿过一遍，过程停止，最小距离表得到了
"""
import random

from graph import createGraph


def dijkstra1(start):
    distance = {start: 0}   # start 到各个点的距离表
    selected = set()        # 已经被选过的点
    min_node = get_min_distance_and_unselected_node(distance, selected)
    while min_node:
        dis = distance[min_node]
        for edge in min_node.edges:                     # 遍历所有的边
            t_node = edge.t_node                        # 根据边, 找到点
            if t_node not in distance:                  # 如果不在距离表中, 加入
                distance[t_node] = dis + edge.weight
            else:                                       # 如果在, 看能不能更新
                distance[t_node] = min(distance[t_node], dis + edge.weight)
        selected.add(min_node)                          # 将改点加入到已被选择的带你中
        min_node = get_min_distance_and_unselected_node(distance, selected)
    return distance


def get_min_distance_and_unselected_node(distance, selected):
    """ 从未被选过的点中，选择一个距离最小的点
    :param distance: 现有的距离表
    :param selected: 已经被选过的点
    :return:
    """
    min_node = None
    min_dis = float('inf')
    for node, dis in distance.items():
        if node not in selected and dis < min_dis:
            min_dis = dis
            min_node = node
    return min_node


class NodeHeap(object):
    """ Dijkstra 辅助加强堆
    """
    def __init__(self, size):
        self.size = 0
        self.distance = {}
        self.index_map = {}
        self.nodes = [None] * size

    def isEmpty(self):
        return self.size == 0

    def addOrUpdateOrIgnore(self, node, dis):
        """
        :param node: 节点
        :param dis: 距离
        :return:
        """
        # 如果node在堆中, 尝试更新
        if self.in_heap(node):
            self.distance[node] = min(self.distance[node], dis)
            self.heap_insert(self.index_map[node])
        # 如果node从未加入过, 新节点加入
        elif not self.is_entered(node):
            self.distance[node] = dis
            self.nodes[self.size] = node
            self.index_map[node] = self.size
            self.heap_insert(self.size)
            self.size += 1
        # 如果曾经加入过, 不做任何操作
        # else:
        #     pass

    def pop(self):
        """ 弹出元素
        """
        node = self.nodes[0]
        self.size -= 1
        self.swap(0, self.size)
        self.index_map[node] = -1         # 将node索引置为-1, 代表加入过堆, 然后已经被弹出
        dis = self.distance.pop(node)
        # 将node移除
        self.nodes[self.size] = None
        self.heapify(0, self.size)
        return node, dis

    def heap_insert(self, index):
        """ 从索引位置向堆顶浮
        """
        nodes = self.nodes
        distance = self.distance
        while index and distance[nodes[index]] < distance[nodes[(index - 1) // 2]]:
            self.swap(index, (index - 1) // 2)
            index = (index - 1) // 2

    def heapify(self, index, size):
        """ 从索引位置向下沉
        """
        nodes = self.nodes
        distance = self.distance
        left = index * 2 + 1
        while left < size:
            smaller = left + 1 if left + 1 < size and distance[nodes[left + 1]] < distance[nodes[left]] else left
            smaller = smaller if distance[nodes[smaller]] < distance[nodes[index]] else index
            if smaller == index:
                return
            self.swap(smaller, index)
            index = smaller
            left = index * 2 + 1

    def is_entered(self, node):
        """ 该点是否加入过
        """
        return node in self.index_map

    def in_heap(self, node):
        """ 该点当前是否在堆中
        """
        return self.is_entered(node) and self.index_map[node] != -1

    def swap(self, index1, index2):
        """ 交换两点位置, 及 index_map 对应关系
        """
        self.index_map[self.nodes[index1]] = index2
        self.index_map[self.nodes[index2]] = index1
        self.nodes[index1], self.nodes[index2] = self.nodes[index2], self.nodes[index1]


def dijkstra2(start, size):
    """ dijkstra 改进版(加强堆实现)
    """
    nodeheap = NodeHeap(size)
    nodeheap.addOrUpdateOrIgnore(start, 0)
    result = {}
    while not nodeheap.isEmpty():
        min_node, dis = nodeheap.pop()
        for edge in min_node.edges:
            nodeheap.addOrUpdateOrIgnore(edge.t_node, edge.weight + dis)
        result[min_node] = dis
    return result


if __name__ == "__main__":
    matrix = [[1, 0, 1], [3, 0, 2], [5, 0, 3], [1, 1, 2], [2, 2, 3], [1, 2, 4], [1, 3, 4]]
    graph = createGraph(matrix)
    start = random.choice(graph.nodes.values())
    result1 = dijkstra1(start)
    result2 = dijkstra2(start, 4)
    print("Start: {}".format(start))
    print(result1)
    print(result2)
    print(result1 == result2)

