# -*- coding: utf-8 –*-

"""
打印一个字符串的全部子序列

打印一个字符串的全部子序列，要求不要出现重复字面值的子序列
"""


def sub_string(string):
    ans = []
    path = ""
    process(string, 0, path, ans)
    return ans


def process(string, index, path, ans):
    """
    """
    if index == len(string):
        ans.append(path)
        return
    # 不要index位置
    process(string, index + 1, path, ans)
    # 要index位置
    process(string, index + 1, path + string[index], ans)


def subsNoRepeat(string):
    ans = set()
    path = ""
    process2(string, 0, path, ans)
    return list(ans)


def process2(string, index, path, ans):
    if index == len(string):
        ans.add(path)
        return
    # 不要index位置
    process2(string, index + 1, path, ans)
    # 要index位置
    process2(string, index + 1, path + string[index], ans)


if __name__ == "__main__":
    string = 'accc'
    ans = sub_string(string)
    print(ans)
    no_repeat = subsNoRepeat(string)
    print(no_repeat)


