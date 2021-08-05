# -*- coding: utf-8 –*-


"""
最小生成树算法之Prim

1）可以从任意节点出发来寻找最小生成树
2）某个点加入到被选取的点中后，解锁这个点出发的所有新的边
3）在所有解锁的边中选最小的边，然后看看这个边会不会形成环
4）如果会，不要当前边，继续考察剩下解锁的边中最小的边，重复3）
5）如果不会，要当前边，将该边的指向点加入到被选取的点中，重复2）
6）当所有点都被选取，最小生成树就得到了
"""
import heapq


def primMST(graph):

    small_heap = []     # 解锁的边进小根堆
    node_set = set()    # 哪些点被解锁出来了
    result = set()      # 依次挑选的边放在result里面

    for node in graph.nodes:    # 随便挑了一个点
        # node 是开始点
        if node in node_set:
            continue
        node_set.add(node)
        for edge in node.edges:     # 由一个点，解锁所有相连的边
            heapq.heappush(small_heap, (edge.weight, edge))
        while small_heap:
            _, edge = heapq.heappop(small_heap)     # 弹出解锁的边中，最小的边
            t_node = edge.t_node                    # 可能的一个新的点
            if t_node in node_set:                  # 含有的时候 直接放弃
                continue
            node_set.add(t_node)                    # 不含有的时候，就是新的点
            result.add(edge)                        # 将新边加入result
            for edge in t_node.edges:               # 将 t_node 点 解锁的新边加入小根堆中
                heapq.heappush(small_heap, (edge.weight, edge))

    return result


def prim(graph):
    """
    保证graph是连通图
    graph[i][j]表示点i到点j的距离，如果是系统最大值代表无路
    返回值是最小连通图的路径之和
    """
    size = len(graph)
    distances = [0] * size
    visit = [0] * size
    visit[0] = 1
    for i in range(size):
        distances[i] = graph[0][i]
    sum_ = 0
    for i in range(1, size):
        min_path = -float('inf')
        min_index = -1
        for j in range(size):
            if not visit[j] and distances[j] < min_path:
                min_path = distances[j]
                min_index = j
        if min_index == -1:
            return sum_
        visit[min_index] = 1
        sum_ += min_path
        for j in range(size):
            if not visit[j] and distances[j] > graph[min_index][j]:
                distances[j] = graph[min_index][j]
    return sum_

