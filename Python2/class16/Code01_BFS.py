# -*- coding: utf-8 –*-

"""
宽度优先遍历
"""

from collections import deque


def bfs(start):
    if not start:
        return
    queue = deque()
    visited = set()
    visited.add(start)
    queue.append(start)
    while queue:
        node = queue.popleft()
        print(node.val),
        for n in node.nexts:
            if n in visited:
                continue
            visited.add(n)
            queue.append(n)


