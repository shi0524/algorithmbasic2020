# -*- coding: utf-8 –*-

"""
深度优先

1、将头结点压入栈 stack 和 访问集合 visited 中, 加入时打印
2、如果栈不为空时, 从栈中弹出 节点 cur
3、遍历 cur的邻节点, 如果有节点 n 未被访问过, 将 cur 重新压入栈中
4、将 节点 n 压入栈 stack 和访问集合 visited 中, 加入时打印, break
"""


def dfs(node):
    if not node:
        return
    stack = []
    visited = set()
    stack.append(node)
    visited.add(node)
    print(node.val),
    while stack:
        cur = stack.pop()
        for n in cur.nexts:
            if n in visited:
                continue
            stack.append(cur)
            visited.add(n)
            stack.append(n)
            print(n.val),
            break


