# -*- coding: utf-8 –*-

class Node(object):
    def __init__(self):
        self.end = 0
        self.fail = None
        self.nexts = [None] * 26


class ACAutomation(object):
    def __init__(self):
        self.root = Node()

    def insert(self, s):
        cur = self.root
        for ch in s:
            path = ord(ch) - 97
            if not cur.nexts[path]:
                cur.nexts[path] = Node()
            cur = cur.nexts[path]
        cur.end += 1

    def build(self):
        from collections import deque
        queue = deque()
        root = self.root
        queue.append(root)
        while queue:
            cur = queue.popleft()
            for i in range(26):
                if cur.nexts[i]:
                    cur.nexts[i].fail = root
                    cfail = cur.fail
                    while cfail:
                        if cfail.nexts[i]:
                            cur.nexts[i].fail = cfail.nexts[i]
                            break
                        cfail = cfail.fail
                    queue.append(cur.nexts[i])

    def contain_num(self, content):
        root = self.root
        cur = root
        ans = 0
        for ch in content:
            path = ord(ch) - 97
            while cur.nexts[path] == None and cur != root:
                cur = cur.fail
            cur = cur.nexts[path] if cur.nexts[path] else root

            follow = cur
            while follow != root:
                if follow.end == -1:
                    break
                ans += follow.end
                follow.end = -1
                follow = follow.fail
        return ans


if __name__ == "__main__":
    ac = ACAutomation()
    ac.insert("dhe")
    ac.insert("he")
    ac.insert("c")
    ac.build()

    ans = ac.contain_num("asdofnjofmewa[porfigndheajdfnc")
    print(ans)


