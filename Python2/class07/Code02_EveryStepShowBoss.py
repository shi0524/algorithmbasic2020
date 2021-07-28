# -*- coding: utf-8 –*-
import random
from HeapGreater import HeapGreater
from collections import defaultdict

"""
手动改写堆题目练习

给定一个整型数组，int[] arr；和一个布尔类型数组，boolean[] op
两个数组一定等长，假设长度为N，arr[i]表示客户编号，op[i]表示客户操作
arr = [ 3   ,   3   ,   1   ,  2,      1,      2,      5…
op = [ T   ,   T,      T,     T,      F,      T,       F…
依次表示：3用户购买了一件商品，3用户购买了一件商品，1用户购买了一件商品，
        2用户购买了一件商品，1用户退货了一件商品，2用户购买了一件商品，
        5用户退货了一件商品…

一对arr[i]和op[i]就代表一个事件：
用户号为arr[i]，op[i] == T就代表这个用户购买了一件商品
op[i] == F就代表这个用户退货了一件商品
现在你作为电商平台负责人，你想在每一个事件到来的时候，
都给购买次数最多的前K名用户颁奖。
所以每个事件发生后，你都需要一个得奖名单（得奖区）。

得奖系统的规则：
1，如果某个用户购买商品数为0，但是又发生了退货事件，
     则认为该事件无效，得奖名单和上一个事件发生后一致，例子中的5用户

2，某用户发生购买商品事件，购买商品数+1，发生退货事件，购买商品数-1

3，每次都是最多K个用户得奖，K也为传入的参数
      如果根据全部规则，得奖人数确实不够K个，那就以不够的情况输出结果

4，得奖系统分为得奖区和候选区，任何用户只要购买数>0，一定在这两个区域中的一个

5，购买数最大的前K名用户进入得奖区，
      在最初时如果得奖区没有到达K个用户，那么新来的用户直接进入得奖区

6，如果购买数不足以进入得奖区的用户，进入候选区

7，如果候选区购买数最多的用户，已经足以进入得奖区，
     该用户就会替换得奖区中购买数最少的用户（大于才能替换），
     如果得奖区中购买数最少的用户有多个，就替换最早进入得奖区的用户
     如果候选区中购买数最多的用户有多个，机会会给最早进入候选区的用户

8，候选区和得奖区是两套时间，
     因用户只会在其中一个区域，所以只会有一个区域的时间，另一个没有
     从得奖区出来进入候选区的用户，得奖区时间删除，
     进入候选区的时间就是当前事件的时间（可以理解为arr[i]和op[i]中的i）
     从候选区出来进入得奖区的用户，候选区时间删除，
     进入得奖区的时间就是当前事件的时间（可以理解为arr[i]和op[i]中的i）

9，如果某用户购买数==0，不管在哪个区域都离开，区域时间删除，
     离开是指彻底离开，哪个区域也不会找到该用户
     如果下次该用户又发生购买行为，产生>0的购买数，
     会再次根据之前规则回到某个区域中，进入区域的时间重记
     
请遍历arr数组和op数组，遍历每一步输出一个得奖名单

"""


class Customer(object):

    def __init__(self, v, b, o):
        self.id = v
        self.buy = b
        self.enter_time = o

    def __repr__(self):
        return "%s_%s_%s " % (self.id, self.buy, self.enter_time)

    @staticmethod
    def daddyComparator(o1, o2):
        return o1.buy - o2.buy if o1.buy != o2.buy else o1.enter_time - o2.enter_time

    @staticmethod
    def candidateComparator(o1, o2):
        return o2.buy - o1.buy if o1.buy != o2.buy else o1.enter_time - o2.enter_time


