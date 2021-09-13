# -*- coding: utf-8 –*-

"""
AC自动机
解决在一个大字符串中，找到多个候选字符串的问题

1）把所有匹配串生成一棵前缀树
2）前缀树节点增加fail指针
3）fail指针的含义：如果必须以当前字符结尾，当前形成的路径是str，剩下哪一个字符串的前缀和str的后缀，拥有最大的匹配长度。
  fail指针就指向那个字符串的最后一个字符所对应的节点。
"""


class Node(object):
    def __init__(self):
        self.end_use = False
        self.end = None
        self.fail = None
        self.nexts = [None] * 26   # 假设只有小写字母


class ACAutomation(object):
    """ AC自动机
    """
    def __init__(self):
        self.root = Node()

    def insert(self, s):
        cur = self.root
        for ch in s:
            index = ord(ch) - 97
            if not cur.nexts[index]:
                cur.nexts[index] = Node()
            cur = cur.nexts[index]
        cur.end = s

    def buid(self):
        from collections import deque
        root = self.root
        queue = deque()
        queue.append(root)
        while queue:
            # 某个父节点 cur
            cur = queue.popleft()
            for i in range(26):  # 所有的节点
                # cur -> 父节点  i号儿子, 必须把号儿子的fail指针设置好
                if cur.nexts[i]:
                    cur.nexts[i].fail = root
                    cfail = cur.fail
                    while cfail:
                        if cfail.nexts[i]:
                            cur.nexts[i].fail = cfail.nexts[i]
                            break
                        cfail = cfail.fail
                    queue.append(cur.nexts[i])

    def contain_words(self, content):
        """ content 是否包含前缀树中的词
        """
        root = self.root
        cur = root
        ans = []
        for ch in content:
            path = ord(ch) - 97
            # 如果当前字符在这条路上没有匹配出来，就随着fail 方向走向下条路径
            while cur.nexts[path] is None and cur != root:
                cur = cur.fail

            # 1.现在来到的路径, 是可以继续匹配的
            # 2.现在来到的节点, 就是前缀树的根节点
            cur = cur.nexts[path] if cur.nexts[path] else root
            follow = cur
            while follow != root:
                if follow.end_use:
                    break
                """不同的需求, 在这一段之间修改"""
                if follow.end:
                    ans.append(follow.end)
                    follow.end_use = True
                """不同的需求, 在这一段之间修改"""
                follow = follow.fail
        return ans


if __name__ == "__main__":
    ac = ACAutomation()
    ac.insert("dhe")
    ac.insert("he")
    ac.insert("abcdheks")

    ac.buid()
    content = "abcdhekskdjfafhasldkflskdjhwqaeruv"
    ans = ac.contain_words(content)
    print(ans)

