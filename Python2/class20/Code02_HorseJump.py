# -*- coding: utf-8 –*-

"""
请同学们自行搜索或者想象一个象棋的棋盘，
然后把整个棋盘放入第一象限，棋盘的最左下角是(0,0)位置
那么整个棋盘就是横坐标上9条线、纵坐标上10条线的区域
给你三个 参数 x，y，k
返回“马”从(0,0)位置出发，必须走k步
最后落在(x,y)上的方法数有多少种?
"""


def jump1(a, b, k):

    return process(0, 0, k, a, b)


def process(x, y, rest, a, b):
    if x < 0 or y < 0 or x > 9 or y > 8:
        return 0
    if rest == 0:
        return 1 if x == a and y == b else 0

    ways = process(x + 2, y + 1, rest - 1, a, b)
    ways += process(x - 2, y + 1, rest - 1, a, b)
    ways += process(x + 2, y - 1, rest - 1, a, b)
    ways += process(x - 2, y - 1, rest - 1, a, b)
    ways += process(x + 1, y + 2, rest - 1, a, b)
    ways += process(x - 1, y + 2, rest - 1, a, b)
    ways += process(x + 1, y - 2, rest - 1, a, b)
    ways += process(x - 1, y - 2, rest - 1, a, b)

    return ways


def jump2(a, b, k):

    dp = [[[0] * 9 for _ in range(10)] for _ in range(k + 1)]

    # 开始位置为 (a, b), 如果 rest = 0
    dp[0][a][b] = 1

    for rest in range(1, k + 1):
        for x in range(10):
            for y in range(9):
                ways = pick(dp, x + 2, y + 1, rest - 1)
                ways += pick(dp, x - 2, y + 1, rest - 1)
                ways += pick(dp, x + 2, y - 1, rest - 1)
                ways += pick(dp, x - 2, y - 1, rest - 1)
                ways += pick(dp, x + 1, y + 2, rest - 1)
                ways += pick(dp, x - 1, y + 2, rest - 1)
                ways += pick(dp, x + 1, y - 2, rest - 1)
                ways += pick(dp, x - 1, y - 2, rest - 1)
                dp[rest][x][y] = ways

    return dp[k][0][0]


def pick(dp, x, y, rest):
    if x < 0 or y < 0 or x > 9 or y > 8:
        return 0
    return dp[rest][x][y]


if __name__ == "__main__":
    x = 1
    y = 2
    k = 7
    ans1 = jump1(x, y, k)
    ans2 = jump2(x, y, k)
    print ans1, ans2


