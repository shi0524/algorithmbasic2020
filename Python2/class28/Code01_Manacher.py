# -*- coding: utf-8 –*-

def manacher(string):
    if not string:
        return 0

    # 生成 manacher字符串
    s = manacher_string(string)

    n = len(s)
    # 回文半径数组
    pArr = [0] * n

    # 中心点
    C = -1

    # 讲述中: R 代表最右扩成功的位置
    # coding: 最右扩成功位置的再下一个位置
    R = -1
    max_R = -float('inf')
    for i in range(n):
        # R 第一个违规的位置 i >= R
        # i 位置扩出来的答案
        # i位置扩的区域，至少是多大
        pArr[i] = min(pArr[2 * C - i], R - i) if R > i else 1

        # 判断后续还能不能扩
        while i + pArr[i] < n and i - pArr[i] > -1:
            if s[i + pArr[i]] == s[i - pArr[i]]:
                pArr[i] += 1
            else:
                break

        # 判断 R 和 C 用不用变
        if i + pArr[i] > R:
            R = i + pArr[i]
            C = i
        max_R = max(max_R, pArr[i])
    # 打印各个位置对应的回文长度
    # print map(lambda x: x-1, [pArr[i] for i in range(1, n, 2)])
    return max_R - 1


def manacher_string(string):
    """ 加工成 manacher 字符串
        "12132" -> "#1#2#1#3#2#"
    :param string: "121321"
    :return: "#1#2#1#3#2#"
    """
    return "".join(["#", "#".join(string), "#"])


if __name__ == "__main__":
    s = "12321234321"
    print manacher(s)