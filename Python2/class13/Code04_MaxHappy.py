# -*- coding: utf-8 –*-

"""
派对的最大快乐值
员工信息的定义如下:
class Employee {
    public int happy; // 这名员工可以带来的快乐值
    List<Employee> subordinates; // 这名员工有哪些直接下级
}
"""
import random


class Employee(object):
    def __init__(self, happy):
        self.happy = happy
        self.nexts = []


def maxHappy1(boss):
    if not boss:
        return 0
    return process1(boss, False)


def process1(cur, up):
    """
    当前来到的节点叫cur，
    up表示cur的上级是否来，
    该函数含义：
    如果up为true，表示在cur上级已经确定来，的情况下，cur整棵树能够提供最大的快乐值是多少？
    如果up为false，表示在cur上级已经确定不来，的情况下，cur整棵树能够提供最大的快乐值是多少？
    """
    if up:
        # 如果cur的上级来的话，cur没得选，只能不来
        ans = 0
        for n in cur.nexts:
            ans += process1(n, False)
        return ans
    else:
        # 如果cur的上级不来的话，cur可以选，可以来也可以不来
        p1 = cur.happy
        p2 = 0
        for n in cur.nexts:
            p1 += process1(n, True)
            p2 += process1(n, False)
        return max(p1, p2)


def maxHappy2(boss):
    info = process2(boss)
    return max(info['yes'], info['no'])


def process2(x):
    if not x:
        return {"yes": 0, "no": 0}
    no = 0
    yes = x.happy
    for e in x.nexts:
        info = process2(e)
        no += max(info['yes'], info['no'])
        yes += info['no']
    return {'yes': yes, 'no': no}


# for test
def generate_boss(max_level, max_nexts, max_happy):
    if not random.randint(0, 50):
        return None
    boss = Employee(random.randint(1, max_happy))
    genarate_nexts(boss, 1, max_level, max_nexts, max_happy)
    return boss


def genarate_nexts(e, level, max_level, max_nexts, max_happy):
    if level > max_level:
        return
    next_size = random.randint(1, max_nexts)
    for i in range(next_size):
        next_e = Employee(random.randint(1, max_happy))
        e.nexts.append(next_e)
        genarate_nexts(next_e, level + 1, max_level, max_nexts, max_happy)


if __name__ == "__main__":
    maxLevel = 5
    maxNexts = 5
    maxValue = 100
    testTimes = 1000000
    print("test begin !!!")
    for _ in range(testTimes):
        head = generate_boss(maxLevel, maxNexts, maxValue)
        ans1 = maxHappy1(head)
        ans2 = maxHappy2(head)
        if ans1 != ans2:
            print(ans1, ans2)
            print("test break because of error !!!")
            break
    print("test end !!!")


