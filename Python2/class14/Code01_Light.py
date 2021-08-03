# -*- coding: utf-8 –*-

"""
给定一个字符串str，只由‘X’和‘.’两种字符构成。
‘X’表示墙，不能放灯，也不需要点亮
‘.’表示居民点，可以放灯，需要点亮
如果灯放在i位置，可以让i-1，i和i+1三个位置被点亮
返回如果点亮str中所有需要点亮的位置，至少需要几盏灯
"""
import random


def minLight1(road):
    if not road:
        return 0
    lights = set()
    return process(road, 0, lights)


def process(road, idx, lights):
    """
    road[idx...]位置，自由选择放不放灯
    road[0..index-1]位置呢？已经做完决定了，那些放了灯的位置，存在lights里
    要求选出能照亮所有.的方案，并且在这些有效的方案中，返回最少需要几个灯
    """
    if idx == len(road):
        for i in range(len(road)):
            if road[i] != 'X':   # 当前位置是点
                if i - 1 not in lights and i not in lights and i + 1 not in lights:
                    return float('inf')
        return len(lights)
    else:
        no = process(road, idx + 1, lights)
        yes = float('inf')
        if road[idx] == '.':
            lights.add(idx)
            yes = process(road, idx + 1, lights)
            lights.remove(idx)
        return min(yes, no)


def minLight2(road):
    if not road:
        return 0
    i = 0
    light = 0
    N = len(road)
    while i < N:
        if road[i] == 'X':
            i += 1
        else:
            light += 1
            if i + 1 == N:
                break
            else:
                if road[i + 1] == 'X':
                    i = i + 2
                else:
                    i = i + 3
    return light


def generateRandomRoad(arrlen):
    """ 生成只由‘X’和‘.’两种字符构成的字符串
    """
    alen = random.randint(1, arrlen)
    return "".join(['.' if random.randint(0, 3) else 'X' for _ in range(alen)])


if __name__ == "__main__":
    arrlen = 100
    max_time = 20
    test_times = 100000
    print('test begin !!!')
    for _ in range(test_times):
        strs = generateRandomRoad(arrlen)
        ans1 = minLight1(strs[::])
        ans2 = minLight2(strs[::])
        if ans1 != ans2:
            print(strs)
            print(ans1, ans2)
            print("test break because of error !!!")
            break
    print("test end !!!")