# -*- coding: utf-8 –*-

"""
拓扑排序
"""

from collections import deque


def topology_sort(graph):
    """
    :param graph: 无环有向图, 图的结构在 graph.py
    :return:
    """
    in_map = {}                 # key: 某个节点, value: 剩余入度
    zero_in_queue = deque()     # 只有入度为0的点, 才能进入这个队列(双端队列, 也可用列表代替)
    for node in graph.nodes:
        in_map[node] = node.in_num
        if not node.in_num:
            zero_in_queue.append(node)
    result = []
    while zero_in_queue:
        cur = zero_in_queue.popleft()
        result.append(cur)
        for node in cur.nexts:
            in_map[node] -= 1
            # 如果入度为0, 加入队列中
            if not in_map[node]:
                zero_in_queue.append(node)
    return result

