# -*- coding: utf-8 –*-

"""
一些项目要占用一个会议室宣讲，会议室不能同时容纳两个项目的宣讲。
给你每一个项目开始的时间和结束的时间
你来安排宣讲的日程，要求会议室进行的宣讲的场次最多。
返回最多的宣讲场次。
"""
import random


def best_arrange1(programs):
    if not programs:
        return 0
    return process(programs, 0, 0)


def process(programs, done, timeline):
    """
    目前来到timeLine的时间点，已经安排了done多的会议，
    剩下的会议programs可以自由安排
    返回能安排的最多会议数量
    :param programs: 还剩下的会议
    :param done: 之前已经安排了多少会议的数量
    :param timeline: 目前来到的时间点是什么
    :return:
    """
    if not programs:
        return done
    # 还剩下会议
    max_ = done
    # 当前安排的会议是什么会，每一个都枚举
    for s_time, e_time in programs:
        if s_time >= timeline:
            programs_copy = programs[::]
            programs_copy.remove([s_time, e_time])
            max_ = max(max_, process(programs_copy, done + 1, e_time))
    return max_


# for test
def generateRandomProgram(max_time):
    """ 生成单个会议时间
    """
    p = [random.randint(0, max_time) for _ in range(2)]
    while p[0] == p[1]:
        p = [random.randint(0, max_time) for _ in range(2)]
    p.sort()
    return p


def generateRandomProgramArray(arrlen, max_time):
    """ 生成会议列表
    """
    alen = random.randint(1, arrlen)
    return [generateRandomProgram(max_time) for _ in range(alen)]


def best_arrange2(programs):
    programs.sort(key=lambda x: x[1])
    done = 0
    timeline = 0
    for s_time, e_time in programs:
        if s_time >= timeline:
            done += 1
            timeline = e_time
    return done


if __name__ == "__main__":
    arrlen = 100
    max_time = 20
    test_times = 100000
    print('test begin !!!')
    for _ in range(test_times):
        strs = generateRandomProgramArray(arrlen, max_time)
        ans1 = best_arrange1(strs[::])
        ans2 = best_arrange2(strs[::])
        if ans1 != ans2:
            print()
            print(ans1, ans2)
            print("test break because of error !!!")
            break
    print("test end !!!")
