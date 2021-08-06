# -*- coding: utf-8 –*-

"""
打印一个字符串的全部排列

打印一个字符串的全部排列，要求不要出现重复的排列
"""


def permutation1(s):
    if not s:
        return []
    rest = list(s)
    path = ""
    ans = []
    process1(rest, path, ans)
    return ans


def process1(rest, path, ans):
    if not rest:
        ans.append(path)
        return
    for idx in range(len(rest)):
        item = rest.pop(idx)
        process1(rest, path + item, ans)
        rest.insert(idx, item)


def permutation2(string):
    if not string:
        return []
    s = list(string)
    ans = []
    process2(s, 0, ans)
    return ans


def process2(s, idx, ans):
    if idx == len(s):
        ans.append("".join(s))
        return
    for i in range(idx, len(s)):
        swap(s, idx, i)
        process2(s, idx + 1, ans)
        swap(s, idx, i)


def permutation_no_repeat(string):
    if not string:
        return []
    s = list(string)
    ans = []
    process3(s, 0, ans)
    return ans


def process3(s, idx, ans):
    if idx == len(s):
        ans.append("".join(s))
        return
    visited = set()
    for i in range(idx, len(s)):
        if s[i] not in visited:
            visited.add(s[i])
            swap(s, idx, i)
            process3(s, idx + 1, ans)
            swap(s, idx, i)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    string = "acc"
    ans1 = permutation1(string)
    print(ans1)
    ans2 = permutation2(string)
    print(ans2)
    ans3 = permutation_no_repeat(string)
    print(ans3)