class WhosYourDaddy(object):
    def __init__(self, K):
        self.customers = {}
        self.daddyHeap = HeapGreater(Customer.daddyComparator)
        self.cand_heap = HeapGreater(Customer.candidateComparator)
        self.daddyLimit = K

    def operate(self, cur_time, id_, isbuy):
        """ 当前处理i号事件，arr[i] -> id, buyOrRefund
        :param cur_time:
        :param id_:
        :param isbuy:
        :return:
        """
        customers = self.customers
        cand_heap = self.cand_heap
        daddyHeap = self.daddyHeap
        daddyLimit = self.daddyLimit
        if not isbuy and id_ not in customers:
            return
        if id_ not in customers:
            customers[id_] = Customer(id_, 0, 0)
        c = customers[id_]
        if isbuy:
            c.buy += 1
        else:
            c.buy -= 1
        if c.buy == 0:
            customers.pop(id_)

        if not cand_heap.containts(c) and not daddyHeap.containts(c):
            if daddyHeap.size < daddyLimit:
                c.enter_time = cur_time
                daddyHeap.push(c)
            else:
                c.enter_time = cur_time
                cand_heap.push(c)
        elif cand_heap.containts((c)):
            if c.buy == 0:
                cand_heap.remove(c)
            else:
                cand_heap.resign(c)
        else:
            if c.buy == 0:
                daddyHeap.remove(c)

            else:
                daddyHeap.resign(c)
        self.daddyMove(cur_time)

    def daddyMove(self, cur_time):
        cand_heap = self.cand_heap
        daddyHeap = self.daddyHeap
        daddyLimit = self.daddyLimit
        if cand_heap.isEmpty():
            return
        if daddyHeap.size < daddyLimit:

            p = cand_heap.pop()
            p.enter_time = cur_time
            daddyHeap.push(p)
        else:
            if cand_heap.peek().buy > daddyHeap.peek().buy:
                oldDaddy = daddyHeap.pop()
                newDaddy = cand_heap.pop()
                oldDaddy.enter_time = cur_time
                newDaddy.enter_time = cur_time
                daddyHeap.push(newDaddy)
                cand_heap.push(oldDaddy)

    def getDaddies(self):
        return [c.id for c in self.daddyHeap.getAllElements()]


def topK(arr, op, k):
    ans = []
    whoDaddies = WhosYourDaddy(k)
    for i in range(len(arr)):
        whoDaddies.operate(i, arr[i], op[i])
        ans.append(whoDaddies.getDaddies())
    return ans

# for test

def compare(arr, op, k):
    mapping = {}
    cands = []
    daddy = []
    ans = []
    for i in range(len(arr)):
        id_ = arr[i]
        isbuy = op[i]
        if not isbuy and id_ not in mapping:
            ans.append(get_cur_ans(daddy))
            continue

        # 没有发生：用户购买数为0并且又退货了
        # 用户之前购买数是0，此时买货事件
        # 用户之前购买数 > 0， 此时买货
        # 用户之前购买数 > 0, 此时退货
        if id_ not in mapping:
            mapping[id_] = Customer(id_, 0, 0)

        # 买 卖
        c = mapping[id_]
        if isbuy:
            c.buy += 1
        else:
            c.buy -= 1

        if c.buy == 0:
            mapping.pop(id_)

        if c not in cands and c not in daddy:
            if len(daddy) < k:
                c.enter_time = i
                daddy.append(c)
            else:
                c.enter_time = i
                cands.append(c)
        cleanZeroBuy(cands)
        cleanZeroBuy(daddy)
        cands.sort(cmp=Customer.candidateComparator)
        daddy.sort(cmp=Customer.daddyComparator)
        move(cands, daddy, k, i)
        ans.append(get_cur_ans(daddy))
    return ans


def move(cands, daddy, k, cur_time):
    # 候选区为空
    if not cands:
        return

    # 候选区不为空
    if len(daddy) < k:
        c = cands[0]
        c.enter_time = cur_time
        daddy.append(c)
        cands.remove(c)
    else:
        if cands[0].buy > daddy[0].buy:
            oldDaddy = daddy[0]
            daddy.remove(oldDaddy)
            newDaddy = cands[0]
            cands.remove(newDaddy)
            newDaddy.enter_time = cur_time
            oldDaddy.enter_time = cur_time
            daddy.append(newDaddy)
            cands.append(oldDaddy)


def cleanZeroBuy(arr):
    arr_ = [c for c in arr if c.buy == 0]
    for o in arr_:
        arr.remove(o)


def get_cur_ans(daddy):
    return [c.id for c in daddy]


# for test
def random_data(maxValue, maxLen):
    data_len = random.randint(1, maxLen)
    buy_times = defaultdict(int)
    arr, ops = [], []
    for _ in range(data_len):
        no = random.randint(1, maxValue)
        arr.append(no)
        op = 1 if not buy_times[no] else random.randint(0, 1)
        ops.append(op)
        buy_times[no] += 1 if op else -1
    return arr, ops


# for test
def sameAnswer(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        if set(arr1[i]) != set(arr2[i]):
            return False
    return True


if __name__ == "__main__":
    maxValue = 10
    maxLen = 100
    maxK = 6
    testTime = 100000
    print("test begin !!!")
    for _ in range(testTime):
        arr, op = random_data(maxValue, maxLen)
        k = random.randint(1, maxK)
        ans1 = topK(arr, op, k)
        ans2 = compare(arr, op, k)
        if not sameAnswer(ans1, ans2):
            print k
            print arr
            print op
            print("ans1", ans1)
            print("ans2", ans2)
            break
    print("test end !!!")
