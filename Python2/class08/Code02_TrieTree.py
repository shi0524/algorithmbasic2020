# -*- coding: utf-8 –*-
import random


class Node1(object):
    def __init__(self):
        self.p = 0
        self.e = 0
        self.nexts = [0] * 26


class Trie1(object):
    def __init__(self):
        self.root = Node1()

    def insert(self, word):
        if not word:
            return
        node = self.root
        node.p += 1
        for ch in word:
            path = ord(ch) - ord('a')
            if not node.nexts[path]:
                node.nexts[path] = Node1()
            node = node.nexts[path]
            node.p += 1
        node.e += 1

    def delete(self, word):
        if not self.search(word):
            return
        node = self.root
        node.p -= 1
        for ch in word:
            path = ord(ch) - ord('a')
            if node.nexts[path].p == 1:
                node.nexts[path] = 0
                return
            node = node.nexts[path]
            node.p -= 1
        node.e -= 1

    def search(self, word):
        """ 查找字符串被加入了几次
        """
        if not word:
            return 0
        node = self.root
        for ch in word:
            path = ord(ch) - ord('a')
            if not node.nexts[path]:
                return 0
            node = node.nexts[path]
        return node.e

    def prefix_number(self, pre):
        if not pre:
            return 0
        node = self.root
        for ch in pre:
            path = ord(ch) - ord('a')
            node = node.nexts[path]
            if not node:
                return 0
        return node.p


class Node2(object):
    def __init__(self):
        self.p = 0
        self.e = 0
        self.nexts = {}


class Trie2(object):
    def __init__(self):
        self.root = Node2()

    def insert(self, word):
        if not word:
            return
        node = self.root
        node.p += 1
        for ch in word:
            if ch not in node.nexts:
                node.nexts[ch] = Node2()
            node = node.nexts[ch]
            node.p += 1
        node.e += 1

    def delete(self, word):
        if not self.search(word):
            return
        node = self.root
        node.p -= 1
        for ch in word:
            if node.nexts[ch].p == 1:
                del node.nexts[ch]
                return
            node = node.nexts[ch]
            node.p -= 1
        node.e -= 1

    def search(self, word):
        if not word:
            return
        node = self.root
        for ch in word:
            if ch not in node.nexts:
                return 0
            node = node.nexts[ch]
        return node.e

    def prefix_number(self, pre):
        if not pre:
            return 0
        node = self.root
        for ch in pre:
            if ch not in node.nexts:
                return 0
            node = node.nexts[ch]
        return node.p


class Right(object):
    """ Trie 对数器
    """
    def __init__(self):
        self.box = {}

    def insert(self, word):
        self.box[word] = self.box.get(word, 0) + 1

    def delete(self, word):
        if word not in self.box:
            return
        self.box[word] -= 1
        if not self.box[word]:
            del self.box[word]

    def search(self, word):
        return self.box.get(word, 0)

    def prefix_number(self, pre):
        count = 0
        for k, v in self.box.items():
            if k.startswith(pre):
                count += v
        return count

# for test
def generateRandomString(strlen):
    """ 生成字符串
    """
    slen = random.randint(1, strlen)
    return "".join([chr(random.randint(97, 122)) for _ in range(slen)])


def generateRandomStringArray(arrlen, strlen):
    """ 生成字符串列表
    """
    alen = random.randint(1, arrlen)
    return [generateRandomString(strlen) for _ in range(alen)]


if __name__ == "__main__":
    arrlen = 100
    strlen = 20
    test_times = 100000
    print('test begin !!!')
    for _ in range(test_times):
        arr = generateRandomStringArray(arrlen, strlen)
        trie1 = Trie1()
        trie2 = Trie2()
        right = Right()
        for word in arr:
            decide = random.random()
            if decide < 0.25:
                trie1.insert(word)
                trie2.insert(word)
                right.insert(word)
            elif decide < 0.5:
                trie1.delete(word)
                trie2.delete(word)
                right.delete(word)
            elif decide < 0.75:
                ans1 = trie1.search(word)
                ans2 = trie2.search(word)
                ans3 = right.search(word)
                if ans1 != ans2 or ans2 != ans3:
                    print("Oops !!!")
                    break
            else:
                ans1 = trie1.prefix_number(word)
                ans2 = trie2.prefix_number(word)
                ans3 = right.prefix_number(word)
                if ans1 != ans2 or ans2 != ans3:
                    print("Oops !!!")
                    break
    print('test end !!!')